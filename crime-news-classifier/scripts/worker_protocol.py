#!/usr/bin/env python3
"""Build and validate narrow worker envelopes for delegated classification stages."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from preflight import STAGE_CAPABILITIES


ROLE_CAPABILITIES = {
    "sheet_worker": {"sheet_read", "sheet_write", "local_state_write"},
    "metadata_worker": {"local_state_read", "ai_decision"},
    "article_fetch_worker": {"article_fetch", "local_state_read", "local_state_write"},
    "category_worker": {"local_state_read", "ai_decision"},
    "bad_category_worker": {"local_state_read", "ai_decision"},
    "policy_worker": {"local_state_read", "ai_decision"},
    "taxonomy_worker": {"local_state_read", "local_state_write", "taxonomy_write", "ai_decision"},
}

ROLE_TOOLS = {
    "sheet_worker": ["sheet.exact_read", "sheet.exact_write", "local.receipt_write"],
    "metadata_worker": ["local.read", "ai.classify"],
    "article_fetch_worker": ["article.fetch_assigned", "local.read", "local.write"],
    "category_worker": ["local.read", "ai.classify"],
    "bad_category_worker": ["local.read", "ai.classify"],
    "policy_worker": ["local.read", "ai.classify"],
    "taxonomy_worker": ["local.read", "local.write_proposal", "ai.classify"],
}

ROLE_REFERENCES = {
    "sheet_worker": ["references/worker-contracts.md", "references/output-schema.md", "references/preflight.md"],
    "metadata_worker": ["references/worker-contracts.md", "references/primary-taxonomy.md", "references/category-selection.md"],
    "article_fetch_worker": ["references/worker-contracts.md", "references/local-state.md"],
    "category_worker": ["references/worker-contracts.md", "references/output-schema.md", "references/primary-taxonomy.md", "references/category-selection.md"],
    "bad_category_worker": ["references/worker-contracts.md", "references/output-schema.md", "references/bad-taxonomy.md"],
    "policy_worker": ["references/worker-contracts.md", "references/output-schema.md", "references/policy-boundary.md"],
    "taxonomy_worker": ["references/worker-contracts.md", "references/local-state.md", "references/primary-taxonomy.md", "references/category-selection.md"],
}

ROLE_STAGE_REQUIREMENTS = {
    "sheet_worker": {"metadata": {"sheet_read"}, "writeback": {"sheet_read", "sheet_write", "local_state_write"}},
    "metadata_worker": {"metadata": {"local_state_read", "ai_decision"}},
    "article_fetch_worker": {"article_fetch": {"article_fetch", "local_state_read", "local_state_write"}},
    "category_worker": {"category": {"local_state_read", "ai_decision"}},
    "bad_category_worker": {"bad_category": {"local_state_read", "ai_decision"}},
    "policy_worker": {"policy": {"local_state_read", "ai_decision"}},
    "taxonomy_worker": {"taxonomy": {"local_state_read", "local_state_write", "taxonomy_write", "ai_decision"}},
}


def read_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def build(args: argparse.Namespace) -> int:
    receipt = read_json(args.receipt)
    scope = receipt.get("scope", {})
    approved = set(receipt.get("approved_capabilities", []))
    if receipt.get("status") != "approved":
        raise ValueError("permission receipt is not approved")
    try:
        if datetime.now(timezone.utc) >= datetime.fromisoformat(receipt["expires_at"]):
            raise ValueError("permission receipt has expired")
    except KeyError as exc:
        raise ValueError("permission receipt has no expiry") from exc
    if args.stage not in receipt.get("stages", []):
        raise ValueError(f"stage is not approved: {args.stage}")
    if scope.get("tab") != args.tab or args.start_row < scope.get("start_row", 0) or args.end_row > scope.get("end_row", 0):
        raise ValueError("worker rows or tab exceed receipt scope")
    if args.role not in ROLE_CAPABILITIES:
        raise ValueError(f"unknown worker role: {args.role}")
    effective = sorted(approved & ROLE_CAPABILITIES[args.role])
    stage_required = STAGE_CAPABILITIES.get(args.stage, set())
    worker_required = ROLE_STAGE_REQUIREMENTS.get(args.role, {}).get(args.stage, set())
    if not stage_required or not worker_required:
        raise ValueError(f"role {args.role} cannot handle stage {args.stage}")
    if not stage_required <= approved:
        raise ValueError("receipt does not approve every capability required by this stage")
    if not worker_required <= approved:
        raise ValueError("receipt does not approve every capability required by this worker")
    missing = ROLE_CAPABILITIES[args.role] - approved
    input_path = Path(args.input).resolve()
    payload = {
        "protocol_version": 1,
        "status": "ready",
        "worker_id": args.worker_id,
        "role": args.role,
        "stage": args.stage,
        "skill": {
            "name": "crime-news-classifier",
            "entrypoint": str((Path(args.skill_dir).resolve() / "SKILL.md")),
            "references": ROLE_REFERENCES[args.role],
            "protected_context_required": True,
        },
        "scope": {"tab": args.tab, "start_row": args.start_row, "end_row": args.end_row},
        "approved_capabilities": effective,
        "role_capabilities": sorted(ROLE_CAPABILITIES[args.role]),
        "allowed_tools": ROLE_TOOLS[args.role],
        "input": {"path": str(input_path), "sha256": hashlib.sha256(input_path.read_bytes()).hexdigest()},
        "forbidden": ["broaden_scope", "fetch_unassigned_urls", "write_unapproved_sheet_range", "invent_missing_evidence"],
        "required_result_fields": ["worker_id", "role", "stage", "physical_rows", "capabilities_used"],
    }
    if missing:
        payload["missing_role_capabilities"] = sorted(missing)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0


def validate(args: argparse.Namespace) -> int:
    envelope = read_json(args.envelope)
    result = read_json(args.result)
    errors = []
    if envelope.get("status") != "ready":
        errors.append("envelope is not ready")
    for field in ("worker_id", "role", "stage"):
        if result.get(field) != envelope.get(field):
            errors.append(f"result {field} does not match envelope")
    scope = envelope.get("scope", {})
    rows = result.get("physical_rows")
    if not isinstance(rows, list) or any(not isinstance(row, int) for row in rows):
        errors.append("physical_rows must be a list of integers")
    else:
        if len(rows) != len(set(rows)):
            errors.append("duplicate physical rows")
        if any(row < scope.get("start_row", 0) or row > scope.get("end_row", 0) for row in rows):
            errors.append("result row outside envelope scope")
    used = set(result.get("capabilities_used", []))
    allowed = set(envelope.get("approved_capabilities", []))
    if not used <= allowed:
        errors.append("result claims an unapproved capability")
    if result.get("unauthorized_actions"):
        errors.append("result reports unauthorized actions")
    if errors:
        print("WORKER RESULT REJECTED: " + "; ".join(errors), file=sys.stderr)
        return 2
    print("WORKER RESULT ACCEPTED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("--receipt", required=True)
    build_parser.add_argument("--worker-id", required=True)
    build_parser.add_argument("--role", choices=sorted(ROLE_CAPABILITIES), required=True)
    build_parser.add_argument("--stage", required=True)
    build_parser.add_argument("--skill-dir", required=True)
    build_parser.add_argument("--tab", required=True)
    build_parser.add_argument("--start-row", type=int, required=True)
    build_parser.add_argument("--end-row", type=int, required=True)
    build_parser.add_argument("--input", required=True)
    build_parser.add_argument("--output", required=True)
    build_parser.set_defaults(func=build)
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("--envelope", required=True)
    validate_parser.add_argument("--result", required=True)
    validate_parser.set_defaults(func=validate)
    args = parser.parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"WORKER PROTOCOL ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
