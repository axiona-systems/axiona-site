#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"STOP_R94_REVIEW_REPLACE {path.relative_to(ROOT)} count={count} old={old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# Human, explicit hero promise: document + matter, not an abstract "it".
replace_once(
    ROOT / "keeper.html",
    '<h1>Ne azt kelljen megjegyezned, <em>hol van.</em> Elég legyen tudnod, mihez tartozik.</h1>',
    '<h1>Ne azt kelljen megjegyezned, <em>hol van egy dokumentum.</em> Elég legyen tudnod, melyik ügyhöz tartozik.</h1>',
)
replace_once(
    ROOT / "keeper.html",
    '<p class="keeper-hero-lead">A fontos iratok ritkán maradnak egyedül. Egy szerződéshez jön módosítás, számla, levél, fotó és határidő. Ma ezek könnyen szétszóródnak a telefonon, az e-mailben és mappákban. A Keeper egy ügy köré rendezi őket, hogy amikor szükséged van rájuk, rögtön lásd, mi van meg és mi következik.</p>',
    '<p class="keeper-hero-lead">A fontos iratok ritkán állnak önmagukban. Egy szerződés mellé idővel módosítás, számla, levél, fotó és határidő kerül. Ezek könnyen szétszóródnak a telefonon, az e-mailben és külön mappákban. A Keeper egy ügy köré rendezi őket, hogy amikor szükséged van rájuk, rögtön lásd, mi tartozik hozzá és mi következik.</p>',
)
replace_once(
    ROOT / "en/keeper.html",
    '<h1>You shouldn\'t have to remember <em>where it is.</em> It should be enough to know what it belongs to.</h1>',
    '<h1>You shouldn\'t have to remember <em>where a document is.</em> It should be enough to know which matter it belongs to.</h1>',
)
replace_once(
    ROOT / "en/keeper.html",
    '<p class="keeper-hero-lead">Important documents rarely stand alone. A contract soon has an amendment, invoice, email, photo and deadline attached to it. Today those pieces easily end up scattered across your phone, inbox and folders. Keeper brings them together around one matter, so when you need them you can immediately see what you have and what comes next.</p>',
    '<p class="keeper-hero-lead">Important documents rarely stand alone. A contract can soon be joined by amendments, invoices, emails, photos and deadlines. Those pieces quickly end up scattered across your phone, inbox and folders. Keeper brings them together around one matter, so when you need them you can see what belongs there and what comes next.</p>',
)
replace_once(
    ROOT / "de/keeper.html",
    '<h1>Sie sollten sich nicht merken müssen, <em>wo etwas liegt.</em> Es sollte reichen zu wissen, wozu es gehört.</h1>',
    '<h1>Sie sollten sich nicht merken müssen, <em>wo ein Dokument liegt.</em> Es sollte reichen zu wissen, zu welchem Vorgang es gehört.</h1>',
)
replace_once(
    ROOT / "de/keeper.html",
    '<p class="keeper-hero-lead">Wichtige Unterlagen bleiben selten allein. Zu einem Vertrag kommen Änderung, Rechnung, Nachricht, Foto und Frist hinzu. Heute verteilen sich diese Dinge schnell auf Telefon, E-Mail und Ordner. Keeper führt sie in einem Vorgang zusammen, damit Sie bei Bedarf sofort sehen, was vorhanden ist und was als Nächstes ansteht.</p>',
    '<p class="keeper-hero-lead">Wichtige Unterlagen stehen selten für sich. Zu einem Vertrag kommen später Änderungen, Rechnungen, E-Mails, Fotos und Fristen. Diese Dinge verteilen sich schnell auf Smartphone, Postfach und Ordner. Keeper führt sie in einem Vorgang zusammen, damit Sie bei Bedarf sofort sehen, was dazugehört und was als Nächstes ansteht.</p>',
)

# Six-document count is now semantically exact: 1 contract + amendment + invoice + 2 emails + attachment.
for rel, row in (
    ("keeper.html", '        <div class="keeper-matter-doc"><span class="keeper-doc-type">DÁTUM</span><div><b>Fontos határidő</b><small>szeptember 12.</small></div><span class="keeper-doc-state">KÖVETKEZŐ</span></div>\n'),
    ("en/keeper.html", '        <div class="keeper-matter-doc"><span class="keeper-doc-type">DATE</span><div><b>Important deadline</b><small>September 12</small></div><span class="keeper-doc-state">NEXT</span></div>\n'),
    ("de/keeper.html", '        <div class="keeper-matter-doc"><span class="keeper-doc-type">TERMIN</span><div><b>Wichtige Frist</b><small>12. September</small></div><span class="keeper-doc-state">NÄCHSTER</span></div>\n'),
):
    replace_once(ROOT / rel, row, "")

# Hungarian UI labels and copy: remove engineering shorthand that reads unnaturally to a visitor.
for rel in ("index.html", "keeper.html", "solutions.html"):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if "KAPCSOLAT" not in text:
        raise SystemExit(f"STOP_R94_REVIEW_HU_STATE_MISSING {rel}")
    path.write_text(text.replace('class="keeper-doc-state">KAPCSOLAT</span>', 'class="keeper-doc-state">KAPCSOLÓDÓ</span>'), encoding="utf-8")

replace_once(
    ROOT / "keeper.html",
    '<h3>Ne külön mappákból kelljen összerakni.</h3>',
    '<h3>Ne külön mappákból kelljen összerakni az ügyet.</h3>',
)
replace_once(
    ROOT / "keeper.html",
    '<div class="keeper-folder-rule"><strong>A rend feletted marad.</strong> A Keeper felismerheti a valószínű kapcsolatokat, de a rendezést te hagyod jóvá.</div>',
    '<div class="keeper-folder-rule"><strong>A rend a te kezedben marad.</strong> A Keeper felismerheti a valószínű kapcsolatokat, de a rendezést te hagyod jóvá.</div>',
)
replace_once(
    ROOT / "de/keeper.html",
    '<h3>Nicht aus mehreren Ordnern zusammensuchen.</h3>',
    '<h3>Nicht jedes Mal den Vorgang aus mehreren Ordnern zusammensuchen.</h3>',
)

print("OK_KEEPER_R94_REVIEW_PATCH")
