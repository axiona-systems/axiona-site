#!/usr/bin/env python3
"""Build the complete AXIONA logo export package from two canonical SVG sources.

Source of truth:
- axiona-master-horizontal-fullcolor.svg
- axiona-symbol-fullcolor.svg

All other SVG/PNG/PDF/ZIP files are generated artifacts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import cairosvg
from PIL import Image

HORIZONTAL_SIZE = (2172, 724)
SYMBOL_SIZES = (1024, 512, 256, 192, 180, 128, 64, 48, 32, 16)
PAPER_SYMBOL_SIZES = (1024, 512, 192, 180)
PETROL = "#082830"
PAPER = "#F1EEE6"
REVERSE = "#FBFAF6"
DARK_BG = "#041A20"
DARK_SYMBOL_STROKE = "#0E6A74"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_svg(path: Path) -> ET.ElementTree:
    return ET.parse(path)


def add_background(root: ET.Element, color: str) -> None:
    rect = ET.Element(f"{{{SVG_NS}}}rect", {"width": "100%", "height": "100%", "fill": color})
    root.insert(0, rect)


def write_tree(tree: ET.ElementTree, path: Path) -> None:
    tree.write(path, encoding="unicode", xml_declaration=False)
    with path.open("a", encoding="utf-8") as f:
        f.write("\n")


def generate_variants(master: Path, symbol: Path, out: Path) -> None:
    tree = load_svg(master)
    add_background(tree.getroot(), PAPER)
    write_tree(tree, out / "axiona-horizontal-fullcolor-paper.svg")

    tree = load_svg(master)
    root = tree.getroot()
    add_background(root, DARK_BG)
    petrol_paths = [e for e in root.iter() if e.tag.endswith("path") and e.get("fill", "").upper() == PETROL.upper()]
    for e in petrol_paths:
        e.set("fill", REVERSE)
    if petrol_paths:
        petrol_paths[-1].set("fill", DARK_SYMBOL_STROKE)
    write_tree(tree, out / "axiona-horizontal-fullcolor-dark.svg")

    for name, color in (
        ("axiona-horizontal-monochrome-petrol.svg", PETROL),
        ("axiona-horizontal-monochrome-white.svg", "#FFFFFF"),
    ):
        tree = load_svg(master)
        for e in tree.getroot().iter():
            if e.tag.endswith("path"):
                e.set("fill", color)
        write_tree(tree, out / name)

    tree = load_svg(symbol)
    add_background(tree.getroot(), PAPER)
    write_tree(tree, out / "axiona-symbol-fullcolor-paper.svg")


def render_png(svg: Path, out: Path, width: int, height: int) -> None:
    cairosvg.svg2png(url=str(svg), write_to=str(out), output_width=width, output_height=height)


def render_pdf(svg: Path, out: Path) -> None:
    cairosvg.svg2pdf(url=str(svg), write_to=str(out))


def square_symbol_wrapper(symbol: Path, background: str | None) -> str:
    bg = f'<rect width="100%" height="100%" fill="{background}"/>' if background else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
{bg}
<image href="{symbol.resolve().as_uri()}" x="82" y="219" width="860" height="562" preserveAspectRatio="xMidYMid meet"/>
</svg>'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    src = args.source_dir.resolve()
    out = args.output.resolve()
    master = src / "axiona-master-horizontal-fullcolor.svg"
    symbol = src / "axiona-symbol-fullcolor.svg"
    for p in (master, symbol):
        if not p.is_file():
            raise SystemExit(f"missing canonical source: {p.name}")

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    shutil.copy2(master, out / master.name)
    shutil.copy2(symbol, out / symbol.name)
    if (src / "README.md").is_file():
        shutil.copy2(src / "README.md", out / "README.md")

    generate_variants(master, symbol, out)

    render_png(master, out / "axiona-master-horizontal-fullcolor.png", *HORIZONTAL_SIZE)
    render_pdf(master, out / "axiona-master-horizontal-fullcolor.pdf")
    render_pdf(symbol, out / "axiona-symbol-fullcolor.pdf")

    for svg_name in (
        "axiona-horizontal-fullcolor-paper.svg",
        "axiona-horizontal-fullcolor-dark.svg",
        "axiona-horizontal-monochrome-petrol.svg",
        "axiona-horizontal-monochrome-white.svg",
    ):
        render_png(out / svg_name, out / svg_name.replace(".svg", ".png"), *HORIZONTAL_SIZE)

    with tempfile.TemporaryDirectory() as td_raw:
        td = Path(td_raw)
        transparent = td / "symbol-transparent.svg"
        paper = td / "symbol-paper.svg"
        transparent.write_text(square_symbol_wrapper(symbol, None), encoding="utf-8")
        paper.write_text(square_symbol_wrapper(symbol, PAPER), encoding="utf-8")
        for size in SYMBOL_SIZES:
            render_png(transparent, out / f"axiona-symbol-{size}.png", size, size)
        for size in PAPER_SYMBOL_SIZES:
            render_png(paper, out / f"axiona-symbol-paper-{size}.png", size, size)

    records = []
    for p in sorted(out.iterdir()):
        if not p.is_file():
            continue
        rec = {"file": p.name, "bytes": p.stat().st_size, "sha256": sha256(p)}
        if p.suffix.lower() == ".png":
            with Image.open(p) as im:
                rec["width"], rec["height"] = im.size
        records.append(rec)
    manifest = {
        "schema": "axiona.brand.package.v1",
        "status": "derived-export-package",
        "authoritative_master": master.name,
        "authoritative_symbol": symbol.name,
        "files": records,
    }
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    checksums = []
    for p in sorted(out.iterdir()):
        if p.is_file() and p.name != "CHECKSUMS.sha256":
            checksums.append(f"{sha256(p)}  {p.name}")
    (out / "CHECKSUMS.sha256").write_text("\n".join(checksums) + "\n", encoding="utf-8")

    zip_path = out.parent / "axiona-brand-master-v1.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(out.iterdir()):
            if p.is_file():
                zf.write(p, arcname=p.name)

    print("AXIONA_BRAND_EXPORT=PASS")
    print(f"OUTPUT_DIR={out}")
    print(f"ZIP={zip_path}")
    print(f"FILE_COUNT={len([p for p in out.iterdir() if p.is_file()])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
