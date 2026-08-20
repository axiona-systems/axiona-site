#!/usr/bin/env python3
"""Fail-closed public-site quality gates for AXIONA Systems."""

from __future__ import annotations

import binascii
import struct
import sys
import zlib
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
    "keeper.html",
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
KEEPER_EXPECTED_LINKS = {
    "": "/keeper.html",
    "en/": "/en/keeper.html",
    "de/": "/de/keeper.html",
}
KEEPER_REQUIRED_MARKERS = (
    'class="keeper-status-badge"',
    'class="keeper96-workcard"',
    'class="keeper96-process-grid"',
    'class="keeper96-compare"',
    'class="keeper96-example-grid"',
    'class="keeper96-trust-grid"',
    'class="keeper-dev-status keeper96-dev section-pad"',
)
KEEPER_PLATFORM_MARKERS = ("iPhone", "iPad", "Apple App Store")
KEEPER_HUMAN_COPY_FORBIDDEN = {
    "": (
        "PDF, kép vagy fotó",
        "strukturált, ellenőrizhető adatot",
        "KEEPER FEJLESZTÉSI IRÁNY",
        "tervezett termékműködés szemléltető példái",
    ),
    "en/": (
        "PDF, image or photo",
        "structured, reviewable information",
        "KEEPER PRODUCT DIRECTION",
        "illustrative examples of the planned product experience",
    ),
    "de/": (
        "PDF, Bild oder Foto",
        "strukturierte, prüfbare Information",
        "KEEPER PRODUKTRICHTUNG",
        "veranschaulichen die geplante Produktfunktion",
    ),
}

GENERAL_SOCIAL_IMAGES = {
    "": "https://axiona.systems/assets/social/axiona-social-preview-r92-hu.png",
    "en/": "https://axiona.systems/assets/social/axiona-social-preview-r92-en.png",
    "de/": "https://axiona.systems/assets/social/axiona-social-preview-r92-de.png",
}
KEEPER_SOCIAL_IMAGES = {
    "": "https://axiona.systems/assets/social/axiona-keeper-social-preview-r92-hu.png",
    "en/": "https://axiona.systems/assets/social/axiona-keeper-social-preview-r92-en.png",
    "de/": "https://axiona.systems/assets/social/axiona-keeper-social-preview-r92-de.png",
}
LEGACY_SOCIAL_IMAGES = (
    "https://axiona.systems/assets/social/axiona-social-preview-r91.png",
    "https://axiona.systems/assets/social/axiona-keeper-social-preview-r91.png",
    "https://axiona.systems/assets/social/axiona-social-preview-r86.png",
)
SOCIAL_IMAGE_ASSETS = (
    "assets/social/axiona-social-preview-r92-hu.png",
    "assets/social/axiona-social-preview-r92-en.png",
    "assets/social/axiona-social-preview-r92-de.png",
    "assets/social/axiona-keeper-social-preview-r92-hu.png",
    "assets/social/axiona-keeper-social-preview-r92-en.png",
    "assets/social/axiona-keeper-social-preview-r92-de.png",
    "assets/social/axiona-social-preview-r86.png",
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


def validate_social_png(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        return f"cannot read PNG: {exc}"
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return "invalid PNG signature"

    pos = 8
    width = height = color_type = None
    idat = bytearray()
    has_trns = False
    saw_iend = False
    try:
        while pos + 12 <= len(data):
            length = struct.unpack(">I", data[pos:pos + 4])[0]
            end = pos + 12 + length
            if end > len(data):
                return f"truncated PNG chunk at byte {pos}"
            kind = data[pos + 4:pos + 8]
            payload = data[pos + 8:pos + 8 + length]
            expected_crc = struct.unpack(">I", data[pos + 8 + length:end])[0]
            actual_crc = binascii.crc32(kind + payload) & 0xFFFFFFFF
            if expected_crc != actual_crc:
                return f"CRC mismatch in {kind.decode('latin1')}"
            if kind == b"IHDR":
                width, height, _depth, color_type, compression, filtering, interlace = struct.unpack(">IIBBBBB", payload)
                if compression != 0 or filtering != 0 or interlace not in (0, 1):
                    return "unsupported PNG header"
            elif kind == b"IDAT":
                idat.extend(payload)
            elif kind == b"tRNS":
                has_trns = True
            elif kind == b"IEND":
                saw_iend = True
                pos = end
                break
            pos = end
    except (struct.error, ValueError) as exc:
        return f"malformed PNG structure: {exc}"

    if not saw_iend or pos != len(data):
        return "missing terminal IEND or trailing data"
    if (width, height) != (1200, 630):
        return f"expected 1200x630, got {width}x{height}"
    if color_type in (4, 6) or has_trns:
        return "social PNG must use an opaque RGB/palette background"
    try:
        zlib.decompress(bytes(idat))
    except zlib.error as exc:
        return f"invalid IDAT zlib stream: {exc}"
    return None


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
        relative_label = page.relative_to(ROOT).as_posix()
        social_prefix = "en/" if relative_label.startswith("en/") else "de/" if relative_label.startswith("de/") else ""
        expected_social_image = (
            KEEPER_SOCIAL_IMAGES[social_prefix]
            if page.name == "keeper.html"
            else GENERAL_SOCIAL_IMAGES[social_prefix]
        )
        required_social_meta = (
            f'content="{expected_social_image}" property="og:image"',
            f'content="{expected_social_image}" name="twitter:image"',
            'content="1200" property="og:image:width"',
            'content="630" property="og:image:height"',
            'content="image/png" property="og:image:type"',
        )
        for token in required_social_meta:
            if token not in text:
                errors.append(f"social preview invariant missing in {label}: {token}")
        for legacy_social_image in LEGACY_SOCIAL_IMAGES:
            if legacy_social_image in text:
                errors.append(f"legacy social preview URL remains active in {label}: {legacy_social_image}")

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

    keeper_css = ROOT / "assets/keeper-r87.css"
    if not keeper_css.is_file():
        errors.append("missing Keeper product stylesheet: assets/keeper-r87.css")

    for prefix, keeper_href in KEEPER_EXPECTED_LINKS.items():
        homepage = ROOT / prefix / "index.html"
        solutions = ROOT / prefix / "solutions.html"
        keeper = ROOT / prefix / "keeper.html"

        for source in (homepage, solutions):
            text = source.read_text(encoding="utf-8") if source.is_file() else ""
            if f'href="{keeper_href}"' not in text:
                errors.append(f"Keeper product entry link missing in {source}: {keeper_href}")
            for stylesheet in ("/assets/keeper-r87.css", "/assets/keeper-r94.css", "/assets/keeper-r96.css"):
                if stylesheet not in text:
                    errors.append(f"Keeper stylesheet missing from product entry page: {source}: {stylesheet}")
            for marker in KEEPER_PLATFORM_MARKERS:
                if marker not in text:
                    errors.append(f"Keeper platform marker missing in {source}: {marker}")

        homepage_text = homepage.read_text(encoding="utf-8") if homepage.is_file() else ""
        if 'class="keeper96-preview-panel"' not in homepage_text:
            errors.append(f"Keeper R96 intelligence preview missing from overview page: {homepage}")
        if 'keeper-matter-demo' in homepage_text:
            errors.append(f"Legacy Keeper matter demo must remain off overview page: {homepage}")

        solutions_text = solutions.read_text(encoding="utf-8") if solutions.is_file() else ""
        if 'class="keeper96-mini-process"' not in solutions_text:
            errors.append(f"Keeper R96 mini process missing from solutions page: {solutions}")
        if 'keeper-matter-demo' in solutions_text:
            errors.append(f"Legacy Keeper matter demo must remain off solutions page: {solutions}")

        keeper_text = keeper.read_text(encoding="utf-8") if keeper.is_file() else ""
        if "/assets/keeper-r87.css" not in keeper_text:
            errors.append(f"Keeper stylesheet missing from product page: {keeper}")
        if "/assets/keeper-r94.css" not in keeper_text:
            errors.append(f"Keeper R94 compatibility stylesheet missing from product page: {keeper}")
        if "/assets/keeper-r96.css" not in keeper_text:
            errors.append(f"Keeper R96 product-story stylesheet missing from product page: {keeper}")
        for marker in KEEPER_REQUIRED_MARKERS:
            if marker not in keeper_text:
                errors.append(f"Keeper transparency marker missing in {keeper}: {marker}")
        for marker in KEEPER_PLATFORM_MARKERS:
            if marker not in keeper_text:
                errors.append(f"Keeper platform marker missing in {keeper}: {marker}")
        for forbidden in KEEPER_HUMAN_COPY_FORBIDDEN[prefix]:
            if forbidden in keeper_text:
                errors.append(f"Keeper human-copy regression in {keeper}: {forbidden}")

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

    for asset in SOCIAL_IMAGE_ASSETS:
        asset_path = ROOT / asset
        if not asset_path.is_file():
            errors.append(f"missing social preview asset: {asset}")
            continue
        png_error = validate_social_png(asset_path)
        if png_error:
            errors.append(f"invalid social preview asset {asset}: {png_error}")

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
    print("OK_AXIONA_KEEPER_PRODUCT_PREVIEW_INVARIANTS")
    print("OK_AXIONA_CONTACT_INTAKE_LOCAL_ONLY")
    print("OK_AXIONA_SECURITY_TXT")
    print("OK_AXIONA_SOCIAL_PREVIEW_R92_LOCALES")
    print("OK_AXIONA_PUBLIC_QUALITY_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
