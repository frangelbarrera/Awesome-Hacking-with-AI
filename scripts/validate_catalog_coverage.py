#!/usr/bin/env python3
"""Ensure public resource URLs promoted in README have catalog metadata."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
CATALOGS = [ROOT / 'docs' / 'RESOURCE_CATALOG.md', ROOT / 'docs' / 'RESOURCE_CATALOG_SUPPLEMENT.md']
URL_RE = re.compile(r'https?://[^\s)"<>]+')
EXEMPT_HOSTS = {'img.shields.io', 'awesome.re'}
EXEMPT_PREFIXES = (
    'https://github.com/frangelbarrera/Awesome-Hacking-with-AI',
    'https://cheatsheetseries.owasp.org/',
    'https://certcc.github.io/',
)

def urls(path: Path) -> set[str]:
    return {value.rstrip('.,') for value in URL_RE.findall(path.read_text(encoding='utf-8'))}

readme_body = README.read_text(encoding='utf-8').split('\n## References\n', 1)[0]
readme_urls = {value.rstrip('.,') for value in URL_RE.findall(readme_body)}
catalog_urls = set().union(*(urls(path) for path in CATALOGS))

required = {
    url for url in readme_urls
    if urlparse(url).netloc not in EXEMPT_HOSTS and not url.startswith(EXEMPT_PREFIXES)
}
missing = sorted(required - catalog_urls)
if missing:
    print('README resource URLs without catalog metadata:')
    print('\n'.join(f'- {url}' for url in missing))
    sys.exit(1)
print(f'Catalog coverage passed: {len(required)} README resource URLs have catalog metadata.')
