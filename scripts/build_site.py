#!/usr/bin/env python3
"""AXIONA Systems — statikus oldalgenerátor (v4, „Nyugta”).

Sablonok + tartalom + adatfájlok (data/proof.json, data/ideas.json) → kész HTML.
Futtatás a repó gyökeréből:  python3 scripts/build_site.py
"""

from __future__ import annotations

import html
import json
import pathlib
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROOF = json.loads((ROOT / "data/proof.json").read_text(encoding="utf-8"))
IDEAS = json.loads((ROOT / "data/ideas.json").read_text(encoding="utf-8"))
MILES = json.loads((ROOT / "data/milestones.json").read_text(encoding="utf-8"))
SITE = "https://axiona.systems"
# Szigorú tartalombiztonsági szabály: csak saját forrásból tölthet bármit, beágyazott kód és stílus nélkül.
CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; "
       "manifest-src 'self'; connect-src 'none'; base-uri 'none'; form-action 'none'; upgrade-insecure-requests")
SECURITY_META = (f'  <meta http-equiv="Content-Security-Policy" content="{CSP}">\n'
                 '  <meta name="referrer" content="strict-origin-when-cross-origin">')
SOCIAL_IMAGE = "/assets/social/axiona-social-preview-r147-hu.png"
MAIL = "hello@axiona.systems"
ASSET_V = "13"

E = html.escape


def num(n: int) -> str:
    """Magyar ezres tagolás nem törő szóközzel: 2588 → 2 588."""
    return f"{n:,}".replace(",", " ")


def hu_date(iso: str) -> str:
    return iso.replace("-", ".") + "."


def rfc822(iso: str) -> str:
    import datetime, email.utils
    d = datetime.datetime.fromisoformat(iso + "T12:00:00+01:00")
    return email.utils.format_datetime(d)


def mailto(subject: str) -> str:
    return f"mailto:{MAIL}?subject={quote(subject)}"


PRODUCTS = {
    "kockalmar": {
        "name": "Kockalmár",
        "path": "/kockalmar/",
        "type": "Webshop",
        "line": "Használt LEGO®-alkatrészek webshopja. Darabra, valós készletből, hogy pontosan azt vehesd meg, ami hiányzik.",
        "short": "Használt LEGO®-alkatrészek, darabra, valós készletből.",
        "since": "2026",
        "state": "Fejlesztés alatt",
        "changes": 402,
    },
    "fejtorpe": {
        "name": "Fejtörpe",
        "path": "/fejtorpe/",
        "type": "Nyomtatható füzet",
        "line": "Személyre szabott készségfejlesztő füzetek gyerekeknek, a korukhoz és a szintjükhöz igazítva, magyar nyelven.",
        "short": "Személyre szabott készségfejlesztő füzetek gyerekeknek.",
        "since": "2026",
        "state": "Fejlesztés alatt",
        "changes": 234,
    },
    "keeper": {
        "name": "Keeper",
        "path": "/keeper/",
        "type": "iPhone- és iPad-app",
        "line": "Iratkezelő app. Elolvassa az iratot, kiemeli a lényeget, és csak a te jóváhagyásoddal lép tovább.",
        "short": "Iratkezelő app iPhone-ra és iPadre.",
        "since": "2026",
        "state": "Fejlesztés alatt",
        "changes": 85,
    },
}

RECEIPTS = PROOF["receipts"]
COUNTS = PROOF["counts"]
AS_OF = PROOF["as_of"]

RULES = [
    ("Egy kör.",
     "Egy szándék bemegy, és egy kiadott, ellenőrzött, figyelt változás jön ki belőle.",
     ["Nincs „majdnem kész” állapot, ami félúton marad. Egy változtatás vagy végigér a körön, vagy megáll, és a megállásnak is oka és nyoma van."]),
    ("Egy út, egy bizonyíték.",
     "Minden változtatásnak útrekordja van, és ennek összefoglalója a nyugta.",
     ["A szándék, az elvárás, az ellenőrzés, a jóváhagyás, a kiadás és a működés állapota egy helyen, visszakereshetően. Ami nincs a rekordban, az nem történt meg."]),
    ("A bizonyíték az igazság.",
     "Ami nincs igazolva, az nincs kész.",
     ["Sem egy beszélgetés, sem egy régi jegyzet, sem egy meggyőző összefoglaló nem pótolja a bizonyítékot. A „működik nálam” nem állapot."]),
    ("Kétértelműség = megállás.",
     "Ha egy feladat többféleképpen érthető, a munka el sem indul.",
     ["Előbb tisztázni kell, mi számít késznek. A megállás ilyenkor nem hiba, hanem a rendszer legfontosabb tulajdonsága: nem talál ki választ ott, ahol nincs."]),
    ("Semmi nem igazolja önmagát.",
     "Ami egy munkát elvégez, nem lehet a saját ellenőrzője.",
     ["Az MI által írt kód és az MI által írt teszt együtt nem bizonyíték. Az ellenőrzés független, és a végső döntést ember hozza."]),
    ("Határok és gazdák.",
     "Minden résznek megvan a felelőse és a határa.",
     ["A termék független: akkor is működik, ha az AXIONA áll. A rendszer építi és ellenőrzi a termékeket, de nem fut bennük."]),
    ("Jóváhagyott tanulás.",
     "Ami egy projektben kiderül, csak emberi jóváhagyással válik szabállyá.",
     ["A rendszer javasolhat, de nem írhatja át magát. Egy új szabály ugyanúgy rögzített elvárással, ellenőrzéssel és döntéssel kerül be, mint bármely más változtatás."]),
]

LOOP = [
    ("Szándék", "Mit kell elérni, és miért.", "a kérés"),
    ("Elvárás", "Mi számít késznek, és mihez nem szabad nyúlni.", "elfogadási feltételek"),
    ("Munka", "A változtatás elkülönített környezetben készül, nagyrészt MI-vel.", "változtatás + napló"),
    ("Független ellenőrzés", "Tesztek és ellenőrzők, amelyeket nem a munka végzője írt alá.", "a nyugta"),
    ("Emberi döntés", "Egy ember elfogadja vagy visszaküldi.", "jóváhagyás"),
    ("Kiadás", "Csak az kerül ki, ami a fenti lépéseken átment.", "kiadási rekord"),
    ("Figyelés", "A működés állapotát mérem, nem feltételezem.", "működési állapot"),
]

# A gépház: valódi, egyedi mérnöki megoldások az AXIONA-ból, belső nevek nélkül.
ENGINE = [
    ("Két ellenőrzés, két kézben.",
     "A tesztek a termék saját ellenőrzésében futnak. Mellette egy független ellenőrző a változtatást olvassa el: a kódot nem futtatja, és nem az irányítja, aki a változtatást készítette. Az AXIONA a saját módosításait sem fogadhatja el maga.",
     "tesztek + független átnézés"),
    ("A nyugta ujjlenyomathoz kötött.",
     "Minden ítélet a változtatás pontos ujjlenyomatához tartozik. Ha utána egyetlen bájt is változik, a nyugta érvénytelen, és az ellenőrzés elölről indul.",
     "nyugta = ítélet + ujjlenyomat"),
    ("A hiányzó eredmény nem zöld.",
     "Ha egy ellenőrzés nem futott le, az eredménye „nem értékelt”; ha két forrás ellentmond, „ismeretlen”. Zöldet csak valódi, lefutott ellenőrzés adhat, és a megállás is eredmény: leírja, mi nem igazolódott.",
     "nem értékelt ≠ rendben"),
    ("A leírás nem maradhat le a kódról.",
     "Minden változtatásból kiszámolható, mely dokumentumokat érinti. Mindegyikről kifejezett döntés kell: frissítve, vagy átnézve és nem kell változás. Ha egy hiányzik, a változtatás megáll.",
     "frissítve | átnézve, nincs változás"),
    ("Az MI előre leírt műveletekkel dolgozik.",
     "Az MI és a gépek között egy híd áll, amely csak előre regisztrált műveleteket ismer: külön felhasználóval, elszigetelt gépen, pontos változatra kötve. A kétszer beküldött kérés egyszer fut le, az ütköző kérés megáll.",
     "regisztrált művelet · elszigetelt gép"),
    ("A jogosultság emberhez kötött.",
     "Kiadást, éles üzemet, törlést vagy adatvédelmi döntést csak ember nyithat meg, egy feladatleírás, egy fájl vagy egy MI-válasz nem. Ahol kell, a jóváhagyást az ember eszköze írja alá, biztonsági kulccsal.",
     "kiadás · éles üzem · törlés · jog → ember"),
]


def engine_html(idx: list[int] | None = None) -> str:
    rows = []
    for i, (t, x, spec) in enumerate(ENGINE, 1):
        if idx and i not in idx:
            continue
        rows.append(f"""          <li class="eng__item">
            <span class="eng__no">Megoldás {i:02d}</span>
            <h3 class="eng__title">{E(t)}</h3>
            <p class="eng__text">{E(x)}</p>
            <code class="eng__spec">{E(spec)}</code>
          </li>""")
    return '        <ol class="eng reveal">\n' + "\n".join(rows) + "\n        </ol>"


# ---------------------------------------------------------------- vázak

NAV = [
    ("termekek", "Termékek", "/#termekek"),
    ("egyutt", "Együttműködés", "/egyuttmukodes/"),
    ("hogyan", "Hogyan készül", "/hogyan-keszul/"),
    ("naplo", "Napló", "/naplo/"),
    ("otletlada", "Ötletláda", "/otletlada/"),
    ("rolam", "Rólam", "/rolam/"),
]


def head(path: str, title: str, desc: str, current: str = "", extra_head: str = "") -> str:
    nav = "\n".join(
        f'          <li><a class="nav__link" href="{href}"{" aria-current=\"page\"" if key == current else ""}>{label}</a></li>'
        for key, label, href in NAV)
    menu = "\n".join(f'          <li><a href="{href}">{label}</a></li>' for _, label, href in NAV)
    if path == "/404.html":
        identity = '  <meta name="robots" content="noindex">'
    else:
        identity = f'  <link rel="canonical" href="{SITE}{path}">\n  <meta property="og:url" content="{SITE}{path}">'
    return f"""<!DOCTYPE html>
<html lang="hu">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{SECURITY_META}
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}">
  <meta name="theme-color" content="#0a0f11">
{identity}
  <meta property="og:site_name" content="AXIONA Systems">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="hu_HU">
  <meta property="og:title" content="{E(title)}">
  <meta property="og:description" content="{E(desc)}">
  <meta property="og:image" content="{SITE}{SOCIAL_IMAGE}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="AXIONA Systems">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{SITE}{SOCIAL_IMAGE}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon-32x32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="/favicon-16x16.png" sizes="16x16" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="alternate" type="application/rss+xml" title="AXIONA Systems – Napló" href="/naplo/feed.xml">
  <link rel="preload" href="/assets/fonts/InterVariable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css?v={ASSET_V}">
  <script src="/assets/site.js?v={ASSET_V}" defer></script>{extra_head}
</head>
<body>
  <a class="skip-link" href="#tartalom">Ugrás a tartalomhoz</a>
  <header class="site-header">
    <div class="wrap site-header__inner">
      <a class="brand" href="/" aria-label="AXIONA Systems – főoldal">
        <img src="/assets/brand/axiona-horizontal-monochrome-white.svg" width="2172" height="724" alt="AXIONA Systems">
      </a>
      <nav class="nav" aria-label="Fő navigáció">
        <ul class="nav__list">
{nav}
        </ul>
        <a class="button button--small button--light" href="/kapcsolat/"{" aria-current=\"page\"" if current == "kapcsolat" else ""}>Kapcsolat</a>
      </nav>
      <details class="menu">
        <summary>Menü</summary>
        <ul class="menu__panel">
{menu}
          <li><a href="/kapcsolat/">Kapcsolat</a></li>
        </ul>
      </details>
    </div>
  </header>
  <main id="tartalom">
"""


FOOT = f"""  </main>
  <footer class="site-footer dark">
    <div class="wrap">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="/assets/brand/axiona-horizontal-monochrome-white.svg" width="2172" height="724" alt="AXIONA Systems">
          <p>Termék- és fejlesztőstúdió. Saját termékek és megrendelésre készülő szoftverek, egy saját mérnöki rendszeren, minden változtatáshoz nyugtával.</p>
        </div>
        <div class="footer__col">
          <h2>Termékek</h2>
          <ul>
            <li><a href="/kockalmar/">Kockalmár</a></li>
            <li><a href="/fejtorpe/">Fejtörpe</a></li>
            <li><a href="/keeper/">Keeper</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h2>Stúdió</h2>
          <ul>
            <li><a href="/hogyan-keszul/">Hogyan készül</a></li>
            <li><a href="/naplo/">Napló</a></li>
            <li><a href="/egyuttmukodes/">Együttműködés</a></li>
            <li><a href="/otletlada/">Ötletláda</a></li>
            <li><a href="/rolam/">Rólam</a></li>
            <li><a href="/kapcsolat/">Kapcsolat</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h2>Bizalom</h2>
          <ul>
            <li><a href="/impresszum/">Impresszum</a></li>
            <li><a href="/adatvedelem/">Adatvédelem</a></li>
            <li><a href="/biztonsag/">Biztonság</a></li>
            <li><a href="/tamogatas/">Támogatás</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__base">
        <span>© 2026 AXIONA Systems · Asztalos Zoltán</span>
        <span>Süti és követés nélkül · <a href="{mailto('Kérdés')}">{MAIL}</a></span>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    if path.endswith("/"):
        target = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    else:
        target = ROOT / path.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def redirect(old: str, new: str) -> None:
    write(old, f"""<!DOCTYPE html>
<html lang="hu">
<head>
  <meta charset="utf-8">
{SECURITY_META}
  <title>Átirányítás | AXIONA Systems</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{SITE}{new}">
  <meta http-equiv="refresh" content="0; url={new}">
</head>
<body>
  <p>Ez az oldal átköltözött: <a href="{new}">{SITE}{new}</a></p>
</body>
</html>
""")


# ---------------------------------------------------------------- összetevők

def receipt(r: dict, print_anim: bool = False, pins: bool = False) -> str:
    p = PRODUCTS[r["product"]]
    tests = f'{num(r["tests"])} teszt · OK' if r.get("tests") else "OK"

    def pin(n: int) -> str:
        return f'<span class="pin" aria-hidden="true">{n}</span>' if pins else ""

    rows = [
        ("Termék", E(p["name"]), ""),
        ("Változás", E(r["text"]), " receipt__row--change"),
        (f"Elvárás{pin(1)}", '<span class="receipt__ok">rögzítve</span>', ""),
        (f"Ellenőrzés{pin(2)}", f'<span class="receipt__ok">{tests}</span>', ""),
        (f"Emberi döntés{pin(3)}", '<span class="receipt__ok">elfogadva</span>', ""),
        (f"Dátum{pin(4)}", r["date"], ""),
    ]
    rows_html = "\n".join(
        f'          <div class="receipt__row{cls}"><dt>{k}</dt><dd>{v}</dd></div>' for k, v, cls in rows)
    return f"""      <div class="receipt"{' data-print' if print_anim else ''}>
        <div class="receipt__head"><span>AXIONA · Nyugta</span><span class="receipt__no">{r["id"]}</span></div>
        <dl class="receipt__rows">
{rows_html}
        </dl>
        <p class="receipt__stamp"><span>Állapot{pin(5)}</span><strong>Ellenőrizve</strong></p>
      </div>"""


MILESTONES = sorted(MILES["milestones"], key=lambda m: m["date"], reverse=True)
KIND_NAME = {"kockalmar": "Kockalmár", "fejtorpe": "Fejtörpe", "keeper": "Keeper", "axiona": "AXIONA"}
KIND_PATH = {"kockalmar": "/kockalmar/", "fejtorpe": "/fejtorpe/", "keeper": "/keeper/", "axiona": "/hogyan-keszul/#gephaz"}


def ms_entry(m: dict, h: str = "h3", show_kind: bool = True) -> str:
    kind = m["product"]
    kind_html = f'<span class="ms__kind dot-{kind}">{KIND_NAME[kind]}</span>' if show_kind else ""
    return f"""        <li class="ms{' ms--top' if m.get('top') else ''}" data-kind="{kind}">
          <div class="ms__meta"><time datetime="{m['date']}">{hu_date(m['date'])}</time>{kind_html}</div>
          <div class="ms__body">
            <{h} class="ms__title"><a href="{KIND_PATH[kind]}">{E(m['title'])}</a></{h}>
            <p class="ms__text">{E(m['text'])}</p>
            <span class="ms__proof"><b>elfogadva</b> · {E(m['proof'])}</span>
          </div>
        </li>"""


# Saját jelek a két termékhez, egyszerű vonalas rajzként, a termék anyagszínében.
SYMBOLS = {
    # Fejtörpe: füzetlap, rajta pontösszekötő feladat.
    "fejtorpe": (
        '<svg class="lockup__sym" viewBox="0 0 64 80" aria-hidden="true" focusable="false">'
        '<rect x="3" y="3" width="58" height="74" rx="4" fill="none" stroke="currentColor" stroke-width="3"/>'
        '<path d="M14 58 L22 30 L32 46 L42 22 L50 56" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="1 5" stroke-linecap="round"/>'
        '<g fill="currentColor"><circle cx="14" cy="58" r="3"/><circle cx="22" cy="30" r="3"/><circle cx="32" cy="46" r="3"/>'
        '<circle cx="42" cy="22" r="3"/><circle cx="50" cy="56" r="3"/></g>'
        '<path d="M14 68 H50" stroke="currentColor" stroke-width="2" opacity=".45"/></svg>'
    ),
    # Keeper: irat behajtott sarokkal, kiemelt sorral és könyvjelzővel.
    "keeper": (
        '<svg class="lockup__sym" viewBox="0 0 64 80" aria-hidden="true" focusable="false">'
        '<path d="M5 3 H43 L59 19 V77 H5 Z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>'
        '<path d="M43 3 V19 H59" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>'
        '<path d="M14 32 H50 M14 52 H44 M14 62 H38" stroke="currentColor" stroke-width="2.5" opacity=".5" stroke-linecap="round"/>'
        '<rect x="12" y="38" width="40" height="8" rx="2" fill="currentColor" opacity=".9"/>'
        '<path d="M48 63 V80 L53 75 L58 80 V63 Z" fill="currentColor"/></svg>'
    ),
}


def ms_note(n: dict, h: str = "h3") -> str:
    return f"""        <li class="ms ms--note" data-kind="iras">
          <div class="ms__meta"><time datetime="{n['date']}">{hu_date(n['date'])}</time><span class="ms__kind dot-iras">Írás</span></div>
          <div class="ms__body">
            <{h} class="ms__title"><a href="{n['path']}">{E(n['title'])}</a></{h}>
            <p class="ms__text">{E(n['lead'])}</p>
            <span class="ms__proof">{n['minutes']} perc olvasás</span>
          </div>
        </li>"""


def mark(key: str, size: str = "") -> str:
    if key == "kockalmar":
        return ('<img src="/assets/img/kockalmar-logo-v2-512.webp" width="512" height="384" decoding="async" loading="lazy" '
                'alt="A Kockalmár logója: sárga kocka kabalafigura, Régi darabok. Új történetek.">')
    sym = SYMBOLS.get(key, "")
    return (f'<span class="lockup lockup--{key}">{sym}'
            f'<span class="wordmark{size}">{E(PRODUCTS[key]["name"])}</span></span>')


def last_receipts(key: str, n: int = 3) -> list[dict]:
    return sorted((r for r in RECEIPTS if r["product"] == key), key=lambda r: (r["date"], r["id"]), reverse=True)[:n]


def sec_head(no: str, title: str, lead: str = "", hid: str = "") -> str:
    lead_html = f'\n          <p class="sec-head__lead">{lead}</p>' if lead else ""
    return f"""      <header class="sec-head reveal">
        <span class="label sec-head__no">{no}</span>
        <div>
          <h2 class="sec-head__title"{f' id="{hid}"' if hid else ''}>{title}</h2>{lead_html}
        </div>
      </header>"""


def loop_html() -> str:
    items = []
    for i, (name, text, trace) in enumerate(LOOP, 1):
        ok = " loop__st--ok" if name == "Független ellenőrzés" else ""
        items.append(f"""          <li class="loop__st{ok}">
            <span class="loop__no">{i:02d}</span>
            <span class="loop__name">{name}</span>
            <span class="loop__text">{text}</span>
            <span class="loop__trace">{trace}</span>
          </li>""")
    items.append("""          <li class="loop__st loop__st--back" aria-label="A kör vége: vissza a szándékhoz">
            <span class="loop__name">↺ vissza a szándékhoz</span>
            <span class="loop__text">Amit a figyelés mutat, abból lesz a következő szándék.</span>
          </li>""")
    return '        <ol class="loop" aria-label="Egy változtatás útja az AXIONA-ban">\n' + "\n".join(items) + "\n        </ol>"


def claims_html() -> str:
    return """      <div class="claims">
        <div class="claims__col claims__col--yes reveal">
          <span class="label">Állítom</span>
          <h3>Amit a rendszerem minden változtatásnál rögzít</h3>
          <ul>
            <li>Minden változtatásnak előre rögzített elvárása, független ellenőrzése és nyoma van.</li>
            <li>A végső döntést ember hozza, nem az MI.</li>
            <li>Ha valami nem bizonyítható, nem kerül ki.</li>
            <li>A termékek az AXIONA nélkül is működnek.</li>
          </ul>
        </div>
        <div class="claims__col claims__col--no reveal">
          <span class="label">Nem állítom</span>
          <h3>Amit senki nem tud tisztességesen</h3>
          <ul>
            <li>Hogy a szoftver hibamentes.</li>
            <li>Hogy minden hibát megtalálok.</li>
            <li>Hogy feltörhetetlen.</li>
            <li>Felhasználószámot, amíg a termékek nem élnek.</li>
            <li>Hogy a nyugtákat kívülről ellenőrizni lehet: a forráskód privát, a nyugta a saját rendszerem kivonata.</li>
          </ul>
        </div>
      </div>"""


def kpis_html() -> str:
    items = [
        (str(COUNTS["products_in_development"]), "termék, egy ember"),
        (str(len(MILES["milestones"])), "elfogadott mérföldkő a Naplóban"),
        ("2", "munkanapon belül válaszolok"),
        ("0", "süti és követőkód ezen az oldalon"),
    ]
    cells = "\n".join(
        f'        <div class="kpi"><span class="kpi__value">{v}</span><span class="kpi__label">{l}</span></div>' for v, l in items)
    return f"""      <div class="kpis reveal">
{cells}
      </div>
      <p class="kpis__note">Állapot: {hu_date(AS_OF)}</p>"""


OFFER = [
    ("Webes rendszerek",
     "Webshop, ügyfélportál, foglalási vagy rendeléskezelő rendszer, adminfelület, és a meglévő rendszereid összekötése.",
     "mint a Kockalmár"),
    ("iPhone- és iPad-appok",
     "Natív app a cégednek vagy az ügyfeleidnek, a készüléken tartott adatokkal, ahol ez számít.",
     "mint a Keeper"),
    ("Belső céges eszközök",
     "Nyilvántartások, dokumentumgyártás, jelentések és megfelelési feladatok, amelyeket ma táblázatban vagy papíron vezetsz.",
     "mint a Fejtörpe PDF-gyártása"),
]
# Csak olyan eszköz kerül ide, amelyet a termékeim ténylegesen használnak.
TOOLS = [
    ("Nyelvek és keretrendszerek", "", ["Python", "Django", "Swift", "SwiftUI", "HTML, CSS, JavaScript"]),
    ("Adatbázis", "", ["PostgreSQL", "SQLite", "SQLCipher (titkosított tárolás)"]),
    ("Üzemeltetés", "", ["Linux-szerver", "nginx", "systemd", "restic (titkosított mentés)", "Sentry (hibafigyelés)"]),
    ("Minőség és biztonság", "", ["automatizált tesztek", "böngészős tesztek (Selenium, Playwright)", "Ruff", "Semgrep", "pip-audit", "gitleaks", "SonarQube", "SBOM minden kiadáshoz", "Lighthouse", "axe"]),
    ("Fejlesztési folyamat", "", ["Git és GitHub", "GitHub Actions", "saját macOS- és Linux-futtatók", "Xcode"]),
    ("MI a fejlesztésben", "", ["Claude Code", "ChatGPT és Codex", "a saját AXIONA-ellenőrzés"]),
    ("Integrációk", "már használom", ["Stripe", "NAV Online Számla séma", "FOXPOST csomagautomaták", "képgeneráló MI-modellek"]),
    ("Integrációk", "ha a projekt kéri", [
        "Barion, SimplePay", "Számlázz.hu, Billingo", "GLS, MPL, Packeta",
        "Microsoft 365, Google Workspace", "egyszeri belépés (OAuth 2.0, OpenID Connect)",
        "REST API-k és webhookok", "CSV-, Excel- és PDF-export", "e-mail- és SMS-értesítés",
        "Apple Push értesítések", "Sign in with Apple",
    ]),
    ("Biztonság", "ha a projekt kéri", [
        "kétlépcsős belépés (TOTP, passkey)", "szerepkör alapú jogosultságok", "auditnapló",
        "titkosítás tároláskor és átvitelkor", "titokkezelés (1Password, felhős kulcstár)",
        "OWASP ASVS szerinti ellenőrzés", "OWASP ZAP, Trivy szkennelés", "WAF és DDoS-védelem (Cloudflare)",
        "mentés és helyreállítási próba", "külső behatolásteszt", "GDPR- és NIS2-dokumentáció",
    ]),
]


def offer_html() -> str:
    cards = "\n".join(f"""          <article class="offer__item">
            <h3>{E(t)}</h3>
            <p>{E(x)}</p>
            <span class="label">{E(ref)}</span>
          </article>""" for t, x, ref in OFFER)
    return f"""        <div class="offer reveal">
{cards}
        </div>"""


NOTES = [
    {
        "slug": "megallas-nem-hiba",
        "path": "/naplo/megallas-nem-hiba/",
        "date": "2026-11-24",
        "minutes": 3,
        "title": "Miért nem hiba, ha a rendszer megáll",
        "lead": "A legtöbb szoftver akkor is ad valamilyen választ, ha nem tudja a jót. Az AXIONA ilyenkor megáll.",
        "body": [
            ("p", "Egy feladat ritkán hibás. Sokkal gyakrabban kétértelmű: kétféleképpen is érthető, és mindkét olvasat ésszerűnek tűnik. Egy ember ilyenkor visszakérdez. Egy MI-alapú rendszer hajlamos választani, és magabiztosan továbbmenni."),
            ("p", "Az AXIONA-ban a kétértelműség nem a munka része, hanem a munka előtti akadály. Ha nem egyértelmű, mi számít késznek, a változtatás el sem indul. A rendszer megáll, és leírja, mit nem tud eldönteni."),
            ("h2", "Megállás vagy hiba?"),
            ("p", "A hiba az, amikor valami rosszul működik. A megállás az, amikor a rendszer felismeri, hogy nem tudná biztosan jól csinálni. Az elsőből javítás lesz, a másodikból egy jobb kérdés."),
            ("p", "Kívülről a megállás lassúnak tűnhet. Valójában ez a legolcsóbb pont egy hiba megfogására: még mielőtt egyetlen sor kód elkészülne rossz feltevésre."),
        ],
    },
    {
        "slug": "onmagat-nem-igazolja",
        "path": "/naplo/onmagat-nem-igazolja/",
        "date": "2026-11-23",
        "minutes": 3,
        "title": "Miért nem igazolhatja az MI a saját munkáját",
        "lead": "Ha ugyanaz írja a kódot és a tesztet, a teszt csak azt bizonyítja, hogy a kettő egyetért egymással.",
        "body": [
            ("p", "Az MI gyorsan ír kódot, és ugyanilyen gyorsan ír hozzá tesztet. A kettő szinte mindig egyezik, hiszen ugyanabból a feltevésből készült. Ha a feltevés rossz, mindkettő rossz, és a teszt mégis zöld."),
            ("p", "Ezért az AXIONA egyik alapszabálya: semmi nem igazolja önmagát. Ami egy munkát elvégez, nem lehet a saját ellenőrzője. Az ellenőrzés független forrásból jön: előre rögzített elfogadási feltételekből, a munkától elkülönített ellenőrzőkből, és végül egy emberi döntésből."),
            ("h2", "Mit jelent ez a gyakorlatban?"),
            ("p", "Egy változtatás előre rögzített elvárással indul: mi számít késznek, és mihez nem szabad nyúlni. A munka után a független ellenőrzés ehhez méri az eredményt, nem ahhoz, amit a munka végzője állít magáról. A nyugta ennek a mérésnek az összefoglalója."),
            ("p", "Ez nem teszi hibátlanná a szoftvert. Azt teszi lehetővé, hogy minden állítás mögött ott legyen, mi igazolja, és ki döntött."),
        ],
    },
]

# ---------------------------------------------------------------- főoldal

hero_r = next(r for r in RECEIPTS if r.get("hero"))


def product_block(key: str) -> str:
    p = PRODUCTS[key]
    latest_ms = next(m for m in MILESTONES if m["product"] == key and not m.get("tech"))
    return f"""        <article class="product product--{key}" aria-labelledby="p-{key}">
          <div class="product__mark">{mark(key)}</div>
          <div class="product__body">
            <span class="label">{E(p['type'])}</span>
            <h3 class="product__name" id="p-{key}">{E(p['name'])}</h3>
            <p class="product__line">{E(p['line'])}</p>
            <p class="product__proof">Legutóbb: {E(latest_ms['title'])}</p>
            <div class="actions">
              <a class="button" href="{p['path']}">Megnézem <span class="button__arrow" aria-hidden="true">→</span></a>
              <a class="button button--ghost" href="{mailto(p['name'] + ' – értesítést kérek')}">Értesítést kérek</a>
            </div>
          </div>
        </article>"""


home = head("/", "AXIONA Systems — Szoftver, amihez nyugta jár.",
            "Termék- és fejlesztőstúdió: saját termékek (Kockalmár, Fejtörpe, Keeper) és megrendelésre készülő szoftverek, minden változtatáshoz független ellenőrzéssel.") + f"""
    <section class="sec dark grid-lines hero" aria-labelledby="hero-cim">
      <div class="wrap hero__grid">
        <div>
          <span class="label hero__kicker">AXIONA Systems · termék- és fejlesztőstúdió</span>
          <h1 class="hero__title" id="hero-cim">Szoftver, amihez nyugta jár.</h1>
          <p class="hero__lead"><strong>Saját termékeket építek, és megrendelésre neked is.</strong> Minden változtatás előre rögzített elvárással indul, független ellenőrzéssel zárul, és nyoma marad.</p>
          <div class="actions">
            <a class="button" href="#termekek">A termékek <span class="button__arrow" aria-hidden="true">↓</span></a>
            <a class="button button--ghost" href="/egyuttmukodes/">Neked is építek</a>
          </div>
        </div>
        <figure class="fig">
          <figcaption class="fig__cap"><span>Ábra 01 · Legutóbbi nyugta</span><span>belső kivonat</span></figcaption>
{receipt(hero_r, print_anim=True)}
        </figure>
      </div>
    </section>

    <section class="sec sec--tight dark grid-lines" aria-label="Számok">
      <div class="wrap">
{kpis_html()}
      </div>
    </section>

    <section class="sec light" id="termekek" aria-labelledby="termekek-cim">
      <div class="wrap">
{sec_head("01 — Termékek", "Három termék. Mindegyik a saját útján.", "Egy webshop, egy füzetkészítő és egy iPhone-app. Közös bennük, ahogyan készülnek.", "termekek-cim")}
        <div class="products">
{product_block("kockalmar")}
{product_block("fejtorpe")}
{product_block("keeper")}
        </div>
      </div>
    </section>

    <section class="sec dark grid-lines" aria-labelledby="hogyan-cim">
      <div class="wrap">
{sec_head("02 — Hogyan készül", "Gép segít, ember dönt.", "A kód nagy részét MI írja velem, de a szabályt, a mércét és a végső döntést én adom. Az AXIONA a saját mérnöki rendszerem: ez az a rend, amelyben minden készül. Nem termék, és nem eladó.", "hogyan-cim")}
        <figure class="fig reveal">
          <figcaption class="fig__cap"><span>Ábra 02 · A kör</span><span>egy változtatás útja</span></figcaption>
{loop_html()}
        </figure>
        <p class="mt-l"><a class="text-link" href="/hogyan-keszul/">Hogyan működik a gépház: hat megoldás, hét szabály →</a></p>
      </div>
    </section>

    <section class="sec light" aria-labelledby="egyutt-cim">
      <div class="wrap">
{sec_head("03 — Együttműködés", "Neked is építek.", "Webes rendszert, iPhone-appot vagy belső céges eszközt ugyanúgy építek, mint a saját termékeimet: előre rögzített elvárásokkal, független ellenőrzéssel, és úgy, hogy minden lépést látsz.", "egyutt-cim")}
{offer_html()}
        <div class="actions mt-l">
          <a class="button" href="/egyuttmukodes/">Hogyan dolgozunk együtt <span class="button__arrow" aria-hidden="true">→</span></a>
          <a class="button button--ghost" href="/kapcsolat/?tema=fejlesztes">Írd le, mire van szükséged</a>
        </div>
      </div>
    </section>

    <section class="sec light" aria-labelledby="allitas-cim">
      <div class="wrap">
{sec_head("04 — Őszintén", "Mit állítok, és mit nem.", "A határok kiírása olcsóbb és tisztességesebb, mint bármilyen ígéret.", "allitas-cim")}
{claims_html()}
      </div>
    </section>

    <section class="sec light" aria-labelledby="naplo-cim">
      <div class="wrap">
{sec_head("05 — Napló", "A nagy lépések.", "Amikor valami először működött végig, vagy a rendszer új képességet kapott. Mind elfogadott, dátummal.", "naplo-cim")}
        <ol class="mslist reveal">
{chr(10).join(ms_entry(m) for m in [x for x in MILESTONES if x.get("top")][:5])}
        </ol>
        <p class="mt-m"><a class="text-link" href="/naplo/">Mind a {len(MILESTONES)} mérföldkő →</a></p>
      </div>
    </section>

    <section class="sec dark grid-lines" aria-labelledby="ps-cim">
      <div class="wrap ps">
        <span class="label">06 — Utóirat</span>
        <div>
          <h2 class="visually-hidden" id="ps-cim">Utóirat</h2>
          <div class="ps__body reveal">
            <p>Az AXIONA Systems mögött egyetlen ember áll: én. Én találom ki a termékeket, én építem őket, és én felelek értük.</p>
            <p>A kód nagy részét ma már MI írja velem együtt, de minden változtatást én nézek át és én hagyok jóvá. Csak az kerül ki, amiről tudom, mit csinál.</p>
            <p>Még nem minden hibátlan, de makacsul azon vagyok, hogy az legyen. Ha valami mégis elromlik, megkeresem az okát, kijavítom, és őszintén megírom, mi történt.</p>
            <div class="ps__sign">
              <span class="ps__name">Zoli</span>
              <span class="label">Asztalos Zoltán</span>
            </div>
          </div>
          <p class="now"><span class="label">Most</span><span>A Kockalmár pénztárán és a Fejtörpe füzetstúdióján dolgozom.</span><a class="text-link" href="/kapcsolat/">Írj nekem →</a></p>
        </div>
      </div>
    </section>
""" + FOOT

write("/", home)

# ---------------------------------------------------------------- termékoldalak

PRODUCT_PAGES = {
    "kockalmar": {
        "title": "Kockalmár — Használt LEGO®-alkatrészek webshopja | AXIONA Systems",
        "desc": "Kockalmár: használt LEGO®-alkatrészek webshopja, darabra, valós készletből. Fejlesztés alatt.",
        "sheet": [("Platform", "Webshop"), ("Nyelv", "magyar, angol"), ("Pénznem", "forint"), ("Állapot", "Fejlesztés alatt")],
        "what": [
            "Webshop használt LEGO®-alkatrészekhez. Nem készleteket árul, hanem egyes darabokat: ha egy építéshez hiányzik néhány elem, itt célzottan megtalálod őket.",
            "A bolt mögött saját raktárrendszer áll, így a webshopban látható mennyiség a valós készletet követi.",
        ],
        "now": [
            "Keresés és szűrés, amely megjegyzi, hol jártál, amikor visszalépsz a katalógusba.",
            "Termékoldal egyetlen, átlátható vásárlási blokkal.",
            "Kosár érthető mennyiségekkel és részösszeggel.",
            "Pénztár vendégként vagy fiókkal, külön számlázási címmel.",
            "Szállítás házhoz vagy csomagautomatába, látható ingyenes szállítási határral.",
        ],
        "next": [
            "Éles fizetés és számlázás bekötése.",
            "Az első valódi készlet feltöltése.",
            "Indulás, saját domainen.",
        ],
        "faq": [
            ("Mikor indul?", "Még nincs dátum. Akkor indul, amikor a fizetés, a számlázás és a készlet is éles próbán átment. Ha kérsz értesítést, szólok."),
            ("Mit lehet majd venni?", "Használt LEGO®-alkatrészeket darabra: konkrét elemeket, színben és mennyiségben, a valós raktárkészletből."),
            ("Mennyibe kerül?", "Az árak forintban lesznek, darabonként. Árlistát az indulásig nem teszek közzé."),
            ("Kapcsolatban áll a LEGO Grouppal?", "Nem. A Kockalmár független kereskedés, a LEGO Grouppal nem áll kapcsolatban."),
        ],
        "notice": "A LEGO® a LEGO Group védjegye. A Kockalmár független kereskedés, a LEGO Grouppal nem áll kapcsolatban, és nem tőle származó jóváhagyással működik.",
    },
    "fejtorpe": {
        "title": "Fejtörpe — Személyre szabott készségfejlesztő füzetek | AXIONA Systems",
        "desc": "Fejtörpe: személyre szabott, nyomtatható készségfejlesztő füzetek gyerekeknek, a korukhoz és szintjükhöz igazítva, magyar nyelven.",
        "sheet": [("Formátum", "nyomtatható PDF, A4"), ("Nyelv", "magyar"), ("Személyre szabás", "név, kor, szint, téma"), ("Állapot", "Fejlesztés alatt")],
        "what": [
            "Készségfejlesztő füzet, amely egy konkrét gyereknek készül. A feladatok a korához és a szintjéhez igazodnak, és a saját nevével, a kedvenc témájával találkozik benne.",
            "Minden oldalt ember néz át és hagy jóvá, mielőtt a füzet elkészül. A végén nyomtatható PDF-et kapsz.",
        ],
        "now": [
            "Füzet összeállítása lépésről lépésre, egy füzetstúdióban.",
            "Minden oldal valódi előnézete, egyenkénti jóváhagyással.",
            "Nyomtatható PDF letöltése a végén.",
            "A jóváhagyott rajzstílus újra felhasználható a hasonló füzeteknél.",
            "Magyar feladatutasítások, az ellenőrzött feladatokhoz kötve.",
        ],
        "next": [
            "Első kipróbálás valódi családokkal.",
            "Több feladattípus és korosztály.",
            "Rendelés.",
        ],
        "faq": [
            ("Hány éves gyerekeknek szól?", "Nem egy korosztálynak. A feladatok a gyerek korához és szintjéhez igazodnak, ezért ugyanaz a rendszer kisebbeknek és nagyobbaknak is készít füzetet."),
            ("Milyen adatot kell megadni?", "Csak ami a füzethez kell: a gyerek keresztnevét, korát, szintjét és egy témát. A részleteket a megjelenés előtti adatvédelmi tájékoztató írja le."),
            ("Ki ellenőrzi a feladatokat?", "Minden oldal emberi jóváhagyáson megy át. A gép összeállít, de nem ő dönti el, hogy egy oldal jó-e."),
            ("Mikor rendelhető?", "Még nincs dátum. Előbb valódi családokkal próbálom ki. Ha kérsz értesítést, szólok."),
        ],
        "notice": "",
    },
    "keeper": {
        "title": "Keeper — Iratkezelő app iPhone-ra | AXIONA Systems",
        "desc": "Keeper: iPhone- és iPad-alkalmazás, amely elolvassa az iratot, kiemeli a lényeget, és csak a jóváhagyásoddal lép tovább. Fejlesztés alatt.",
        "sheet": [("Platform", "iPhone, iPad"), ("Terjesztés", "App Store"), ("Bemenet", "PDF vagy fotó"), ("Állapot", "Fejlesztés alatt")],
        "what": [
            "Egy PDF vagy egy iratról készült fotó elég. A Keeper megpróbálja felismerni, mi érkezett (számla, szerződés, értesítő vagy levél), és kiemeli a fontos adatokat: dátumot, összeget, azonosítót, határidőt.",
            "Ha valamiben nem biztos, rákérdez. Rendezés, emlékeztető vagy más lépés csak a jóváhagyásoddal történik.",
        ],
        "now": [
            "Keresés a saját irataidban.",
            "„Kérdezd a Keepert”: válasz csak a betöltött iratokból, mindig forrással.",
            "Ha nincs biztos válasz, ezt mondja, és nem talál ki semmit.",
            "Valódi iPhone-on kipróbált felület.",
        ],
        "next": [
            "Határidők és teendők jelzése.",
            "Iratok rendezése személy, szolgáltató vagy ügy szerint.",
            "Megjelenés az App Store-ban.",
        ],
        "faq": [
            ("Hová kerülnek az irataim?", "A keresés és a válasz a készüléken fut, külső MI-szolgáltatás nélkül. A részleteket a megjelenés előtti adatvédelmi tájékoztató írja le."),
            ("Kitalál válaszokat?", "Nem. Ha az irataidban nincs egyértelmű forrás, a Keeper ezt mondja, és megmutatja, mit talált."),
            ("Milyen eszközön működik?", "iPhone-on és iPaden."),
            ("Mikor tölthető le?", "Még nincs dátum. Ha kérsz értesítést, szólok, amikor az App Store-ban elérhető."),
        ],
        "notice": "Az Apple, az iPhone, az iPad és az App Store az Apple Inc. védjegyei.",
    },
}

for key, pp in PRODUCT_PAGES.items():
    p = PRODUCTS[key]
    sheet = "\n".join(f'        <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in pp["sheet"])
    now = "\n".join(f"              <li>{E(x)}</li>" for x in pp["now"])
    nxt = "\n".join(f"              <li>{E(x)}</li>" for x in pp["next"])
    faq = "\n".join(
        f'        <details><summary>{E(q)}</summary><p class="faq__a">{E(a)}</p></details>' for q, a in pp["faq"])
    pms = "\n".join(ms_entry(m, show_kind=False) for m in MILESTONES if m["product"] == key and not m.get("tech"))
    latest = receipt(last_receipts(key, 1)[0])
    what = "\n".join(f"            <p>{E(x)}</p>" for x in pp["what"])
    notice = f'\n      <p class="note mt-l">{E(pp["notice"])}</p>' if pp["notice"] else ""
    shot = ""
    if key == "kockalmar":
        shot = """    <section class="sec sec--tight light" aria-label="A webshop képernyőképe">
      <div class="wrap">
        <figure class="fig shot reveal">
          <figcaption class="fig__cap"><span>Ábra 01 · A webshop nyitóoldala</span><span>fejlesztői változat</span></figcaption>
          <div class="shot__frame">
            <div class="shot__bar" aria-hidden="true"><i></i><i></i><i></i><span>kockalmar</span></div>
            <img src="/assets/img/kockalmar-webshop-1600.webp" srcset="/assets/img/kockalmar-webshop-800.webp 800w, /assets/img/kockalmar-webshop-1600.webp 1600w" sizes="(max-width: 80rem) 100vw, 80rem" width="1600" height="1000" loading="lazy" decoding="async" alt="A Kockalmár webshop nyitóoldala: „Keresd meg a hiányzó darabot.” cím, alkatrészkereső mező és LEGO-figurák egy épülő falnál.">
          </div>
        </figure>
        <figure class="fig flow reveal mt-xl">
          <figcaption class="fig__cap"><span>Ábra 02 · Egy vásárlás útja</span><span>4 lépés · fejlesztői változat</span></figcaption>
          <ol class="flow__steps">
            <li class="flow__step">
              <span class="flow__no">01 · Keresés</span>
              <div class="shot__frame"><img src="/assets/img/kockalmar-kereses-1600.webp" srcset="/assets/img/kockalmar-kereses-800.webp 800w, /assets/img/kockalmar-kereses-1600.webp 1600w" sizes="(max-width: 900px) 100vw, 40rem" width="1600" height="1000" loading="lazy" decoding="async" alt="Keresési találatok: evező, hajókormány és papagáj, áruk és elérhető mennyiségük."></div>
              <p class="flow__text">A „pirate” keresésre 12 klasszikus kalóz-alkatrész, színnel, állapottal, készlettel és árral.</p>
            </li>
            <li class="flow__step">
              <span class="flow__no">02 · Termékoldal</span>
              <div class="shot__frame"><img src="/assets/img/kockalmar-termek-1600.webp" srcset="/assets/img/kockalmar-termek-800.webp 800w, /assets/img/kockalmar-termek-1600.webp 1600w" sizes="(max-width: 900px) 100vw, 40rem" width="1600" height="1000" loading="lazy" decoding="async" alt="Egy fekete kalózkalap termékoldala: szín, állapot, ár és elérhető mennyiség."></div>
              <p class="flow__text">Szín és állapot kiválasztása, egy átlátható vásárlási blokkban.</p>
            </li>
            <li class="flow__step">
              <span class="flow__no">03 · Kosár</span>
              <div class="shot__frame"><img src="/assets/img/kockalmar-kosar-1600.webp" srcset="/assets/img/kockalmar-kosar-800.webp 800w, /assets/img/kockalmar-kosar-1600.webp 1600w" sizes="(max-width: 900px) 100vw, 40rem" width="1600" height="1000" loading="lazy" decoding="async" alt="Kosár négy alkatrésszel és 1 360 forintos részösszeggel."></div>
              <p class="flow__text">Érthető mennyiségek és részösszeg. A kosárba tétel még nem foglal készletet.</p>
            </li>
            <li class="flow__step">
              <span class="flow__no">04 · Pénztár</span>
              <div class="shot__frame"><img src="/assets/img/kockalmar-szallitas-1600.webp" srcset="/assets/img/kockalmar-szallitas-800.webp 800w, /assets/img/kockalmar-szallitas-1600.webp 1600w" sizes="(max-width: 900px) 100vw, 40rem" width="1600" height="1000" loading="lazy" decoding="async" alt="Szállítási mód választása: belföldi és nyomkövetett szállítás, áraikkal."></div>
              <p class="flow__text">Fiók nélkül is: adatok, majd szállítási mód, valós díjjal.</p>
            </li>
          </ol>
          <p class="note mt-s">A képeken tesztárak láthatók. Alkatrészképek: <a href="https://rebrickable.com/">Rebrickable</a>, <a href="https://www.ldraw.org/">LDraw</a> (CC BY 4.0).</p>
        </figure>
      </div>
    </section>

"""
    page = head(p["path"], pp["title"], pp["desc"], "termekek") + f"""
    <section class="p-hero p-hero--{key}" aria-labelledby="oldal-cim">
      <div class="wrap p-hero__grid">
        <div>
          <nav class="crumbs" aria-label="Morzsamenü"><a href="/#termekek">Termékek</a><span aria-hidden="true">/</span><span>{E(p['name'])}</span></nav>
          <span class="label">{E(p['type'])} · {p['state']}</span>
          <h1 class="page-title mt-s" id="oldal-cim">{E(p['name'])}</h1>
          <p class="page-lead">{E(p['line'])}</p>
          <div class="actions">
            <a class="button" href="{mailto(p['name'] + ' – értesítést kérek')}">Értesítést kérek <span class="button__arrow" aria-hidden="true">→</span></a>
            <a class="button button--ghost" href="#merfoldkovek">Mérföldkövek</a>
          </div>
        </div>
        <div class="product__mark">{mark(key)}</div>
      </div>
    </section>

    <section class="sec sec--tight light" aria-label="Adatlap">
      <div class="wrap">
      <dl class="datasheet">
{sheet}
      </dl>
      </div>
    </section>

{shot}    <section class="sec light" aria-labelledby="mi-cim">
      <div class="wrap">
        <div class="split">
          <div class="split__head"><span class="label">01</span><h2 id="mi-cim" class="mt-xs">Mi ez?</h2></div>
          <div class="prose">
{what}
          </div>
        </div>
        <div class="twocol mt-xl">
          <div class="panel panel--now reveal">
            <span class="label">02 · A fejlesztői változatban már működik</span>
            <h3>Mit tud ma</h3>
            <ul>
{now}
            </ul>
          </div>
          <div class="panel panel--next reveal">
            <span class="label">03 · Tervben</span>
            <h3>Mi jön</h3>
            <ul>
{nxt}
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="sec dark grid-lines" id="merfoldkovek" aria-labelledby="nyugta-cim">
      <div class="wrap">
{sec_head("04 — Mérföldkövek", "Ahogy a " + E(p['name']) + " összeállt.", "Valódi, elfogadott lépések a fejlesztésből. Mindegyiknél előre rögzítettem, mi számít késznek, független ellenőrzésen ment át, és ember fogadta el.", "nyugta-cim")}
        <div class="ms-split">
          <ol class="mslist reveal">
{pms}
          </ol>
          <figure class="fig ms-split__receipt reveal">
            <figcaption class="fig__cap"><span>Legutóbbi nyugta</span><span>belső kivonat</span></figcaption>
{latest}
          </figure>
        </div>
        <p class="mt-l"><a class="text-link" href="/hogyan-keszul/">Mit jelent egy nyugta? →</a></p>
      </div>
    </section>

    <section class="sec light" aria-labelledby="gyik-cim">
      <div class="wrap">
        <div class="split">
          <div class="split__head"><span class="label">05</span><h2 id="gyik-cim" class="mt-xs">Kérdések</h2></div>
          <div class="faq">
{faq}
          </div>
        </div>
        <div class="notify mt-xl">
          <p class="notify__text">Szólok, amikor a {E(p['name'])} elérhető.</p>
          <a class="button" href="{mailto(p['name'] + ' – értesítést kérek')}">Értesítést kérek <span class="button__arrow" aria-hidden="true">→</span></a>
        </div>{notice}
      </div>
    </section>
""" + FOOT
    write(p["path"], page)

# ---------------------------------------------------------------- Hogyan készül

rules_full = "\n".join(
    f"""        <li><details>
          <summary><span class="rule__no">{i:02d}</span><span class="rule__title">{E(t)}</span></summary>
          <div class="rulelist__body"><p><strong>{E(s)}</strong></p>{''.join(f'<p>{E(x)}</p>' for x in more)}</div>
        </details></li>"""
    for i, (t, s, more) in enumerate(RULES, 1))

anat_r = hero_r
how = head("/hogyan-keszul/", "Hogyan készül — az AXIONA | AXIONA Systems",
           "Az AXIONA a saját mérnöki rendszerem: egy szándék bemegy, egy ellenőrzött, kiadott, figyelt változás jön ki, és minden lépésnek nyoma marad.",
           "hogyan") + f"""
    <section class="sec dark grid-lines page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>Hogyan készül</span></nav>
        <h1 class="page-title" id="oldal-cim">AXIONA. A rend, amelyben a kód készül.</h1>
        <p class="page-lead">Saját mérnöki rendszer, amelyben ember és MI dolgozik. Egy szándék bemegy, egy kiadott, ellenőrzött, figyelt változás jön ki, és közben minden lépésnek nyoma marad. Nem termék, és nem eladó: ezen keresztül épülnek a termékek.</p>
      </div>
    </section>

    <section class="sec dark grid-lines" aria-labelledby="kor-cim">
      <div class="wrap">
{sec_head("01 — A kör", "Egy változtatás útja.", "Hét állomás. Mindegyiknél keletkezik valami, ami később visszakereshető.", "kor-cim")}
        <figure class="fig reveal">
          <figcaption class="fig__cap"><span>Ábra 01 · A kör</span><span>minden állomás nyomot hagy</span></figcaption>
{loop_html()}
        </figure>
      </div>
    </section>

    <section class="sec light" aria-labelledby="anat-cim">
      <div class="wrap">
{sec_head("02 — A nyugta", "Egy nyugta anatómiája.", "A nyugta egy elfogadott változtatás kivonata a saját rendszeremből. Nem külső tanúsítvány: a forráskód privát, így kívülről nem ellenőrizhető. Azt mutatja meg, milyen lépéseken ment át egy változtatás, mielőtt elfogadtam.", "anat-cim")}
        <figure class="fig anatomy reveal">
          <div>
            <figcaption class="fig__cap"><span>Ábra 02 · Valódi nyugta, jelölésekkel</span><span>{anat_r['id']}</span></figcaption>
{receipt(anat_r, pins=True)}
          </div>
          <ol class="anatomy__notes">
            <li><span class="pin">1</span><div><b>Elvárás</b><span>Mielőtt a munka elindul, rögzítve van, mi számít késznek, és mihez nem szabad nyúlni.</span></div></li>
            <li><span class="pin">2</span><div><b>Ellenőrzés</b><span>Tesztek és ellenőrzők, amelyeket nem a munka végzője írt alá. A szám a lefutott tesztek száma.</span></div></li>
            <li><span class="pin">3</span><div><b>Emberi döntés</b><span>Egy ember fogadja el. Az MI javasol, de nem dönt.</span></div></li>
            <li><span class="pin">4</span><div><b>Dátum</b><span>Mikor fogadtam el a változtatást.</span></div></li>
            <li><span class="pin">5</span><div><b>Állapot</b><span>Az „Ellenőrizve” csak akkor jelenik meg, ha az előző négy mind megvan. A narancs szín az oldalon csak ezt jelenti.</span></div></li>
          </ol>
        </figure>
      </div>
    </section>

    <section class="sec dark grid-lines" id="gephaz" aria-labelledby="gephaz-cim">
      <div class="wrap">
{sec_head("03 — A gépház", "Hat megoldás, amitől másképp működik.", "Nem eszközök, hanem döntések: hol áll meg a rendszer, mit nem hisz el magának, és mit nem engedhet át embertől gépnek.", "gephaz-cim")}
{engine_html()}
      </div>
    </section>

    <section class="sec light" aria-labelledby="szabaly-cim">
      <div class="wrap">
{sec_head("04 — Szabályok", "Hét szabály.", "Ezek nem ajánlások. Ha egy változtatás bármelyiket megszegné, nem megy tovább.", "szabaly-cim")}
        <ol class="rulelist reveal">
{rules_full}
        </ol>
      </div>
    </section>

    <section class="sec dark grid-lines" aria-labelledby="szam-cim">
      <div class="wrap">
{sec_head("05 — Számokban", "A rendszer, megszámolva.", "Csak az kerül ide, ami megszámolható.", "szam-cim")}
        <div class="kpis reveal">
          <div class="kpi"><span class="kpi__value">7</span><span class="kpi__label">állomás egy változtatás útján</span></div>
          <div class="kpi"><span class="kpi__value">1</span><span class="kpi__label">ember dönt minden elfogadásról</span></div>
          <div class="kpi"><span class="kpi__value">{num(COUNTS['max_tests_kockalmar'])}</span><span class="kpi__label">teszt egy Kockalmár-változtatás előtt</span></div>
          <div class="kpi"><span class="kpi__value">{num(COUNTS['max_tests_fejtorpe'])}</span><span class="kpi__label">teszt egy Fejtörpe-változtatás előtt</span></div>
        </div>
        <p class="kpis__note">Állapot: {hu_date(AS_OF)}</p>
      </div>
    </section>

    <section class="sec light" aria-labelledby="hatar-cim">
      <div class="wrap">
{sec_head("06 — Határok", "Mit bizonyít a rendszer, és mit nem.", "Egy rendszer attól hiteles, hogy pontosan kiírja, hol ér véget.", "hatar-cim")}
        <div class="claims">
          <div class="claims__col claims__col--yes reveal">
            <span class="label">A rendszer garantálja</span>
            <h3>Nyom, ellenőrzés, döntés</h3>
            <ul>
              <li>Minden elfogadott változtatásnak van útrekordja.</li>
              <li>Az ellenőrzés független a munka végzőjétől.</li>
              <li>Minden elfogadásról ember dönt.</li>
              <li>Egy rossz változtatás visszavonható.</li>
            </ul>
          </div>
          <div class="claims__col claims__col--no reveal">
            <span class="label">A rendszer nem garantálja</span>
            <h3>Hibamentesség</h3>
            <ul>
              <li>Hogy a szoftverben nincs hiba.</li>
              <li>Hogy a tesztek minden hibát megtalálnak.</li>
              <li>Hogy az előre rögzített elvárás mindenre gondolt.</li>
              <li>Hogy egy emberi döntés mindig jó.</li>
              <li>Hogy kívülálló is ellenőrizheti: a nyugta belső kivonat, nem külső tanúsítvány.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="sec dark grid-lines" aria-labelledby="jegyzet-cim">
      <div class="wrap">
{sec_head("07 — Jegyzetek", "Bővebben a Naplóban.", "", "jegyzet-cim")}
        <ol class="mslist">
{chr(10).join(ms_note(n) for n in NOTES)}
        </ol>
      </div>
    </section>
""" + FOOT
write("/hogyan-keszul/", how)

# ---------------------------------------------------------------- Napló

all_items = [("m", m) for m in MILESTONES] + [("n", n) for n in NOTES]
all_items.sort(key=lambda x: x[1]["date"], reverse=True)
log_html = "\n".join(ms_entry(x, h="h2") if k == "m" else ms_note(x, h="h2") for k, x in all_items)
filters = """        <div class="filters" data-filters hidden role="group" aria-label="Szűrés">
          <button type="button" data-filter="all" aria-pressed="true">Mind</button>
          <button type="button" data-filter="kockalmar" aria-pressed="false">Kockalmár</button>
          <button type="button" data-filter="fejtorpe" aria-pressed="false">Fejtörpe</button>
          <button type="button" data-filter="keeper" aria-pressed="false">Keeper</button>
          <button type="button" data-filter="axiona" aria-pressed="false">AXIONA</button>
          <button type="button" data-filter="iras" aria-pressed="false">Írások</button>
        </div>"""
naplo = head("/naplo/", "Napló | AXIONA Systems",
             "A nagy lépések a Kockalmár, a Fejtörpe, a Keeper és az AXIONA fejlesztéséből: amikor valami először működött végig. Elfogadott változtatások, dátummal, és rövid írások.",
             "naplo") + f"""
    <section class="sec light page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>Napló</span></nav>
        <h1 class="page-title" id="oldal-cim">Napló</h1>
        <p class="page-lead">A nagy lépések: amikor valami először működött végig, vagy a rendszer új képességet kapott. Mind elfogadott változtatás, dátummal. <a href="/naplo/feed.xml">RSS</a></p>
      </div>
    </section>
    <section class="sec light pt-0" aria-label="Bejegyzések">
      <div class="wrap">
{filters}
        <ol class="mslist">
{log_html}
        </ol>
      </div>
    </section>
""" + FOOT
write("/naplo/", naplo)

for n in NOTES:
    body = "\n".join(f"          <{t}>{E(x)}</{t}>" for t, x in n["body"])
    page = head(n["path"], f"{n['title']} | AXIONA Systems", n["lead"], "naplo") + f"""
    <section class="sec light page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/naplo/">Napló</a><span aria-hidden="true">/</span><span>Írás</span></nav>
        <span class="label"><time datetime="{n['date']}">{hu_date(n['date'])}</time> · {n['minutes']} perc olvasás</span>
        <h1 class="page-title mt-s" id="oldal-cim">{E(n['title'])}</h1>
        <p class="page-lead">{E(n['lead'])}</p>
      </div>
    </section>
    <section class="sec light pt-0">
      <div class="wrap">
        <article class="article">
{body}
          <p><a class="text-link" href="/hogyan-keszul/">Hogyan készül →</a></p>
        </article>
      </div>
    </section>
""" + FOOT
    write(n["path"], page)

# RSS
rss_items = []
for k, x in all_items:
    if k == "m":
        title, link, desc = f"{KIND_NAME[x['product']]}: {x['title']}", SITE + KIND_PATH[x["product"]], f"{x['text']} ({x['proof']})"
    else:
        title, link, desc = x["title"], SITE + x["path"], x["lead"]
    rss_items.append(f"""    <item>
      <title>{E(title)}</title>
      <link>{link}</link>
      <guid isPermaLink="false">{x.get('slug') or (x['date'] + '-' + x['product'] + '-' + __import__('hashlib').sha1(x['title'].encode()).hexdigest()[:8])}</guid>
      <pubDate>{rfc822(x['date'])}</pubDate>
      <description>{E(desc)}</description>
    </item>""")
write("/naplo/feed.xml", f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <title>AXIONA Systems – Napló</title>
    <link>{SITE}/naplo/</link>
    <description>A nagy lépések és rövid írások.</description>
    <language>hu</language>
{chr(10).join(rss_items)}
  </channel>
</rss>
""")

# ---------------------------------------------------------------- Ötletláda


def idea(i: dict) -> str:
    scope = "".join(f"<li>{E(x)}</li>" for x in i["scope"])
    return f"""          <article class="idea">
            <span class="label">{E(i['who'])}</span>
            <h3>{E(i['name'])}</h3>
            <p class="idea__line">{E(i['line'])}</p>
            <ul class="idea__scope">{scope}</ul>
            <p class="idea__why"><span class="label inline">Miért most · </span>{E(i['why'])}</p>
            <a class="text-link idea__vote" href="{mailto('Érdekel: ' + i['name'])}">Ez érdekel →</a>
          </article>"""


groups = IDEAS["groups"]
total = sum(len(g["items"]) for g in groups)
chips = [f'          <li><a class="chip" href="#{g["id"]}">{E(g["name"])} <span>{len(g["items"])}</span></a></li>' for g in groups]
group_html = "\n".join(f"""    <section class="sec {'dark grid-lines' if n % 2 else 'light'}" id="{g['id']}" aria-labelledby="t-{g['id']}">
      <div class="wrap">
{sec_head(f"{n:02d} — {len(g['items'])} rendszer", E(g['name']), E(g['sub']), "t-" + g['id'])}
        <div class="ideas">
{chr(10).join(idea(i) for i in g['items'])}
        </div>
      </div>
    </section>
""" for n, g in enumerate(groups, 1))
otlet = head("/otletlada/", "Ötletláda | AXIONA Systems",
             f"{total} nagyobb szoftverrendszer, amelyen gondolkodom: kiberbiztonság, uniós adatszolgáltatás, energia. Ha valamelyik a te gondod is, szólj.",
             "otletlada") + f"""
    <section class="sec light page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>Ötletláda</span></nav>
        <h1 class="page-title" id="oldal-cim">Ötletláda</h1>
        <p class="page-lead">{total} nagyobb rendszer, amelyen gondolkodom. Mindegyik mögött egy valódi szabály vagy határidő áll, amelyhez ma a legtöbb kis cégnek nincs jó eszköze. Ha a cégednek szüksége van valamelyikre, megépíthetem neked; ha csak érdekel, az is segít eldönteni, mi legyen a következő.</p>
        <ul class="chipnav mt-l">
{chr(10).join(chips)}
        </ul>
      </div>
    </section>

{group_html}
    <section class="sec sec--tight light">
      <div class="wrap">
        <div class="notify">
          <p class="notify__text">Olyan problémád van, amire nincs jó szoftver?</p>
          <a class="button" href="{mailto('Ötlet az Ötletládába')}">Megírom <span class="button__arrow" aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>
""" + FOOT
write("/otletlada/", otlet)

# ---------------------------------------------------------------- Rólam

rolam = head("/rolam/", "Rólam | AXIONA Systems",
             "Asztalos Zoltán vagyok. Az AXIONA Systems mögött egyetlen ember áll: én találom ki, építem és tartom karban a termékeket.",
             "rolam") + f"""
    <section class="sec light page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>Rólam</span></nav>
        <h1 class="page-title" id="oldal-cim">Szia, Zoli vagyok.</h1>
        <p class="page-lead">Asztalos Zoltán. Az AXIONA Systems mögött nincs csapat és nincs iroda, csak én. Én találom ki a termékeket, én építem őket, és én felelek értük, ha valami nem úgy működik, ahogy kellene.</p>
      </div>
    </section>
    <section class="sec dark grid-lines" aria-labelledby="ps-cim">
      <div class="wrap ps">
        <span class="label">Pár szóban</span>
        <div>
          <h2 class="visually-hidden" id="ps-cim">Pár szóban</h2>
          <div class="ps__body">
            <p>Olyan dolgokat szeretek építeni, amiknek kézzelfogható haszna van. Egy webshopot, ahol pontosan azt az egy hiányzó LEGO-darabot veheted meg, ami kell. Füzeteket, amelyek egy konkrét gyereknek készülnek, nem egy átlagos korosztálynak. És egy appot, amely rendet tart a papírok között, hogy ne neked kelljen.</p>
            <p>A kód nagy részét ma már MI írja velem együtt. Ettől gyorsabban haladok, de nem lettem kevésbé felelős. Minden változtatást én nézek át és én hagyok jóvá, és csak az kerül ki, amiről tudom, mit csinál. Hogy ebben ne a memóriámra kelljen hagyatkoznom, építettem magamnak egy rendet: ez az AXIONA.</p>
            <p>Még nem minden hibátlan, de makacsul azon vagyok, hogy az legyen. Ha valami mégis elromlik, megkeresem az okát, kijavítom, és őszintén megírom, mi történt.</p>
            <p>A saját termékeim mellett megrendelésre is építek: webes rendszert, iPhone-appot vagy belső céges eszközt. <a href="/egyuttmukodes/">Így dolgozunk együtt.</a></p>
            <p>Ha kérdésed van, ötleted, vagy csak szólnál, hogy valami nem működik, írj nyugodtan: <a href="{mailto('Kérdés')}">{MAIL}</a>. Minden levelet én olvasok, és két munkanapon belül válaszolok.</p>
            <div class="ps__sign">
              <span class="ps__name">Zoli</span>
            </div>
          </div>
          <p class="now"><span class="label">Most</span><span>A Kockalmár pénztárán és a Fejtörpe füzetstúdióján dolgozom.</span><a class="text-link" href="/kapcsolat/">Írj nekem →</a></p>
        </div>
      </div>
    </section>
""" + FOOT
write("/rolam/", rolam)

# ---------------------------------------------------------------- Együttműködés

STEPS = [
    ("Beszélgetés", "Elmondod, mi a gond ma, és mit szeretnél. Ez nem kötelez semmire, és ha nem én vagyok a jó választás, megmondom."),
    ("Felmérés és ajánlat", "Írásban rögzítem, mit építek, mi számít késznek, mihez nem nyúlok, mennyi idő és mennyibe kerül. Szakaszokra bontva, fix áron."),
    ("Építés, szakaszonként", "Rendszeresen megmutatom, hol tartunk. Minden elfogadott változtatásról tudod, mi volt, mi ellenőrizte, és mikor fogadtuk el."),
    ("Átadás", "Megkapod a teljes forráskódot, a hozzáféréseket és a leírást, hogy más is tovább tudja vinni."),
    ("Utána", "Hibajavítás, karbantartás és továbbfejlesztés külön megállapodással, ha kéred."),
]
WORK_FAQ = [
    ("Kié lesz a kód?", "A tiéd. Az átadáskor megkapod a teljes forráskódot és minden hozzáférést."),
    ("Látja az MI a cégem adatait?", "Az éles ügyféladataidat nem adom át MI-szolgáltatásnak. A fejlesztés tesztadatokon folyik; ha valódi adat kell, azt előre egyeztetjük, és írásban rögzítjük."),
    ("Mennyibe kerül?", "Az árat a felmérés után adom meg, szakaszokra bontva, fix áron, hogy előre tudd, mire mennyit fizetsz."),
    ("Mekkora munkát vállalsz?", "Egy ember által jól végigvihető projekteket, néhány héttől néhány hónapig. Ha a feladat ennél nagyobb, ezt az első beszélgetésen megmondom."),
    ("Mi van, ha valami elromlik az átadás után?", "Megkeresem az okát, kijavítom, és leírom, mi történt. Az átadás utáni időszak feltételeit az ajánlat rögzíti."),
]

steps_html = "\n".join(f"""          <li class="steps__item">
            <span class="steps__no">{i:02d}</span>
            <h3>{E(t)}</h3>
            <p>{E(x)}</p>
          </li>""" for i, (t, x) in enumerate(STEPS, 1))
tools_html = "\n".join(
    f'          <div class="tools__row"><dt>{E(g)}{f"""<span class="tools__note">{E(note)}</span>""" if note else ""}</dt>'
    f'<dd><ul>{"".join(f"<li>{E(t)}</li>" for t in items)}</ul></dd></div>'
    for g, note, items in TOOLS)
work_faq = "\n".join(f'        <details><summary>{E(q)}</summary><p class="faq__a">{E(a)}</p></details>' for q, a in WORK_FAQ)
egyutt = head("/egyuttmukodes/", "Együttműködés — egyedi szoftverfejlesztés | AXIONA Systems",
              "Webes rendszert, iPhone-appot vagy belső céges eszközt építek megrendelésre, ugyanazzal a gondossággal, mint a saját termékeimet.",
              "egyutt") + f"""
    <section class="sec dark grid-lines page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>Együttműködés</span></nav>
        <h1 class="page-title" id="oldal-cim">Neked is építek.</h1>
        <p class="page-lead">Webes rendszert, iPhone-appot vagy belső céges eszközt építek megrendelésre. Ugyanúgy, mint a saját termékeimet: előre rögzített elvárásokkal, független ellenőrzéssel, és úgy, hogy minden lépést látsz.</p>
        <div class="actions">
          <a class="button" href="/kapcsolat/?tema=fejlesztes">Írd le, mire van szükséged <span class="button__arrow" aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>

    <section class="sec light" aria-labelledby="mit-cim">
      <div class="wrap">
{sec_head("01 — Mit vállalok", "Három fajta munka.", "Mindháromra van saját, működő példám ezen az oldalon.", "mit-cim")}
{offer_html()}
      </div>
    </section>

    <section class="sec dark grid-lines" aria-labelledby="menet-cim">
      <div class="wrap">
{sec_head("02 — Menete", "Így dolgozunk együtt.", "Öt lépés. Mindegyik végén tudod, hol tartunk, és dönthetsz a következőről.", "menet-cim")}
        <ol class="steps reveal">
{steps_html}
        </ol>
      </div>
    </section>

    <section class="sec light" id="eszkozok" aria-labelledby="eszkoz-cim">
      <div class="wrap">
{sec_head("03 — Eszközök", "Mivel dolgozom.", "Amivel a saját termékeim készülnek és futnak, és amit egy megrendelés megkívánhat.", "eszkoz-cim")}
        <dl class="tools reveal">
{tools_html}
        </dl>
      </div>
    </section>

    <section class="sec light" aria-labelledby="kerdes-cim">
      <div class="wrap">
        <div class="split">
          <div class="split__head"><span class="label">04</span><h2 id="kerdes-cim" class="mt-xs">Amit tudni szeretnél</h2></div>
          <div class="faq">
{work_faq}
          </div>
        </div>
        <div class="notify mt-xl">
          <p class="notify__text">Két munkanapon belül válaszolok.</p>
          <a class="button" href="/kapcsolat/?tema=fejlesztes">Írd le, mire van szükséged <span class="button__arrow" aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>
""" + FOOT
write("/egyuttmukodes/", egyutt)

# ---------------------------------------------------------------- Kapcsolat

kapcsolat = head("/kapcsolat/", "Kapcsolat | AXIONA Systems",
                 "Írj e-mailt az AXIONA Systemsnek. Két munkanapon belül válaszolok.",
                 "kapcsolat") + f"""
    <section class="sec light page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>Kapcsolat</span></nav>
        <h1 class="page-title" id="oldal-cim">Írj nekem.</h1>
        <p class="page-lead">Egy szoftver, amire a cégednek szüksége lenne, kérdés egy termékről, vagy csak szólnál, amikor valami elindul. Két munkanapon belül válaszolok.</p>
      </div>
    </section>
    <section class="sec light pt-0" aria-label="Kapcsolatfelvétel">
      <div class="wrap split">
        <div class="split__head">
          <span class="label">E-mail</span>
          <p class="contact-mail"><a href="{mailto('Kérdés')}">{MAIL}</a></p>
        </div>
        <form class="form" data-mailto="{MAIL}" novalidate>
          <div class="field">
            <label for="tema">Téma</label>
            <select id="tema" name="tema">
              <option>Kérdés</option>
              <option data-key="fejlesztes">Egyedi fejlesztés</option>
              <option>Kockalmár</option>
              <option>Fejtörpe</option>
              <option>Keeper</option>
              <option>Ötletláda</option>
              <option>Biztonsági bejelentés</option>
            </select>
          </div>
          <div class="field">
            <label for="uzenet">Üzenet</label>
            <textarea id="uzenet" name="uzenet" required aria-describedby="uzenet-tipp"></textarea>
            <p class="form__hint" id="uzenet-tipp">Fejlesztésnél segít, ha leírod: mi a gond ma, kik használnák, mikorra kellene, és van-e már meglévő rendszer.</p>
          </div>
          <div class="field">
            <label for="nev">Neved (nem kötelező)</label>
            <input id="nev" name="nev" autocomplete="name">
          </div>
          <div class="actions">
            <button class="button" type="submit">Levél előkészítése <span class="button__arrow" aria-hidden="true">→</span></button>
          </div>
          <p class="form__hint">Az űrlap nem küld és nem tárol semmit: a saját levelezőprogramodban készíti elő a levelet.</p>
        </form>
      </div>
    </section>
""" + FOOT
write("/kapcsolat/", kapcsolat)

# ---------------------------------------------------------------- jogi és bizalmi oldalak


def legal_page(path: str, title: str, h1: str, lead: str, desc: str, blocks: list[tuple[str, str]]) -> None:
    body = "\n".join(f"""        <div class="split">
          <div class="split__head"><h2>{E(h)}</h2></div>
          <div class="prose">{t}</div>
        </div>""" for h, t in blocks)
    write(path, head(path, title, desc) + f"""
    <section class="sec light page-hero" aria-labelledby="oldal-cim">
      <div class="wrap">
        <nav class="crumbs" aria-label="Morzsamenü"><a href="/">Főoldal</a><span aria-hidden="true">/</span><span>{E(h1 if len(h1) < 20 else title.split(' |')[0])}</span></nav>
        <h1 class="page-title" id="oldal-cim">{E(h1)}</h1>
        <p class="page-lead">{lead}</p>
      </div>
    </section>
    <section class="sec light pt-0">
      <div class="wrap">
{body}
      </div>
    </section>
""" + FOOT)


def P(*xs: str) -> str:
    return "".join(f"<p>{x}</p>" for x in xs)


legal_page("/impresszum/", "Impresszum | AXIONA Systems", "Impresszum",
           "Ki áll az oldal mögött, és milyen feltételekkel használható.",
           "Az axiona.systems impresszuma: üzemeltető, tárhely, védjegyek és felelősség.",
           [
               ("Üzemeltető", P(f'Az axiona.systems az AXIONA Systems név alatt fejlesztett saját szoftvertermékeket mutatja be. A tartalomért és a kapcsolatfelvételért felelős: Asztalos Zoltán. Kapcsolat: <a href="{mailto("Kérdés")}">{MAIL}</a>.')),
               ("Tárhely", P("A weboldalt a GitHub Pages szolgálja ki (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA).")),
               ("A kapcsolatfelvétel nem szerződés", P("Egy e-mailes érdeklődés önmagában nem hoz létre szerződést. Feltételek csak kifejezett, írásos elfogadással válnak kötelezővé.")),
               ("Fejlesztés alatt álló termékek", P("A „Fejlesztés alatt” jelöléssel bemutatott termékek nem megvásárolhatók. Funkciójuk, nevük és elérhetőségük a fejlesztés során változhat.")),
               ("Védjegyek", P("A LEGO® a LEGO Group védjegye. A Kockalmár független kereskedés, a LEGO Grouppal nem áll kapcsolatban. Az Apple, az iPhone, az iPad és az App Store az Apple Inc. védjegyei.")),
               ("Szövegek és arculat", P("A weboldal saját szövegei és arculati elemei szerzői jogi védelem alatt állhatnak. A betűtípusok (Inter, JetBrains Mono) a SIL Open Font License szerint használhatók.")),
               ("Pontosság és elérhetőség", P("A tartalmat gondosan karbantartom, de az információk változhatnak. Nem ígérem, hogy a weboldal minden pillanatban megszakítás nélkül működik. Ez nem korlátoz olyan felelősséget, amelyet kötelező jogszabály alapján nem lehet kizárni.")),
               ("Adatvédelem és biztonság", P('Az adatkezelést az <a href="/adatvedelem/">Adatvédelem</a>, a biztonsági alapelveket a <a href="/biztonsag/">Biztonság</a> oldal írja le.')),
           ])

legal_page("/adatvedelem/", "Adatvédelem | AXIONA Systems", "Adatvédelem",
           "Az axiona.systems nagyon kevés adatot kezel. Nincs felhasználói fiók, rendelés, süti vagy marketingkövetés.",
           "Röviden és világosan arról, milyen adatot kezel az axiona.systems.",
           [
               ("Ki felel az adatkezelésért?", P(f'A weboldalhoz és a közvetlen megkeresésekhez kapcsolódó adatkezelésért Asztalos Zoltán felel az AXIONA Systems név alatt. Kérdés vagy kérelem: <a href="{mailto("Adatvédelem")}">{MAIL}</a>.')),
               ("Amikor meglátogatod az oldalt", P("A weboldalt a GitHub Pages szolgálja ki. A GitHub a szolgáltatás működtetéséhez és biztonságához technikai adatokat, köztük IP-címet naplózhat. Az oldal betűtípusai és képei ugyanerről a címről töltődnek be; harmadik féltől származó követőkód, hirdetés vagy közösségi beágyazás nincs.")),
               ("Ha e-mailt írsz", P("Az e-mail-címedet, a megadott nevedet, az üzenet tartalmát és az önként csatolt fájlokat kezelem, a megkeresés megválaszolására és az abból következő teendőkre. A Kapcsolat oldal űrlapja nem küld és nem tárol adatot: csak a saját levelezőprogramodban készíti elő a levelet.")),
               ("Jogalap", P("A weboldal működtetése és biztonsága jogos érdeken alapul. Az e-mailes kapcsolatfelvétel a kérésedre tett lépéshez vagy jogos érdekhez kapcsolódik. Ha egy helyzet más jogalapot vagy hozzájárulást kíván, azt alkalmazzuk.")),
               ("Szolgáltatók", P("A weboldal kiszolgálásában a GitHub Pages, az e-mailek kézbesítésében a levelezési szolgáltató vesz részt. Ezek több országban is működhetnek; ha a jog nemzetközi adattovábbításhoz külön garanciát ír elő, annak megfelelő megoldást alkalmazok.")),
               ("Meddig őrzöm meg?", P("Az e-mailes adatokat addig tartom meg, ameddig a megkeresés kezelése, jogi kötelezettség vagy igényérvényesítés indokolja. A szolgáltatók saját technikai naplóinak megőrzését az adott szolgáltató szabályai határozzák meg.")),
               ("Sütik és profilozás", P("A weboldal nem állít be sütit, nem használ látogatói azonosítót, és nem készít profilt. Automatizált döntéshozatal nincs.")),
               ("Jogaid", P(f'Kérhetsz hozzáférést, helyesbítést, törlést, korlátozást, tiltakozhatsz az adatkezelés ellen, kérhetsz adathordozhatóságot, és panaszt tehetsz a Nemzeti Adatvédelmi és Információszabadság Hatóságnál (NAIH). Kérelemmel a <a href="{mailto("Adatvédelem")}">{MAIL}</a> címen lehet jelentkezni.')),
               ("Termékek", P("Ez a tájékoztató a weboldalra vonatkozik. A Kockalmár, a Fejtörpe és a Keeper saját adatvédelmi tájékoztatót kap, mielőtt elérhetővé válik.")),
           ])

legal_page("/biztonsag/", "Biztonság | AXIONA Systems", "Feltörhetetlen rendszer nincs. A jó védelem viszont megtervezhető.",
           "A biztonság nem a végén kerül hozzá. Már a tervezésnél eldől, milyen adat kerül be, ki fér hozzá, mi követhető, és hogyan áll helyre a működés egy hiba után.",
           "Biztonsági alapelvek és sebezhetőség bejelentése.",
           [
               ("Alapelvek", "<ul>" + "".join(f"<li><strong>{a}.</strong> {b}</li>" for a, b in [
                   ("Csak a szükséges adat", "Ami nem kell, az be sem kerül."),
                   ("Hozzáférés feladat szerint", "Mindenki csak azt látja és módosíthatja, ami a munkájához kell."),
                   ("Mentés és visszaállítás", "Nem elég menteni: tudni kell, hogyan áll helyre a működés."),
                   ("Követhető változások", "Minden elfogadott változtatásnak nyoma és nyugtája van."),
                   ("Karbantartott függőségek", "Ismert összetevők, rendszeres biztonsági frissítések."),
                   ("Ellenőrzött kiadás", "Egy változás csak független ellenőrzés és emberi döntés után kerül ki."),
               ]) + "</ul>"),
               ("Sebezhetőség bejelentése", P(
                   f'Ha biztonsági hibát találsz a weboldalon vagy valamelyik terméken, írj a <a href="{mailto("Biztonsági bejelentés")}">{MAIL}</a> címre, a tárgyban „Biztonsági bejelentés” megjelöléssel. Írd le, mit találtál, és hogyan reprodukálható. Kérlek, ne hozd nyilvánosságra, amíg nem javítottam. Jelszót vagy más titkos adatot ne küldj e-mailben.',
                   'Gépi olvasásra: <a href="/.well-known/security.txt">/.well-known/security.txt</a>')),
           ])

legal_page("/tamogatas/", "Támogatás | AXIONA Systems", "Támogatás",
           "Kérdésed van egy termék használatáról, vagy hibát látsz? Írj közvetlenül e-mailt.",
           "Segítség a Kockalmár, a Fejtörpe és a Keeper használatához.",
           [
               ("Hova írj?", P(f'<a href="{mailto("Támogatás")}">{MAIL}</a> — a tárgyban add meg a termék nevét. Két munkanapon belül válaszolok.')),
               ("Ami sokat segít", "<ul><li><strong>Termék:</strong> melyikről van szó, és ha látszik, a verziószám.</li><li><strong>Mi történt:</strong> mit csináltál, mit vártál, és mi történt helyette.</li><li><strong>Környezet:</strong> eszköz, rendszer vagy böngésző.</li><li><strong>Képernyőkép:</strong> ha segít, a személyes adatokat kitakarva.</li></ul>"),
               ("Biztonsági probléma", P('Ha biztonsági hibára gyanakszol, a <a href="/biztonsag/">Biztonság</a> oldal szerint jelezd.')),
           ])

# ---------------------------------------------------------------- 404

write("/404.html", head("/404.html", "Az oldal nem található | AXIONA Systems", "Ez az oldal nem létezik.") + """
    <section class="sec dark grid-lines page-hero min-h" aria-labelledby="oldal-cim">
      <div class="wrap">
        <span class="label">404 · megállás</span>
        <h1 class="page-title mt-s" id="oldal-cim">Itt megállt a rendszer.</h1>
        <p class="page-lead">Ez nem hiba, hanem információ: ez az oldal nem létezik. Lehet, hogy a hivatkozás régi, vagy elírás történt.</p>
        <div class="actions mt-l">
          <a class="button button--light" href="/">Vissza a főoldalra <span class="button__arrow" aria-hidden="true">→</span></a>
          <a class="button button--ghost" href="/naplo/">Napló</a>
        </div>
      </div>
    </section>
""" + FOOT)

# ---------------------------------------------------------------- átirányítások

REDIRECTS = {
    "/kockalmar.html": "/kockalmar/",
    "/fejtorpe.html": "/fejtorpe/",
    "/keeper.html": "/keeper/",
    "/muhely.html": "/hogyan-keszul/",
    "/process.html": "/hogyan-keszul/",
    "/systems.html": "/hogyan-keszul/",
    "/solutions.html": "/#termekek",
    "/otletlada.html": "/otletlada/",
    "/contact.html": "/kapcsolat/",
    "/legal.html": "/impresszum/",
    "/privacy.html": "/adatvedelem/",
    "/security.html": "/biztonsag/",
    "/support.html": "/tamogatas/",
}
for lang in ("en", "de"):
    for name, target in [("index", "/"), ("keeper", "/keeper/"), ("contact", "/kapcsolat/"), ("legal", "/impresszum/"),
                         ("privacy", "/adatvedelem/"), ("security", "/biztonsag/"), ("support", "/tamogatas/"),
                         ("process", "/hogyan-keszul/"), ("systems", "/hogyan-keszul/"), ("solutions", "/#termekek")]:
        REDIRECTS[f"/{lang}/{name}.html"] = target
for old, new in REDIRECTS.items():
    redirect(old, new)

# ---------------------------------------------------------------- gépeknek

PAGES = ["/", "/kockalmar/", "/fejtorpe/", "/keeper/", "/egyuttmukodes/", "/hogyan-keszul/", "/naplo/",
         *[n["path"] for n in NOTES], "/otletlada/", "/rolam/", "/kapcsolat/",
         "/impresszum/", "/adatvedelem/", "/biztonsag/", "/tamogatas/"]
write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{AS_OF}</lastmod></url>\n" for p in PAGES)
      + "</urlset>\n")

write("/llms.txt", f"""# AXIONA Systems

> Termék- és fejlesztőstúdió (Asztalos Zoltán). Saját szoftvertermékek és megrendelésre készülő szoftverek egy saját mérnöki rendszeren (AXIONA), minden elfogadott változtatáshoz független ellenőrzéssel és nyugtával. Az oldal nyelve magyar.

## Termékek
- [Kockalmár]({SITE}/kockalmar/): használt LEGO®-alkatrészek webshopja, darabra. Fejlesztés alatt.
- [Fejtörpe]({SITE}/fejtorpe/): személyre szabott, nyomtatható készségfejlesztő füzetek gyerekeknek. Fejlesztés alatt.
- [Keeper]({SITE}/keeper/): iratkezelő app iPhone-ra és iPadre. Fejlesztés alatt.

## Együttműködés
- [Együttműködés]({SITE}/egyuttmukodes/): webes rendszereket, iPhone- és iPad-appokat és belső céges eszközöket is építek megrendelésre. Fix áras szakaszok, a kód a megrendelőé.

## A rendszer
- [Hogyan készül]({SITE}/hogyan-keszul/): az AXIONA köre, a nyugta felépítése, hét szabály, és amit a rendszer nem garantál. Az AXIONA nem termék és nem eladó.

## Bizonyíték
- Legfeljebb {num(COUNTS['max_tests_kockalmar'])} teszt fut egy Kockalmár-, {num(COUNTS['max_tests_fejtorpe'])} egy Fejtörpe-változtatás előtt ({PROOF['source']}, {AS_OF}).
- [Napló]({SITE}/naplo/): a nagy lépések, elfogadott változtatások dátummal. RSS: {SITE}/naplo/feed.xml

## Kapcsolat
- {MAIL} (válasz két munkanapon belül)
""")

print("kész:", len(PAGES), "oldal,", len(REDIRECTS), "átirányítás")
