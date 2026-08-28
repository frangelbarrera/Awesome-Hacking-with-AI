#!/usr/bin/env python3
"""Export normalized catalog tables to a machine-readable JSON artifact."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / 'docs' / 'RESOURCE_CATALOG.md', ROOT / 'docs' / 'RESOURCE_CATALOG_SUPPLEMENT.md']
OUTPUT = ROOT / 'docs' / 'resource-catalog.json'
LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')


def field_name(value: str) -> str:
    value = value.lower().replace('/', '_').replace(' ', '_').replace('-', '_')
    return re.sub(r'_+', '_', re.sub(r'[^a-z0-9_]', '', value)).strip('_')


def parse_table(source: Path, heading: str, header: list[str], rows: list[str]) -> list[dict]:
    entries = []
    keys = [field_name(item) for item in header]
    for row in rows:
        cells = [cell.strip() for cell in row.strip().split('|')[1:-1]]
        if len(cells) != len(keys):
            continue
        match = LINK.search(cells[0])
        if not match:
            continue
        entry = {
            'name': match.group(1),
            'canonical_url': match.group(2),
            'catalog_source': str(source.relative_to(ROOT)),
            'catalog_section': heading,
        }
        for key, value in zip(keys[1:], cells[1:]):
            entry[key] = value
        entries.append(entry)
    return entries


def collect(source: Path) -> list[dict]:
    lines = source.read_text(encoding='utf-8').splitlines()
    heading = ''
    output = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith('## '):
            heading = line[3:].strip()
        if line.startswith('| Resource |') and index + 1 < len(lines) and lines[index + 1].startswith('|---'):
            header = [cell.strip() for cell in line.split('|')[1:-1]]
            rows = []
            index += 2
            while index < len(lines) and lines[index].startswith('|'):
                rows.append(lines[index])
                index += 1
            output.extend(parse_table(source, heading, header, rows))
            continue
        index += 1
    return output


def render() -> str:
    entries = []
    for source in SOURCES:
        entries.extend(collect(source))
    document = {
        'schema_version': '1.0',
        'generated_from': [str(source.relative_to(ROOT)) for source in SOURCES],
        'entry_count': len(entries),
        'entries': entries,
    }
    return json.dumps(document, indent=2, ensure_ascii=False) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if the committed JSON is stale.')
    args = parser.parse_args()
    rendered = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding='utf-8') != rendered:
            print('resource-catalog.json is missing or out of date; run scripts/export_catalog.py')
            sys.exit(1)
        print('Machine-readable catalog is current.')
    else:
        OUTPUT.write_text(rendered, encoding='utf-8')
        print(f'Wrote {OUTPUT.relative_to(ROOT)}')
