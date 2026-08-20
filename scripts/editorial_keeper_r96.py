#!/usr/bin/env python3
from pathlib import Path

repls = {
"keeper.html": [
("<h1>Behozod az iratot. A Keeper elvégzi a rendrakás nagy részét.</h1>", "<h1>Behozod az iratot. A Keeper elvégzi körülötte az adminisztráció nagy részét.</h1>"),
("<p class=\"keeper96-hero-lead\">PDF, kép vagy fotó érkezik. A Keeper célja, hogy elolvassa, felismerje, milyen dokumentumról van szó, kiemelje a fontos adatokat és dátumokat, majd javaslatot tegyen arra, mihez tartozik és van-e vele teendőd. Nem neked kell minden fájlt kézzel végigolvasni, elnevezni és besorolni.</p>", "<p class=\"keeper96-hero-lead\">PDF, kép vagy fotó érkezik. A Keeper elolvassa, megpróbálja felismerni, miről van szó, röviden összefoglalja, kiemeli a fontos adatokat és dátumokat, majd javasolja, hová tartozik és van-e vele teendőd. Neked nem kell minden fájlt külön végigolvasni, elnevezni, besorolni és észben tartani.</p>"),
("<p class=\"keeper96-hero-note\">A Keeper javasol és előkészít. A bizonytalan adatokat ellenőrizheted, a következménnyel járó lépések pedig csak a jóváhagyásoddal történhetnek meg.</p>", "<p class=\"keeper96-hero-note\">Ha valami bizonytalan, a Keeper ezt jelzi, és te javíthatod. Emlékeztető vagy más következő lépés csak a jóváhagyásoddal készül.</p>"),
("<div class=\"keeper96-workrow\"><span>02 / FELISMERI</span><div><strong>Javaslatot készít arra, milyen irat érkezett.</strong><p>Például számla, szerződés, értesítő vagy levél.</p></div></div>", "<div class=\"keeper96-workrow\"><span>02 / FELISMERI</span><div><strong>Megpróbálja felismerni, milyen irat érkezett.</strong><p>Például számla, szerződés, értesítő vagy levél.</p></div></div>"),
("<div class=\"keeper96-workrow\"><span>03 / KIEMELI</span><div><strong>Kiszedi, ami az ügyintézéshez fontos lehet.</strong><p>Dátum, összeg, azonosító, kibocsátó, határidő — ahol a forrás ezt alátámasztja.</p></div></div>", "<div class=\"keeper96-workrow\"><span>03 / KIEMELI</span><div><strong>Röviden összefoglalja, miről szól, és kiemeli, ami fontos.</strong><p>Dátum, összeg, azonosító, kibocsátó vagy határidő — és megmutathatja azt is, honnan olvasta ki.</p></div></div>"),
("<div class=\"keeper96-control\"><span>TE DÖNTESZ</span><div><strong>A Keeper nem intéz el következménnyel járó lépést a háttérben.</strong><p>Emlékeztető és más gyakorlati lépés csak ellenőrzés és jóváhagyás után készülhet.</p></div></div>", "<div class=\"keeper96-control\"><span>TE DÖNTESZ</span><div><strong>A Keeper előkészít és javasol, de a fontos lépéseket nem végzi el helyetted.</strong><p>Amit ellenőrizni kell, azt megmutatja. Emlékeztető vagy más teendő csak a jóváhagyásoddal készül.</p></div></div>"),
("A Keeper ebből a kézi munkából akar minél többet levenni rólad.", "A Keeper célja, hogy ennek a kézi munkának a nagy részét levegye rólad."),
("<article class=\"keeper96-question\"><span>01</span><h3>Mi ez?</h3><p>A Keeper dokumentumtípus-javaslatot készít, hogy ne neked kelljen a fájlnévből kitalálni.</p></article>", "<article class=\"keeper96-question\"><span>01</span><h3>Mi ez?</h3><p>Megpróbálja felismerni, hogy például számla, szerződés, értesítő vagy levél érkezett.</p></article>"),
("<article class=\"keeper96-question\"><span>02</span><h3>Mi fontos benne?</h3><p>A lényeges adatokat és dátumokat kiemeli, a fontos értékeket pedig forráshoz köti.</p></article>", "<article class=\"keeper96-question\"><span>02</span><h3>Miről szól, és mi fontos benne?</h3><p>Röviden összefoglalja, kiemeli a lényeges adatokat és dátumokat, és megmutathatja, melyik részből olvasta ki őket.</p></article>"),
("<article class=\"keeper96-question\"><span>03</span><h3>Mihez tartozik?</h3><p>Kategóriát és kapcsolatot javasolhat személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy ügyhöz.</p></article>", "<article class=\"keeper96-question\"><span>03</span><h3>Mihez tartozik?</h3><p>Megkeresi, melyik személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy ügyhöz kapcsolódhat.</p></article>"),
("<article class=\"keeper96-question\"><span>04</span><h3>Kell vele valamit tennem?</h3><p>Ha határidő vagy következő lépés látszik, a Keeper ezt külön jelzi és teendőt javasolhat.</p></article>", "<article class=\"keeper96-question\"><span>04</span><h3>Kell vele valamit tennem?</h3><p>Ha az iratban határidő vagy tennivaló van, külön jelzi, és javaslatot tehet a következő lépésre.</p></article>"),
("<h2 class=\"keeper96-title\">Te behozod. A feldolgozás nagy részét a rendszer végzi.</h2>", "<h2 class=\"keeper96-title\">Te behozod. A feldolgozás nagy részét a Keeper végzi.</h2>"),
("<small>TE MŰVELETED: BEHOZOD AZ IRATOT</small>", "<small>TE: BEHOZOD AZ IRATOT</small>"),
("<small>KEEPER MUNKÁJA: TARTALOMFELISMERÉS</small>", "<small>KEEPER: ELOLVASSA</small>"),
("<small>KEEPER MUNKÁJA: OSZTÁLYOZÁSI JAVASLAT</small>", "<small>KEEPER: FELISMERI ÉS ÖSSZEFOGLALJA</small>"),
("<small>KEEPER MUNKÁJA: KINYERÉS + FORRÁS</small>", "<small>KEEPER: KIEMELI ÉS MEGMUTATJA A FORRÁST</small>"),
("<small>KEEPER MUNKÁJA: KONTEXTUS + BESOROLÁS</small>", "<small>KEEPER: BESOROLÁST ÉS KAPCSOLATOT JAVASOL</small>"),
("<small>TE DÖNTESZ: JÓVÁHAGYÁS VAGY JAVÍTÁS</small>", "<small>TE: ELLENŐRZÖD ÉS JÓVÁHAGYOD</small>"),
],
"en/keeper.html": [
("<h1>Bring in the document. Keeper does most of the organising work around it.</h1>", "<h1>Bring in the document. Keeper does most of the admin work around it.</h1>"),
("<p class=\"keeper96-hero-lead\">A PDF, image or photo comes in. Keeper is designed to read it, recognize what kind of document it may be, surface important facts and dates, then suggest what it relates to and whether it needs your attention. You should not have to read, name and classify every file by hand before it becomes useful.</p>", "<p class=\"keeper96-hero-lead\">A PDF, image or photo comes in. Keeper is designed to read it, work out what it may be, summarize it, surface important facts and dates, then suggest where it belongs and whether it needs your attention. You should not have to read, name, classify and remember every file by hand before it becomes useful.</p>"),
("<h2 class=\"keeper96-title\">You bring the document in. The system does most of the processing.</h2>", "<h2 class=\"keeper96-title\">You bring the document in. Keeper does most of the processing.</h2>"),
("<small>YOUR STEP: BRING IN THE DOCUMENT</small>", "<small>YOU: BRING IN THE DOCUMENT</small>"),
("<small>KEEPER WORK: CONTENT RECOGNITION</small>", "<small>KEEPER: READS IT</small>"),
("<small>KEEPER WORK: CLASSIFICATION PROPOSAL</small>", "<small>KEEPER: RECOGNIZES AND SUMMARIZES</small>"),
("<small>KEEPER WORK: EXTRACTION + SOURCE</small>", "<small>KEEPER: SURFACES FACTS AND SOURCE</small>"),
("<small>KEEPER WORK: CONTEXT + CLASSIFICATION</small>", "<small>KEEPER: SUGGESTS CLASSIFICATION AND CONTEXT</small>"),
("<small>YOU DECIDE: APPROVE OR CORRECT</small>", "<small>YOU: REVIEW AND APPROVE</small>"),
],
"de/keeper.html": [
("<h1>Sie geben das Dokument hinein. Keeper liest es, erkennt es und ordnet die Verwaltung vor.</h1>", "<h1>Sie geben das Dokument hinein. Keeper übernimmt einen großen Teil der Verwaltungsarbeit darum.</h1>"),
("<h2 class=\"keeper96-title\">Sie bringen das Dokument hinein. Das System übernimmt den größten Teil der Verarbeitung.</h2>", "<h2 class=\"keeper96-title\">Sie bringen das Dokument hinein. Keeper übernimmt den größten Teil der Verarbeitung.</h2>"),
("<small>IHR SCHRITT: DOKUMENT HINZUFÜGEN</small>", "<small>SIE: DOKUMENT HINZUFÜGEN</small>"),
("<small>KEEPER-ARBEIT: INHALTSERKENNUNG</small>", "<small>KEEPER: LIEST ES</small>"),
("<small>KEEPER-ARBEIT: KLASSIFIZIERUNGSVORSCHLAG</small>", "<small>KEEPER: ERKENNT UND FASST ZUSAMMEN</small>"),
("<small>KEEPER-ARBEIT: EXTRAKTION + QUELLE</small>", "<small>KEEPER: HEBT ANGABEN UND QUELLE HERVOR</small>"),
("<small>KEEPER-ARBEIT: KONTEXT + ZUORDNUNG</small>", "<small>KEEPER: SCHLÄGT ZUORDNUNG UND KONTEXT VOR</small>"),
("<small>SIE ENTSCHEIDEN: FREIGEBEN ODER KORRIGIEREN</small>", "<small>SIE: PRÜFEN UND GEBEN FREI</small>"),
],
}

for rel, pairs in repls.items():
    p = Path(rel)
    text = p.read_text(encoding="utf-8")
    for old, new in pairs:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"STOP_R96_EDITORIAL {rel} count={count} old={old[:80]}")
        text = text.replace(old, new, 1)
    p.write_text(text, encoding="utf-8")

print("OK_KEEPER_R96_EDITORIAL_POLISH")
