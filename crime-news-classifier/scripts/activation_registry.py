#!/usr/bin/env python3
"""Track skill activation once per session and expose durable context metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def skill_hash(skill_file: Path) -> str:
    return hashlib.sha256(skill_file.read_bytes()).hexdigest()


def resource_paths(skill_dir: Path) -> list[str]:
    resources = []
    for path in sorted(skill_dir.glob("references/*")):
        if path.is_file():
            resources.append(str(path.relative_to(skill_dir)))
    for path in sorted(skill_dir.glob("scripts/*")):
        if path.is_file():
            resources.append(str(path.relative_to(skill_dir)))
    return resources


def load(path: Path) -> dict:
    if not path.exists():
        return {"registry_version": 1, "sessions": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def activate(args: argparse.Namespace) -> int:
    skill_dir = Path(args.skill_dir).resolve()
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise SystemExit(f"missing skill entrypoint: {skill_file}")
    data = load(Path(args.registry))
    sessions = data.setdefault("sessions", {})
    session = sessions.setdefault(args.session_id, {"skills": {}})
    skills = session.setdefault("skills", {})
    digest = skill_hash(skill_file)
    previous = skills.get(args.skill_name)
    status = "already_active" if previous and previous.get("content_sha256") == digest else "activated"
    timestamp = now()
    entry = {
        "skill_name": args.skill_name,
        "skill_dir": str(skill_dir),
        "skill_file": str(skill_file),
        "content_sha256": digest,
        "first_activated_at": previous.get("first_activated_at", timestamp) if previous else timestamp,
        "last_activated_at": timestamp,
        "activation_count": (previous.get("activation_count", 0) + 1) if previous else 1,
        "protected_context": True,
        "deduplication_key": f"{args.session_id}:{args.skill_name}:{digest}",
        "resources": resource_paths(skill_dir),
    }
    skills[args.skill_name] = entry
    save(Path(args.registry), data)
    print(json.dumps({"status": status, "context_manifest": entry}, indent=2))
    return 0


def check(args: argparse.Namespace) -> int:
    data = load(Path(args.registry))
    entry = data.get("sessions", {}).get(args.session_id, {}).get("skills", {}).get(args.skill_name)
    if not entry:
        print("NOT_ACTIVE")
        return 2
    if args.skill_dir and entry.get("content_sha256") != skill_hash(Path(args.skill_dir).resolve() / "SKILL.md"):
        print("STALE_ACTIVATION")
        return 2
    print(json.dumps(entry, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    activate_parser = sub.add_parser("activate")
    activate_parser.add_argument("--registry", required=True)
    activate_parser.add_argument("--session-id", required=True)
    activate_parser.add_argument("--skill-name", required=True)
    activate_parser.add_argument("--skill-dir", required=True)
    activate_parser.set_defaults(func=activate)
    check_parser = sub.add_parser("check")
    check_parser.add_argument("--registry", required=True)
    check_parser.add_argument("--session-id", required=True)
    check_parser.add_argument("--skill-name", required=True)
    check_parser.add_argument("--skill-dir")
    check_parser.set_defaults(func=check)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
