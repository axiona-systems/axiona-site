#!/usr/bin/env python3
"""A v4 nyilvános oldal statikus ellenőrzése.

Hibás állapotban megáll (STOP_AXIONA_SITE), és felsorolja, mi nem teljesült.
Ellenőrzi:
  - a generált fájlok frissek-e (a generátor újrafuttatása nem változtat semmit);
  - a sitemap és a valódi oldalak egyeznek-e;
  - minden belső hivatkozás, kép és horgony létezik-e;
  - minden oldal feje teljes-e (nyelv, cím, leírás, kanonikus cím, közösségi és ikonlinkek);
  - nincs-e külső szkript, követőkód vagy külső erőforrás;
  - az átirányítások és a 404-es oldal helyesek-e;
  - a nyilvános fájlokban nincs-e privát belső név;
  - az adatfájlok szerkezete érvényes-e.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://axiona.systems"
GENERATOR = ROOT / "scripts" / "build_site.py"
GENERATED_SUFFIXES = {".html", ".xml", ".txt"}
SKIP_DIRS = {".git", "node_modules", ".claude", "BUILD", ".lighthouseci"}
PRODUCTS = {"kockalmar", "fejtorpe", "keeper", "axiona"}

# Privát repók és belső rendszerek nevei: nyilvános fájlban nem szerepelhetnek.
PRIVATE_PATTERNS = [
    r"AXIONA_(ENGINE|VERIFIER|HARNESS|KEEPER_WORKTREE|MAC_STEWARD|CHAT_EXECUTION|RELEASE_LIFECYCLE|REFERENCE_LAB|OPERATIONS)",
    r"WORKRUN_BRIDGE", r"\bAXPM\b", r"lego-parts-platform", r"kids-activity-booklets",
    r"axiona-contracts", r"otthon-projekt", r"\bHetzner\b", r"/Users/[a-z]",
]
TRACKING_PATTERNS = [r"googletagmanager", r"google-analytics", r"\bgtag\(", r"connect\.facebook", r"hotjar", r"plausible\.io", r"document\.cookie"]
REQUIRED_ICONS = {
    ("icon", "/favicon.svg"), ("icon", "/favicon-32x32.png"), ("icon", "/favicon-16x16.png"),
    ("apple-touch-icon", "/apple-touch-icon.png"), ("manifest", "/site.webmanifest"),
}

errors: list[str] = []


def stop(msg: str) -> None:
    errors.append(msg)


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.ids: set[str] = set()
        self.h1 = 0
        self.title = ""
        self._in_title = False
        self.meta: dict[str, str] = {}
        self.links: list[tuple[str, str]] = []
        self.refs: list[str] = []
        self.scripts: list[str] = []
        self.imgs: list[dict[str, str]] = []
        self.refresh = ""

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property") or a.get("http-equiv")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            self.links.append((a.get("rel", ""), a.get("href", "")))
            self.refs.append(a.get("href", ""))
        elif tag == "script":
            self.scripts.append(a.get("src", ""))
            if a.get("src"):
                self.refs.append(a["src"])
        elif tag == "img":
            self.imgs.append(a)
            self.refs.append(a.get("src", ""))
            for part in a.get("srcset", "").split(","):
                if part.strip():
                    self.refs.append(part.strip().split()[0])
        elif tag == "a":
            self.refs.append(a.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def public_files() -> list[Path]:
    try:
        out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.splitlines()
        return [ROOT / p for p in out if (ROOT / p).is_file()]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in ROOT.rglob("*") if p.is_file() and not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)]


def generated_snapshot() -> dict[str, str]:
    snap = {}
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if p.is_file() and p.suffix in GENERATED_SUFFIXES and not SKIP_DIRS.intersection(rel.parts) and rel.parts[0] != "scripts":
            snap[rel.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return snap


def route_to_file(route: str) -> Path | None:
    path = urlsplit(route).path
    target = ROOT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    if target.is_file():
        return target
    if (target / "index.html").is_file():
        return target / "index.html"
    return None


def check_generator() -> None:
    before = generated_snapshot()
    run = subprocess.run([sys.executable, str(GENERATOR)], cwd=ROOT, capture_output=True, text=True)
    if run.returncode != 0:
        stop(f"a generátor hibával állt le: {run.stderr.strip()[-300:]}")
        return
    after = generated_snapshot()
    changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
    if changed:
        stop(f"a generált fájlok nem frissek, futtasd: python3 scripts/build_site.py ({', '.join(changed[:8])})")


def check_data() -> None:
    proof = json.loads((ROOT / "data/proof.json").read_text(encoding="utf-8"))
    for r in proof["receipts"]:
        date.fromisoformat(r["date"])
        if r["product"] not in PRODUCTS or not re.fullmatch(r"[A-Z]{2}-\d{4}", r["id"]):
            stop(f"hibás nyugta: {r.get('id')}")
    miles = json.loads((ROOT / "data/milestones.json").read_text(encoding="utf-8"))["milestones"]
    for m in miles:
        date.fromisoformat(m["date"])
        if m["product"] not in PRODUCTS or not all(m.get(k) for k in ("title", "text", "proof")):
            stop(f"hibás mérföldkő: {m.get('title')}")
    if len(miles) < 10:
        stop("túl kevés mérföldkő a Naplóban")
    ideas = json.loads((ROOT / "data/ideas.json").read_text(encoding="utf-8"))["groups"]
    for g in ideas:
        for i in g["items"]:
            if not all(i.get(k) for k in ("name", "line", "who", "why", "scope")):
                stop(f"hiányos ötlet: {i.get('name')}")


def main() -> int:
    check_generator()
    check_data()

    sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text.strip() for el in sitemap.findall("s:url/s:loc", ns)]
    if len(set(locs)) != len(locs):
        stop("ismétlődő sitemap-bejegyzés")

    parsed: dict[Path, Page] = {}
    for f in sorted(p for p in ROOT.rglob("*.html") if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)):
        page = Page()
        page.feed(f.read_text(encoding="utf-8"))
        parsed[f] = page

    content_pages = {f for f, p in parsed.items() if "refresh" not in p.meta and f.name != "404.html"}
    redirects = {f for f, p in parsed.items() if "refresh" in p.meta}
    sitemap_files = set()
    for loc in locs:
        if not loc.startswith(SITE + "/"):
            stop(f"idegen sitemap-cím: {loc}")
            continue
        target = route_to_file(loc[len(SITE):])
        if not target:
            stop(f"a sitemap nem létező oldalra mutat: {loc}")
        else:
            sitemap_files.add(target)
    for f in sorted(content_pages - sitemap_files):
        stop(f"oldal hiányzik a sitemapből: {f.relative_to(ROOT)}")
    for f in sorted(sitemap_files & redirects):
        stop(f"átirányítás a sitemapben: {f.relative_to(ROOT)}")

    for f, p in sorted(parsed.items()):
        label = f.relative_to(ROOT).as_posix()
        route = "/" + label.removesuffix("index.html")
        if p.lang != "hu":
            stop(f"{label}: a nyelv nem hu")
        if f in redirects:
            target = p.meta["refresh"].split("url=", 1)[-1]
            if p.meta.get("robots") != "noindex" or not route_to_file(target):
                stop(f"{label}: hibás átirányítás ({target})")
            continue
        if not p.title.strip() or not p.meta.get("description"):
            stop(f"{label}: hiányzik a cím vagy a leírás")
        if p.h1 != 1:
            stop(f"{label}: {p.h1} darab h1")
        canon = [h for r, h in p.links if r == "canonical"]
        if f.name == "404.html":
            if canon or p.meta.get("robots") != "noindex":
                stop(f"{label}: a 404 legyen noindex, kanonikus cím nélkül")
        elif canon != [SITE + route] or p.meta.get("og:url") != SITE + route:
            stop(f"{label}: hibás kanonikus cím {canon}")
        for key in ("og:title", "og:description", "og:image", "twitter:card", "twitter:image"):
            if not p.meta.get(key):
                stop(f"{label}: hiányzó {key}")
        icons = {(r, h) for r, h in p.links if r in {"icon", "apple-touch-icon", "manifest"}}
        if icons != REQUIRED_ICONS:
            stop(f"{label}: ikonlinkek eltérnek: {sorted(icons ^ REQUIRED_ICONS)}")
        for src in p.scripts:
            if src and not src.startswith("/assets/"):
                stop(f"{label}: külső vagy ismeretlen szkript: {src}")
        for img in p.imgs:
            if "alt" not in img or not img.get("width") or not img.get("height"):
                stop(f"{label}: kép alt vagy méret nélkül: {img.get('src')}")
        for ref in p.refs:
            if not ref or ref.startswith(("mailto:", "tel:")):
                continue
            parts = urlsplit(ref)
            if parts.scheme in {"http", "https"}:
                if parts.netloc == "axiona.systems":
                    ref = parts.path + (f"#{parts.fragment}" if parts.fragment else "")
                    parts = urlsplit(ref)
                elif ref in (r.get("src") for r in p.imgs):
                    stop(f"{label}: külső kép: {ref}")
                    continue
                else:
                    continue
            if ref.startswith("#"):
                if parts.fragment and parts.fragment not in p.ids:
                    stop(f"{label}: nem létező horgony: {ref}")
                continue
            if not ref.startswith("/"):
                stop(f"{label}: relatív hivatkozás: {ref}")
                continue
            target = route_to_file(parts.path)
            if not target and not (ROOT / parts.path.lstrip("/")).is_file():
                stop(f"{label}: nem létező cél: {ref}")
                continue
            if parts.fragment and target in parsed and parts.fragment not in parsed[target].ids:
                stop(f"{label}: nem létező horgony: {ref}")

    for f in public_files():
        if f.suffix.lower() not in {".html", ".xml", ".txt", ".json", ".js", ".css", ".md", ".py", ".mjs", ".yml", ".webmanifest"}:
            continue
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(encoding="utf-8", errors="ignore")
        if rel != "scripts/verify_site.py":
            for pat in PRIVATE_PATTERNS:
                if re.search(pat, text):
                    stop(f"privát belső név nyilvános fájlban: {rel} ({pat})")
        if f.suffix in {".html", ".js"}:
            for pat in TRACKING_PATTERNS:
                if re.search(pat, text):
                    stop(f"követőkód vagy süti: {rel} ({pat})")

    if errors:
        for e in errors:
            print(f"STOP_AXIONA_SITE: {e}")
        return 1
    print("OK_AXIONA_SITE")
    print(f"CONTENT_PAGES={len(content_pages)} REDIRECTS={len(redirects)} SITEMAP={len(locs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
