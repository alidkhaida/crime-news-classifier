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
        categories = str(item.get("categories", ""))
        if CODE_RE.search(categories):
            errors.append(f"row {row}: machine code leaked into categories")
        if status == "crime" and not categories:
            errors.append(f"row {row}: crime row has no category")
        if status == "noncrime" and categories:
            errors.append(f"row {row}: noncrime row has categories")
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
