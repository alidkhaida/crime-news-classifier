#!/usr/bin/env python3
"""Validate staged result JSON before Sheet writeback."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CODE_RE = re.compile(r"\b[A-Z]{2}-\d{2}\b")
ALLOWED_STATUS = {"crime", "noncrime", "needs_article"}
ALLOWED_ARTICLE_STATUS = {"not_needed", "fetched", "fetch_failed", "infrastructure_error"}
MAINTAINED_PARENTS = {
    "Child Neglect, Endangerment & Child Abuse",
    "Family, Domestic & Relationship Cases",
    "Teen & Juvenile-Involved Crime",
    "Theft, Fraud & Financial Crime",
    "Traffic, DUI & Vehicle Crime",
    "Employee, Workplace & Occupational Crime",
    "Homicide, Suspicious Death & Body Discovery",
    "Resisting, Evading, Obstruction & Public Disturbance",
    "Assault, Weapons & Violent Crime",
    "Drugs & Narcotics",
    "Kidnapping, Abduction, Unlawful Restraint & Missing Persons",
    "Arson, Vandalism & Destruction of Property",
    "Robbery, Burglary, Trespass & Home Invasion",
    "Cybercrime, Digital Crime & Identity Abuse",
    "Stalking, Harassment, Threats & Protection-Order Violations",
    "Human Trafficking, Forced Labor & Exploitation",
    "Elder & Vulnerable Adult Abuse or Exploitation",
    "Hate Crime, Bias & Extremism",
    "School, Institutional & Public-Facility Crime",
    "Organized Contraband Smuggling",
}
MAINTAINED_BAD_PARENTS = {
    "Suicide / Self-Harm",
    "Court / Sentencing Stories",
    "Prison / Jail-Only Incidents",
    "Animal-Related Stories",
    "White-Collar / Corporate Crime",
    "Officer Misconduct / Administrative Stories",
    "Prostitution / Commercial Sex",
    "Sexual Crimes / Exploitation",
    "Excluded",
}


def category_parents(rendered: str) -> list[str]:
    return [
        line.split(":", 1)[0].strip()
        for line in rendered.splitlines()
        if line.strip() and line.strip() != "-"
    ]


def empty_display_value(value: object) -> bool:
    """Treat the Sheet dash sentinel as empty during local-result validation."""
    return value is None or value == {} or value == [] or str(value).strip() in {"", "-"}


def category_text(value: object) -> str:
    """Normalize structured or rendered categories for parent validation."""
    if empty_display_value(value):
        return ""
    if isinstance(value, dict):
        lines = []
        for parent, subcategories in value.items():
            parent_text = str(parent).strip()
            if not parent_text:
                continue
            if isinstance(subcategories, str):
                subcategories = [subcategories] if subcategories.strip() else []
            if subcategories is None:
                subcategories = []
            if not isinstance(subcategories, list):
                raise ValueError(f"subcategories for {parent_text!r} must be a list")
            children = [str(item).strip() for item in subcategories if str(item).strip()]
            lines.append(f"{parent_text}: {', '.join(children)}" if children else parent_text)
        return "\n".join(lines)
    return str(value).strip()


def validate(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("rows")
    if not isinstance(rows, list):
        return ["rows must be a list"]
    errors: list[str] = []
    seen_rows: set[int] = set()
    for item in rows:
        row = item.get("row")
        if not isinstance(row, int) or row <= 0:
            errors.append(f"invalid physical row: {row!r}")
        elif row in seen_rows:
            errors.append(f"duplicate physical row: {row}")
        else:
            seen_rows.add(row)
        status = item.get("crime_status")
        if status not in ALLOWED_STATUS:
            errors.append(f"row {row}: invalid crime_status {status!r}")
        confidence = item.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"row {row}: confidence must be between 0 and 1")
        good_categories_raw = item.get("good_categories", item.get("categories", ""))
        bad_categories_raw = item.get("bad_categories", "")
        unmapped_raw = item.get("unmapped_candidates", "")
        unmapped_bad_raw = item.get("unmapped_bad_candidates", "")
        try:
            good_categories = category_text(good_categories_raw)
            bad_categories = category_text(bad_categories_raw)
        except ValueError as exc:
            errors.append(f"row {row}: {exc}")
            good_categories = ""
            bad_categories = ""
        unmapped = "" if empty_display_value(unmapped_raw) else str(unmapped_raw)
        unmapped_bad = "" if empty_display_value(unmapped_bad_raw) else str(unmapped_bad_raw)
        has_unmapped = bool(unmapped or unmapped_bad)
        needs_review = bool(item.get("needs_review", False))
        article = item.get("article", {"status": "not_needed"})
        article_status = article.get("status") if isinstance(article, dict) else None
        if article_status not in ALLOWED_ARTICLE_STATUS:
            errors.append(f"row {row}: invalid article.status {article_status!r}")
        if article_status in {"fetch_failed", "infrastructure_error"} and not needs_review:
            errors.append(f"row {row}: failed article attempt requires needs_review")
        if CODE_RE.search(good_categories) or CODE_RE.search(bad_categories):
            errors.append(f"row {row}: machine code leaked into category fields")
        parents = category_parents(good_categories)
        unknown_parents = [parent for parent in parents if parent not in MAINTAINED_PARENTS]
        if unknown_parents:
            errors.append(f"row {row}: unapproved Good Category parent(s): {', '.join(unknown_parents)}")
        bad_parents = category_parents(bad_categories)
        unknown_bad_parents = [parent for parent in bad_parents if parent not in MAINTAINED_BAD_PARENTS]
        if unknown_bad_parents:
            errors.append(f"row {row}: unapproved Bad Category parent(s): {', '.join(unknown_bad_parents)}")
        if status == "crime" and not good_categories and not bad_categories and not (needs_review and has_unmapped):
            errors.append(f"row {row}: crime row has no good/bad category or explicit taxonomy review state")
        if status == "crime" and not good_categories and not bad_categories and needs_review and not has_unmapped:
            errors.append(f"row {row}: taxonomy review row is missing good/bad unmapped candidates")
        if has_unmapped and not needs_review:
            errors.append(f"row {row}: unmapped candidate requires needs_review")
        if status == "noncrime" and good_categories:
            errors.append(f"row {row}: noncrime row has Good Categories")
        if "Human Trafficking, Forced Labor & Exploitation" in parents:
            evidence = str(item.get("evidence", "")).lower()
            candidate = unmapped.lower()
            trafficking_terms = (
                "human trafficking", "sex trafficking", "forced labor", "force", "fraud", "coerc",
                "exploit", "debt bondage", "abuse of vulnerability", "controlled", "commercial sexual",
                "sold for sex", "child sex trafficking",
            )
            sexual_possession_terms = ("porn", "csam", "child sexual abuse material")
            if any(term in evidence or term in candidate for term in sexual_possession_terms) and not any(term in evidence for term in trafficking_terms):
                errors.append(f"row {row}: trafficking parent lacks trafficking/commercial-exploitation evidence")
            voluntary_terms = ("prostitution", "commercial sex", "sex worker", "human smuggling", "migrant smuggling")
            if any(term in evidence for term in voluntary_terms) and not any(term in evidence for term in trafficking_terms):
                errors.append(f"row {row}: trafficking parent lacks force/coercion/exploitation evidence")
        if "Organized Contraband Smuggling" in parents:
            evidence = str(item.get("evidence", "")).lower()
            operation_terms = (
                "smuggl", "contraband", "cross-border", "across the border", "border crossing",
                "concealed shipment", "cargo", "trafficking ring", "trafficking operation",
            )
            if not any(term in evidence for term in operation_terms):
                errors.append(f"row {row}: organized contraband parent lacks smuggling-operation evidence")
        if not item.get("evidence"):
            errors.append(f"row {row}: missing evidence")
    scope = payload.get("scope")
    if isinstance(scope, dict):
        start_row = scope.get("start_row")
        end_row = scope.get("end_row")
        if isinstance(start_row, int) and isinstance(end_row, int) and end_row >= start_row:
            expected_rows = set(range(start_row, end_row + 1))
            if seen_rows != expected_rows:
                missing = sorted(expected_rows - seen_rows)
                extra = sorted(seen_rows - expected_rows)
                errors.append(f"scope row mismatch: missing={missing}, extra={extra}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result_json", type=Path)
    args = parser.parse_args()
    errors = validate(args.result_json)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"valid: {args.result_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
