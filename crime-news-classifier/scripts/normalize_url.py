#!/usr/bin/env python3
"""Print a stable cache key for a URL while preserving the original URL elsewhere."""

from __future__ import annotations

import argparse
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING_PREFIXES = ("utm_", "ga_", "mc_", "ref")
TRACKING_NAMES = {"fbclid", "gclid", "dclid", "yclid", "msclkid"}


def normalize_url(value: str) -> str:
    parts = urlsplit(value.strip())
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    if not scheme or not host:
        raise ValueError("URL must include a scheme and host")
    port = parts.port
    default_port = (scheme == "http" and port == 80) or (scheme == "https" and port == 443)
    netloc = host if not port or default_port else f"{host}:{port}"
    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/")
    query_pairs = []
    for key, val in parse_qsl(parts.query, keep_blank_values=True):
        lowered = key.lower()
        if lowered in TRACKING_NAMES or lowered.startswith(TRACKING_PREFIXES):
            continue
        query_pairs.append((key, val))
    query_pairs.sort()
    return urlunsplit((scheme, netloc, path, urlencode(query_pairs), ""))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    print(normalize_url(args.url))


if __name__ == "__main__":
    main()
