#!/usr/bin/env python3
"""Validate Open Graph and Twitter metadata across the 30 active AXIONA pages."""

from __future__ import annotations

import argparse
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
HOST = "https://axiona.systems"
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
OG_REQUIRED = (
    "og:site_name",
    "og:title",
    "og:description",
    "og:type",
    "og:url",
    "og:image",
    "og:image:secure_url",
    "og:image:width",
    "og:image:height",
    "og:image:type",
)
TWITTER_REQUIRED = (
    "twitter:card",
    "twitter:title",
    "twitter:description",
    "twitter:image",
)


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.og: dict[str, list[str]] = {}
        self.twitter: dict[str, list[str]] = {}
        self.canonicals: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): (value or "").strip() for key, value in attrs}
        if tag.lower() == "meta":
            prop = values.get("property", "").lower()
            name = values.get("name", "").lower()
            content = values.get("content", "")
            if prop.startswith("og:"):
                self.og.setdefault(prop, []).append(content)
            if name.startswith("twitter:"):
                self.twitter.setdefault(name, []).append(content)
        elif tag.lower() == "link":
            rel = set(values.get("rel", "").lower().split())
            if "canonical" in rel and values.get("href"):
                self.canonicals.append(values["href"])


def public_url(prefix: str, route: str) -> str:
    return f"{HOST}/{prefix}" if route == "index.html" else f"{HOST}/{prefix}{route}"


def expected_image(lang: str, route: str) -> str:
    stem = "axiona-keeper-social-preview-r92" if route == "keeper.html" else "axiona-social-preview-r92"
    return f"{HOST}/assets/social/{stem}-{lang}.png"


def png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    if len(raw) < 24 or raw[:8] != b"\x89PNG\r\n\x1a\n" or raw[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", raw[16:24])


def verify(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for lang, prefix in LANGS.items():
        for route in ROUTES:
            page = root / prefix / route
            label = page.relative_to(root).as_posix()
            if not page.is_file():
                errors.append(f"social page missing: {label}")
                continue

            parser = MetaParser()
            parser.feed(page.read_text(encoding="utf-8"))

            for key in OG_REQUIRED:
                values = parser.og.get(key, [])
                if len(values) != 1 or not values[0]:
                    errors.append(f"social OG field mismatch: {label} -> {key}={values or '<missing>'}")
            for key in TWITTER_REQUIRED:
                values = parser.twitter.get(key, [])
                if len(values) != 1 or not values[0]:
                    errors.append(f"social Twitter field mismatch: {label} -> {key}={values or '<missing>'}")

            expected_url = public_url(prefix, route)
            if parser.og.get("og:site_name") != ["AXIONA Systems"]:
                errors.append(f"social og:site_name mismatch: {label}")
            if parser.og.get("og:type") != ["website"]:
                errors.append(f"social og:type mismatch: {label}")
            if parser.og.get("og:url") != [expected_url]:
                errors.append(f"social og:url mismatch: {label}")
            if parser.canonicals != [expected_url]:
                errors.append(f"social canonical mismatch: {label}")

            image = expected_image(lang, route)
            if parser.og.get("og:image") != [image]:
                errors.append(f"social og:image mismatch: {label}")
            if parser.og.get("og:image:secure_url") != [image]:
                errors.append(f"social og:image:secure_url mismatch: {label}")
            if parser.twitter.get("twitter:image") != [image]:
                errors.append(f"social twitter:image mismatch: {label}")
            if parser.og.get("og:image:width") != ["1200"]:
                errors.append(f"social image width mismatch: {label}")
            if parser.og.get("og:image:height") != ["630"]:
                errors.append(f"social image height mismatch: {label}")
            if parser.og.get("og:image:type") != ["image/png"]:
                errors.append(f"social image type mismatch: {label}")
            if parser.twitter.get("twitter:card") != ["summary_large_image"]:
                errors.append(f"social twitter:card mismatch: {label}")

    for lang in LANGS:
        for keeper in (False, True):
            stem = "axiona-keeper-social-preview-r92" if keeper else "axiona-social-preview-r92"
            image_path = root / "assets" / "social" / f"{stem}-{lang}.png"
            dims = png_dimensions(image_path)
            if dims != (1200, 630):
                errors.append(
                    f"social image asset mismatch: {image_path.relative_to(root).as_posix()} -> {dims or '<invalid>'}"
                )

    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = cli.parse_args()
    errors = verify(args.root)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_SOCIAL_METADATA: {error}", file=sys.stderr)
        return 1
    print("OK_AXIONA_SOCIAL_METADATA_R132")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
