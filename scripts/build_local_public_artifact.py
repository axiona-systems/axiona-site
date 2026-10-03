#!/usr/bin/env python3
"""Build immutable public bytes for an isolated HTTP proof; never publish them."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile

ROOT_FILES = frozenset({
    '.nojekyll', '.well-known/security.txt', '404.html', 'apple-touch-icon.png',
    'favicon-16x16.png', 'favicon-32x32.png', 'favicon.ico', 'favicon.svg',
    'humans.txt', 'robots.txt', 'site.webmanifest', 'sitemap.xml',
})
PAGES = frozenset({
    'index.html', 'contact.html', 'keeper.html', 'legal.html', 'privacy.html',
    'process.html', 'security.html', 'solutions.html', 'support.html', 'systems.html',
})
ASSET_EXTENSIONS = frozenset({'.css', '.js', '.svg', '.png', '.ico', '.json'})
SHA = re.compile(r'[0-9a-f]{40}')
PATH = re.compile(r'[A-Za-z0-9_.\-/]+')
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_ARCHIVE_INPUT_BYTES = 128 * 1024 * 1024
MAX_FILES = 512


class ArtifactError(ValueError):
    pass


def git(repo: Path, *args: str) -> bytes:
    result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True)
    if result.returncode:
        raise ArtifactError('Git source unavailable')
    return result.stdout


def public_path(name: str) -> bool:
    path = PurePosixPath(name)
    if not PATH.fullmatch(name) or path.is_absolute() or any(p in {'.', '..'} for p in path.parts):
        raise ArtifactError('unsafe source path')
    if name in ROOT_FILES or name in PAGES:
        return True
    if len(path.parts) == 2 and path.parts[0] in {'en', 'de'} and path.name in PAGES:
        return True
    if path.suffix == '.html' and (len(path.parts) == 1 or path.parts[0] in {'en', 'de'}):
        raise ArtifactError('new public route requires recipe admission')
    if path.parts[0] == 'assets':
        if path.suffix not in ASSET_EXTENSIONS or any(p.startswith('.') for p in path.parts):
            raise ArtifactError('unadmitted asset type')
        return True
    return False


def collect(repo: Path, revision: str) -> tuple[str, list[tuple[str, str, bytes]]]:
    if not SHA.fullmatch(revision):
        raise ArtifactError('exact immutable commit required')
    if git(repo, 'rev-parse', '--verify', revision + '^{commit}').decode().strip() != revision:
        raise ArtifactError('source commit mismatch')
    tree = git(repo, 'rev-parse', revision + '^{tree}').decode().strip()
    files = []
    total_bytes = 0
    for entry in git(repo, 'ls-tree', '-rz', revision).split(b'\0'):
        if not entry:
            continue
        metadata, raw_path = entry.split(b'\t', 1)
        try:
            name = raw_path.decode('utf-8')
        except UnicodeDecodeError as error:
            raise ArtifactError('source path encoding') from error
        if not public_path(name):
            continue
        mode, kind, oid = metadata.decode().split()
        if mode != '100644' or kind != 'blob':
            raise ArtifactError('public artifact requires regular non-executable files')
        size = int(git(repo, 'cat-file', '-s', oid))
        total_bytes += size
        if size > MAX_FILE_BYTES or total_bytes > MAX_ARCHIVE_INPUT_BYTES or len(files) >= MAX_FILES:
            raise ArtifactError('artifact size limit exceeded')
        files.append((name, oid, git(repo, 'cat-file', 'blob', oid)))
    names = {name for name, _, _ in files}
    required = ROOT_FILES | PAGES | {f'{locale}/{page}' for locale in ('en', 'de') for page in PAGES}
    if not required <= names:
        raise ArtifactError('required public surface missing')
    return tree, sorted(files)


def build(repo: Path, revision: str, output: Path) -> dict:
    # Output must be new and outside source: no retained bytes may be overwritten.
    if output.exists() or output.is_symlink():
        raise ArtifactError('output already exists')
    source = Path(git(repo, 'rev-parse', '--show-toplevel').decode().strip()).resolve()
    destination = output.resolve()
    if destination == source or source in destination.parents:
        raise ArtifactError('output must be outside source worktree')
    tree, files = collect(repo, revision)
    data = io.BytesIO()
    with tarfile.open(fileobj=data, mode='w', format=tarfile.USTAR_FORMAT) as archive:
        for name, _, content in files:
            info = tarfile.TarInfo(name)
            info.size, info.mode, info.mtime = len(content), 0o644, 0
            info.uid = info.gid = 0
            info.uname = info.gname = ''
            archive.addfile(info, io.BytesIO(content))
    artifact = data.getvalue()
    manifest = {
        'schema_version': 'axiona.site.local-public-artifact.v1',
        'source_commit': revision, 'source_tree': tree,
        'recipe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'archive_sha256': hashlib.sha256(artifact).hexdigest(),
        'archive_bytes': len(artifact), 'format': 'deterministic-ustar',
        'files': [{'path': name, 'git_blob': oid, 'bytes': len(content),
                   'sha256': hashlib.sha256(content).hexdigest()} for name, oid, content in files],
        'release_admission': 'PENDING', 'deployment_performed': False,
        'production_activation': 'BLOCKED',
    }
    output.mkdir(parents=True, exist_ok=False)
    (output / 'public.tar').write_bytes(artifact)
    (output / 'source-manifest.json').write_text(json.dumps(manifest, sort_keys=True, indent=2) + '\n')
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(args.repo, args.revision, args.output)
    except (ArtifactError, OSError, ValueError):
        print('STOP_LOCAL_PUBLIC_ARTIFACT')
        return 1
    print(json.dumps({k: result[k] for k in ('source_commit', 'archive_sha256', 'release_admission', 'deployment_performed')}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
