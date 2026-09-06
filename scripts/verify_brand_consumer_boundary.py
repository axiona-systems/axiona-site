#!/usr/bin/env python3
"""Fail closed if axiona-site regains AXIONA master-brand authority."""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = ROOT / "docs" / "status" / "AXIONA_BRAND_CONSUMER_PROVENANCE.md"

FORBIDDEN = (
    ROOT / "brand",
    ROOT / ".github" / "workflows" / "brand-master-package.yml",
    ROOT / "scripts" / "verify_brand_master.py",
)

REQUIRED_RUNTIME_ASSETS = (
    ROOT / "assets" / "axiona-mark.png",
    ROOT / "favicon.svg",
    ROOT / "favicon-16x16.png",
    ROOT / "favicon-32x32.png",
    ROOT / "favicon.ico",
    ROOT / "apple-touch-icon.png",
    ROOT / "assets" / "brand" / "axiona-icon-192.png",
    ROOT / "assets" / "brand" / "axiona-icon-512.png",
)

REQUIRED_PROVENANCE = (
    "axiona-systems/AXIONA_BRAND",
    "aebf0f112bd5f4e589ef58f337a55d9be861b493",
    "374cc2f8738cb0abd519016cac2759b1cc43be0d",
    "1fbe0628bf1d6240495da75dfab2b51a28aac391",
)


def fail(message: str) -> None:
    print(f"STOP_AXIONA_BRAND_CONSUMER_BOUNDARY: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    for path in FORBIDDEN:
        if path.exists():
            fail(f"site contains system-level brand authority: {path.relative_to(ROOT)}")

    if not PROVENANCE.is_file():
        fail(f"missing consumer provenance: {PROVENANCE.relative_to(ROOT)}")
    text = PROVENANCE.read_text(encoding="utf-8")
    for token in REQUIRED_PROVENANCE:
        if token not in text:
            fail(f"consumer provenance missing authority token: {token}")

    for path in REQUIRED_RUNTIME_ASSETS:
        if not path.is_file():
            fail(f"public runtime identity asset unexpectedly missing: {path.relative_to(ROOT)}")

    print("AXIONA_BRAND_CONSUMER_BOUNDARY=PASS")
    print("SITE_BRAND_AUTHORITY=false")
    print("SYSTEM_BRAND_AUTHORITY=axiona-systems/AXIONA_BRAND")
    print("RUNTIME_ASSET_MUTATION=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
