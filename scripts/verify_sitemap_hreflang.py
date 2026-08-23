#!/usr/bin/env python3
"""Verify AXIONA sitemap locale-family and hreflang invariants."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
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
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"


def public_url(prefix: str, route: str) -> str:
    if route == "index.html":
        return f"{HOST}/{prefix}"
    return f"{HOST}/{prefix}{route}"


def expected_hreflangs(route: str) -> dict[str, str]:
    hu = public_url("", route)
    return {
        "hu": hu,
        "en": public_url("en/", route),
        "de": public_url("de/", route),
        "x-default": hu,
    }


def expected_entries() -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for route in ROUTES:
        family = expected_hreflangs(route)
        for prefix in LANGS.values():
            entries[public_url(prefix, route)] = family
    return entries


def verify(root: Path) -> list[str]:
    root = root.resolve()
    sitemap = root / "sitemap.xml"
    errors: list[str] = []
    if not sitemap.is_file():
        return ["missing sitemap.xml"]

    try:
        xml_root = ET.parse(sitemap).getroot()
    except ET.ParseError as exc:
        return [f"invalid sitemap.xml: {exc}"]

    if xml_root.tag != f"{{{SITEMAP_NS}}}urlset":
        errors.append(f"unexpected root element: {xml_root.tag}")

    expected = expected_entries()
    seen: set[str] = set()

    for index, node in enumerate(xml_root.findall(f"{{{SITEMAP_NS}}}url"), start=1):
        loc_nodes = node.findall(f"{{{SITEMAP_NS}}}loc")
        if len(loc_nodes) != 1:
            errors.append(f"url[{index}] must contain exactly one loc")
            continue
        loc = (loc_nodes[0].text or "").strip()
        if not loc:
            errors.append(f"url[{index}] has empty loc")
            continue
        if loc in seen:
            errors.append(f"duplicate sitemap loc: {loc}")
        seen.add(loc)

        family = expected.get(loc)
        if family is None:
            errors.append(f"unexpected sitemap loc: {loc}")
            continue

        alternates: dict[str, str] = {}
        duplicate_hreflangs: set[str] = set()
        link_nodes = node.findall(f"{{{XHTML_NS}}}link")
        for link in link_nodes:
            rel = (link.get("rel") or "").strip().lower()
            hreflang = (link.get("hreflang") or "").strip().lower()
            href = (link.get("href") or "").strip()
            if rel != "alternate":
                errors.append(f"sitemap alternate rel mismatch: {loc} -> {rel or '<missing>'}")
                continue
            if not hreflang:
                errors.append(f"sitemap alternate hreflang missing: {loc}")
                continue
            if not href:
                errors.append(f"sitemap alternate href missing: {loc} -> {hreflang}")
                continue
            if hreflang in alternates:
                duplicate_hreflangs.add(hreflang)
            alternates[hreflang] = href

        if duplicate_hreflangs:
            errors.append(f"duplicate sitemap hreflang: {loc} -> {', '.join(sorted(duplicate_hreflangs))}")
        if len(link_nodes) != 4:
            errors.append(f"sitemap alternate count mismatch: {loc} -> {len(link_nodes)}, expected 4")
        if alternates != family:
            errors.append(f"sitemap hreflang mismatch: {loc}")

    expected_locs = set(expected)
    if seen != expected_locs:
        missing = sorted(expected_locs - seen)
        extra = sorted(seen - expected_locs)
        if missing:
            errors.append("sitemap locale-family missing: " + ", ".join(missing))
        if extra:
            errors.append("sitemap locale-family extra: " + ", ".join(extra))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    errors = verify(args.root)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_SITEMAP_HREFLANG: {error}", file=sys.stderr)
        return 1
    print("OK_AXIONA_SITEMAP_HREFLANG")
    print("SITEMAP_URLS=30")
    print("SITEMAP_HREFLANG_LINKS=120")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
