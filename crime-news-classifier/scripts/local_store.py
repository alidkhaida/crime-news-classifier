#!/usr/bin/env python3
"""Initialize and inspect the durable local classification cache."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS articles (
  url_key TEXT PRIMARY KEY,
  original_url TEXT NOT NULL,
  input_fingerprint TEXT,
  title TEXT,
  description TEXT,
  final_url TEXT,
  content_hash TEXT,
  text_path TEXT,
  fetch_status TEXT NOT NULL DEFAULT 'new',
  fetched_at TEXT
);
CREATE TABLE IF NOT EXISTS classifications (
  url_key TEXT NOT NULL,
  taxonomy_version TEXT NOT NULL,
  policy_version TEXT NOT NULL,
  result_json TEXT NOT NULL,
  classification_status TEXT NOT NULL,
  classified_at TEXT,
  PRIMARY KEY (url_key, taxonomy_version, policy_version)
);
CREATE TABLE IF NOT EXISTS row_receipts (
  run_id TEXT NOT NULL,
  physical_row INTEGER NOT NULL,
  url_key TEXT NOT NULL,
  source_fingerprint TEXT,
  write_range TEXT,
  readback_verified INTEGER NOT NULL DEFAULT 0,
  conflict_reason TEXT,
  PRIMARY KEY (run_id, physical_row)
);
CREATE TABLE IF NOT EXISTS taxonomy_candidates (
  parent_category TEXT NOT NULL,
  normalized_candidate TEXT NOT NULL,
  evidence_count INTEGER NOT NULL DEFAULT 0,
  examples_json TEXT NOT NULL DEFAULT '[]',
  status TEXT NOT NULL DEFAULT 'pending',
  PRIMARY KEY (parent_category, normalized_candidate)
);
"""


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.execute("PRAGMA journal_mode=WAL")
    db.executescript(SCHEMA)
    db.commit()
    return db


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("db", type=Path)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    lookup = sub.add_parser("lookup")
    lookup.add_argument("url_key")
    args = parser.parse_args()
    db = connect(args.db)
    if args.command == "init":
        print(f"initialized: {args.db}")
        return
    row = db.execute("SELECT * FROM articles WHERE url_key = ?", (args.url_key,)).fetchone()
    print(json.dumps(row, ensure_ascii=False) if row else "null")


if __name__ == "__main__":
    main()
