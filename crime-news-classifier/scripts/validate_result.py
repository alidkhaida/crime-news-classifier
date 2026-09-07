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
    "Human Trafficking, Smuggling & Exploitation",
    "Elder & Vulnerable Adult Abuse or Exploitation",
    "Hate Crime, Bias & Extremism",
    "School, Institutional & Public-Facility Crime",
}
MAINTAINED_BAD_PARENTS = {
    "Suicide / Self-Harm",
    "Court / Sentencing Stories",
    "Prison / Jail-Only Incidents",
    "Animal-Only Stories",
    "White-Collar / Corporate Crime",
    "Officer Misconduct / Administrative Stories",
    "Prostitution / Sex Trafficking",
    "Sexual Crimes / Exploitation",
}


def category_parents(rendered: str) -> list[str]:
    return [line.split(":", 1)[0].strip() for line in rendered.splitlines() if line.strip()]


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
        good_categories = str(item.get("good_categories", item.get("categories", "")))
        bad_categories = str(item.get("bad_categories", ""))
        unmapped = str(item.get("unmapped_candidates", ""))
        needs_review = bool(item.get("needs_review", False))
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
        if status == "crime" and not good_categories and not (needs_review and unmapped):
            errors.append(f"row {row}: crime row has no category or explicit taxonomy review state")
        if status == "crime" and not good_categories and needs_review and not unmapped:
            errors.append(f"row {row}: taxonomy review row is missing unmapped_candidates")
        if status == "noncrime" and good_categories:
            errors.append(f"row {row}: noncrime row has Good Categories")
        if "Human Trafficking, Smuggling & Exploitation" in parents:
            evidence = str(item.get("evidence", "")).lower()
            candidate = unmapped.lower()
            trafficking_terms = ("traffick", "commercial exploitation", "recruit", "transport", "advertis", "sell", "sold", "commercial sexual")
            sexual_possession_terms = ("porn", "csam", "child sexual abuse material")
            if any(term in evidence or term in candidate for term in sexual_possession_terms) and not any(term in evidence for term in trafficking_terms):
                errors.append(f"row {row}: trafficking parent lacks trafficking/commercial-exploitation evidence")
        if not item.get("evidence"):
            errors.append(f"row {row}: missing evidence")
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
