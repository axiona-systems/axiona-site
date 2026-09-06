#!/usr/bin/env python3
"""Build every standard AXIONA logo derivative from the two canonical SVG sources."""
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
ORANGE = "#E06838"
YELLOW = "#E8B038"
BEIGE = "#D0C8B0"
PAPER = "#F1EEE6"
REVERSE = "#FBFAF6"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_svg(path: Path) -> ET.ElementTree:
    return ET.parse(path)


def svg_paths(root: ET.Element) -> list[ET.Element]:
    return [element for element in root.iter() if element.tag.endswith("path")]


def add_background(root: ET.Element, color: str) -> None:
    root.insert(
        0,
        ET.Element(
            f"{{{SVG_NS}}}rect",
            {"width": "100%", "height": "100%", "fill": color},
        ),
    )


def write_tree(tree: ET.ElementTree, path: Path) -> None:
    tree.write(path, encoding="unicode", xml_declaration=False)
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n")


def verify_source(master: Path, symbol: Path) -> None:
    master_root = load_svg(master).getroot()
    symbol_root = load_svg(symbol).getroot()
    if master_root.get("viewBox") != "0 0 2172 724":
        raise SystemExit("invalid master viewBox")
    if symbol_root.get("viewBox") != "0 0 590 385":
        raise SystemExit("invalid symbol viewBox")
    symbol_paths = svg_paths(symbol_root)
    if len(symbol_paths) != 4:
        raise SystemExit(f"invalid symbol path count: {len(symbol_paths)}")
    fills = [path.get("fill", "").upper() for path in symbol_paths]
    expected = [PETROL, ORANGE, YELLOW, BEIGE]
    if fills != [color.upper() for color in expected]:
        raise SystemExit(f"invalid symbol palette/order: {fills}")


def generate_svg_variants(master: Path, symbol: Path, output: Path) -> None:
    tree = load_svg(master)
    add_background(tree.getroot(), PAPER)
    write_tree(tree, output / "axiona-horizontal-fullcolor-paper.svg")

    tree = load_svg(master)
    root = tree.getroot()
    add_background(root, PETROL)
    for path in svg_paths(root):
        if path.get("fill", "").upper() == PETROL.upper():
            path.set("fill", REVERSE)
    write_tree(tree, output / "axiona-horizontal-inverse-fullcolor-dark.svg")

    for name, color in (
        ("axiona-horizontal-monochrome-petrol.svg", PETROL),
        ("axiona-horizontal-monochrome-white.svg", "#FFFFFF"),
    ):
        tree = load_svg(master)
        for path in svg_paths(tree.getroot()):
            path.set("fill", color)
        write_tree(tree, output / name)

    tree = load_svg(symbol)
    add_background(tree.getroot(), PAPER)
    write_tree(tree, output / "axiona-symbol-fullcolor-paper.svg")


def render_png(svg: Path, output: Path, width: int, height: int) -> None:
    cairosvg.svg2png(
        url=str(svg),
        write_to=str(output),
        output_width=width,
        output_height=height,
    )


def render_pdf(svg: Path, output: Path) -> None:
    cairosvg.svg2pdf(url=str(svg), write_to=str(output))


def square_symbol_svg(symbol: Path, background: str | None) -> str:
    root = load_svg(symbol).getroot()
    _, _, source_width, source_height = [
        float(value) for value in root.get("viewBox", "0 0 590 385").split()
    ]
    target_width = 860.0
    scale = target_width / source_width
    rendered_height = source_height * scale
    x = (1024.0 - target_width) / 2.0
    y = (1024.0 - rendered_height) / 2.0
    background_tag = (
        f'<rect width="1024" height="1024" fill="{background}"/>'
        if background
        else ""
    )
    content = []
    for path in svg_paths(root):
        attrs = " ".join(f'{key}="{value}"' for key, value in path.attrib.items())
        content.append(f"<path {attrs}/>")
    return (
        f'<svg xmlns="{SVG_NS}" width="1024" height="1024" viewBox="0 0 1024 1024">\n'
        f"{background_tag}\n"
        f'<g transform="translate({x:.6f} {y:.6f}) scale({scale:.9f})">\n'
        + "\n".join(content)
        + "\n</g>\n</svg>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-dir", type=Path, default=Path(__file__).resolve().parent
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source = args.source_dir.resolve()
    output = args.output.resolve()
    master = source / "axiona-master-horizontal-fullcolor.svg"
    symbol = source / "axiona-symbol-fullcolor.svg"
    for path in (master, symbol):
        if not path.is_file():
            raise SystemExit(f"missing canonical source: {path.name}")

    verify_source(master, symbol)

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    for path in (master, symbol):
        shutil.copy2(path, output / path.name)
    for documentation in ("README.md", "EXPORT_SPEC_V1.md"):
        if (source / documentation).is_file():
            shutil.copy2(source / documentation, output / documentation)

    generate_svg_variants(master, symbol, output)

    render_png(
        master,
        output / "axiona-master-horizontal-fullcolor.png",
        *HORIZONTAL_SIZE,
    )
    render_pdf(master, output / "axiona-master-horizontal-fullcolor.pdf")
    render_pdf(symbol, output / "axiona-symbol-fullcolor.pdf")

    for name in (
        "axiona-horizontal-fullcolor-paper.svg",
        "axiona-horizontal-inverse-fullcolor-dark.svg",
        "axiona-horizontal-monochrome-petrol.svg",
        "axiona-horizontal-monochrome-white.svg",
    ):
        render_png(
            output / name,
            output / name.replace(".svg", ".png"),
            *HORIZONTAL_SIZE,
        )

    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary = Path(temporary_directory)
        transparent = temporary / "symbol-transparent.svg"
        paper = temporary / "symbol-paper.svg"
        transparent.write_text(
            square_symbol_svg(symbol, None), encoding="utf-8"
        )
        paper.write_text(square_symbol_svg(symbol, PAPER), encoding="utf-8")
        for size in SYMBOL_SIZES:
            render_png(
                transparent, output / f"axiona-symbol-{size}.png", size, size
            )
        for size in PAPER_SYMBOL_SIZES:
            render_png(
                paper, output / f"axiona-symbol-paper-{size}.png", size, size
            )

    ico_images = [
        Image.open(output / f"axiona-symbol-{size}.png").convert("RGBA")
        for size in (16, 32, 48)
    ]
    ico_images[-1].save(
        output / "axiona-symbol.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=ico_images[:-1],
    )

    records = []
    for path in sorted(output.iterdir()):
        if not path.is_file():
            continue
        record = {
            "file": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        if path.suffix.lower() == ".png":
            with Image.open(path) as image:
                record["width"], record["height"] = image.size
        records.append(record)

    package_manifest = {
        "schema": "axiona.brand.package.v1",
        "status": "derived-export-package",
        "authoritative_master": master.name,
        "authoritative_symbol": symbol.name,
        "files": records,
    }
    (output / "PACKAGE_MANIFEST.json").write_text(
        json.dumps(package_manifest, indent=2) + "\n", encoding="utf-8"
    )

    checksums = []
    for path in sorted(output.iterdir()):
        if path.is_file() and path.name != "CHECKSUMS.sha256":
            checksums.append(f"{sha256(path)}  {path.name}")
    (output / "CHECKSUMS.sha256").write_text(
        "\n".join(checksums) + "\n", encoding="utf-8"
    )

    zip_path = output.parent / "axiona-brand-master-v1.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(
        zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in sorted(output.iterdir()):
            if path.is_file():
                archive.write(path, arcname=path.name)

    print("AXIONA_BRAND_EXPORT=PASS")
    print(f"OUTPUT_DIR={output}")
    print(f"ZIP={zip_path}")
    print(f"FILE_COUNT={len([path for path in output.iterdir() if path.is_file()])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
