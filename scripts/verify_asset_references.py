#!/usr/bin/env python3
"""Verify the public runtime asset graph and canonical correction bindings."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path('.')
ASSET_RE = re.compile(r'(?:https://axiona\.systems)?(/assets/[A-Za-z0-9_./-]+)')
CSS_URL_RE = re.compile(r'url\(\s*["\']?([^\)"\']+)')

runtime_sources: list[Path] = []
for path in ROOT.rglob('*'):
    if not path.is_file():
        continue
    if any(part in {'.git', '.lighthouseci', 'node_modules'} for part in path.parts):
        continue
    if path.suffix.lower() in {'.html', '.css', '.js', '.mjs', '.json', '.xml'} or path.name == 'site.webmanifest':
        runtime_sources.append(path)

referenced: set[str] = set()
missing: list[tuple[str, str]] = []

for source in sorted(runtime_sources):
    try:
        text = source.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue

    for match in ASSET_RE.finditer(text):
        rel = match.group(1).lstrip('/').split('?', 1)[0].split('#', 1)[0]
        referenced.add(rel)
        if not (ROOT / rel).is_file():
            missing.append((source.as_posix(), rel))

    if source.suffix.lower() == '.css':
        for match in CSS_URL_RE.finditer(text):
            raw = match.group(1).strip()
            if not raw or raw.startswith(('data:', 'http://', 'https://', '#', '/')):
                continue
            clean = raw.split('?', 1)[0].split('#', 1)[0]
            resolved = (source.parent / clean).resolve()
            try:
                rel = resolved.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                continue
            if rel.startswith('assets/'):
                referenced.add(rel)
                if not (ROOT / rel).is_file():
                    missing.append((source.as_posix(), rel))

errors: list[str] = []
if missing:
    for source, rel in missing:
        errors.append(f'{source}: missing local asset {rel}')

for stale in ('assets/r135-ux-fixes.css', 'assets/r136-ux-fixes.css', 'assets/motion-r105.css', 'assets/motion-r108.css'):
    if (ROOT / stale).exists():
        errors.append(f'stale compatibility asset still exists: {stale}')

public_html = sorted([*ROOT.glob('*.html'), *Path('en').glob('*.html'), *Path('de').glob('*.html')])
for path in public_html:
    text = path.read_text(encoding='utf-8')
    expectations = {
        '/assets/r137-ux-fixes.css?release=R137': 1,
        '/assets/motion-r138.css?release=R142': 1,
        '/assets/js/motion-r138.js?release=R142': 1,
    }
    for token, expected in expectations.items():
        count = text.count(token)
        if count != expected:
            errors.append(f'{path}: {token} count={count}, expected={expected}')
    if 'r135-ux-fixes.css' in text or 'r136-ux-fixes.css' in text:
        errors.append(f'{path}: stale R135/R136 binding present')

manifest = Path('site.webmanifest').read_text(encoding='utf-8')
for icon in ('/assets/brand/axiona-icon-192.png', '/assets/brand/axiona-icon-512.png'):
    if icon not in manifest:
        errors.append(f'site.webmanifest missing required icon {icon}')

if errors:
    print('STOP_AXIONA_ASSET_REFERENCES')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'OK_AXIONA_ASSET_REFERENCES sources={len(runtime_sources)} refs={len(referenced)} html={len(public_html)}')
