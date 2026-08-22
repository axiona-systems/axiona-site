#!/usr/bin/env python3
"""Validate the current public AXIONA Systems website surface."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
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
        self.refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): (v or "") for k, v in attrs}
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content", "").strip()
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


def local_target(page: Path, raw: str) -> Path | None:
    if raw.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc:
        return None
    path = parsed.path
    if not path:
        return None
    target = ROOT / path.lstrip("/") if path.startswith("/") else page.parent / path
    if path.endswith("/"):
        target = target / "index.html"
    return target.resolve()


def expected_urls() -> set[str]:
    urls: set[str] = set()
    for prefix in LANGS.values():
        for route in ROUTES:
            if route == "index.html":
                urls.add(f"{HOST}/{prefix}")
            else:
                urls.add(f"{HOST}/{prefix}{route}")
    return urls


def main() -> int:
    errors: list[str] = []
    active_pages = [ROOT / prefix / route for prefix in LANGS.values() for route in ROUTES]

    for page in active_pages:
        label = page.relative_to(ROOT).as_posix()
        if not page.is_file():
            errors.append(f"missing active page: {label}")
            continue
        text = page.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(text)
        if not parser.title:
            errors.append(f"missing title: {label}")
        if not parser.description:
            errors.append(f"missing description: {label}")
        for ref in parser.refs:
            target = local_target(page, ref)
            if target is not None and not target.exists():
                errors.append(f"broken local reference: {label} -> {ref}")

    sitemap = ROOT / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("missing sitemap.xml")
    else:
        try:
            root = ET.parse(sitemap).getroot()
            actual = {
                (node.find(f"{{{SITEMAP_NS}}}loc").text or "").strip()
                for node in root.findall(f"{{{SITEMAP_NS}}}url")
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

    robots = ROOT / "robots.txt"
    if not robots.is_file() or "Sitemap: https://axiona.systems/sitemap.xml" not in robots.read_text(encoding="utf-8"):
        errors.append("robots.txt sitemap pointer missing")

    security_contact = ROOT / ".well-known" / "security.txt"
    if not security_contact.is_file():
        errors.append("missing .well-known/security.txt")

    text_suffixes = {".html", ".md", ".txt", ".xml", ".json", ".js", ".css", ".py", ".yml", ".yaml"}
    verifier_path = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in text_suffixes:
            continue
        if path.resolve() == verifier_path:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SENSITIVE_PATTERNS:
            if pattern.search(text):
                errors.append(f"sensitive material pattern: {path.relative_to(ROOT).as_posix()}")
                break
        for email in EMAIL_PATTERN.findall(text):
            domain = email.rsplit("@", 1)[1].lower()
            if domain not in ALLOWED_PUBLIC_EMAIL_DOMAINS:
                errors.append(f"non-public email domain: {path.relative_to(ROOT).as_posix()}")
                break

    if errors:
        for error in errors:
            print(f"STOP_AXIONA_PUBLIC_SURFACE: {error}", file=sys.stderr)
        return 1

    print("OK_AXIONA_PUBLIC_SURFACE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
