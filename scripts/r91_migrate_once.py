#!/usr/bin/env python3
from pathlib import Path
import binascii
import re
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = ('', 'en/', 'de/')
ROUTES = (
    'index.html', 'systems.html', 'process.html', 'security.html',
    'solutions.html', 'keeper.html', 'contact.html', 'privacy.html',
    'legal.html', 'support.html',
)
GENERAL = 'https://axiona.systems/assets/social/axiona-social-preview-r91.png'
KEEPER = 'https://axiona.systems/assets/social/axiona-keeper-social-preview-r91.png'
LEGACY = 'https://axiona.systems/assets/social/axiona-social-preview-r86.png'


def replace_required(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly one matching meta tag, got {count}')
    return updated


def migrate_html() -> None:
    changed = 0
    for prefix in PREFIXES:
        for route in ROUTES:
            path = ROOT / prefix / route
            text = path.read_text(encoding='utf-8')
            expected = KEEPER if route == 'keeper.html' else GENERAL
            text = replace_required(
                text,
                r'<meta content="[^"]+" property="og:image"/>',
                f'<meta content="{expected}" property="og:image"/>',
                path.as_posix(),
            )
            text = replace_required(
                text,
                r'<meta content="[^"]+" name="twitter:image"/>',
                f'<meta content="{expected}" name="twitter:image"/>',
                path.as_posix(),
            )
            text = re.sub(
                r'<meta content="[^"]+" property="og:image:secure_url"/>',
                f'<meta content="{expected}" property="og:image:secure_url"/>',
                text,
            )
            if LEGACY in text:
                raise RuntimeError(f'{path}: legacy R86 social image URL remains after migration')
            path.write_text(text, encoding='utf-8')
            changed += 1
    if changed != 30:
        raise RuntimeError(f'expected 30 active pages, migrated {changed}')
    print('R91_MIGRATED_ACTIVE_PAGES=30')


def create_keeper_png() -> None:
    width, height = 1200, 630
    bg = (241, 238, 230)
    ink = (11, 30, 37)
    accent = (239, 107, 67)
    muted = (95, 102, 95)
    pixels = bytearray(bg * (width * height))

    def rect(x0, y0, x1, y1, color):
        x0, y0 = max(0, x0), max(0, y0)
        x1, y1 = min(width, x1), min(height, y1)
        row = bytes(color) * max(0, x1 - x0)
        for y in range(y0, y1):
            i = (y * width + x0) * 3
            pixels[i:i + len(row)] = row

    font = {
        'A': ('01110','10001','10001','11111','10001','10001','10001'),
        'X': ('10001','10001','01010','00100','01010','10001','10001'),
        'I': ('11111','00100','00100','00100','00100','00100','11111'),
        'O': ('01110','10001','10001','10001','10001','10001','01110'),
        'N': ('10001','11001','11001','10101','10011','10011','10001'),
        'K': ('10001','10010','10100','11000','10100','10010','10001'),
        'E': ('11111','10000','10000','11110','10000','10000','11111'),
        'P': ('11110','10001','10001','11110','10000','10000','10000'),
        'R': ('11110','10001','10001','11110','10100','10010','10001'),
    }

    def draw_text(x, y, text, scale, color):
        cursor = x
        for ch in text:
            glyph = font[ch]
            for gy, row in enumerate(glyph):
                for gx, bit in enumerate(row):
                    if bit == '1':
                        rect(cursor + gx * scale, y + gy * scale,
                             cursor + (gx + 1) * scale, y + (gy + 1) * scale, color)
            cursor += 6 * scale

    rect(58, 54, 1142, 58, ink)
    rect(58, 572, 1142, 576, ink)
    rect(58, 54, 62, 576, ink)
    rect(1138, 54, 1142, 576, ink)
    rect(76, 74, 96, 556, accent)
    draw_text(132, 118, 'AXIONA', 11, ink)
    draw_text(132, 254, 'KEEPER', 22, ink)
    rect(132, 442, 720, 449, accent)
    rect(894, 168, 1020, 408, ink)
    rect(902, 178, 1012, 390, bg)
    rect(1050, 200, 1115, 408, ink)
    rect(1056, 210, 1109, 390, bg)
    rect(132, 510, 380, 516, muted)

    def chunk(kind: bytes, data: bytes) -> bytes:
        crc = binascii.crc32(kind + data) & 0xffffffff
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', crc)

    raw = bytearray()
    stride = width * 3
    for y in range(height):
        raw.append(0)
        raw.extend(pixels[y * stride:(y + 1) * stride])
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(bytes(raw), 9))
    png += chunk(b'IEND', b'')
    path = ROOT / 'assets/social/axiona-keeper-social-preview-r91.png'
    path.write_bytes(png)
    print(f'R91_KEEPER_ASSET_BYTES={path.stat().st_size}')


def update_verifier() -> None:
    path = ROOT / 'scripts/verify_public_quality.py'
    text = path.read_text(encoding='utf-8')
    constant_anchor = 'KEEPER_PLATFORM_MARKERS = ("iPhone", "iPad", "Apple App Store")\n'
    constants = '''\nGENERAL_SOCIAL_IMAGE = "https://axiona.systems/assets/social/axiona-social-preview-r91.png"\nKEEPER_SOCIAL_IMAGE = "https://axiona.systems/assets/social/axiona-keeper-social-preview-r91.png"\nLEGACY_SOCIAL_IMAGE = "https://axiona.systems/assets/social/axiona-social-preview-r86.png"\nSOCIAL_IMAGE_ASSETS = (\n    "assets/social/axiona-social-preview-r91.png",\n    "assets/social/axiona-keeper-social-preview-r91.png",\n)\n'''
    if 'GENERAL_SOCIAL_IMAGE =' not in text:
        if constant_anchor not in text:
            raise RuntimeError('verifier constant anchor not found')
        text = text.replace(constant_anchor, constant_anchor + constants, 1)

    loop_anchor = '        text = page.read_text(encoding="utf-8")\n        for prefix in ("/fr/", "/es/", "/it/"):\n'
    social_gate = '''        text = page.read_text(encoding="utf-8")\n        expected_social_image = KEEPER_SOCIAL_IMAGE if page.name == "keeper.html" else GENERAL_SOCIAL_IMAGE\n        required_social_meta = (\n            f'content="{expected_social_image}" property="og:image"',\n            f'content="{expected_social_image}" name="twitter:image"',\n            'content="1200" property="og:image:width"',\n            'content="630" property="og:image:height"',\n            'content="image/png" property="og:image:type"',\n        )\n        for token in required_social_meta:\n            if token not in text:\n                errors.append(f"social preview invariant missing in {label}: {token}")\n        if LEGACY_SOCIAL_IMAGE in text:\n            errors.append(f"legacy R86 social preview URL remains active in {label}")\n\n        for prefix in ("/fr/", "/es/", "/it/"):\n'''
    if 'required_social_meta = (' not in text:
        if loop_anchor not in text:
            raise RuntimeError('verifier active-page loop anchor not found')
        text = text.replace(loop_anchor, social_gate, 1)

    manifest_anchor = '    manifest = ROOT / "site.webmanifest"\n'
    asset_gate = '''    for asset in SOCIAL_IMAGE_ASSETS:\n        if not (ROOT / asset).is_file():\n            errors.append(f"missing R91 social preview asset: {asset}")\n\n'''
    if 'missing R91 social preview asset' not in text:
        if manifest_anchor not in text:
            raise RuntimeError('verifier manifest anchor not found')
        text = text.replace(manifest_anchor, asset_gate + manifest_anchor, 1)

    print_anchor = '    print("OK_AXIONA_PUBLIC_QUALITY_PASSED")\n'
    if 'OK_AXIONA_SOCIAL_PREVIEW_R91' not in text:
        if print_anchor not in text:
            raise RuntimeError('verifier print anchor not found')
        text = text.replace(print_anchor, '    print("OK_AXIONA_SOCIAL_PREVIEW_R91")\n' + print_anchor, 1)
    path.write_text(text, encoding='utf-8')


def update_docs() -> None:
    path = ROOT / 'Docs/AXIONA_WEBSITE_MAINTENANCE.md'
    text = path.read_text(encoding='utf-8')
    heading = '## R91 social preview invariant'
    if heading not in text:
        text += '''\n\n## R91 social preview invariant\n\nAll 30 active HU / EN / DE pages use fixed 1200×630 PNG social previews. Normal pages use `assets/social/axiona-social-preview-r91.png`; the three Keeper pages use `assets/social/axiona-keeper-social-preview-r91.png`. `og:image` and `twitter:image` must match, and the width, height and PNG type metadata are release invariants. The old R86 URL must not appear in active HTML. Keep the R91 filenames stable until a deliberate cache-busting release introduces a newer filename.\n'''
        path.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    migrate_html()
    create_keeper_png()
    update_verifier()
    update_docs()
