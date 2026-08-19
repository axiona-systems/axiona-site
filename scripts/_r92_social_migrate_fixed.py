#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import _r92_social_migrate as migration


def migrate_html_fixed() -> None:
    for prefix, lang in migration.LOCALES:
        for route in migration.ROUTES:
            path = migration.ROOT / prefix / route
            text = path.read_text(encoding="utf-8")
            target = migration.image_url(lang, route == "keeper.html")

            og_pattern = r'<meta content="[^"]+" property="og:image"/>'
            og_repl = f'<meta content="{target}" property="og:image"/>'
            text, og_count = re.subn(og_pattern, og_repl, text, count=1)
            if og_count != 1:
                raise RuntimeError(f"expected exactly one og:image in {path}, got {og_count}")

            secure_pattern = r'<meta content="[^"]+" property="og:image:secure_url"/>'
            secure_repl = f'<meta content="{target}" property="og:image:secure_url"/>'
            text, secure_count = re.subn(secure_pattern, secure_repl, text, count=1)
            if secure_count == 0:
                anchor = og_repl
                text = text.replace(anchor, anchor + "\n  " + secure_repl, 1)
            elif secure_count != 1:
                raise RuntimeError(f"expected at most one og:image:secure_url in {path}, got {secure_count}")

            twitter_pattern = r'<meta content="[^"]+" name="twitter:image"/>'
            twitter_repl = f'<meta content="{target}" name="twitter:image"/>'
            text, twitter_count = re.subn(twitter_pattern, twitter_repl, text, count=1)
            if twitter_count != 1:
                raise RuntimeError(f"expected exactly one twitter:image in {path}, got {twitter_count}")

            path.write_text(text, encoding="utf-8")


original_commit_changes = migration.commit_changes


def commit_changes_fixed() -> None:
    docs = migration.ROOT / "Docs/AXIONA_WEBSITE_MAINTENANCE.md"
    docs.write_text(docs.read_text(encoding="utf-8").rstrip() + "\n", encoding="utf-8")
    helper = migration.ROOT / "scripts/_r92_social_migrate_fixed.py"
    if helper.exists():
        helper.unlink()
    original_commit_changes()


migration.migrate_html = migrate_html_fixed
migration.commit_changes = commit_changes_fixed

if __name__ == "__main__":
    raise SystemExit(migration.main())
