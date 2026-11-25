#!/usr/bin/env python3
"""A kiszolgált oldal bájtra egyezik-e a kicsekkolt forrással.

--mode local: http://127.0.0.1:4176 (a CI statikus szervere)
--mode live:  https://axiona.systems (élesítés után, gyorsítótár-kerülő paraméterrel)

Minden sitemap-oldalt, az átirányításokat, a 404-et és a futásidejű fájlokat letölti,
és összeveti a helyi bájtokkal. Eltérésnél megáll.
"""

from __future__ import annotations

import argparse
import ssl
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://axiona.systems"
RUNTIME = [
    "/assets/site.css", "/assets/site.js", "/.well-known/security.txt", "/sitemap.xml", "/llms.txt",
    "/naplo/feed.xml", "/site.webmanifest", "/favicon.svg", "/favicon-32x32.png", "/favicon-16x16.png",
    "/apple-touch-icon.png", "/assets/brand/axiona-horizontal-monochrome-white.svg",
    "/assets/social/axiona-social-preview-r147-hu.png", "/assets/fonts/InterVariable.woff2",
    "/assets/fonts/JetBrainsMono-Regular.woff2",
]


def local_file(route: str) -> Path:
    p = ROOT / route.lstrip("/")
    return p / "index.html" if route.endswith("/") else p


def routes() -> list[str]:
    locs = [el.text.strip() for el in ET.parse(ROOT / "sitemap.xml").getroot().findall("{*}url/{*}loc")]
    pages = [loc[len(SITE):] or "/" for loc in locs]
    redirects = sorted(
        "/" + p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*.html")
        if ".git" not in p.parts and "node_modules" not in p.parts and 'http-equiv="refresh"' in p.read_text(encoding="utf-8")
    )
    return pages + redirects + ["/404.html"] + RUNTIME


# Csak két rögzített cél lehetséges, parancssori vagy környezeti bemenet nem módosíthatja őket.
ORIGINS = {
    "live": "https://axiona.systems",
    "local": "http://127.0.0.1:4176",  # NOSONAR: a CI helyi statikus szervere csak HTTP-n fut
}


def fetch(origin: str, route: str, token: str) -> bytes:
    # Az útvonal a saját sitemapből és fájllistából jön; csak gyökérrelatív, séma és gép nélkül.
    if not route.startswith("/") or route.startswith("//") or "://" in route:
        raise ValueError(f"érvénytelen útvonal: {route}")
    url = f"{origin}{route}?axiona_verify={token}"
    req = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "User-Agent": "axiona-site-verifier"})
    ctx = ssl.create_default_context() if origin.startswith("https://") else None
    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
        return r.read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["local", "live"], required=True)
    ap.add_argument("--attempts", type=int, default=1)
    args = ap.parse_args()
    base = ORIGINS[args.mode]
    todo = routes()
    for attempt in range(1, args.attempts + 1):
        token = f"{int(time.time())}-{attempt}"
        bad = []
        for route in todo:
            expected = local_file(route).read_bytes()
            try:
                got = fetch(base, route, token)
            except (urllib.error.URLError, OSError) as exc:
                bad.append(f"{route}: {exc}")
                continue
            if got != expected:
                bad.append(f"{route}: a kiszolgált tartalom eltér a forrástól")
        if not bad:
            print(f"OK_AXIONA_SERVED_SITE mode={args.mode} routes={len(todo)} attempt={attempt}")
            return 0
        if attempt < args.attempts:
            time.sleep(10)
    for b in bad:
        print(f"STOP_AXIONA_SERVED_SITE: {b}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
