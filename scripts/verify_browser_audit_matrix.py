#!/usr/bin/env python3
"""Verify AXIONA browser-audit route coverage tiers."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

EXPECTED_LIGHTHOUSE = [
    "/",
    "/systems.html",
    "/process.html",
    "/security.html",
    "/solutions.html",
    "/keeper.html",
    "/contact.html",
    "/support.html",
    "/privacy.html",
    "/legal.html",
    "/en/",
    "/de/",
]

ROUTES = [
    "",
    "systems.html",
    "process.html",
    "security.html",
    "solutions.html",
    "keeper.html",
    "contact.html",
    "support.html",
    "privacy.html",
    "legal.html",
]

EXPECTED_AXE = [
    (f"/{prefix}/{route}" if route else f"/{prefix}/")
    if prefix
    else (f"/{route}" if route else "/")
    for prefix in ("", "en", "de")
    for route in ROUTES
]


def fail(message: str) -> int:
    print(f"STOP_AXIONA_BROWSER_AUDIT_MATRIX: {message}", file=sys.stderr)
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    lighthouse_path = root / "lighthouserc.json"
    axe_path = root / "scripts" / "axe-audit.mjs"
    if not lighthouse_path.is_file():
        return fail("missing lighthouserc.json")
    if not axe_path.is_file():
        return fail("missing scripts/axe-audit.mjs")

    try:
        lighthouse = json.loads(lighthouse_path.read_text(encoding="utf-8"))
        raw_urls = lighthouse["ci"]["collect"]["url"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        return fail(f"invalid Lighthouse config: {exc}")

    if not isinstance(raw_urls, list) or not all(isinstance(item, str) for item in raw_urls):
        return fail("Lighthouse url matrix must be a string list")

    lighthouse_routes: list[str] = []
    for raw in raw_urls:
        parsed = urlsplit(raw)
        if parsed.scheme not in {"http", "https"} or parsed.hostname != "localhost":
            return fail(f"unexpected Lighthouse origin: {raw}")
        route = parsed.path or "/"
        if parsed.query or parsed.fragment:
            return fail(f"Lighthouse route must not carry query/fragment: {raw}")
        lighthouse_routes.append(route)

    if lighthouse_routes != EXPECTED_LIGHTHOUSE:
        missing = [route for route in EXPECTED_LIGHTHOUSE if route not in lighthouse_routes]
        extra = [route for route in lighthouse_routes if route not in EXPECTED_LIGHTHOUSE]
        return fail(f"Lighthouse coverage mismatch missing={missing} extra={extra} actual={lighthouse_routes}")
    if len(set(lighthouse_routes)) != len(lighthouse_routes):
        return fail("duplicate Lighthouse route")

    axe_text = axe_path.read_text(encoding="utf-8")
    match = re.search(r"const\s+paths\s*=\s*(\[[\s\S]*?\])\s*;", axe_text)
    if not match:
        return fail("unable to locate axe paths array")
    try:
        axe_routes = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        return fail(f"invalid axe paths array: {exc}")
    if axe_routes != EXPECTED_AXE:
        missing = [route for route in EXPECTED_AXE if route not in axe_routes]
        extra = [route for route in axe_routes if route not in EXPECTED_AXE]
        return fail(f"axe coverage mismatch missing={missing} extra={extra} actual_count={len(axe_routes)}")
    if len(set(axe_routes)) != 30:
        return fail(f"axe route matrix must contain 30 unique active routes, got {len(set(axe_routes))}")

    lighthouse_families = {route.removeprefix("/en").removeprefix("/de") or "/" for route in lighthouse_routes}
    required_hu_families = {f"/{route}" if route else "/" for route in ROUTES}
    if not required_hu_families.issubset(lighthouse_families):
        return fail("Lighthouse representative family coverage incomplete")

    print("OK_AXIONA_BROWSER_AUDIT_MATRIX")
    print(f"LIGHTHOUSE_ROUTES={len(lighthouse_routes)}")
    print(f"AXE_ROUTES={len(axe_routes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
