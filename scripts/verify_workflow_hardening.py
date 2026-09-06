#!/usr/bin/env python3
"""Fail closed on GitHub Actions hardening regressions.

The public website repository intentionally keeps a very small Actions surface.
Every external action must be pinned by immutable full commit SHA and workflows
must declare least-privilege permissions explicitly at top level.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

WORKFLOW_DIR = Path('.github/workflows')
FULL_SHA = re.compile(r'^[0-9a-f]{40}$')
USES = re.compile(r'^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)', re.MULTILINE)
WRITE_SCOPE = re.compile(r'^\s{2,}([a-zA-Z-]+):\s*write\s*$', re.MULTILINE)

errors: list[str] = []
workflows = sorted([*WORKFLOW_DIR.glob('*.yml'), *WORKFLOW_DIR.glob('*.yaml')])

if not workflows:
    errors.append('no GitHub Actions workflows found')

for path in workflows:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()

    # Require an explicit top-level permissions key before jobs:.
    top_level_permissions = False
    for line in lines:
        if line.startswith('permissions:'):
            top_level_permissions = True
            break
        if line.startswith('jobs:'):
            break
    if not top_level_permissions:
        errors.append(f'{path}: missing top-level permissions block')

    if re.search(r'^\s*pull_request_target\s*:', text, re.MULTILINE):
        errors.append(f'{path}: pull_request_target is forbidden in the public-site repo')
    if re.search(r'^\s*permissions\s*:\s*write-all\s*$', text, re.MULTILINE):
        errors.append(f'{path}: write-all permissions are forbidden')
    if re.search(r'^\s*secrets\s*:\s*inherit\s*$', text, re.MULTILINE):
        errors.append(f'{path}: inherited secrets are forbidden')
    if re.search(r'(curl|wget)[^\n|]*\|\s*(ba)?sh\b', text):
        errors.append(f'{path}: network-to-shell execution is forbidden')

    for action, ref in USES.findall(text):
        if action.startswith('./'):
            continue
        if not FULL_SHA.fullmatch(ref):
            errors.append(f'{path}: action {action}@{ref} is not pinned to a full 40-char SHA')

    if 'actions/checkout@' in text and 'persist-credentials: false' not in text:
        errors.append(f'{path}: checkout must set persist-credentials: false')

    if 'npm install' in text and '--ignore-scripts' not in text:
        errors.append(f'{path}: npm install must disable lifecycle scripts')

    # Only the Pages publisher needs a write scope; all validation stays read-only.
    for scope in WRITE_SCOPE.findall(text):
        if path.name != 'axiona-pages-rebuild.yml' or scope != 'pages':
            errors.append(f'{path}: unexpected write permission {scope}: write')

allowed_names = {
    'axiona-repo-guard.yml',
    'axiona-browser-audit.yml',
    'axiona-render-contract.yml',
    'axiona-pages-rebuild.yml',
}
actual_names = {p.name for p in workflows}
extra = sorted(actual_names - allowed_names)
missing = sorted(allowed_names - actual_names)
if extra:
    errors.append('unexpected workflow files: ' + ', '.join(extra))
if missing:
    errors.append('missing canonical workflow files: ' + ', '.join(missing))

if errors:
    print('STOP_AXIONA_WORKFLOW_HARDENING')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'OK_AXIONA_WORKFLOW_HARDENING workflows={len(workflows)} actions=immutable permissions=least-privilege')
