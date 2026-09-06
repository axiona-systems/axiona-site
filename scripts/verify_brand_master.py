#!/usr/bin/env python3
"""Fail closed if the canonical AXIONA V1 master-logo sources drift."""

from __future__ import annotations

import subprocess
import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

MASTER = Path("brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg")
SYMBOL = Path("brand/assets/master-v1/axiona-symbol-fullcolor.svg")

EXPECTED_BLOBS = {
    MASTER: "374cc2f8738cb0abd519016cac2759b1cc43be0d",
    SYMBOL: "1fbe0628bf1d6240495da75dfab2b51a28aac391",
}
EXPECTED_META = {
    MASTER: ("2172", "724", "0 0 2172 724", 16),
    SYMBOL: ("590", "385", "0 0 590 385", 4),
}
EXPECTED_MASTER_FILLS = Counter({
    "#082830": 13,
    "#E06838": 1,
    "#E8B038": 1,
    "#D0C8B0": 1,
})
EXPECTED_SYMBOL_FILLS = Counter({
    "#082830": 1,
    "#E06838": 1,
    "#E8B038": 1,
    "#D0C8B0": 1,
})


def fail(message: str) -> None:
    print(f"BRAND_MASTER_FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def git_blob(path: Path) -> str:
    result = subprocess.run(
        ["git", "hash-object", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def verify_svg(path: Path, expected_fills: Counter[str]) -> None:
    if not path.is_file():
        fail(f"missing authoritative source: {path}")

    actual_blob = git_blob(path)
    if actual_blob != EXPECTED_BLOBS[path]:
        fail(
            f"authoritative source bytes drifted: {path}; "
            f"expected_blob={EXPECTED_BLOBS[path]} actual_blob={actual_blob}"
        )

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        fail(f"invalid SVG XML: {path}: {exc}")

    expected_width, expected_height, expected_viewbox, expected_path_count = EXPECTED_META[path]
    if root.attrib.get("width") != expected_width:
        fail(f"unexpected width in {path}")
    if root.attrib.get("height") != expected_height:
        fail(f"unexpected height in {path}")
    if root.attrib.get("viewBox") != expected_viewbox:
        fail(f"unexpected viewBox in {path}")

    elements = list(root.iter())
    forbidden = {"image", "text", "script", "foreignObject", "use"}
    found_forbidden = sorted({local_name(e.tag) for e in elements if local_name(e.tag) in forbidden})
    if found_forbidden:
        fail(f"non-path/external SVG content in {path}: {found_forbidden}")

    for element in elements:
        for key in element.attrib:
            if key.lower().endswith("href"):
                fail(f"external/reference href is forbidden in {path}")

    paths = [e for e in elements if local_name(e.tag) == "path"]
    if len(paths) != expected_path_count:
        fail(
            f"path-count drift in {path}; expected={expected_path_count} actual={len(paths)}"
        )

    fills = Counter(e.attrib.get("fill") for e in paths)
    if fills != expected_fills:
        fail(f"palette/path-role drift in {path}; expected={expected_fills} actual={fills}")

    if any(not e.attrib.get("d", "").strip() for e in paths):
        fail(f"empty path geometry in {path}")


def main() -> None:
    verify_svg(MASTER, EXPECTED_MASTER_FILLS)
    verify_svg(SYMBOL, EXPECTED_SYMBOL_FILLS)
    print("AXIONA_BRAND_MASTER_V1=PASS")
    print(f"MASTER_BLOB={EXPECTED_BLOBS[MASTER]}")
    print(f"SYMBOL_BLOB={EXPECTED_BLOBS[SYMBOL]}")
    print("CENTER_OPEN=true")
    print("SMALL_INNER_TRIANGLE=false")


if __name__ == "__main__":
    main()
