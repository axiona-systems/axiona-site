#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "hu": {
        "home": ROOT / "index.html",
        "keeper": ROOT / "keeper.html",
        "solutions": ROOT / "solutions.html",
    },
    "en": {
        "home": ROOT / "en/index.html",
        "keeper": ROOT / "en/keeper.html",
        "solutions": ROOT / "en/solutions.html",
    },
    "de": {
        "home": ROOT / "de/index.html",
        "keeper": ROOT / "de/keeper.html",
        "solutions": ROOT / "de/solutions.html",
    },
}

DATA = {
    "hu": {
        "status": "FEJLESZTÉS ALATT",
        "product_label": "SAJÁT FEJLESZTÉS",
        "home_h2": "Ami összetartozik, maradjon együtt.",
        "home_lead": "Egy szerződés, számla vagy levél ritkán önmagában fontos. A Keeper az összetartozó dokumentumokat egy ügy köré rendezi, és együtt mutatja a fontos dátumokat, az előzményeket és a következő lépést. Elsőként iPhone-on és iPaden, az Apple App Store-ban lesz elérhető.",
        "home_points": ("kapcsolódó iratok", "fontos dátumok", "következő lépés", "helyi működés"),
        "home_cta": "A Keeper megismerése",
        "home_how": "Hogyan működik?",
        "hero_h1": "Ne azt kelljen megjegyezned, <em>hol van.</em> Elég legyen tudnod, mihez tartozik.",
        "hero_lead": "A fontos iratok ritkán maradnak egyedül. Egy szerződéshez jön módosítás, számla, levél, fotó és határidő. Ma ezek könnyen szétszóródnak a telefonon, az e-mailben és mappákban. A Keeper egy ügy köré rendezi őket, hogy amikor szükséged van rájuk, rögtön lásd, mi van meg és mi következik.",
        "scatter_aria": "A dokumentumok ma több helyen vannak: PDF a Letöltésekben, levél az e-mailben, fotó a telefonon, dátum a naptárban. Keeperben egy ügyhöz tartozhatnak.",
        "scatter": (("PDF", "Letöltések"), ("LEVÉL", "E-mail"), ("FOTÓ", "Telefon"), ("DÁTUM", "Naptár")),
        "scatter_result": "egy ügyben",
        "hero_primary": "Hogyan működik?",
        "hero_secondary": "Kapcsolat",
        "demo_aria": "AXIONA Keeper ügy-nézet: egy szerződéses ügy kapcsolódó dokumentumokkal, határidővel és következő teendővel",
        "demo_bar": "KEEPER / ÜGY NÉZET",
        "demo_count": "6 IRAT",
        "demo_kicker": "SZERZŐDÉSES ÜGY",
        "demo_title": "Szerződés és kapcsolódó iratok",
        "stats": ("6 dokumentum", "1 határidő", "1 teendő"),
        "docs": (
            ("PDF", "Szerződés.pdf", "eredeti dokumentum", "EREDETI"),
            ("PDF", "Módosítás.pdf", "kapcsolódó irat", "KAPCSOLAT"),
            ("PDF", "Számla.pdf", "kapcsolódó irat", "KAPCSOLAT"),
            ("LEVÉL", "Kapcsolódó levelezés", "2 dokumentum", "2 IRAT"),
            ("KÉP", "Melléklet.jpg", "kapcsolódó irat", "KAPCSOLAT"),
            ("DÁTUM", "Fontos határidő", "szeptember 12.", "KÖVETKEZŐ"),
        ),
        "next_label": "KÖVETKEZŐ",
        "next_title": "Válasz szükséges",
        "next_detail": "határidő · szeptember 12.",
        "next_status": "VÁLASZRA VÁR",
        "intro_kicker": "MIÉRT KEEPER?",
        "intro_title": "Nem több mappa kell. Hanem kevesebb keresgélés.",
        "intro_p1": "A mappa azt mutatja meg, hová tetted a fájlt. Ez önmagában kevés, amikor hónapokkal később már arra kell emlékezni, melyik szerződéshez, autóhoz, ingatlanhoz vagy projekthez tartozott.",
        "intro_p2": "A Keeper ezeket a kapcsolatokat tartja egyben. Egy ügyet megnyitva együtt látod az eredeti iratot, a hozzá kapcsolódó dokumentumokat, a fontos dátumokat és azt, mi következik.",
        "callout_title": "A cél nem az, hogy többet rendszerezz.",
        "callout_body": "Hanem hogy amikor szükséged van valamire, ne kelljen újra összeraknod a történetet.",
        "examples_kicker": "HOL SEGÍT?",
        "examples_title": "Ugyanaz a rend, egészen különböző ügyekben.",
        "examples_lead": "Nem a dokumentum típusa a lényeg. Az számít, hogy több irat, dátum és teendő ugyanahhoz a dologhoz tartozik.",
        "examples": (
            ("01 / SZERZŐDÉS ÉS ELŐFIZETÉS", "Lásd időben, mikor kell lépni.", "Szerződés, módosítások, számlák és kapcsolódó levelek egy ügyben.", ("eredeti szerződés és módosítások", "lejárat vagy felülvizsgálati időpont", "kapcsolódó levelezés")),
            ("02 / AUTÓ ÉS BIZTOSÍTÁS", "Egy kárügy teljes története egy helyen.", "A kötvény, kárbejelentés, szakértői irat, szervizszámla és a biztosító levelei ugyanahhoz az ügyhöz tartoznak.", ("kapcsolódó dokumentumok egy ügyben", "események időrendben", "következő határidő vagy várt válasz")),
            ("03 / INGATLAN ÉS FELÚJÍTÁS", "Ne külön mappákból kelljen összerakni.", "Ajánlatok, szerződés, számlák, fotók és garanciális iratok együtt maradhatnak a munkával.", ("ajánlatok és szerződés", "számlák és mellékletek", "átadás és garanciális iratok")),
            ("04 / KISVÁLLALKOZÁS", "Egy projekt iratai együtt.", "Az ügyfélhez, munkához és elszámoláshoz tartozó dokumentumok egy helyről követhetők.", ("ajánlat és megrendelés", "projektiratok és levelezés", "számlák és könyvelési csomag")),
        ),
        "folder_kicker": "MAPPÁK ÉS KAPCSOLATOK",
        "folder_title": "A mappa megmutatja, hol van. A kapcsolat azt, mihez tartozik.",
        "folder_p1": "Egy számla egyszerre kapcsolódhat egy szerződéshez, projekthez vagy eszközhöz. Nem kell ugyanazt a fájlt több helyre másolni.",
        "folder_p2": "Az ügyben együtt láthatók a kapcsolódó iratok, dátumok és teendők. Így hónapokkal később is abból a kontextusból indulhatsz, ahol abbahagytad.",
        "folder_aria": "Tervezett mappa- és ügykapcsolati nézet szerződéses ügyhöz",
        "folder_head": "MAPPÁK ÉS ÜGYEK",
        "planned": "TERVEZETT FUNKCIÓ",
        "tree": (
            "▾ Szerződéses ügy",
            "&nbsp;&nbsp;├─ Eredeti dokumentum",
            "&nbsp;&nbsp;│&nbsp;&nbsp;└─ Szerződés.pdf",
            "&nbsp;&nbsp;├─ Kapcsolódó iratok",
            "&nbsp;&nbsp;│&nbsp;&nbsp;├─ Módosítás.pdf",
            "&nbsp;&nbsp;│&nbsp;&nbsp;├─ Számla.pdf",
            "&nbsp;&nbsp;│&nbsp;&nbsp;└─ Melléklet.jpg",
            "&nbsp;&nbsp;└─ Következő: válasz szeptember 12-ig",
        ),
        "folder_rule_title": "A rend feletted marad.",
        "folder_rule_body": "A Keeper felismerheti a valószínű kapcsolatokat, de a rendezést te hagyod jóvá.",
        "ask_kicker": "KERESÉS ÉS KÉRDÉSEK",
        "ask_title": "Nem kell emlékezned a fájlnévre.",
        "answer_title": "A válasz mögött ott marad az eredeti dokumentum.",
        "answer_body": "Egy fontos adatnál vissza tudsz menni ahhoz az irathoz, ahonnan az információ származik.",
        "questions": ("„Mikor jár le ez a szerződés?”", "„Melyik ügyhöz tartozik ez a számla?”", "„Hol van a tavalyi javítás számlája?”", "„Mire várok még választ?”"),
        "solutions_eyebrow": "05 / SAJÁT FEJLESZTÉS",
        "solutions_intro": "Kapcsolódó iratok, fontos dátumok és teendők egy ügy köré rendezve.",
        "solutions_h3": "A dokumentumok ne külön fájlokként éljenek.",
        "solutions_body": "A Keeper az összetartozó iratokat, dátumokat és teendőket egy ügy köré rendezi. Így nem csak azt látod, hogy egy dokumentum megvan-e, hanem azt is, mihez tartozik és mi következik. Elsőként iPhone-on és iPaden, az Apple App Store-ban lesz elérhető.",
        "solutions_link": "Részletes Keeper-bemutató",
    },
    "en": {
        "status": "IN DEVELOPMENT",
        "product_label": "AXIONA PRODUCT",
        "home_h2": "What belongs together should stay together.",
        "home_lead": "A contract, invoice or email rarely matters on its own. Keeper organises related documents around one matter and keeps the important dates, history and next action visible with them. It will launch first on iPhone and iPad through the Apple App Store.",
        "home_points": ("related documents", "important dates", "next action", "local-first"),
        "home_cta": "Meet Keeper",
        "home_how": "How it works",
        "hero_h1": "You shouldn't have to remember <em>where it is.</em> It should be enough to know what it belongs to.",
        "hero_lead": "Important documents rarely stand alone. A contract soon has an amendment, invoice, email, photo and deadline attached to it. Today those pieces easily end up scattered across your phone, inbox and folders. Keeper brings them together around one matter, so when you need them you can immediately see what you have and what comes next.",
        "scatter_aria": "Documents are often scattered: a PDF in Downloads, an email in your inbox, a photo on your phone and a date in your calendar. Keeper can keep them around one matter.",
        "scatter": (("PDF", "Downloads"), ("EMAIL", "Inbox"), ("PHOTO", "Phone"), ("DATE", "Calendar")),
        "scatter_result": "one matter",
        "hero_primary": "How it works",
        "hero_secondary": "Contact",
        "demo_aria": "AXIONA Keeper matter view with a contract and its related documents, deadline and next action",
        "demo_bar": "KEEPER / MATTER VIEW",
        "demo_count": "6 DOCS",
        "demo_kicker": "CONTRACT MATTER",
        "demo_title": "Contract and related documents",
        "stats": ("6 documents", "1 deadline", "1 action"),
        "docs": (
            ("PDF", "Contract.pdf", "original document", "ORIGINAL"),
            ("PDF", "Amendment.pdf", "related document", "RELATED"),
            ("PDF", "Invoice.pdf", "related document", "RELATED"),
            ("EMAIL", "Related correspondence", "2 documents", "2 DOCS"),
            ("IMAGE", "Attachment.jpg", "related document", "RELATED"),
            ("DATE", "Important deadline", "September 12", "NEXT"),
        ),
        "next_label": "NEXT",
        "next_title": "Reply required",
        "next_detail": "deadline · September 12",
        "next_status": "WAITING",
        "intro_kicker": "WHY KEEPER?",
        "intro_title": "You do not need more folders. You need less searching.",
        "intro_p1": "A folder tells you where you put a file. That is not enough months later, when what you actually need to remember is which contract, vehicle, property or project it belonged to.",
        "intro_p2": "Keeper keeps those relationships together. Open a matter and you can see the original document, everything connected to it, the important dates and what comes next.",
        "callout_title": "The goal is not to make you organise more.",
        "callout_body": "It is to stop you having to rebuild the whole story every time you need something.",
        "examples_kicker": "WHERE IT HELPS",
        "examples_title": "The same order, across very different matters.",
        "examples_lead": "The document type is not the important part. What matters is that several files, dates and actions belong to the same thing.",
        "examples": (
            ("01 / CONTRACTS AND SUBSCRIPTIONS", "See the deadline before you need to act.", "Keep the contract, amendments, invoices and related correspondence in one matter.", ("original contract and amendments", "expiry or review date", "related correspondence")),
            ("02 / VEHICLE AND INSURANCE", "One claim, with its whole history together.", "The policy, claim form, assessment, repair invoice and insurer correspondence belong to the same matter.", ("related documents in one matter", "events in chronological order", "next deadline or expected reply")),
            ("03 / PROPERTY AND RENOVATION", "Stop rebuilding the story from separate folders.", "Quotes, contract, invoices, photos and warranty documents can stay with the work they belong to.", ("quotes and contract", "invoices and attachments", "handover and warranty documents")),
            ("04 / SMALL BUSINESS", "Keep one project's documents together.", "Documents for the client, the work and the accounting side can be followed from one place.", ("quote and order", "project documents and correspondence", "invoices and accounting packet")),
        ),
        "folder_kicker": "FOLDERS AND RELATIONSHIPS",
        "folder_title": "A folder shows where it is. A relationship shows what it belongs to.",
        "folder_p1": "An invoice can relate to a contract, a project or an asset at the same time. You do not need duplicate copies of the same file.",
        "folder_p2": "Related documents, dates and actions stay visible in the matter. Months later, you can pick up from the context you left behind instead of reconstructing it.",
        "folder_aria": "Planned folder and matter relationship view for a contract matter",
        "folder_head": "FOLDERS AND MATTERS",
        "planned": "PLANNED FEATURE",
        "tree": (
            "▾ Contract matter",
            "&nbsp;&nbsp;├─ Original document",
            "&nbsp;&nbsp;│&nbsp;&nbsp;└─ Contract.pdf",
            "&nbsp;&nbsp;├─ Related documents",
            "&nbsp;&nbsp;│&nbsp;&nbsp;├─ Amendment.pdf",
            "&nbsp;&nbsp;│&nbsp;&nbsp;├─ Invoice.pdf",
            "&nbsp;&nbsp;│&nbsp;&nbsp;└─ Attachment.jpg",
            "&nbsp;&nbsp;└─ Next: reply by September 12",
        ),
        "folder_rule_title": "You stay in control of the order.",
        "folder_rule_body": "Keeper can recognise likely relationships, but you approve how documents are organised.",
        "ask_kicker": "SEARCH AND QUESTIONS",
        "ask_title": "You do not need to remember the filename.",
        "answer_title": "The original document stays behind the answer.",
        "answer_body": "For an important detail, you can go back to the document the information came from.",
        "questions": ("“When does this contract expire?”", "“Which matter does this invoice belong to?”", "“Where is last year's repair invoice?”", "“What am I still waiting for a reply on?”"),
        "solutions_eyebrow": "05 / AXIONA PRODUCT",
        "solutions_intro": "Related documents, important dates and actions organised around one matter.",
        "solutions_h3": "Documents should not live as isolated files.",
        "solutions_body": "Keeper organises related documents, dates and actions around one matter. You can see not only whether a document exists, but what it belongs to and what comes next. It will launch first on iPhone and iPad through the Apple App Store.",
        "solutions_link": "Detailed Keeper overview",
    },
    "de": {
        "status": "IN ENTWICKLUNG",
        "product_label": "AXIONA PRODUKT",
        "home_h2": "Was zusammengehört, soll zusammenbleiben.",
        "home_lead": "Ein Vertrag, eine Rechnung oder eine Nachricht ist selten für sich allein wichtig. Keeper ordnet zusammengehörige Unterlagen einem Vorgang zu und hält wichtige Termine, den Verlauf und den nächsten Schritt gemeinsam sichtbar. Zuerst erscheint Keeper für iPhone und iPad im Apple App Store.",
        "home_points": ("zugehörige Unterlagen", "wichtige Termine", "nächster Schritt", "lokale Verarbeitung"),
        "home_cta": "Keeper kennenlernen",
        "home_how": "So funktioniert es",
        "hero_h1": "Sie sollten sich nicht merken müssen, <em>wo etwas liegt.</em> Es sollte reichen zu wissen, wozu es gehört.",
        "hero_lead": "Wichtige Unterlagen bleiben selten allein. Zu einem Vertrag kommen Änderung, Rechnung, Nachricht, Foto und Frist hinzu. Heute verteilen sich diese Dinge schnell auf Telefon, E-Mail und Ordner. Keeper führt sie in einem Vorgang zusammen, damit Sie bei Bedarf sofort sehen, was vorhanden ist und was als Nächstes ansteht.",
        "scatter_aria": "Unterlagen liegen oft an verschiedenen Orten: PDF im Download-Ordner, Nachricht im E-Mail-Postfach, Foto auf dem Telefon und Termin im Kalender. Keeper kann sie in einem Vorgang zusammenhalten.",
        "scatter": (("PDF", "Downloads"), ("MAIL", "E-Mail"), ("FOTO", "Telefon"), ("TERMIN", "Kalender")),
        "scatter_result": "ein Vorgang",
        "hero_primary": "So funktioniert es",
        "hero_secondary": "Kontakt",
        "demo_aria": "AXIONA Keeper Vorgangsansicht mit Vertrag, zugehörigen Unterlagen, Frist und nächstem Schritt",
        "demo_bar": "KEEPER / VORGANG",
        "demo_count": "6 DOK.",
        "demo_kicker": "VERTRAGSVORGANG",
        "demo_title": "Vertrag und zugehörige Unterlagen",
        "stats": ("6 Dokumente", "1 Frist", "1 Aufgabe"),
        "docs": (
            ("PDF", "Vertrag.pdf", "Originaldokument", "ORIGINAL"),
            ("PDF", "Änderung.pdf", "zugehöriges Dokument", "VERKNÜPFT"),
            ("PDF", "Rechnung.pdf", "zugehöriges Dokument", "VERKNÜPFT"),
            ("MAIL", "Zugehöriger Schriftverkehr", "2 Dokumente", "2 DOK."),
            ("BILD", "Anlage.jpg", "zugehöriges Dokument", "VERKNÜPFT"),
            ("TERMIN", "Wichtige Frist", "12. September", "NÄCHSTER"),
        ),
        "next_label": "NÄCHSTER SCHRITT",
        "next_title": "Antwort erforderlich",
        "next_detail": "Frist · 12. September",
        "next_status": "WARTET",
        "intro_kicker": "WARUM KEEPER?",
        "intro_title": "Nicht mehr Ordner. Weniger Suchen.",
        "intro_p1": "Ein Ordner zeigt, wo eine Datei abgelegt wurde. Monate später reicht das oft nicht, wenn eigentlich wichtig ist, zu welchem Vertrag, Fahrzeug, Objekt oder Projekt sie gehört.",
        "intro_p2": "Keeper hält diese Zusammenhänge zusammen. Öffnen Sie einen Vorgang, sehen Sie das Originaldokument, die zugehörigen Unterlagen, wichtige Termine und den nächsten Schritt gemeinsam.",
        "callout_title": "Das Ziel ist nicht, dass Sie mehr sortieren.",
        "callout_body": "Sie sollen nicht jedes Mal die ganze Geschichte neu zusammensuchen müssen, wenn Sie etwas brauchen.",
        "examples_kicker": "WO KEEPER HILFT",
        "examples_title": "Die gleiche Ordnung für ganz unterschiedliche Vorgänge.",
        "examples_lead": "Nicht die Dokumentart ist entscheidend. Wichtig ist, dass mehrere Unterlagen, Termine und Aufgaben zur gleichen Sache gehören.",
        "examples": (
            ("01 / VERTRÄGE UND ABOS", "Fristen sehen, bevor Handlungsbedarf entsteht.", "Vertrag, Änderungen, Rechnungen und zugehöriger Schriftverkehr bleiben in einem Vorgang.", ("Originalvertrag und Änderungen", "Ablauf- oder Prüftermin", "zugehöriger Schriftverkehr")),
            ("02 / FAHRZEUG UND VERSICHERUNG", "Ein Schadenfall mit seiner ganzen Geschichte.", "Police, Schadenmeldung, Gutachten, Werkstattrechnung und Versicherungsschreiben gehören zum selben Vorgang.", ("zugehörige Dokumente in einem Vorgang", "Ereignisse in zeitlicher Reihenfolge", "nächste Frist oder erwartete Antwort")),
            ("03 / IMMOBILIE UND RENOVIERUNG", "Nicht aus mehreren Ordnern zusammensuchen.", "Angebote, Vertrag, Rechnungen, Fotos und Garantieunterlagen bleiben bei der Arbeit, zu der sie gehören.", ("Angebote und Vertrag", "Rechnungen und Anlagen", "Übergabe und Garantieunterlagen")),
            ("04 / KLEINUNTERNEHMEN", "Unterlagen eines Projekts zusammenhalten.", "Kunden-, Arbeits- und Abrechnungsunterlagen lassen sich von einem Ort aus verfolgen.", ("Angebot und Auftrag", "Projektunterlagen und Schriftverkehr", "Rechnungen und Buchhaltungsunterlagen")),
        ),
        "folder_kicker": "ORDNER UND ZUSAMMENHÄNGE",
        "folder_title": "Der Ordner zeigt, wo etwas liegt. Die Verbindung zeigt, wozu es gehört.",
        "folder_p1": "Eine Rechnung kann gleichzeitig zu einem Vertrag, Projekt oder Gegenstand gehören. Dafür müssen Sie dieselbe Datei nicht mehrfach ablegen.",
        "folder_p2": "Unterlagen, Termine und Aufgaben bleiben im Vorgang gemeinsam sichtbar. Auch Monate später können Sie im vorhandenen Zusammenhang weiterarbeiten, statt alles neu zusammenzusuchen.",
        "folder_aria": "Geplante Ordner- und Vorgangsansicht für einen Vertragsvorgang",
        "folder_head": "ORDNER UND VORGÄNGE",
        "planned": "GEPLANTE FUNKTION",
        "tree": (
            "▾ Vertragsvorgang",
            "&nbsp;&nbsp;├─ Originaldokument",
            "&nbsp;&nbsp;│&nbsp;&nbsp;└─ Vertrag.pdf",
            "&nbsp;&nbsp;├─ Zugehörige Unterlagen",
            "&nbsp;&nbsp;│&nbsp;&nbsp;├─ Änderung.pdf",
            "&nbsp;&nbsp;│&nbsp;&nbsp;├─ Rechnung.pdf",
            "&nbsp;&nbsp;│&nbsp;&nbsp;└─ Anlage.jpg",
            "&nbsp;&nbsp;└─ Nächster Schritt: Antwort bis 12. September",
        ),
        "folder_rule_title": "Die Ordnung bleibt unter Ihrer Kontrolle.",
        "folder_rule_body": "Keeper kann wahrscheinliche Zusammenhänge erkennen; Sie bestätigen, wie die Unterlagen geordnet werden.",
        "ask_kicker": "SUCHE UND FRAGEN",
        "ask_title": "Sie müssen sich den Dateinamen nicht merken.",
        "answer_title": "Hinter der Antwort bleibt das Originaldokument.",
        "answer_body": "Bei einer wichtigen Angabe können Sie direkt zu dem Dokument zurückgehen, aus dem die Information stammt.",
        "questions": ("„Wann läuft dieser Vertrag ab?“", "„Zu welchem Vorgang gehört diese Rechnung?“", "„Wo ist die Reparaturrechnung vom letzten Jahr?“", "„Auf welche Antwort warte ich noch?“"),
        "solutions_eyebrow": "05 / AXIONA PRODUKT",
        "solutions_intro": "Zugehörige Unterlagen, wichtige Termine und Aufgaben in einem Vorgang gebündelt.",
        "solutions_h3": "Dokumente sollten nicht als einzelne Dateien leben.",
        "solutions_body": "Keeper ordnet zusammengehörige Unterlagen, Termine und Aufgaben einem Vorgang zu. So sehen Sie nicht nur, ob ein Dokument vorhanden ist, sondern auch, wozu es gehört und was als Nächstes ansteht. Zuerst erscheint Keeper für iPhone und iPad im Apple App Store.",
        "solutions_link": "Ausführliche Keeper-Übersicht",
    },
}

CSS = r'''/* AXIONA R94 — Keeper product story and matter-view visualization. */
.keeper-page-hero{
  grid-template-columns:minmax(0,.98fr) minmax(430px,1.02fr);
  gap:clamp(54px,6vw,94px);
}
.keeper-page-hero h1{font-size:clamp(50px,5.35vw,88px);max-width:940px}
.keeper-hero-lead{max-width:790px}

.keeper-scatter-map{
  display:grid;
  grid-template-columns:repeat(5,minmax(0,1fr));
  margin:28px 0 0;
  border:1px solid #b8b0a6;
  background:#f7f2ea;
}
.keeper-scatter-map>span{
  min-height:62px;
  padding:12px 13px;
  border-right:1px solid #cbc3b8;
  display:grid;
  align-content:center;
  gap:6px;
}
.keeper-scatter-map>span:last-child{border-right:0}
.keeper-scatter-map b{
  color:#9b3f24;
  font:900 9px/1 monospace;
  letter-spacing:.12em;
}
.keeper-scatter-map small{
  color:#5d625d;
  font-size:11px;
  font-weight:760;
}
.keeper-scatter-map .keeper-scatter-result{
  background:var(--navy);
}
.keeper-scatter-map .keeper-scatter-result b{color:var(--acid);font-size:14px}
.keeper-scatter-map .keeper-scatter-result small{color:var(--white);text-transform:uppercase;letter-spacing:.08em;font:800 9px/1.2 monospace}

.keeper-matter-demo{
  background:#fbfaf6;
  color:var(--ink);
  border:1px solid #8fa0a2;
  box-shadow:14px 14px 0 #0a1d20;
  overflow:hidden;
  position:relative;
}
.keeper-page-hero .keeper-matter-demo,
.keeper-solutions-card .keeper-matter-demo{
  box-shadow:14px 14px 0 #d2c6b8;
}
.keeper-matter-bar{
  min-height:52px;
  padding:0 20px;
  border-bottom:1px solid #c8cfcc;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:18px;
  background:#f5f6f1;
}
.keeper-matter-bar span{
  color:#536267;
  font:850 9px/1 monospace;
  letter-spacing:.15em;
}
.keeper-matter-bar b{
  background:var(--navy);
  color:var(--acid);
  padding:7px 9px;
  font:850 9px/1 monospace;
  letter-spacing:.09em;
}
.keeper-matter-summary{
  padding:27px 24px 23px;
  border-bottom:1px solid #c8cfcc;
  background:
    linear-gradient(90deg,rgba(31,73,77,.045) 1px,transparent 1px),
    linear-gradient(rgba(31,73,77,.045) 1px,transparent 1px),
    #fffdf8;
  background-size:22px 22px;
}
.keeper-matter-summary>small{
  display:block;
  margin-bottom:9px;
  color:#6d7470;
  font:850 9px/1 monospace;
  letter-spacing:.15em;
}
.keeper-matter-summary>strong{
  display:block;
  max-width:540px;
  font-size:clamp(27px,2.55vw,41px);
  line-height:1.02;
  letter-spacing:-.035em;
}
.keeper-matter-meta{
  display:flex;
  flex-wrap:wrap;
  gap:7px;
  margin-top:20px;
}
.keeper-matter-meta span{
  border:1px solid #bbc6c2;
  background:#ffffffd9;
  padding:7px 9px;
  color:#4f5b58;
  font:800 9px/1 monospace;
  letter-spacing:.04em;
}
.keeper-matter-docs{padding:8px 20px 10px;background:#fbfaf6}
.keeper-matter-doc{
  min-height:54px;
  display:grid;
  grid-template-columns:auto minmax(0,1fr) auto;
  gap:12px;
  align-items:center;
  border-bottom:1px solid #ddd8cf;
}
.keeper-matter-doc:last-child{border-bottom:0}
.keeper-doc-type{
  min-width:42px;
  padding:7px 6px;
  border:1px solid #bbc6c2;
  background:#edf1ed;
  color:#31565a;
  text-align:center;
  font:900 8px/1 monospace;
  letter-spacing:.08em;
}
.keeper-matter-doc div{min-width:0}
.keeper-matter-doc b{
  display:block;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  font-size:13px;
  line-height:1.25;
}
.keeper-matter-doc small{
  display:block;
  margin-top:4px;
  color:#707873;
  font-size:10px;
  line-height:1.25;
}
.keeper-doc-state{
  color:#6e7773;
  font:850 8px/1 monospace;
  letter-spacing:.07em;
  text-align:right;
}
.keeper-matter-next{
  padding:18px 20px;
  display:grid;
  grid-template-columns:auto minmax(0,1fr) auto;
  gap:15px;
  align-items:center;
  background:var(--navy);
  color:var(--white);
}
.keeper-matter-next>span{
  color:var(--acid);
  font:900 9px/1 monospace;
  letter-spacing:.13em;
}
.keeper-matter-next strong{display:block;font-size:15px;line-height:1.25}
.keeper-matter-next small{display:block;margin-top:4px;color:#b8c9ca;font-size:10px;line-height:1.3}
.keeper-matter-status{
  background:var(--acid);
  color:var(--ink);
  border:1px solid #a9bb4c;
  padding:8px 9px;
  font:900 8px/1 monospace;
  letter-spacing:.08em;
  white-space:nowrap;
}
.keeper-matter-demo--compact .keeper-matter-summary{padding:23px 22px 20px}
.keeper-matter-demo--compact .keeper-matter-summary>strong{font-size:clamp(25px,2.25vw,36px)}
.keeper-matter-demo--compact .keeper-matter-docs{padding-top:6px;padding-bottom:7px}
.keeper-matter-demo--compact .keeper-matter-doc{min-height:50px}

.keeper-examples-lead{
  max-width:760px;
  margin:18px 0 0;
  color:#5b554f;
  font-size:16px;
  line-height:1.7;
}

@media (max-width:1100px){
  .keeper-page-hero{grid-template-columns:1fr;min-height:0}
  .keeper-page-hero .keeper-matter-demo{max-width:800px}
  .keeper-scatter-map{max-width:800px}
}
@media (max-width:760px){
  .keeper-scatter-map{grid-template-columns:repeat(2,minmax(0,1fr))}
  .keeper-scatter-map>span{border-bottom:1px solid #cbc3b8}
  .keeper-scatter-map>span:nth-child(2n){border-right:0}
  .keeper-scatter-map .keeper-scatter-result{grid-column:1/-1;border-bottom:0}
  .keeper-matter-demo{box-shadow:9px 9px 0 #0a1d20}
  .keeper-page-hero .keeper-matter-demo,
  .keeper-solutions-card .keeper-matter-demo{box-shadow:9px 9px 0 #d2c6b8}
  .keeper-matter-doc{grid-template-columns:auto minmax(0,1fr)}
  .keeper-doc-state{grid-column:2;justify-self:start;margin-top:-7px;margin-bottom:7px;text-align:left}
  .keeper-matter-next{grid-template-columns:1fr;gap:8px}
  .keeper-matter-status{justify-self:start;margin-top:3px}
  .keeper-matter-bar{padding-left:16px;padding-right:16px}
  .keeper-matter-summary{padding-left:18px;padding-right:18px}
  .keeper-matter-docs{padding-left:16px;padding-right:16px}
  .keeper-matter-next{padding-left:16px;padding-right:16px}
}
'''


def replace_section(path: Path, class_value: str, html: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(rf'    <section class="{re.escape(class_value)}">.*?    </section>', re.S)
    new_text, count = pattern.subn(html.rstrip(), text, count=1)
    if count != 1:
        raise SystemExit(f"STOP_R94_SECTION_REPLACE {path.relative_to(ROOT)} class={class_value} count={count}")
    path.write_text(new_text, encoding="utf-8")


def ensure_stylesheet_and_release(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    old = '  <link href="/assets/keeper-r87.css" rel="stylesheet"/>'
    new = old + '\n  <link href="/assets/keeper-r94.css" rel="stylesheet"/>'
    if '/assets/keeper-r94.css' not in text:
        if old not in text:
            raise SystemExit(f"STOP_R94_KEEPER_STYLESHEET_ANCHOR {path.relative_to(ROOT)}")
        text = text.replace(old, new, 1)
    text, count = re.subn(r'<meta content="R\d+" name="axiona-release"/>', '<meta content="R94" name="axiona-release"/>', text, count=1)
    if count != 1:
        raise SystemExit(f"STOP_R94_RELEASE_MARKER {path.relative_to(ROOT)}")
    path.write_text(text, encoding="utf-8")


def matter_demo(lang: str, compact: bool) -> str:
    d = DATA[lang]
    docs = d["docs"][:4] if compact else d["docs"]
    rows = "\n".join(
        f'        <div class="keeper-matter-doc"><span class="keeper-doc-type">{kind}</span><div><b>{name}</b><small>{desc}</small></div><span class="keeper-doc-state">{state}</span></div>'
        for kind, name, desc, state in docs
    )
    modifier = " keeper-matter-demo--compact" if compact else " keeper-matter-demo--full"
    stats = "".join(f"<span>{item}</span>" for item in d["stats"])
    return f'''      <aside class="keeper-matter-demo{modifier}" aria-label="{d['demo_aria']}">
        <div class="keeper-matter-bar"><span>{d['demo_bar']}</span><b>{d['demo_count']}</b></div>
        <div class="keeper-matter-summary"><small>{d['demo_kicker']}</small><strong>{d['demo_title']}</strong><div class="keeper-matter-meta">{stats}</div></div>
        <div class="keeper-matter-docs">
{rows}
        </div>
        <div class="keeper-matter-next"><span>{d['next_label']}</span><div><strong>{d['next_title']}</strong><small>{d['next_detail']}</small></div><b class="keeper-matter-status">{d['next_status']}</b></div>
      </aside>'''


def home_section(lang: str) -> str:
    d = DATA[lang]
    prefix = "" if lang == "hu" else f"/{lang}"
    keeper_href = f"{prefix}/keeper.html" if prefix else "/keeper.html"
    anchor = "hogyan-mukodik" if lang == "hu" else "how-it-works" if lang == "en" else "so-funktioniert-es"
    points = "".join(f"<span>{p}</span>" for p in d["home_points"])
    return f'''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">{d['status']}</b><span class="micro">iPhone + iPad</span></div>
        <h2>AXIONA Keeper<span>{d['home_h2']}</span></h2>
        <p class="keeper-preview-lead">{d['home_lead']}</p>
        <div class="keeper-preview-points">{points}</div>
        <div class="actions"><a class="button button-dark" href="{keeper_href}">{d['home_cta']}<span>→</span></a><a class="text-link" href="{keeper_href}#{anchor}">{d['home_how']}<span>↗</span></a></div>
      </div>
{matter_demo(lang, True)}
    </section>'''


def hero_section(lang: str) -> str:
    d = DATA[lang]
    prefix = "" if lang == "hu" else f"/{lang}"
    contact_href = f"{prefix}/contact.html" if prefix else "/contact.html"
    anchor = "hogyan-mukodik" if lang == "hu" else "how-it-works" if lang == "en" else "so-funktioniert-es"
    scatter = "".join(f'<span><b>{kind}</b><small>{where}</small></span>' for kind, where in d["scatter"])
    return f'''    <section class="keeper-page-hero section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>{d['product_label']}</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">{d['status']}</b><span class="micro">iPhone + iPad</span></div>
        <h1>{d['hero_h1']}</h1>
        <p class="keeper-hero-lead">{d['hero_lead']}</p>
        <div class="keeper-scatter-map" aria-label="{d['scatter_aria']}">{scatter}<span class="keeper-scatter-result"><b aria-hidden="true">→</b><small>{d['scatter_result']}</small></span></div>
        <div class="actions"><a class="button button-dark" href="#{anchor}">{d['hero_primary']}<span>↓</span></a><a class="text-link" href="{contact_href}">{d['hero_secondary']}<span>→</span></a></div>
      </div>
{matter_demo(lang, False)}
    </section>'''


def intro_section(lang: str) -> str:
    d = DATA[lang]
    return f'''    <section class="keeper-intro section-pad">
      <div class="keeper-intro-grid">
        <div><p class="keeper-section-kicker">{d['intro_kicker']}</p><h2 class="keeper-section-title">{d['intro_title']}</h2></div>
        <div class="keeper-intro-copy">
          <p>{d['intro_p1']}</p>
          <p>{d['intro_p2']}</p>
          <div class="keeper-plain-callout"><strong>{d['callout_title']}</strong><p>{d['callout_body']}</p></div>
        </div>
      </div>
    </section>'''


def examples_section(lang: str) -> str:
    d = DATA[lang]
    cards = []
    for micro, title, body, items in d["examples"]:
        lis = "".join(f"<li>{item}</li>" for item in items)
        cards.append(f'        <article class="keeper-example-card"><span class="micro">{micro}</span><h3>{title}</h3><p>{body}</p><ul class="keeper-example-list">{lis}</ul></article>')
    return f'''    <section class="keeper-examples section-pad">
      <div class="keeper-examples-head"><p class="keeper-section-kicker">{d['examples_kicker']}</p><h2 class="keeper-section-title">{d['examples_title']}</h2><p class="keeper-examples-lead">{d['examples_lead']}</p></div>
      <div class="keeper-example-grid">
{chr(10).join(cards)}
      </div>
    </section>'''


def folder_section(lang: str) -> str:
    d = DATA[lang]
    tree_lines = []
    for idx, line in enumerate(d["tree"]):
        tag = "strong" if idx == 0 else "i" if idx == len(d["tree"]) - 1 else "span"
        tree_lines.append(f"            <{tag}>{line}</{tag}>")
    return f'''    <section class="keeper-folder-section section-pad">
      <div class="keeper-folder-grid">
        <div class="keeper-folder-copy"><p class="keeper-section-kicker">{d['folder_kicker']}</p><h2 class="keeper-section-title">{d['folder_title']}</h2><p>{d['folder_p1']}</p><p>{d['folder_p2']}</p></div>
        <div class="keeper-folder-tree" aria-label="{d['folder_aria']}">
          <div class="keeper-folder-tree-head"><span>{d['folder_head']}</span><b>{d['planned']}</b></div>
          <div class="keeper-tree-lines">
{chr(10).join(tree_lines)}
          </div>
          <div class="keeper-folder-rule"><strong>{d['folder_rule_title']}</strong> {d['folder_rule_body']}</div>
        </div>
      </div>
    </section>'''


def ask_section(lang: str) -> str:
    d = DATA[lang]
    questions = "".join(f'<div class="keeper-question"><span>{idx:02d}</span><p>{q}</p></div>' for idx, q in enumerate(d["questions"], 1))
    return f'''    <section class="keeper-ask section-pad">
      <div class="keeper-ask-layout">
        <div><p class="keeper-section-kicker">{d['ask_kicker']}</p><h2 class="keeper-section-title">{d['ask_title']}</h2><div class="keeper-answer-note"><strong>{d['answer_title']}</strong><p>{d['answer_body']}</p></div></div>
        <div><div class="keeper-question-list">{questions}</div></div>
      </div>
    </section>'''


def solutions_section(lang: str) -> str:
    d = DATA[lang]
    prefix = "" if lang == "hu" else f"/{lang}"
    keeper_href = f"{prefix}/keeper.html" if prefix else "/keeper.html"
    return f'''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">{d['solutions_eyebrow']}</p><h2>AXIONA Keeper</h2><p>{d['solutions_intro']}</p></header>
      <article class="keeper-solutions-card">
        <div>
          <div class="keeper-status-line"><b class="keeper-status-badge">{d['status']}</b><span class="micro">iPhone + iPad</span></div>
          <h3>{d['solutions_h3']}</h3>
          <p>{d['solutions_body']}</p>
          <a class="text-link" href="{keeper_href}">{d['solutions_link']}<span>→</span></a>
        </div>
{matter_demo(lang, True)}
      </article>
    </section>'''


def update_verifier() -> None:
    path = ROOT / "scripts/verify_public_quality.py"
    text = path.read_text(encoding="utf-8")

    old = '''KEEPER_REQUIRED_MARKERS = (\n    'class="keeper-status-badge"',\n    'class="keeper-planned-note"',\n    'class="keeper-folder-tree"',\n    'class="keeper-dev-status section-pad"',\n)'''
    new = '''KEEPER_REQUIRED_MARKERS = (\n    'class="keeper-status-badge"',\n    'class="keeper-matter-demo keeper-matter-demo--full"',\n    'class="keeper-scatter-map"',\n    'class="keeper-planned-note"',\n    'class="keeper-folder-tree"',\n    'class="keeper-dev-status section-pad"',\n)'''
    if old not in text:
        raise SystemExit("STOP_R94_VERIFIER_MARKER_ANCHOR")
    text = text.replace(old, new, 1)

    old = '''            if "/assets/keeper-r87.css" not in text:\n                errors.append(f"Keeper stylesheet missing from product entry page: {source}")'''
    new = '''            if "/assets/keeper-r87.css" not in text:\n                errors.append(f"Keeper stylesheet missing from product entry page: {source}")\n            if "/assets/keeper-r94.css" not in text:\n                errors.append(f"Keeper R94 product-story stylesheet missing from product entry page: {source}")\n            if 'class="keeper-matter-demo keeper-matter-demo--compact"' not in text:\n                errors.append(f"Keeper R94 matter demo missing from product entry page: {source}")'''
    if old not in text:
        raise SystemExit("STOP_R94_VERIFIER_ENTRY_ANCHOR")
    text = text.replace(old, new, 1)

    old = '''        if "/assets/keeper-r87.css" not in keeper_text:\n            errors.append(f"Keeper stylesheet missing from product page: {keeper}")'''
    new = '''        if "/assets/keeper-r87.css" not in keeper_text:\n            errors.append(f"Keeper stylesheet missing from product page: {keeper}")\n        if "/assets/keeper-r94.css" not in keeper_text:\n            errors.append(f"Keeper R94 product-story stylesheet missing from product page: {keeper}")'''
    if old not in text:
        raise SystemExit("STOP_R94_VERIFIER_KEEPER_ANCHOR")
    text = text.replace(old, new, 1)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    for paths in PAGES.values():
        for path in paths.values():
            ensure_stylesheet_and_release(path)

    for lang, paths in PAGES.items():
        replace_section(paths["home"], "keeper-preview section-pad", home_section(lang))
        replace_section(paths["keeper"], "keeper-page-hero section-pad", hero_section(lang))
        replace_section(paths["keeper"], "keeper-intro section-pad", intro_section(lang))
        replace_section(paths["keeper"], "keeper-examples section-pad", examples_section(lang))
        replace_section(paths["keeper"], "keeper-folder-section section-pad", folder_section(lang))
        replace_section(paths["keeper"], "keeper-ask section-pad", ask_section(lang))
        replace_section(paths["solutions"], "development section-pad", solutions_section(lang))

    (ROOT / "assets/keeper-r94.css").write_text(CSS, encoding="utf-8")
    update_verifier()

    print("OK_KEEPER_R94_PRODUCT_STORY_MIGRATION")


if __name__ == "__main__":
    main()
