#!/usr/bin/env python3
"""Fail closed on AXIONA public-runtime brand drift without regaining brand authority."""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = ROOT / "docs" / "status" / "AXIONA_BRAND_CONSUMER_PROVENANCE.md"
RUNTIME_MANIFEST = ROOT / "assets" / "brand" / "AXIONA_BRAND_RUNTIME_V1.json"
FORBIDDEN_AUTHORITY = (ROOT / "brand", ROOT / ".github" / "workflows" / "brand-master-package.yml", ROOT / "scripts" / "verify_brand_master.py")
FORBIDDEN_LEGACY = (ROOT / "assets" / "axiona-mark.png",)
REQUIRED_PROVENANCE = (
    "axiona-systems/AXIONA_BRAND",
    "aebf0f112bd5f4e589ef58f337a55d9be861b493",
    "374cc2f8738cb0abd519016cac2759b1cc43be0d",
    "1fbe0628bf1d6240495da75dfab2b51a28aac391",
    "sha256:3fbd354301b45ff0fe2e4edff425003eed300b812d228a82ddf798af40ebae0d",
    "R147",
)
HEADER = '/assets/brand/axiona-horizontal-fullcolor.svg'
FOOTER = '/assets/brand/axiona-horizontal-monochrome-white.svg'

def fail(message: str) -> None:
    print(f"STOP_AXIONA_BRAND_CONSUMER_BOUNDARY: {message}", file=sys.stderr)
    raise SystemExit(1)

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    for path in FORBIDDEN_AUTHORITY:
        if path.exists(): fail(f"site contains system-level brand authority: {path.relative_to(ROOT)}")
    for path in FORBIDDEN_LEGACY:
        if path.exists(): fail(f"legacy runtime identity still present: {path.relative_to(ROOT)}")
    if not PROVENANCE.is_file(): fail(f"missing consumer provenance: {PROVENANCE.relative_to(ROOT)}")
    provenance = PROVENANCE.read_text(encoding="utf-8")
    for token in REQUIRED_PROVENANCE:
        if token not in provenance: fail(f"consumer provenance missing authority token: {token}")
    if not RUNTIME_MANIFEST.is_file(): fail("missing machine-readable runtime brand manifest")
    manifest = json.loads(RUNTIME_MANIFEST.read_text(encoding="utf-8"))
    authority = manifest.get("authority", {})
    exact_authority = {
        "repository": "axiona-systems/AXIONA_BRAND",
        "commit": "aebf0f112bd5f4e589ef58f337a55d9be861b493",
        "artifact_digest": "sha256:3fbd354301b45ff0fe2e4edff425003eed300b812d228a82ddf798af40ebae0d",
        "master_git_blob_sha": "374cc2f8738cb0abd519016cac2759b1cc43be0d",
        "symbol_git_blob_sha": "1fbe0628bf1d6240495da75dfab2b51a28aac391",
    }
    for key, value in exact_authority.items():
        if authority.get(key) != value: fail(f"runtime manifest authority mismatch: {key}={authority.get(key)!r}")
    if manifest.get("release") != "R147": fail(f"runtime manifest release mismatch: {manifest.get('release')!r}")
    expected_hashes = manifest.get("sha256")
    if not isinstance(expected_hashes, dict) or not expected_hashes: fail("runtime manifest hash set missing")
    for rel, expected in sorted(expected_hashes.items()):
        path = ROOT / rel
        if not path.is_file(): fail(f"runtime identity asset missing: {rel}")
        observed = sha256(path)
        if observed != expected: fail(f"runtime identity hash drift: {rel} -> {observed} expected {expected}")
    pages = sorted([*ROOT.glob("*.html"), *(ROOT / "en").glob("*.html"), *(ROOT / "de").glob("*.html")])
    if len(pages) != 31: fail(f"public brand page count drift: {len(pages)}")
    for page in pages:
        text = page.read_text(encoding="utf-8"); label = page.relative_to(ROOT).as_posix()
        if '/assets/axiona-mark.png' in text: fail(f"legacy mark binding remains: {label}")
        if text.count(f'src="{HEADER}"') != 1: fail(f"header lockup binding mismatch: {label}")
        if text.count(f'src="{FOOTER}"') != 1: fail(f"footer lockup binding mismatch: {label}")
        if text.count(f'href="{HEADER}"') != 1: fail(f"header lockup preload mismatch: {label}")
        keeper_count = text.count('class="keeper-product-lockup"')
        symbol_count = text.count('src="/assets/brand/axiona-symbol-fullcolor.svg"')
        if label in {"keeper.html", "en/keeper.html", "de/keeper.html"}:
            if keeper_count != 1 or symbol_count != 1: fail(f"Keeper canonical symbol binding mismatch: {label}")
        elif symbol_count: fail(f"unexpected standalone product symbol binding: {label}")
        if 'r92-' in text: fail(f"legacy social-card binding remains: {label}")
    stale_social = sorted((ROOT / "assets" / "social").glob("*r92-*.png"))
    if stale_social: fail("legacy R92 social cards still exist")
    print("AXIONA_BRAND_CONSUMER_BOUNDARY=PASS")
    print("SITE_BRAND_AUTHORITY=false")
    print("SYSTEM_BRAND_AUTHORITY=axiona-systems/AXIONA_BRAND")
    print("BRAND_AUTHORITY_COMMIT=aebf0f112bd5f4e589ef58f337a55d9be861b493")
    print("BRAND_RUNTIME_RELEASE=R147")
    print("PUBLIC_BRAND_PAGES=31")
    print(f"VERIFIED_RUNTIME_ASSETS={len(expected_hashes)}")
    return 0
if __name__ == "__main__": raise SystemExit(main())
