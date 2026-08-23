#!/usr/bin/env python3
"""Validate the complete public AXIONA Systems website surface."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
HOST = "https://axiona.systems"
HOSTNAME = "axiona.systems"
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
SENSITIVE_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |DSA |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[=:]\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"/Users/[^/\s]+/"),
)
EMAIL_PATTERN = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
ALLOWED_PUBLIC_EMAIL_DOMAINS = {"axiona.systems", "users.noreply.github.com"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.title_parts: list[str] = []
        self.description = ""
        self.html_lang = ""
        self.refs: list[str] = []
        self.canonicals: list[str] = []
        self.alternates: list[tuple[str, str]] = []
        self.releases: list[str] = []
        self.robots: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = {k.lower(): (v or "") for k, v in attrs}
        if tag == "html":
            self.html_lang = values.get("lang", "").strip().lower()
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            name = values.get("name", "").strip().lower()
            content = values.get("content", "").strip()
            if name == "description":
                self.description = content
            elif name == "axiona-release":
                self.releases.append(content)
            elif name == "robots":
                self.robots.append(content)
        if tag == "link":
            href = values.get("href", "").strip()
            rel_tokens = set(values.get("rel", "").lower().split())
            if href and "canonical" in rel_tokens:
                self.canonicals.append(href)
            if href and "alternate" in rel_tokens and values.get("hreflang", "").strip():
                self.alternates.append((values["hreflang"].strip().lower(), href))
        for key in ("href", "src"):
            value = values.get(key, "").strip()
            if value:
                self.refs.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()



def same_site(parsed) -> bool:
    if not parsed.netloc:
        return not parsed.scheme
    return (parsed.hostname or "").lower() == HOSTNAME


def local_target(root: Path, page: Path, raw: str) -> Path | None:
    if raw.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlsplit(raw)
    if not same_site(parsed):
        return None
    path = parsed.path
    if parsed.netloc and not path:
        path = "/"
    if not path:
        return None
    target = root / path.lstrip("/") if path.startswith("/") else page.parent / path
    if path.endswith("/"):
        target = target / "index.html"
    return target.resolve()


def has_release_binding(refs: list[str], release: str) -> bool:
    if not release:
        return False
    for raw in refs:
        parsed = urlsplit(raw)
        if not same_site(parsed):
            continue
        if release in parse_qs(parsed.query).get("release", []):
            return True
    return False


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


def expected_urls() -> set[str]:
    return {public_url(prefix, route) for prefix in LANGS.values() for route in ROUTES}


def expected_public_html(root: Path) -> set[Path]:
    pages = {root / prefix / route for prefix in LANGS.values() for route in ROUTES}
    pages.add(root / "404.html")
    return {p.resolve() for p in pages}


def verify(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    expected_html = expected_public_html(root)
    actual_html = {
        path.resolve()
        for path in root.rglob("*.html")
        if path.is_file() and ".git" not in path.parts
    }
    for path in sorted(expected_html - actual_html):
        errors.append(f"missing public html: {path.relative_to(root).as_posix()}")
    for path in sorted(actual_html - expected_html):
        errors.append(f"unexpected public html: {path.relative_to(root).as_posix()}")

    releases_by_route: dict[str, dict[str, str]] = {route: {} for route in ROUTES}

    for lang, prefix in LANGS.items():
        for route in ROUTES:
            page = root / prefix / route
            label = page.relative_to(root).as_posix()
            if not page.is_file():
                continue
            text = page.read_text(encoding="utf-8")
            parser = PageParser()
            parser.feed(text)

            if not parser.title:
                errors.append(f"missing title: {label}")
            if not parser.description:
                errors.append(f"missing description: {label}")
            if parser.html_lang != lang:
                errors.append(f"html lang mismatch: {label} -> {parser.html_lang or '<missing>'}, expected {lang}")

            expected_canonical = public_url(prefix, route)
            if parser.canonicals != [expected_canonical]:
                errors.append(
                    f"canonical mismatch: {label} -> {parser.canonicals or '<missing>'}, expected {expected_canonical}"
                )

            alternate_map: dict[str, str] = {}
            duplicate_hreflangs: set[str] = set()
            for hreflang, href in parser.alternates:
                if hreflang in alternate_map:
                    duplicate_hreflangs.add(hreflang)
                alternate_map[hreflang] = href
            if duplicate_hreflangs:
                errors.append(f"duplicate hreflang: {label} -> {', '.join(sorted(duplicate_hreflangs))}")
            expected_alternates = expected_hreflangs(route)
            if alternate_map != expected_alternates:
                errors.append(f"hreflang mismatch: {label}")

            if len(parser.releases) != 1 or not parser.releases[0]:
                errors.append(f"release marker mismatch: {label} -> {parser.releases or '<missing>'}")
                release = ""
            else:
                release = parser.releases[0]
                releases_by_route[route][lang] = release
                if not has_release_binding(parser.refs, release):
                    errors.append(f"release binding missing: {label} -> {release}")

            for ref in parser.refs:
                target = local_target(root, page, ref)
                if target is None:
                    continue
                try:
                    target.relative_to(root)
                except ValueError:
                    errors.append(f"public reference escapes root: {label} -> {ref}")
                    continue
                if not target.exists():
                    errors.append(f"broken local reference: {label} -> {ref}")

    for route, releases in releases_by_route.items():
        if set(releases) == set(LANGS) and len(set(releases.values())) != 1:
            detail = ", ".join(f"{lang}={release}" for lang, release in sorted(releases.items()))
            errors.append(f"language release mismatch: {route} -> {detail}")

    not_found = root / "404.html"
    if not_found.is_file():
        parser = PageParser()
        parser.feed(not_found.read_text(encoding="utf-8"))
        if not parser.title:
            errors.append("missing title: 404.html")
        if not parser.description:
            errors.append("missing description: 404.html")
        if parser.html_lang != "hu":
            errors.append(f"404 html lang mismatch: {parser.html_lang or '<missing>'}")
        if parser.releases != ["R126"]:
            errors.append(f"404 release mismatch: {parser.releases or '<missing>'}, expected R126")
        if parser.robots != ["noindex,follow"]:
            errors.append(f"404 robots mismatch: {parser.robots or '<missing>'}")
        if not has_release_binding(parser.refs, "R126"):
            errors.append("404 release binding missing: R126")
        if parser.canonicals or parser.alternates:
            errors.append("404 must not publish canonical/hreflang alternates")
        for ref in parser.refs:
            target = local_target(root, not_found, ref)
            if target is None:
                continue
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"public reference escapes root: 404.html -> {ref}")
                continue
            if not target.exists():
                errors.append(f"broken local reference: 404.html -> {ref}")

    sitemap = root / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("missing sitemap.xml")
    else:
        try:
            sitemap_root = ET.parse(sitemap).getroot()
            actual = {
                (node.find(f"{{{SITEMAP_NS}}}loc").text or "").strip()
                for node in sitemap_root.findall(f"{{{SITEMAP_NS}}}url")
                if node.find(f"{{{SITEMAP_NS}}}loc") is not None
            }
            expected = expected_urls()
            if actual != expected:
                missing = sorted(expected - actual)
                extra = sorted(actual - expected)
                if missing:
                    errors.append("sitemap missing: " + ", ".join(missing))
                if extra:
                    errors.append("sitemap extra: " + ", ".join(extra))
        except ET.ParseError as exc:
            errors.append(f"invalid sitemap.xml: {exc}")

    robots = root / "robots.txt"
    if not robots.is_file() or "Sitemap: https://axiona.systems/sitemap.xml" not in robots.read_text(encoding="utf-8"):
        errors.append("robots.txt sitemap pointer missing")

    security_contact = root / ".well-known" / "security.txt"
    if not security_contact.is_file():
        errors.append("missing .well-known/security.txt")

    text_suffixes = {".html", ".md", ".txt", ".xml", ".json", ".js", ".css", ".py", ".yml", ".yaml"}
    verifier_paths = {Path(__file__).resolve(), (root / "scripts" / "verify_site.py").resolve()}
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in text_suffixes:
            continue
        if path.resolve() in verifier_paths:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SENSITIVE_PATTERNS:
            if pattern.search(text):
                errors.append(f"sensitive material pattern: {path.relative_to(root).as_posix()}")
                break
        for email in EMAIL_PATTERN.findall(text):
            domain = email.rsplit("@", 1)[1].lower()
            if domain not in ALLOWED_PUBLIC_EMAIL_DOMAINS:
                errors.append(f"non-public email domain: {path.relative_to(root).as_posix()}")
                break

    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Repository root to verify (used by invariant self-tests).")
    args = cli.parse_args()
    errors = verify(args.root)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_PUBLIC_SURFACE: {error}", file=sys.stderr)
        return 1
    print("OK_AXIONA_PUBLIC_SURFACE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
