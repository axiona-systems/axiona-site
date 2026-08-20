#!/usr/bin/env python3
from pathlib import Path

ROOT = Path('.')

REPLACEMENTS = {
    'keeper.html': [
        ('Az AXIONA Keeper fejlesztés alatt álló, local-first dokumentum-asszisztens:', 'Az AXIONA Keeper fejlesztés alatt álló, privát dokumentum-asszisztens:'),
        ('<h2 class="keeper96-title">Te behozod. A feldolgozás nagy részét a rendszer végzi.</h2>', '<h2 class="keeper96-title">Te behozod az iratot. A feldolgozás nagy részét a Keeper végzi.</h2>'),
        ('<article class="keeper96-process-step"><span>03 / MEGÉRTÉS</span><h3>Felismeri, milyen iratról lehet szó.</h3><p>Dokumentumtípus-, kategória- és fontosadat-javaslat készülhet. A bizonytalan eredmény nem válik csendben biztos adattá.</p><small>KEEPER MUNKÁJA: OSZTÁLYOZÁSI JAVASLAT</small></article>', '<article class="keeper96-process-step"><span>03 / MEGÉRTÉS</span><h3>Megérti, mi érkezett.</h3><p>Rövid, közérthető összefoglalót, dokumentumtípus- és kategóriajavaslatot készíthet. Ha valami bizonytalan, ellenőrzésre hagyja.</p><small>KEEPER MUNKÁJA: MEGÉRTÉS + BESOROLÁSI JAVASLAT</small></article>'),
        ('<article class="keeper96-trust-card"><span>01</span><h3>Helyi működés az alap.</h3><p>A termék local-first irányra épül: a dokumentumfeldolgozás elsődleges helye a saját készülék.</p></article>', '<article class="keeper96-trust-card"><span>01</span><h3>Lehetőleg a saját készülékeden dolgozik.</h3><p>Az alapelv az, hogy a dokumentum feldolgozása helyben történjen, és ne kelljen feleslegesen továbbítani az irataidat.</p></article>'),
        ('helyi OCR, dokumentumértelmezés', 'helyben végzett szövegfelismerés (OCR), dokumentumértelmezés'),
    ],
    'en/keeper.html': [
        ('AXIONA Keeper is a local-first document assistant in development', 'AXIONA Keeper is a private document assistant in development'),
        ('<h2 class="keeper96-title">You bring the document in. The system does most of the processing.</h2>', '<h2 class="keeper96-title">You bring the document in. Keeper does most of the processing.</h2>'),
        ('<article class="keeper96-process-step"><span>03 / UNDERSTAND</span><h3>Recognize what kind of document it may be.</h3><p>Keeper can prepare document-type, category and key-field candidates. Uncertainty must not be silently promoted to certainty.</p><small>KEEPER WORK: CLASSIFICATION PROPOSAL</small></article>', '<article class="keeper96-process-step"><span>03 / UNDERSTAND</span><h3>Understand what arrived.</h3><p>Keeper can prepare a short plain-language summary together with document-type and category suggestions. Uncertain results stay reviewable.</p><small>KEEPER WORK: UNDERSTANDING + CLASSIFICATION</small></article>'),
        ('<article class="keeper96-trust-card"><span>01</span><h3>Local-first by design.</h3><p>The product direction puts the device at the centre of document processing rather than treating remote processing as the default.</p></article>', '<article class="keeper96-trust-card"><span>01</span><h3>Designed to work on your device where possible.</h3><p>The default direction is to process documents locally instead of sending them elsewhere without a clear need.</p></article>'),
    ],
    'de/keeper.html': [
        ('AXIONA Keeper ist ein local-first Dokumentenassistent in Entwicklung', 'AXIONA Keeper ist ein privater Dokumentenassistent in Entwicklung'),
        ('<h2 class="keeper96-title">Sie bringen das Dokument hinein. Das System übernimmt den größten Teil der Verarbeitung.</h2>', '<h2 class="keeper96-title">Sie bringen das Dokument hinein. Keeper übernimmt den größten Teil der Verarbeitung.</h2>'),
        ('<article class="keeper96-process-step"><span>03 / VERSTEHEN</span><h3>Erkennen, welche Art Dokument vorliegen könnte.</h3><p>Keeper kann Vorschläge zu Dokumentart, Kategorie und wichtigen Feldern vorbereiten. Unsicherheit darf nicht stillschweigend zu Gewissheit werden.</p><small>KEEPER-ARBEIT: KLASSIFIZIERUNGSVORSCHLAG</small></article>', '<article class="keeper96-process-step"><span>03 / VERSTEHEN</span><h3>Verstehen, was eingegangen ist.</h3><p>Keeper kann eine kurze verständliche Zusammenfassung sowie Vorschläge zu Dokumentart und Kategorie vorbereiten. Unsichere Ergebnisse bleiben prüfbar.</p><small>KEEPER-ARBEIT: VERSTEHEN + ZUORDNUNG</small></article>'),
        ('<article class="keeper96-trust-card"><span>01</span><h3>Local-first als Grundlage.</h3><p>Die Produktrichtung stellt das eigene Gerät in den Mittelpunkt der Dokumentverarbeitung, statt entfernte Verarbeitung zum Standard zu machen.</p></article>', '<article class="keeper96-trust-card"><span>01</span><h3>Wo möglich, arbeitet Keeper auf Ihrem Gerät.</h3><p>Grundprinzip ist die lokale Dokumentverarbeitung, damit Unterlagen nicht ohne klaren Grund weitergegeben werden müssen.</p></article>'),
    ],
}

for rel, pairs in REPLACEMENTS.items():
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    for old, new in pairs:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f'STOP_R96_COPY_{rel}_{old[:28]!r}_COUNT={count}')
        text = text.replace(old, new, 1)
    path.write_text(text, encoding='utf-8')

print('OK_KEEPER_R96_COPY_REFINED')
