#!/usr/bin/env python3
"""Public artifact custody/exclusion tests using synthetic Git objects."""
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest

from build_local_public_artifact import ArtifactError, PAGES, ROOT_FILES, build


class ArtifactTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'source'
        self.repo.mkdir()
        self.git('init', '-q')
        self.git('config', 'user.name', 'Synthetic artifact test')
        self.git('config', 'user.email', 'synthetic-artifact-test')
        paths = ROOT_FILES | PAGES | {f'{locale}/{page}' for locale in ('en', 'de') for page in PAGES}
        for name in paths | {'assets/example.css', 'CNAME', '.github/workflows/private.yml', 'docs/internal.md', 'scripts/tool.py'}:
            p = self.repo / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(('synthetic:' + name).encode())
        self.commit()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], stderr=subprocess.DEVNULL).decode().strip()

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'synthetic input')
        self.sha = self.git('rev-parse', 'HEAD')

    def test_reproducible_archive_excludes_domain_and_engineering(self):
        first = build(self.repo, self.sha, self.root / 'a')
        second = build(self.repo, self.sha, self.root / 'b')
        self.assertEqual(first, second)
        self.assertEqual((self.root / 'a/public.tar').read_bytes(), (self.root / 'b/public.tar').read_bytes())
        with tarfile.open(self.root / 'a/public.tar') as archive:
            names = archive.getnames()
            self.assertEqual(names, sorted(names))
            self.assertFalse(any(n == 'CNAME' or n.startswith(('.github/', 'docs/', 'scripts/')) for n in names))
            for member in archive:
                self.assertTrue(member.isfile())
                self.assertEqual(archive.extractfile(member).read(), self.git_bytes(member.name))
        self.assertEqual(first['release_admission'], 'PENDING')
        self.assertFalse(first['deployment_performed'])

    def git_bytes(self, name):
        return subprocess.check_output(['git', '-C', str(self.repo), 'show', self.sha + ':' + name])

    def test_worktree_edit_does_not_change_exact_commit_bytes(self):
        (self.repo / 'index.html').write_text('uncommitted replacement')
        build(self.repo, self.sha, self.root / 'artifact')
        with tarfile.open(self.root / 'artifact/public.tar') as archive:
            self.assertEqual(archive.extractfile('index.html').read(), b'synthetic:index.html')

    def test_replacement_ref_cannot_substitute_retained_blob_bytes(self):
        original = self.git('rev-parse', self.sha + ':index.html')
        replacement = subprocess.check_output(
            ['git', '-C', str(self.repo), 'hash-object', '-w', '--stdin'],
            input=b'replacement bytes outside selected commit',
        ).decode().strip()
        self.git('replace', original, replacement)
        self.assertEqual(self.git_bytes('index.html'), b'replacement bytes outside selected commit')
        manifest = build(self.repo, self.sha, self.root / 'replacement-proof')
        with tarfile.open(self.root / 'replacement-proof/public.tar') as archive:
            self.assertEqual(archive.extractfile('index.html').read(), b'synthetic:index.html')
        self.assertEqual(next(f['git_blob'] for f in manifest['files'] if f['path'] == 'index.html'), original)

    def test_replacement_commit_cannot_redirect_selected_tree(self):
        original, tree = self.sha, self.git('rev-parse', self.sha + '^{tree}')
        (self.repo / 'index.html').write_text('replacement commit content')
        self.commit()
        self.git('replace', original, self.sha)
        self.assertNotEqual(self.git('rev-parse', original + '^{tree}'), tree)
        manifest = build(self.repo, original, self.root / 'commit-replacement-proof')
        self.assertEqual(manifest['source_commit'], original)
        self.assertEqual(manifest['source_tree'], tree)
        with tarfile.open(self.root / 'commit-replacement-proof/public.tar') as archive:
            self.assertEqual(archive.extractfile('index.html').read(), b'synthetic:index.html')

    def test_public_symlink_and_unadmitted_asset_are_rejected_before_output(self):
        (self.repo / 'assets/secret.key').write_text('synthetic forbidden asset')
        self.commit()
        with self.assertRaises(ArtifactError):
            build(self.repo, self.sha, self.root / 'bad-type')
        self.assertFalse((self.root / 'bad-type').exists())
        (self.repo / 'assets/secret.key').unlink()
        (self.repo / 'assets/link.css').symlink_to('../index.html')
        self.commit()
        with self.assertRaises(ArtifactError):
            build(self.repo, self.sha, self.root / 'bad-link')
        self.assertFalse((self.root / 'bad-link').exists())

    def test_missing_page_revision_alias_and_output_overwrite_are_rejected(self):
        with self.assertRaises(ArtifactError):
            build(self.repo, 'HEAD', self.root / 'alias')
        with self.assertRaises(ArtifactError):
            build(self.repo, self.sha, self.repo / 'artifact')
        build(self.repo, self.sha, self.root / 'kept')
        before = (self.root / 'kept/public.tar').read_bytes()
        with self.assertRaises(ArtifactError):
            build(self.repo, self.sha, self.root / 'kept')
        self.assertEqual(before, (self.root / 'kept/public.tar').read_bytes())
        (self.repo / 'en/index.html').unlink()
        self.commit()
        with self.assertRaises(ArtifactError):
            build(self.repo, self.sha, self.root / 'missing')
        self.assertFalse((self.root / 'missing').exists())

    def test_new_public_route_requires_recipe_admission(self):
        (self.repo / 'new-page.html').write_text('new synthetic route')
        self.commit()
        with self.assertRaises(ArtifactError):
            build(self.repo, self.sha, self.root / 'new-route')
        self.assertFalse((self.root / 'new-route').exists())


if __name__ == '__main__':
    unittest.main()
