#!/usr/bin/env python3
"""Fail-closed SEO/indexing invariants for the AXIONA public website."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://axiona.systems"
LANG_PREFIXES = {"hu": "", "en": "en/", "de": "de/"}
ROUTES = (
    "",
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
LEGACY_ROUTE_NAMES = (
    "applications.html",
    "automation.html",
    "impact.html",
    "services.html",
    "company.html",
    "practical-tips.html",
    "case-study.html",
)
INACTIVE_LANGUAGE_PREFIXES = ("/fr/", "/es/", "/it/")
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NS = "http://www.w3.org/1999/xhtml"


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.title_parts: list[str] = []
        self.description: str | None = None
        self.robots: list[str] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): (value or "") for key, value in attrs}
        if tag.lower() == "title":
            self.in_title = True
        elif tag.lower() == "meta":
            name = values.get("name", "").lower()
            if name == "description":
                self.description = values.get("content", "").strip()
            elif name == "robots":
                self.robots.append(values.get("content", "").lower())
        elif tag.lower() == "link":
            self.links.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def page_url(lang: str, route: str) -> str:
    prefix = LANG_PREFIXES[lang]
    if not route:
        return f"{HOST}/{prefix}"
    return f"{HOST}/{prefix}{route}"


def page_path(lang: str, route: str) -> Path:
    prefix = LANG_PREFIXES[lang]
    filename = "index.html" if not route else route
    return ROOT / prefix / filename


def expected_alternates(route: str) -> dict[str, str]:
    return {
        "hu": page_url("hu", route),
        "en": page_url("en", route),
        "de": page_url("de", route),
        "x-default": page_url("hu", route),
    }


def parse_html(path: Path) -> HeadParser:
    parser = HeadParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def rel_tokens(link: dict[str, str]) -> set[str]:
    return {part.lower() for part in link.get("rel", "").split() if part}


def canonical_links(parser: HeadParser) -> list[str]:
    return [link.get("href", "") for link in parser.links if "canonical" in rel_tokens(link)]


def alternate_links(parser: HeadParser) -> dict[str, str]:
    result: dict[str, str] = {}
    for link in parser.links:
        if "alternate" not in rel_tokens(link):
            continue
        hreflang = link.get("hreflang", "").lower().strip()
        href = link.get("href", "").strip()
        if hreflang:
            result[hreflang] = href
    return result


def main() -> int:
    errors: list[str] = []

    expected_urls = {
        page_url(lang, route)
        for route in ROUTES
        for lang in LANG_PREFIXES
    }
    url_to_route = {
        page_url(lang, route): route
        for route in ROUTES
        for lang in LANG_PREFIXES
    }

    for route in ROUTES:
        for lang in LANG_PREFIXES:
            path = page_path(lang, route)
            label = path.relative_to(ROOT).as_posix()
            if not path.is_file():
                errors.append(f"missing active public page: {label}")
                continue

            parser = parse_html(path)
            if not parser.title:
                errors.append(f"missing <title>: {label}")
            if not parser.description:
                errors.append(f"missing meta description: {label}")
            if any("noindex" in value for value in parser.robots):
                errors.append(f"active public page is noindex: {label}")

            if route == "":
                expected_canonical = page_url(lang, route)
                canonicals = canonical_links(parser)
                if canonicals != [expected_canonical]:
                    errors.append(
                        f"homepage canonical mismatch: {label}: {canonicals!r} != {[expected_canonical]!r}"
                    )
                alternates = alternate_links(parser)
                expected = expected_alternates(route)
                if alternates != expected:
                    errors.append(
                        f"homepage hreflang mismatch: {label}: {alternates!r} != {expected!r}"
                    )

            if route == "keeper.html":
                expected_canonical = page_url(lang, route)
                canonicals = canonical_links(parser)
                if canonicals != [expected_canonical]:
                    errors.append(
                        f"keeper canonical mismatch: {label}: {canonicals!r} != {[expected_canonical]!r}"
                    )
                alternates = alternate_links(parser)
                expected = expected_alternates(route)
                if alternates != expected:
                    errors.append(
                        f"keeper hreflang mismatch: {label}: {alternates!r} != {expected!r}"
                    )

            if route == "support.html":
                expected_canonical = page_url(lang, route)
                canonicals = canonical_links(parser)
                if canonicals != [expected_canonical]:
                    errors.append(
                        f"support canonical mismatch: {label}: {canonicals!r} != {[expected_canonical]!r}"
                    )

    if not errors:
        print("OK_AXIONA_SEO_HTML_BASELINE")

    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.is_file():
        errors.append("missing sitemap.xml")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
        except ET.ParseError as exc:
            errors.append(f"invalid sitemap.xml: {exc}")
        else:
            entries: dict[str, ET.Element] = {}
            for node in root.findall(f"{{{SITEMAP_NS}}}url"):
                loc_node = node.find(f"{{{SITEMAP_NS}}}loc")
                if loc_node is None or not (loc_node.text or "").strip():
                    errors.append("sitemap entry without loc")
                    continue
                loc = (loc_node.text or "").strip()
                if loc in entries:
                    errors.append(f"duplicate sitemap loc: {loc}")
                entries[loc] = node

            actual_urls = set(entries)
            missing = sorted(expected_urls - actual_urls)
            extra = sorted(actual_urls - expected_urls)
            if missing:
                errors.append("sitemap missing URLs: " + ", ".join(missing))
            if extra:
                errors.append("sitemap contains non-active URLs: " + ", ".join(extra))

            sitemap_text = sitemap_path.read_text(encoding="utf-8")
            for legacy in LEGACY_ROUTE_NAMES:
                if legacy in sitemap_text:
                    errors.append(f"legacy route remains in sitemap: {legacy}")
            for prefix in INACTIVE_LANGUAGE_PREFIXES:
                if prefix in sitemap_text:
                    errors.append(f"inactive language remains in sitemap: {prefix}")

            for loc, node in entries.items():
                route = url_to_route.get(loc)
                if route is None:
                    continue
                alternates: dict[str, str] = {}
                for link in node.findall(f"{{{XHTML_NS}}}link"):
                    if link.attrib.get("rel", "").lower() != "alternate":
                        continue
                    hreflang = link.attrib.get("hreflang", "").lower().strip()
                    href = link.attrib.get("href", "").strip()
                    if hreflang:
                        alternates[hreflang] = href
                expected = expected_alternates(route)
                if alternates != expected:
                    errors.append(
                        f"sitemap hreflang mismatch for {loc}: {alternates!r} != {expected!r}"
                    )

                lastmod = node.find(f"{{{SITEMAP_NS}}}lastmod")
                if lastmod is not None and (lastmod.text or "").strip():
                    value = (lastmod.text or "").strip()
                    parts = value.split("-")
                    if len(parts) != 3 or [len(part) for part in parts] != [4, 2, 2] or not all(
                        part.isdigit() for part in parts
                    ):
                        errors.append(f"invalid lastmod format for {loc}: {value}")

            if not missing and not extra:
                print("OK_AXIONA_SEO_SITEMAP_ROUTE_SET")
            if not any("sitemap hreflang mismatch" in error for error in errors):
                print("OK_AXIONA_SEO_SITEMAP_HREFLANG_GRAPH")

    robots_path = ROOT / "robots.txt"
    robots_expected = "Sitemap: https://axiona.systems/sitemap.xml"
    if not robots_path.is_file():
        errors.append("missing robots.txt")
    elif robots_expected not in robots_path.read_text(encoding="utf-8").splitlines():
        errors.append(f"robots.txt missing exact sitemap directive: {robots_expected}")
    else:
        print("OK_AXIONA_SEO_ROBOTS_SITEMAP_POINTER")

    # The sitemap must only reference the canonical HTTPS host.
    for url in expected_urls:
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != "axiona.systems":
            errors.append(f"non-canonical host in expected URL set: {url}")

    if errors:
        for error in errors:
            print(f"STOP_AXIONA_SEO: {error}", file=sys.stderr)
        print("STOP_AXIONA_SEO_INDEXING_INVARIANTS_FAILED", file=sys.stderr)
        return 1

    print("OK_AXIONA_SEO_INDEXING_INVARIANTS_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
