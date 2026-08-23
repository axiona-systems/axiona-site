#!/usr/bin/env python3
"""Validate favicon, Apple touch icon and Web App Manifest identity bindings."""

from __future__ import annotations

import argparse
import json
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
LANGS = {"hu": "", "en": "en/", "de": "de/"}
ROUTES = (
    "index.html",
    "systems.html",
    "process.html",
    "security.html",
    "solutions.html",
    "keeper.html",
    "contact.html",
    "privacy.html",
    "legal.html",
    "support.html",
)
EXPECTED_LINKS = {
    ("icon", "/favicon.svg", "image/svg+xml", ""),
    ("icon", "/favicon-32x32.png", "image/png", "32x32"),
    ("icon", "/favicon-16x16.png", "image/png", "16x16"),
    ("apple-touch-icon", "/apple-touch-icon.png", "", "180x180"),
    ("manifest", "/site.webmanifest", "", ""),
}
PNG_EXPECTED = {
    "favicon-32x32.png": (32, 32),
    "favicon-16x16.png": (16, 16),
    "apple-touch-icon.png": (180, 180),
    "assets/brand/axiona-icon-192.png": (192, 192),
    "assets/brand/axiona-icon-512.png": (512, 512),
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "link":
            return
        values = {key.lower(): (value or "").strip() for key, value in attrs}
        self.links.append(values)


def png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    if len(raw) < 24 or raw[:8] != b"\x89PNG\r\n\x1a\n" or raw[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", raw[16:24])


def normalized_identity_links(parser: LinkParser) -> list[tuple[str, str, str, str]]:
    result: list[tuple[str, str, str, str]] = []
    for link in parser.links:
        rel_tokens = link.get("rel", "").lower().split()
        if "manifest" in rel_tokens:
            result.append(("manifest", link.get("href", ""), link.get("type", ""), link.get("sizes", "")))
        if "apple-touch-icon" in rel_tokens:
            result.append(("apple-touch-icon", link.get("href", ""), link.get("type", ""), link.get("sizes", "")))
        if "icon" in rel_tokens:
            result.append(("icon", link.get("href", ""), link.get("type", ""), link.get("sizes", "")))
    return result


def verify(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    pages = [root / prefix / route for prefix in LANGS.values() for route in ROUTES] + [root / "404.html"]

    for page in pages:
        label = page.relative_to(root).as_posix()
        if not page.is_file():
            errors.append(f"browser identity page missing: {label}")
            continue
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        identity = normalized_identity_links(parser)

        if any("shortcut" in link.get("rel", "").lower().split() for link in parser.links):
            errors.append(f"browser identity nonconforming shortcut icon: {label}")

        observed = set(identity)
        if observed != EXPECTED_LINKS:
            errors.append(
                f"browser identity link mismatch: {label} -> observed={sorted(observed)!r} expected={sorted(EXPECTED_LINKS)!r}"
            )
        if len(identity) != len(EXPECTED_LINKS):
            errors.append(f"browser identity duplicate/missing link count: {label} -> {len(identity)}")

    for rel_path, expected in PNG_EXPECTED.items():
        dims = png_dimensions(root / rel_path)
        if dims != expected:
            errors.append(f"browser identity PNG mismatch: {rel_path} -> {dims or '<invalid>'}, expected {expected}")

    svg = root / "favicon.svg"
    if not svg.is_file() or "<svg" not in svg.read_text(encoding="utf-8", errors="ignore").lower():
        errors.append("browser identity favicon.svg missing or invalid")

    manifest_path = root / "site.webmanifest"
    if not manifest_path.is_file():
        errors.append("browser identity site.webmanifest missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"browser identity manifest invalid JSON: {exc}")
        else:
            exact = {
                "id": "/",
                "name": "AXIONA Systems",
                "short_name": "AXIONA",
                "start_url": "/",
                "scope": "/",
                "display": "standalone",
                "background_color": "#f6efe3",
                "theme_color": "#142d31",
            }
            for key, value in exact.items():
                if manifest.get(key) != value:
                    errors.append(f"browser identity manifest mismatch: {key}={manifest.get(key)!r}, expected {value!r}")
            icons = manifest.get("icons")
            expected_icons = [
                {"src": "/assets/brand/axiona-icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                {"src": "/assets/brand/axiona-icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            ]
            if icons != expected_icons:
                errors.append("browser identity manifest icon contract mismatch")

    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = cli.parse_args()
    errors = verify(args.root)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_BROWSER_IDENTITY: {error}", file=sys.stderr)
        return 1
    print("OK_AXIONA_BROWSER_IDENTITY_R134=31")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
