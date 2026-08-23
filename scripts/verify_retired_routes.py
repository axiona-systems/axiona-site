#!/usr/bin/env python3
"""Fail closed if a retired AXIONA public route reappears in source or sitemap."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
HOST = "https://axiona.systems"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
LEGACY_BASENAMES = (
    "impact.html",
    "applications.html",
    "automation.html",
    "company.html",
    "case-study.html",
    "practical-tips.html",
)
RETIRED_ROUTES = tuple(
    [f"/{name}" for name in LEGACY_BASENAMES]
    + [f"/en/{name}" for name in LEGACY_BASENAMES]
    + [f"/de/{name}" for name in LEGACY_BASENAMES]
    + ["/en/404.html", "/de/404.html"]
)


def verify(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for route in RETIRED_ROUTES:
        candidate = (root / route.lstrip("/")).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            errors.append(f"retired route escapes root: {route}")
            continue
        if candidate.exists():
            errors.append(f"retired route source exists: {route}")

    sitemap = root / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("retired route check cannot read sitemap.xml")
    else:
        try:
            tree = ET.parse(sitemap)
            locations = {
                (node.text or "").strip()
                for node in tree.findall(f".//{{{SITEMAP_NS}}}loc")
                if (node.text or "").strip()
            }
            for route in RETIRED_ROUTES:
                url = f"{HOST}{route}"
                if url in locations:
                    errors.append(f"retired route present in sitemap: {route}")
        except ET.ParseError as exc:
            errors.append(f"retired route check invalid sitemap.xml: {exc}")

    html_paths = [
        path
        for path in root.rglob("*.html")
        if path.is_file() and ".git" not in path.parts
    ]
    for path in html_paths:
        text = path.read_text(encoding="utf-8")
        label = path.relative_to(root).as_posix()
        for route in RETIRED_ROUTES:
            if f'href="{route}"' in text or f"href='{route}'" in text:
                errors.append(f"retired route linked from active html: {label} -> {route}")

    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    cli.add_argument("--print-routes", action="store_true")
    args = cli.parse_args()

    if args.print_routes:
        print("\n".join(RETIRED_ROUTES))
        return 0

    errors = verify(args.root)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_RETIRED_ROUTE: {error}", file=sys.stderr)
        return 1
    print(f"OK_AXIONA_RETIRED_ROUTES_R133={len(RETIRED_ROUTES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
