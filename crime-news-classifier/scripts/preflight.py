#!/usr/bin/env python3
"""Create and verify narrow, run-scoped permission receipts."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


CAPABILITIES = {
    "sheet_read",
    "sheet_write",
    "article_fetch",
    "ai_decision",
    "local_state_read",
    "local_state_write",
    "taxonomy_write",
}

STAGE_CAPABILITIES = {
    "metadata": {"sheet_read", "local_state_read", "local_state_write", "ai_decision"},
    "article_fetch": {"article_fetch", "local_state_read", "local_state_write"},
    "category": {"local_state_read", "local_state_write", "ai_decision"},
    "policy": {"local_state_read", "local_state_write", "ai_decision"},
    "taxonomy": {"local_state_read", "local_state_write", "taxonomy_write", "ai_decision"},
    "writeback": {"sheet_read", "sheet_write", "local_state_write"},
}


def csv_values(value: str) -> set[str]:
    return {item.strip() for item in value.split(",") if item.strip()}


def resolve_target(args: argparse.Namespace) -> None:
    configured = {}
    if args.config:
        configured = json.loads(Path(args.config).read_text(encoding="utf-8"))
    args.spreadsheet_id = args.spreadsheet_id or configured.get("spreadsheet_id", "")
    args.tab = args.tab or configured.get("tab", "")
    if not args.spreadsheet_id or not args.tab:
        raise ValueError("spreadsheet ID and tab are required, directly or through --config")


def validate_scope(args: argparse.Namespace) -> tuple[set[str], set[str]]:
    stages = csv_values(args.stages) if hasattr(args, "stages") and args.stages else set()
    unknown_stages = stages - set(STAGE_CAPABILITIES)
    if unknown_stages:
        raise ValueError(f"unknown stages: {', '.join(sorted(unknown_stages))}")
    if args.start_row < 1 or args.end_row < args.start_row:
        raise ValueError("physical row bounds are invalid")
    return stages, set().union(*(STAGE_CAPABILITIES[stage] for stage in stages)) if stages else set()


def request(args: argparse.Namespace) -> int:
    resolve_target(args)
    stages, required = validate_scope(args)
    if args.ttl_minutes <= 0:
        raise ValueError("--ttl-minutes must be positive")
    granted = csv_values(args.grant) if args.grant else set()
    unknown = granted - CAPABILITIES
    if unknown:
        raise ValueError(f"unknown capabilities: {', '.join(sorted(unknown))}")
    missing = sorted(required - granted)
    if args.interactive:
        for capability in missing:
            answer = input(f"Approve capability '{capability}' for {args.tab} rows {args.start_row}-{args.end_row}? [y/N] ")
            if answer.strip().lower() in {"y", "yes"}:
                granted.add(capability)
    approved = granted & required
    missing = sorted(required - approved)
    created = datetime.now(timezone.utc)
    receipt = {
        "receipt_version": 1,
        "run_id": args.run_id,
        "created_at": created.isoformat(),
        "expires_at": (created + timedelta(minutes=args.ttl_minutes)).isoformat(),
        "scope": {
            "spreadsheet_id": args.spreadsheet_id,
            "tab": args.tab,
            "start_row": args.start_row,
            "end_row": args.end_row,
        },
        "stages": sorted(stages),
        "requested_capabilities": sorted(granted & CAPABILITIES),
        "approved_capabilities": sorted(approved),
        "required_capabilities": sorted(required),
        "denied_capabilities": missing,
        "status": "approved" if not missing else "denied",
    }
    output = Path(args.receipt)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if not missing else 2


def verify(args: argparse.Namespace) -> int:
    receipt = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
    scope = receipt.get("scope", {})
    problems = []
    now = datetime.now(timezone.utc)
    try:
        expires_at = datetime.fromisoformat(receipt["expires_at"])
        if now >= expires_at:
            problems.append("receipt has expired")
    except (KeyError, ValueError):
        problems.append("receipt has no valid expiry")
    if receipt.get("status") != "approved":
        problems.append("receipt is not approved")
    if args.capability not in STAGE_CAPABILITIES.get(args.stage, set()):
        problems.append(f"capability is not required for stage: {args.stage}")
    if args.capability not in receipt.get("approved_capabilities", []):
        problems.append(f"capability not approved: {args.capability}")
    if args.stage not in receipt.get("stages", []):
        problems.append(f"stage not approved: {args.stage}")
    if scope.get("tab") != args.tab:
        problems.append("tab is outside receipt scope")
    if args.spreadsheet_id and scope.get("spreadsheet_id") != args.spreadsheet_id:
        problems.append("spreadsheet is outside receipt scope")
    if args.start_row < scope.get("start_row", 0) or args.end_row > scope.get("end_row", 0):
        problems.append("physical rows are outside receipt scope")
    if problems:
        print("PREFLIGHT DENIED: " + "; ".join(problems), file=sys.stderr)
        return 2
    print("PREFLIGHT APPROVED")
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)
    req = sub.add_parser("request", help="create a permission receipt")
    req.add_argument("--receipt", required=True)
    req.add_argument("--run-id", required=True)
    req.add_argument("--config")
    req.add_argument("--spreadsheet-id")
    req.add_argument("--tab")
    req.add_argument("--start-row", type=int, required=True)
    req.add_argument("--end-row", type=int, required=True)
    req.add_argument("--stages", required=True)
    req.add_argument("--grant", default="")
    req.add_argument("--interactive", action="store_true")
    req.add_argument("--ttl-minutes", type=int, default=480)
    req.set_defaults(func=request)
    check = sub.add_parser("verify", help="verify a receipt before an operation")
    check.add_argument("--receipt", required=True)
    check.add_argument("--capability", choices=sorted(CAPABILITIES), required=True)
    check.add_argument("--stage", choices=sorted(STAGE_CAPABILITIES), required=True)
    check.add_argument("--spreadsheet-id", default="")
    check.add_argument("--tab", required=True)
    check.add_argument("--start-row", type=int, required=True)
    check.add_argument("--end-row", type=int, required=True)
    check.set_defaults(func=verify)
    return root


if __name__ == "__main__":
    try:
        args = parser().parse_args()
        raise SystemExit(args.func(args))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"PREFLIGHT ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
