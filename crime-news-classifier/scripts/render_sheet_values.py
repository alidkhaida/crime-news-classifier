#!/usr/bin/env python3
"""Render validated classifier records into deterministic K:P Sheet values."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == {} or value == [] or str(value).strip() == "-"


def render_categories(value: Any) -> str:
    if is_empty(value):
        return "-"
    if isinstance(value, str):
        return value.strip() or "-"
    if not isinstance(value, dict):
        raise ValueError("categories must be a rendered string or parent-to-subcategories object")
    lines: list[str] = []
    for parent, subcategories in value.items():
        parent = str(parent).strip()
        if not parent:
            continue
        if isinstance(subcategories, str):
            subcategories = [subcategories] if subcategories.strip() else []
        if subcategories is None:
            subcategories = []
        if not isinstance(subcategories, list):
            raise ValueError(f"subcategories for {parent!r} must be a list")
        rendered_subcategories = [str(item).strip() for item in subcategories if str(item).strip()]
        lines.append(f"{parent}: {', '.join(rendered_subcategories)}" if rendered_subcategories else parent)
    return "\n".join(lines) or "-"


def render_evidence(value: Any) -> str:
    if is_empty(value):
        return "-"
    if isinstance(value, list):
        return "; ".join(str(item).strip() for item in value if str(item).strip()) or "-"
    return str(value).strip() or "-"


def candidate_line(candidate: Any, side: str) -> str:
    if isinstance(candidate, str):
        text = candidate.strip()
        return f"{side}: {text}" if text else ""
    if not isinstance(candidate, dict):
        raise ValueError("unmapped candidates must be strings or objects")
    parent = str(candidate.get("parent_category", "")).strip()
    name = str(candidate.get("candidate_name", "")).strip()
    evidence = str(candidate.get("evidence", "")).strip()
    gap_type = str(candidate.get("gap_type", "")).strip().lower()
    if gap_type not in {"parent", "subcategory"}:
        gap_type = "subcategory" if parent else "parent"
    if gap_type == "subcategory" and parent:
        label = f"{side} subcategory under {parent}: {name or 'Unspecified candidate'}"
    else:
        label = f"{side} parent: {name or parent or 'Unspecified candidate'}"
    return f"{label} — {evidence}" if evidence else label


def render_unmapped(good: Any, bad: Any) -> str:
    lines: list[str] = []
    for side, value in (("Good", good), ("Bad", bad)):
        if is_empty(value):
            continue
        candidates = value if isinstance(value, list) else [value]
        lines.extend(line for line in (candidate_line(item, side) for item in candidates) if line)
    return "\n".join(lines) or "-"


def physical_row(item: dict[str, Any]) -> int:
    row = item.get("physical_row", item.get("row"))
    if not isinstance(row, int) or row <= 0:
        raise ValueError(f"invalid physical row: {row!r}")
    return row


def render(payload: dict[str, Any]) -> dict[str, Any]:
    source_rows = payload.get("rows")
    if not isinstance(source_rows, list) or not source_rows:
        raise ValueError("rows must be a nonempty list")
    ordered = sorted(source_rows, key=physical_row)
    row_numbers = [physical_row(item) for item in ordered]
    expected = list(range(row_numbers[0], row_numbers[-1] + 1))
    if row_numbers != expected:
        raise ValueError("rows must be unique and physically contiguous")
    scope = payload.get("scope")
    if isinstance(scope, dict):
        start_row = scope.get("start_row")
        end_row = scope.get("end_row")
        if isinstance(start_row, int) and isinstance(end_row, int):
            if row_numbers != list(range(start_row, end_row + 1)):
                raise ValueError("rows do not match the declared physical scope")

    values: list[list[Any]] = []
    for item in ordered:
        article = item.get("article") if isinstance(item.get("article"), dict) else {}
        article_check_display = "Yes" if article.get("status") in {
            "fetched", "fetch_failed", "infrastructure_error"
        } else "-"
        confidence = item.get("confidence")
        if not isinstance(confidence, (int, float)):
            raise ValueError(f"row {physical_row(item)}: confidence must be numeric")
        values.append([
            str(item.get("crime_status", "")).strip() or "-",
            render_categories(item.get("good_categories", item.get("categories"))),
            render_categories(item.get("bad_categories")),
            article_check_display,
            render_evidence(item.get("evidence", item.get("evidence_spans"))),
            render_unmapped(item.get("unmapped_candidates"), item.get("unmapped_bad_candidates")),
        ])
    return {
        "start_row": row_numbers[0],
        "end_row": row_numbers[-1],
        "columns": "K:P",
        "range": f"K{row_numbers[0]}:P{row_numbers[-1]}",
        "values": values,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result_json", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.result_json.read_text(encoding="utf-8"))
        print(json.dumps(render(payload), indent=2, ensure_ascii=False))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"RENDER ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
