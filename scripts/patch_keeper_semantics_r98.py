#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one match in {path}, got {count}: {old[:140]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


# HU — make every burden/benefit statement self-contained, including on mobile.
replace(
    "keeper.html",
    '<strong>Megkeresi, mihez tartozik, és javasolja a helyét.</strong>',
    '<strong>Megkeresi, mihez tartozhat, és javasolja a helyét.</strong>',
)
replace(
    "keeper.html",
    '<strong>A Keeper előkészíti a munkát; neked ott kell döntened, ahol valóban döntés kell.</strong>',
    '<strong>A Keeper előkészíti a munkát; te csak ott lépsz be, ahol valóban döntés kell.</strong>',
)
replace(
    "keeper.html",
    '<h2 class="keeper96-title">Nem az a segítség, hogy megvan az irat. Az a segítség, hogy ne neked kelljen újra végigdolgoznod.</h2>',
    '<h2 class="keeper96-title">Nem az számít, hogy a fájl el van-e téve. Az számít, hogy a vele járó munka ne maradjon rajtad.</h2>',
)
replace(
    "keeper.html",
    '<small>TE: ELLENŐRZÖD ÉS JÓVÁHAGYOD</small>',
    '<small>TE: ELLENŐRZÖL / JÓVÁHAGYSZ, HA KELL</small>',
)
for old, new in (
    ('<strong>Neked kell végigolvasni és kiszedni, ami fontos.</strong>', '<strong>Sima tárhelynél neked kell végigolvasni és kiszedni, ami fontos.</strong>'),
    ('<strong>Nem neked kell minden iratot végigolvasni.</strong>', '<strong>Keeperrel nem neked kell minden iratot végigolvasni.</strong>'),
    ('<strong>Neked kell rendben tartani, mi hová tartozik.</strong>', '<strong>Sima tárhelynél neked kell rendben tartani, mi hová tartozik.</strong>'),
    ('<strong>Nem neked kell egyedül összerakni a kapcsolatokat.</strong>', '<strong>Keeperrel nem neked kell egyedül összerakni a kapcsolatokat.</strong>'),
    ('<strong>Neked kell észrevenni és külön felírni a határidőt.</strong>', '<strong>Sima tárhelynél neked kell észrevenni és külön felírni a határidőt.</strong>'),
    ('<strong>Nem neked kell minden dátumot külön figyelni.</strong>', '<strong>Keeperrel nem neked kell minden dátumot külön figyelni.</strong>'),
    ('<strong>Neked kell emlékezned, hol és milyen néven keresd.</strong>', '<strong>Sima tárhelynél neked kell emlékezned, hol és milyen néven keresd.</strong>'),
    ('<strong>Nem kell emlékezned a fájlnévre vagy a mappára.</strong>', '<strong>Keeperrel nem kell emlékezned a fájlnévre vagy a mappára.</strong>'),
    ('<strong>Neked kell észben tartani, mi a következő lépés.</strong>', '<strong>Sima tárhelynél neked kell észben tartani, mi a következő lépés.</strong>'),
    ('<strong>A Keeper külön jelezheti, ha teendőt talál.</strong>', '<strong>Keeperrel külön jelzést kaphatsz, ha teendőt talál.</strong>'),
):
    replace("keeper.html", old, new)
replace(
    "keeper.html",
    'A következő lépést előkészítheti, de csak a jóváhagyásoddal lesz belőle emlékeztető vagy más művelet.',
    'A következő lépést előkészítheti, de csak a jóváhagyásoddal lesz belőle emlékeztető vagy más tényleges lépés.',
)
replace(
    "keeper.html",
    'Beérkezik egy biztosítói levél. A Keeper segíthet rögtön elővenni belőle azt, ami az ügyintézéshez kell.',
    'Beérkezik egy biztosítói levél. A Keeper kiemelheti belőle azt, ami az ügyintézéshez kell, így nem neked kell végigkeresned a teljes iratot.',
)
replace(
    "keeper.html",
    'Egy fontos dátumnál vagy összegnél vissza tudd nézni azt a részt, ahonnan a Keeper kiolvasta.',
    'Egy fontos dátumnál vagy összegnél visszanézheted azt a részt, ahonnan a Keeper kiolvasta.',
)
replace(
    "keeper.html",
    'Ha valamit nem tud elég biztosan felismerni, jelezze, hogy érdemes ellenőrizned.',
    'Ha valamit nem tud elég biztosan felismerni, jelzi, hogy ezt érdemes ellenőrizned.',
)
replace(
    "index.html",
    'Így a munka nagy részét nem neked kell kézzel elvégezni; a döntés ott marad nálad, ahol tényleg dönteni kell.',
    'Így a munka nagy részét nem neked kell kézzel elvégezni. Te csak ott lépsz be, ahol ellenőrizni vagy jóváhagyni kell.',
)
replace(
    "index.html",
    'Megkeresi, mihez tartozhat az irat, és helyet vagy kapcsolatot javasol; a jóváhagyott rendezést elvégezheti.',
    'Megkeresi, mihez tartozhat az irat, és helyet vagy kapcsolatot javasol; jóváhagyásod után a helyére rendezheti.',
)

# EN — make each comparison cell understandable without relying on the column header.
replace(
    "en/keeper.html",
    '<h2 class="keeper96-title">The useful part is not simply having the document. It is not having to do all the work around it yourself.</h2>',
    '<h2 class="keeper96-title">The point is not just to store the document. It is to take the admin around it off your hands.</h2>',
)
replace(
    "en/keeper.html",
    '<small>YOU: REVIEW AND APPROVE</small>',
    '<small>YOU: REVIEW / APPROVE WHEN NEEDED</small>',
)
for old, new in (
    ('<strong>You still have to read the document and pull out what matters.</strong>', '<strong>With basic storage, you still have to read the document and pull out what matters.</strong>'),
    ('<strong>You do not have to read every document end to end.</strong>', '<strong>With Keeper, you do not have to read every document end to end.</strong>'),
    ('<strong>You still have to keep track of what belongs where.</strong>', '<strong>With basic storage, you still have to keep track of what belongs where.</strong>'),
    ('<strong>You do not have to piece all the relationships together yourself.</strong>', '<strong>With Keeper, you do not have to piece all the relationships together yourself.</strong>'),
    ('<strong>You still have to notice the deadline and copy it somewhere else.</strong>', '<strong>With basic storage, you still have to notice the deadline and copy it somewhere else.</strong>'),
    ('<strong>You do not have to watch every date manually.</strong>', '<strong>With Keeper, you do not have to watch every date manually.</strong>'),
    ('<strong>You still have to remember where and under what name to look.</strong>', '<strong>With basic storage, you still have to remember where and under what name to look.</strong>'),
    ('<strong>You do not have to remember the filename or folder.</strong>', '<strong>With Keeper, you do not have to remember the filename or folder.</strong>'),
    ('<strong>You still have to remember what needs to happen next.</strong>', '<strong>With basic storage, you still have to remember what needs to happen next.</strong>'),
    ('<strong>Keeper can flag when it finds a possible next step.</strong>', '<strong>With Keeper, you can be alerted when it finds a possible next step.</strong>'),
):
    replace("en/keeper.html", old, new)
replace(
    "en/index.html",
    'Most of that work should not be yours to do by hand; you step in where a real decision is needed.',
    'Most of that work should not be yours to do by hand. You step in only when something needs checking or approval.',
)
replace(
    "en/index.html",
    'Works out what the document may belong to, suggests the right place or relationship, and can organize it after approval.',
    'Works out what the document may belong to, suggests the right place or relationship, and can organize it after you approve the suggestion.',
)

# DE — same semantic ownership, phrased naturally.
replace(
    "de/keeper.html",
    '<h2 class="keeper96-title">Die Hilfe besteht nicht nur darin, dass das Dokument gespeichert ist. Entscheidend ist, dass Sie die Arbeit darum nicht selbst erledigen müssen.</h2>',
    '<h2 class="keeper96-title">Es reicht nicht, das Dokument zu speichern. Entscheidend ist, dass die Arbeit darum nicht bei Ihnen bleibt.</h2>',
)
replace(
    "de/keeper.html",
    '<small>SIE: PRÜFEN UND GEBEN FREI</small>',
    '<small>SIE: PRÜFEN / FREIGEBEN, WENN NÖTIG</small>',
)
for old, new in (
    ('<strong>Sie müssen das Dokument selbst lesen und Wichtiges heraussuchen.</strong>', '<strong>Bei einfachem Speicher müssen Sie das Dokument selbst lesen und Wichtiges heraussuchen.</strong>'),
    ('<strong>Sie müssen nicht jedes Dokument vollständig lesen.</strong>', '<strong>Mit Keeper müssen Sie nicht jedes Dokument vollständig lesen.</strong>'),
    ('<strong>Sie müssen selbst im Blick behalten, was wohin gehört.</strong>', '<strong>Bei einfachem Speicher müssen Sie selbst im Blick behalten, was wohin gehört.</strong>'),
    ('<strong>Sie müssen die Zusammenhänge nicht allein zusammensetzen.</strong>', '<strong>Mit Keeper müssen Sie die Zusammenhänge nicht allein zusammensetzen.</strong>'),
    ('<strong>Sie müssen die Frist selbst bemerken und separat notieren.</strong>', '<strong>Bei einfachem Speicher müssen Sie die Frist selbst bemerken und separat notieren.</strong>'),
    ('<strong>Sie müssen nicht jedes Datum selbst überwachen.</strong>', '<strong>Mit Keeper müssen Sie nicht jedes Datum selbst überwachen.</strong>'),
    ('<strong>Sie müssen wissen, wo und unter welchem Namen Sie suchen.</strong>', '<strong>Bei einfachem Speicher müssen Sie wissen, wo und unter welchem Namen Sie suchen.</strong>'),
    ('<strong>Sie müssen Dateiname oder Ordner nicht im Kopf behalten.</strong>', '<strong>Mit Keeper müssen Sie Dateiname oder Ordner nicht im Kopf behalten.</strong>'),
    ('<strong>Sie müssen selbst im Kopf behalten, was als Nächstes zu tun ist.</strong>', '<strong>Bei einfachem Speicher müssen Sie selbst im Kopf behalten, was als Nächstes zu tun ist.</strong>'),
    ('<strong>Keeper kann auf einen möglichen nächsten Schritt hinweisen.</strong>', '<strong>Mit Keeper können Sie einen Hinweis bekommen, wenn ein nächster Schritt erkannt wird.</strong>'),
):
    replace("de/keeper.html", old, new)
replace(
    "de/index.html",
    'Den größten Teil dieser Arbeit sollen Sie nicht von Hand erledigen müssen; Sie greifen dort ein, wo eine echte Entscheidung nötig ist.',
    'Den größten Teil dieser Arbeit sollen Sie nicht von Hand erledigen müssen. Sie greifen nur ein, wenn etwas geprüft oder freigegeben werden muss.',
)

# Update the semantic regression markers to the final reviewed wording.
verify = ROOT / "scripts/verify_public_quality.py"
text = verify.read_text(encoding="utf-8")
replacements = {
    '"Nem neked kell egyedül összerakni a kapcsolatokat."': '"Keeperrel nem neked kell egyedül összerakni a kapcsolatokat."',
    '"Nem neked kell minden dátumot külön figyelni."': '"Keeperrel nem neked kell minden dátumot külön figyelni."',
    '"You do not have to piece all the relationships together yourself."': '"With Keeper, you do not have to piece all the relationships together yourself."',
    '"You do not have to watch every date manually."': '"With Keeper, you do not have to watch every date manually."',
    '"Sie müssen die Zusammenhänge nicht allein zusammensetzen."': '"Mit Keeper müssen Sie die Zusammenhänge nicht allein zusammensetzen."',
    '"Sie müssen nicht jedes Datum selbst überwachen."': '"Mit Keeper müssen Sie nicht jedes Datum selbst überwachen."',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"verify marker missing: {old}")
    text = text.replace(old, new, 1)

# Strengthen forbidden phrases so the misleading unanchored wording cannot return.
anchor = '''KEEPER_SEMANTIC_FORBIDDEN = {
    "": (
'''
if anchor not in text:
    raise SystemExit("semantic forbidden anchor missing")
text = text.replace(
    anchor,
    anchor + '        "<strong>Neked kell végigolvasni és kiszedni, ami fontos.</strong>",\n        "<strong>Nem neked kell minden iratot végigolvasni.</strong>",\n',
    1,
)
anchor_en = '''    "en/": (
'''
text = text.replace(
    anchor_en,
    anchor_en + '        "<strong>You still have to read the document and pull out what matters.</strong>",\n        "<strong>You do not have to read every document end to end.</strong>",\n',
    1,
)
anchor_de = '''    "de/": (
'''
# Target the semantic forbidden block's de section, not earlier dictionaries.
pos = text.index("KEEPER_SEMANTIC_FORBIDDEN =")
pre, tail = text[:pos], text[pos:]
if anchor_de not in tail:
    raise SystemExit("semantic forbidden DE anchor missing")
tail = tail.replace(
    anchor_de,
    anchor_de + '        "<strong>Sie müssen das Dokument selbst lesen und Wichtiges heraussuchen.</strong>",\n        "<strong>Sie müssen nicht jedes Dokument vollständig lesen.</strong>",\n',
    1,
)
text = pre + tail
verify.write_text(text, encoding="utf-8")

print("OK_KEEPER_SEMANTICS_R98_REVIEWED")
