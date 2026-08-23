#!/usr/bin/env python3
"""Verify AXIONA HU/EN/DE header navigation, language switch, and footer route parity."""

from __future__ import annotations

import argparse
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
PRIMARY_NAV = (
    "index.html",
    "systems.html",
    "process.html",
    "security.html",
    "solutions.html",
    "contact.html",
)
FOOTER_UTILITY = ("support.html", "privacy.html", "legal.html", "security.html")
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
    "param", "source", "track", "wbr",
}


def route_href(prefix: str, route: str) -> str:
    if route == "index.html":
        return f"/{prefix}"
    return f"/{prefix}{route}"


def expected_language_switch(route: str) -> list[str]:
    return [route_href(prefix, route) for prefix in LANGS.values()]


class NavigationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, set[str]]] = []
        self.brand: list[str] = []
        self.desktop_nav: list[tuple[str, bool]] = []
        self.mobile_nav: list[tuple[str, bool]] = []
        self.language_switch: list[tuple[str, bool]] = []
        self.footer_links: list[str] = []

    def active_markers(self) -> set[str]:
        markers: set[str] = set()
        for _, item_markers in self.stack:
            markers.update(item_markers)
        return markers

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = {k.lower(): (v or "") for k, v in attrs}
        classes = set(values.get("class", "").split())
        active = self.active_markers()
        markers: set[str] = set()
        if tag == "header" and "topbar" in classes:
            markers.add("topbar")
        if tag == "nav" and "topbar" in active:
            markers.add("desktop_nav")
        if tag == "div" and "language-switch" in classes:
            markers.add("language_switch")
        if tag == "div" and "mobile-menu-panel" in classes:
            markers.add("mobile_nav")
        if tag == "footer":
            markers.add("footer")

        if tag == "a":
            href = values.get("href", "").strip()
            is_active = "active" in classes
            if "topbar" in active and "brand" in classes:
                self.brand.append(href)
            elif "desktop_nav" in active:
                self.desktop_nav.append((href, is_active))
            elif "language_switch" in active:
                self.language_switch.append((href, is_active))
            elif "mobile_nav" in active:
                self.mobile_nav.append((href, is_active))
            elif "footer" in active:
                self.footer_links.append(href)

        if tag not in VOID_TAGS:
            self.stack.append((tag, markers))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # No relevant navigation anchors are self-closing; intentionally ignore void markup.
        return

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                return


def verify(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for lang, prefix in LANGS.items():
        expected_primary = [route_href(prefix, route) for route in PRIMARY_NAV]
        expected_footer = [route_href(prefix, route) for route in FOOTER_UTILITY] + ["/", "/en/", "/de/"]
        expected_brand = route_href(prefix, "index.html")
        for route in ROUTES:
            page = root / prefix / route
            label = page.relative_to(root).as_posix()
            if not page.is_file():
                errors.append(f"missing navigation page: {label}")
                continue
            parser = NavigationParser()
            parser.feed(page.read_text(encoding="utf-8"))

            if parser.brand != [expected_brand]:
                errors.append(f"brand route mismatch: {label} -> {parser.brand}, expected {[expected_brand]}")

            desktop_hrefs = [href for href, _ in parser.desktop_nav]
            mobile_hrefs = [href for href, _ in parser.mobile_nav]
            if desktop_hrefs != expected_primary:
                errors.append(f"desktop nav mismatch: {label} -> {desktop_hrefs}")
            if mobile_hrefs != expected_primary:
                errors.append(f"mobile nav mismatch: {label} -> {mobile_hrefs}")
            if desktop_hrefs != mobile_hrefs:
                errors.append(f"desktop/mobile nav drift: {label}")

            current_primary_index = PRIMARY_NAV.index(route) if route in PRIMARY_NAV else None
            expected_active = [index == current_primary_index for index in range(len(PRIMARY_NAV))]
            desktop_active = [active for _, active in parser.desktop_nav]
            mobile_active = [active for _, active in parser.mobile_nav]
            if desktop_active != expected_active:
                errors.append(f"desktop active-state mismatch: {label} -> {desktop_active}")
            if mobile_active != expected_active:
                errors.append(f"mobile active-state mismatch: {label} -> {mobile_active}")

            language_hrefs = [href for href, _ in parser.language_switch]
            expected_languages = expected_language_switch(route)
            if language_hrefs != expected_languages:
                errors.append(f"language switch mismatch: {label} -> {language_hrefs}, expected {expected_languages}")
            language_active = [active for _, active in parser.language_switch]
            expected_language_active = [item_lang == lang for item_lang in LANGS]
            if language_active != expected_language_active:
                errors.append(f"language active-state mismatch: {label} -> {language_active}")

            if parser.footer_links != expected_footer:
                errors.append(f"footer route mismatch: {label} -> {parser.footer_links}, expected {expected_footer}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    errors = verify(args.root)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_NAVIGATION_PARITY: {error}", file=sys.stderr)
        return 1
    print("OK_AXIONA_NAVIGATION_PARITY")
    print("NAVIGATION_PAGES=30")
    print("PRIMARY_NAV_LINKS=360")
    print("LANGUAGE_SWITCH_LINKS=90")
    print("FOOTER_LINKS=210")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
