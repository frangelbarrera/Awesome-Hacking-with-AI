#!/usr/bin/env python3
"""Validate integrity of the generated resource catalog artifact."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "resource-catalog.json"
EXPECTED_SOURCES = {
    "docs/RESOURCE_CATALOG.md",
    "docs/RESOURCE_CATALOG_SUPPLEMENT.md",
}
REQUIRED_FIELDS = {
    "name",
    "canonical_url",
    "catalog_source",
    "catalog_section",
}


def fail(message: str) -> None:
    print(f"Catalog integrity failed: {message}")
    raise SystemExit(1)


if not CATALOG.exists():
    fail("docs/resource-catalog.json is missing; run scripts/export_catalog.py")

try:
    document = json.loads(CATALOG.read_text(encoding="utf-8"))
except json.JSONDecodeError as error:
    fail(f"invalid JSON: {error}")

if document.get("schema_version") != "1.0":
    fail("unsupported or missing schema_version")
if set(document.get("generated_from", [])) != EXPECTED_SOURCES:
    fail("generated_from does not list the canonical catalog Markdown sources")

entries = document.get("entries")
if not isinstance(entries, list):
    fail("entries must be an array")
if document.get("entry_count") != len(entries):
    fail(f"entry_count={document.get('entry_count')} does not match entries={len(entries)}")

seen_urls: set[str] = set()
for index, entry in enumerate(entries, start=1):
    if not isinstance(entry, dict):
        fail(f"entry {index} is not an object")
    missing = sorted(REQUIRED_FIELDS - entry.keys())
    if missing:
        fail(f"entry {index} is missing required fields: {', '.join(missing)}")
    url = entry["canonical_url"]
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(f"entry {index} has an invalid canonical_url: {url!r}")
    if url in seen_urls:
        fail(f"duplicate canonical_url: {url}")
    seen_urls.add(url)

print(f"Catalog integrity passed: {len(entries)} entries with unique canonical URLs.")
