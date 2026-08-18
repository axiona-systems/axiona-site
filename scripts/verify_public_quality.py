#!/usr/bin/env python3
"""Fail-closed public-site quality gates for AXIONA Systems."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LANG_PREFIXES = ("", "en/", "de/")
ACTIVE_ROUTES = (
    "index.html",
    "systems.html",
    "process.html",
    "security.html",
    "solutions.html",
    "contact.html",
    "privacy.html",
    "legal.html",
    "support.html",
)
LEGACY_REDIRECTS = {
    "applications.html": "solutions.html",
    "automation.html": "solutions.html",
    "case-study.html": "process.html",
    "company.html": "",
    "impact.html": "systems.html",
    "practical-tips.html": "process.html",
    "services.html": "solutions.html",
}
INACTIVE_LANGUAGE_DIRS = ("fr", "es", "it")
REMOVED_LEGACY_ASSETS = (
    "styles.css",
    "assets/unified-r73.css",
    "assets/multipage-r72.css",
    "assets/multipage-r75.css",
    "assets/policy-r76.css",
    "apple-touch-icon-r41.png",
    "favicon-r41-16x16.png",
    "favicon-r41-32x32.png",
    "favicon-r41.ico",
    "assets/brand/r41",
)


class RefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): (value or "") for key, value in attrs}
        if "href" in values:
            self.refs.append(("href", values["href"]))
        if "src" in values:
            self.refs.append(("src", values["src"]))


def active_paths() -> list[Path]:
    return [ROOT / prefix / route for prefix in LANG_PREFIXES for route in ACTIVE_ROUTES]


def route_url(prefix: str, target: str) -> str:
    if target:
        return f"https://axiona.systems/{prefix}{target}"
    return f"https://axiona.systems/{prefix}"


def local_target(page: Path, raw: str) -> Path | None:
    value = raw.strip()
    if not value or value.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        return None

    path = parsed.path
    if not path:
        return None

    if path.startswith("/"):
        candidate = ROOT / path.lstrip("/")
    else:
        candidate = page.parent / path

    if path.endswith("/"):
        candidate = candidate / "index.html"
    return candidate.resolve()


def main() -> int:
    errors: list[str] = []

    for dirname in INACTIVE_LANGUAGE_DIRS:
        if (ROOT / dirname).exists():
            errors.append(f"inactive language directory is still public: {dirname}/")

    for item in REMOVED_LEGACY_ASSETS:
        if (ROOT / item).exists():
            errors.append(f"legacy asset remains: {item}")

    for prefix in LANG_PREFIXES:
        for legacy, target in LEGACY_REDIRECTS.items():
            path = ROOT / prefix / legacy
            label = path.relative_to(ROOT).as_posix()
            if not path.is_file():
                errors.append(f"missing legacy redirect shell: {label}")
                continue
            text = path.read_text(encoding="utf-8")
            expected_url = route_url(prefix, target)
            required = (
                'name="robots" content="noindex,follow"',
                f'rel="canonical" href="{expected_url}"',
                f'url={expected_url}',
                f'location.replace("{expected_url}")',
            )
            for token in required:
                if token not in text:
                    errors.append(f"legacy redirect invariant missing in {label}: {token}")
            forbidden = ("styles.css", "page-case", "page-accent-", "hero-core-visual")
            for token in forbidden:
                if token in text:
                    errors.append(f"legacy design leaked into redirect shell {label}: {token}")

    active = active_paths()
    for page in active:
        label = page.relative_to(ROOT).as_posix()
        if not page.is_file():
            errors.append(f"missing active page: {label}")
            continue

        text = page.read_text(encoding="utf-8")
        for prefix in ("/fr/", "/es/", "/it/"):
            if prefix in text:
                errors.append(f"inactive language link in {label}: {prefix}")
        for token in ("data-lang", "site.js?v=4", "Proof HU", "Gate:", "idempotencia", "kill switch"):
            if token in text:
                errors.append(f"forbidden public marker in {label}: {token}")
        for legacy in LEGACY_REDIRECTS:
            if f'href="/{legacy}"' in text or f'href="{legacy}"' in text:
                errors.append(f"active page links to legacy route: {label} -> {legacy}")

        parser = RefParser()
        parser.feed(text)
        for kind, ref in parser.refs:
            candidate = local_target(page, ref)
            if candidate is None:
                continue
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{label}: local {kind} escapes repository: {ref}")
                continue
            if not candidate.exists():
                errors.append(f"{label}: broken local {kind}: {ref}")

    for prefix in LANG_PREFIXES:
        contact = ROOT / prefix / "contact.html"
        text = contact.read_text(encoding="utf-8") if contact.is_file() else ""
        required = (
            "data-intake-form",
            "data-intake-field",
            "/assets/js/contact-intake.js",
            "hello@axiona.systems",
        )
        for token in required:
            if token not in text:
                errors.append(f"contact intake invariant missing in {contact}: {token}")
        if "<form" in text and "action=" in text:
            errors.append(f"contact form must not submit to a new server endpoint: {contact}")

    intake_js = ROOT / "assets/js/contact-intake.js"
    if not intake_js.is_file():
        errors.append("missing contact intake runtime")
    else:
        intake_text = intake_js.read_text(encoding="utf-8")
        if "fetch(" in intake_text or "XMLHttpRequest" in intake_text:
            errors.append("contact intake must remain local-only; network submission detected")

    multipage_css = ROOT / "assets/multipage-r78.css"
    if not multipage_css.is_file():
        errors.append("missing current multipage stylesheet")
    else:
        css_text = multipage_css.read_text(encoding="utf-8")
        for token in (
            ".mobile-menu[open]>.mobile-menu-panel",
            ".mobile-menu summary",
            "font-size:13px",
            "min-height:50px",
        ):
            if token not in css_text:
                errors.append(f"compact mobile navigation invariant missing: {token}")

    site_runtime = ROOT / "assets/js/visit-counter-r80.js"
    if not site_runtime.is_file():
        errors.append("missing current site runtime")
    else:
        runtime_text = site_runtime.read_text(encoding="utf-8")
        for token in (
            "compactMobileMenu",
            'removeAttribute("open")',
            'matchMedia("(max-width: 920px)")',
        ):
            if token not in runtime_text:
                errors.append(f"mobile menu runtime invariant missing: {token}")

    security_txt = ROOT / ".well-known/security.txt"
    if not security_txt.is_file():
        errors.append("missing /.well-known/security.txt")
    else:
        security = security_txt.read_text(encoding="utf-8")
        for token in (
            "Contact: mailto:hello@axiona.systems",
            "Preferred-Languages: hu, en, de",
            "Canonical: https://axiona.systems/.well-known/security.txt",
            "Policy: https://axiona.systems/security.html",
            "Expires:",
        ):
            if token not in security:
                errors.append(f"security.txt missing directive: {token}")

    manifest = ROOT / "site.webmanifest"
    if manifest.is_file():
        manifest_text = manifest.read_text(encoding="utf-8").lower()
        if "r41" in manifest_text or "single-source-icon" in manifest_text:
            errors.append("site.webmanifest still exposes legacy release identifiers")
    else:
        errors.append("missing site.webmanifest")

    if errors:
        for error in errors:
            print(f"STOP_AXIONA_PUBLIC_QUALITY: {error}", file=sys.stderr)
        print("STOP_AXIONA_PUBLIC_QUALITY_FAILED", file=sys.stderr)
        return 1

    print("OK_AXIONA_LEGACY_PUBLIC_SURFACE_CLEAN")
    print("OK_AXIONA_ACTIVE_INTERNAL_LINKS")
    print("OK_AXIONA_CONTACT_INTAKE_LOCAL_ONLY")
    print("OK_AXIONA_SECURITY_TXT")
    print("OK_AXIONA_PUBLIC_QUALITY_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
