#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

KEEPER = {
"keeper.html": r'''    <section class="keeper-page-hero keeper-page-hero--intelligence section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>SAJÁT FEJLESZTÉS</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h1>Bedobod az iratot. <em>A Keeper elvégzi körülötte a rendrakás nagy részét.</em></h1>
        <p class="keeper-hero-lead">Egy számlát, levelet vagy szerződést ma neked kell elolvasnod, megértened, elnevezned, besorolnod, a kapcsolódó iratokhoz kötnöd és észben tartanod, van-e vele teendő. A Keeper ezt az adminisztrációs munkát egyszerűsíti le: feldolgozza az iratot, kiemeli a fontos részeket, javasolja, mihez tartozik, és jelzi, ha valami figyelmet kér.</p>
        <div class="keeper-hero-promise"><strong>Nem csak elteszi.</strong><span>Megérti · rendezi · összekapcsolja · követhetővé teszi.</span></div>
        <div class="actions"><a class="button button-dark" href="#hogyan-dolgozik">Mit csinál a Keeper?<span>↓</span></a><a class="text-link" href="/contact.html">Kapcsolat<span>→</span></a></div>
      </div>
      <aside class="keeper-work-demo" aria-label="A Keeper munkafolyamata egy beérkező irattal">
        <div class="keeper-work-demo-head"><span>EGY IRAT ÚTJA</span><b>KEEPER MUNKA</b></div>
        <div class="keeper-work-input"><span>BEÉRKEZIK</span><div><b>PDF · KÉP · FOTÓ</b><small>eredeti irat</small></div></div>
        <div class="keeper-work-steps">
          <div class="keeper-work-step"><span>01</span><div><b>Elolvassa</b><small>A dokumentum szövege és szerkezete feldolgozhatóvá válik.</small></div><em>OCR</em></div>
          <div class="keeper-work-step"><span>02</span><div><b>Felismeri, mi ez</b><small>Dokumentumtípus, fontos nevek, összegek, dátumok és határidők kerülnek elő.</small></div><em>ÉRTELMEZÉS</em></div>
          <div class="keeper-work-step"><span>03</span><div><b>Megkeresi az összefüggést</b><small>Javasolja, melyik szerződéshez, ügyhöz, eszközhöz vagy más meglévő kontextushoz kapcsolódhat.</small></div><em>KAPCSOLAT</em></div>
          <div class="keeper-work-step"><span>04</span><div><b>Rendezi</b><small>Érthető cím, kategória és kapcsolódások alapján kerül a helyére — nem neked kell mappastruktúrát tervezned.</small></div><em>REND</em></div>
          <div class="keeper-work-step"><span>05</span><div><b>Jelzi, ha van teendő</b><small>Határidő, ellenőrzés vagy emlékeztető-javaslat jelenhet meg az irat mellett.</small></div><em>FIGYELEM</em></div>
        </div>
        <div class="keeper-work-control"><span>TE MARADSZ KONTROLLBAN</span><strong>A fontos adat ellenőrizhető. A bizonytalan javaslat javítható. Emlékeztető csak jóváhagyással készül.</strong></div>
      </aside>
    </section>

    <section class="keeper-value-section section-pad" id="hogyan-dolgozik">
      <div class="keeper-value-head"><p class="keeper-section-kicker">MIÉRT JÓ EZ NEKED?</p><h2 class="keeper-section-title">Nem egy újabb hely a fájloknak. A Keeper dolgozik velük.</h2><p>A legtöbb dokumentumos alkalmazás ott ér véget, hogy a fájl bekerült valahová. A Keeper célja az, hogy onnantól kevesebb dolgod legyen vele.</p></div>
      <div class="keeper-value-grid">
        <article><span>01</span><h3>Nem neked kell kibogarászni, mi fontos.</h3><p>A hosszú vagy nehezen olvasható iratból előkerülhetnek a lényeges adatok, dátumok és határidők, röviden és visszaellenőrizhetően.</p></article>
        <article><span>02</span><h3>Nem neked kell kitalálni, hová tedd.</h3><p>A Keeper kategóriát és kapcsolatot javasolhat a már meglévő iratok, szerződések és ügyek alapján. Ha nem biztos benne, nem talál ki tényt helyetted.</p></article>
        <article><span>03</span><h3>Nem neked kell fejben összekötni a történetet.</h3><p>Egy új levél vagy számla nem külön fájlként marad: láthatóvá válhat, mihez kapcsolódik, mit módosít vagy melyik korábbi iratot egészíti ki.</p></article>
        <article><span>04</span><h3>Nem neked kell észben tartani, mikor kell lépni.</h3><p>Ha az iratban fontos időpont vagy lehetséges teendő van, a Keeper kiemeli és javaslatot készíthet. A döntés és a jóváhagyás nálad marad.</p></article>
      </div>
    </section>

    <section class="keeper-lifecycle section-pad">
      <div class="keeper-lifecycle-head"><p class="keeper-section-kicker">MIT LÁTSZ A VÉGÉN?</p><h2 class="keeper-section-title">Egy nyers dokumentumból érthető helyzet lesz.</h2><p>Nem a fájlnév a lényeg, hanem hogy néhány másodperc alatt tudd: mi ez, mi fontos benne, mihez tartozik és kell-e vele foglalkoznod.</p></div>
      <div class="keeper-lifecycle-grid">
        <div class="keeper-lifecycle-source"><span>BEÉRKEZŐ IRAT</span><strong>szolgaltatoi_ertesites_08.pdf</strong><small>8 oldal · PDF</small><div class="keeper-lifecycle-lines"><i></i><i></i><i></i><i></i><i></i></div></div>
        <div class="keeper-lifecycle-arrow" aria-hidden="true">→</div>
        <div class="keeper-lifecycle-result">
          <span>KEEPER ÖSSZEFOGLALÓ</span>
          <h3>Szolgáltatói értesítő</h3>
          <dl><div><dt>Miről szól?</dt><dd>Feltételek és díjazás változása</dd></div><div><dt>Fontos dátum</dt><dd>Ellenőrzést igényel</dd></div><div><dt>Mihez tartozhat?</dt><dd>Meglévő szolgáltatási szerződés</dd></div><div><dt>Következő lépés</dt><dd>Szerződés ellenőrzése · javaslat</dd></div></dl>
          <p>Az oldal szemlélteti a tervezett működést; a fontos állításokat a Keeper forráshoz köti, a bizonytalan eredményt pedig ellenőrzésre jelöli.</p>
        </div>
      </div>
    </section>

    <section class="keeper-examples section-pad">
      <div class="keeper-examples-head"><p class="keeper-section-kicker">HÉTKÖZNAPI HASZON</p><h2 class="keeper-section-title">Ugyanaz a háttérmunka, egészen különböző ügyeknél.</h2><p class="keeper-examples-lead">Nem attól hasznos a Keeper, hogy milyen mappát készít. Attól, hogy leveszi rólad az iratok megértésének, összekapcsolásának és utánkövetésének egy részét.</p></div>
      <div class="keeper-example-grid">
        <article class="keeper-example-card"><span class="micro">01 / SZERZŐDÉS</span><h3>Észreveszi, ha egy új irat a régi szerződésedhez tartozik.</h3><p>Felismerheti a módosítást, kiemelheti az új dátumot vagy feltételt, és kapcsolatot javasolhat az eredeti szerződéssel.</p></article>
        <article class="keeper-example-card"><span class="micro">02 / AUTÓ ÉS BIZTOSÍTÁS</span><h3>Nem neked kell újra összerakni egy kárügy előzményeit.</h3><p>Egy új biztosítói levél kapcsolódhat a korábbi kárbejelentéshez, szakértői irathoz vagy szervizszámlához, és látszhat, mire vársz még.</p></article>
        <article class="keeper-example-card"><span class="micro">03 / INGATLAN ÉS GARANCIA</span><h3>A számla után a garanciális információ sem vész el.</h3><p>A Keeper felismerheti a kivitelezőt, dátumot és garanciához fontos adatot, majd a munkához kapcsolhatja az új dokumentumot.</p></article>
        <article class="keeper-example-card"><span class="micro">04 / KISVÁLLALKOZÁS</span><h3>A beérkező irat rögtön kapjon értelmet.</h3><p>Ajánlat, megrendelés, számla vagy levél esetén ne neked kelljen minden alkalommal kézzel elnevezni, besorolni és a projekthez kötni.</p></article>
      </div>
    </section>

    <section class="keeper-background-order section-pad">
      <div class="keeper-background-copy"><p class="keeper-section-kicker">RENDEZÉS A HÁTTÉRBEN</p><h2 class="keeper-section-title">A rend legyen a Keeper feladata, ne egy újabb házimunka.</h2><p>A mappák és kategóriák hasznosak, de nem ez a termék lényege. A cél az, hogy az irat érkezése után a Keeper előkészítse a besorolást, felismerje a lehetséges kapcsolatokat és rendezett állapotot javasoljon.</p></div>
      <div class="keeper-background-grid">
        <article><b>JAVASOL</b><h3>Hová tartozhat?</h3><p>Kategória, ügy, szerződés vagy más kapcsolódó elem.</p></article>
        <article><b>ÖSSZEKAPCSOL</b><h3>Mi függ össze vele?</h3><p>Korábbi iratok és adminisztratív előzmények kerülhetnek mellé.</p></article>
        <article><b>NEM ERŐLTETI</b><h3>Ha bizonytalan, jelzi.</h3><p>A javaslat ellenőrizhető és javítható; a felhasználói korrekció elsőbbséget élvez.</p></article>
      </div>
    </section>

    <section class="keeper-trust section-pad">
      <div class="keeper-trust-head"><p class="keeper-section-kicker">BIZALOM ÉS KONTROLL</p><h2 class="keeper-section-title">A segítség csak akkor ér valamit, ha látod, mire alapoz.</h2><p>A Keeper privát, local-first rendszerként készül. Nem az a cél, hogy vakon higgy egy automatikus válasznak, hanem hogy kevesebb munkával, mégis ellenőrizhetően intézd a dokumentumaidat.</p></div>
      <div class="keeper-trust-grid">
        <article><span>FORRÁS</span><h3>A fontos adat visszakereshető az eredeti iratban.</h3><p>A felismert mező és a mögötte álló dokumentumrész összetartozik.</p></article>
        <article><span>BIZONYTALANSÁG</span><h3>Ami nem biztos, nem válik csendben ténnyé.</h3><p>A bizonytalan eredmény ellenőrzést kérhet ahelyett, hogy magabiztosan tévedne.</p></article>
        <article><span>JÓVÁHAGYÁS</span><h3>A Keeper javasolhat, de nem intézkedik helyetted.</h3><p>Emlékeztető és más következménnyel járó lépés csak a jóváhagyásoddal történik.</p></article>
        <article><span>PRIVÁT MŰKÖDÉS</span><h3>Az alapirány: feldolgozás helyben, felesleges adatküldés nélkül.</h3><p>A termék architektúrája a helyi feldolgozást, védett tárolást és kontrollált hozzáférést részesíti előnyben.</p></article>
      </div>
    </section>

    <section class="keeper-dev-status section-pad">
      <div><span class="micro">AXIONA KEEPER</span><h2>Fejlesztés alatt.</h2><p>Az első kiadás iPhone-ra és iPadre készül, és az Apple App Store-ban lesz elérhető. A jelenlegi fejlesztés alapja a dokumentumimport, helyi OCR, dokumentumértelmezés, ellenőrizhető fontos adatok és jóváhagyásra épülő teendők.</p></div>
      <div class="keeper-dev-side"><span>ELSŐ PLATFORM</span><strong>iPhone + iPad</strong><span>TERVEZETT TERJESZTÉS</span><strong>Apple App Store</strong><a class="button button-dark" href="/contact.html">Kapcsolat<span>→</span></a></div>
    </section>

''',
"en/keeper.html": r'''    <section class="keeper-page-hero keeper-page-hero--intelligence section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>AXIONA PRODUCT</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h1>Drop in the document. <em>Keeper takes care of much of the admin around it.</em></h1>
        <p class="keeper-hero-lead">With a bill, letter or contract, you normally have to read it, understand it, name it, file it, connect it to related documents and remember whether anything needs doing. Keeper is being built to simplify that work: it processes the document, brings the important parts forward, suggests what it belongs to and flags anything that may need attention.</p>
        <div class="keeper-hero-promise"><strong>It does more than store it.</strong><span>Understand · organize · connect · keep track.</span></div>
        <div class="actions"><a class="button button-dark" href="#how-keeper-works">What does Keeper do?<span>↓</span></a><a class="text-link" href="/en/contact.html">Contact<span>→</span></a></div>
      </div>
      <aside class="keeper-work-demo" aria-label="How Keeper works with an incoming document">
        <div class="keeper-work-demo-head"><span>ONE DOCUMENT</span><b>KEEPER WORK</b></div>
        <div class="keeper-work-input"><span>ARRIVES</span><div><b>PDF · IMAGE · PHOTO</b><small>original document</small></div></div>
        <div class="keeper-work-steps">
          <div class="keeper-work-step"><span>01</span><div><b>Reads it</b><small>The document text and structure become processable.</small></div><em>OCR</em></div>
          <div class="keeper-work-step"><span>02</span><div><b>Recognizes what it is</b><small>Document type, important names, amounts, dates and deadlines can be brought forward.</small></div><em>UNDERSTAND</em></div>
          <div class="keeper-work-step"><span>03</span><div><b>Looks for context</b><small>It can suggest which contract, matter, asset or other existing context the document may belong to.</small></div><em>CONTEXT</em></div>
          <div class="keeper-work-step"><span>04</span><div><b>Organizes it</b><small>A clear title, category and relationships help put it in the right place without making you design a folder system.</small></div><em>ORDER</em></div>
          <div class="keeper-work-step"><span>05</span><div><b>Flags what needs attention</b><small>A deadline, review or reminder proposal can stay with the document.</small></div><em>ATTENTION</em></div>
        </div>
        <div class="keeper-work-control"><span>YOU STAY IN CONTROL</span><strong>Important facts can be checked. Uncertain suggestions can be corrected. Reminders require approval.</strong></div>
      </aside>
    </section>

    <section class="keeper-value-section section-pad" id="how-keeper-works">
      <div class="keeper-value-head"><p class="keeper-section-kicker">WHY IS THIS USEFUL?</p><h2 class="keeper-section-title">Not another place for files. Keeper works on them.</h2><p>Most document apps stop once a file has been stored somewhere. Keeper is intended to reduce the work that starts after that point.</p></div>
      <div class="keeper-value-grid">
        <article><span>01</span><h3>You should not have to dig through the document for what matters.</h3><p>Important facts, dates and deadlines can be extracted from long or difficult documents and shown in a concise, checkable form.</p></article>
        <article><span>02</span><h3>You should not have to decide where everything goes from scratch.</h3><p>Keeper can propose a category and context from existing documents, contracts and matters. If it is uncertain, it should not invent a fact for you.</p></article>
        <article><span>03</span><h3>You should not have to reconstruct the story in your head.</h3><p>A new letter or invoice does not have to remain an isolated file: Keeper can make the relationship to earlier documents visible.</p></article>
        <article><span>04</span><h3>You should not have to remember every date yourself.</h3><p>If a document contains an important date or possible action, Keeper can surface it and prepare a suggestion. Approval stays with you.</p></article>
      </div>
    </section>

    <section class="keeper-lifecycle section-pad">
      <div class="keeper-lifecycle-head"><p class="keeper-section-kicker">WHAT DO YOU GET?</p><h2 class="keeper-section-title">A raw document becomes an understandable situation.</h2><p>The filename is not the point. What matters is knowing quickly what the document is, what matters in it, what it belongs to and whether you need to act.</p></div>
      <div class="keeper-lifecycle-grid">
        <div class="keeper-lifecycle-source"><span>INCOMING DOCUMENT</span><strong>service_notice_08.pdf</strong><small>8 pages · PDF</small><div class="keeper-lifecycle-lines"><i></i><i></i><i></i><i></i><i></i></div></div>
        <div class="keeper-lifecycle-arrow" aria-hidden="true">→</div>
        <div class="keeper-lifecycle-result">
          <span>KEEPER SUMMARY</span><h3>Service notice</h3>
          <dl><div><dt>What is it about?</dt><dd>Changes to terms and pricing</dd></div><div><dt>Important date</dt><dd>Needs review</dd></div><div><dt>What may it belong to?</dt><dd>Existing service contract</dd></div><div><dt>Next step</dt><dd>Review contract · suggestion</dd></div></dl>
          <p>This page illustrates the intended product behavior. Important claims are tied back to source evidence, while uncertain results remain marked for review.</p>
        </div>
      </div>
    </section>

    <section class="keeper-examples section-pad">
      <div class="keeper-examples-head"><p class="keeper-section-kicker">EVERYDAY VALUE</p><h2 class="keeper-section-title">The same background work across very different situations.</h2><p class="keeper-examples-lead">Keeper is not useful because it creates a folder. It is useful because it reduces the work of understanding, connecting and following up on documents.</p></div>
      <div class="keeper-example-grid">
        <article class="keeper-example-card"><span class="micro">01 / CONTRACT</span><h3>Notice when a new document belongs with an existing contract.</h3><p>Keeper can recognize an amendment, surface a new date or term and suggest a connection to the original contract.</p></article>
        <article class="keeper-example-card"><span class="micro">02 / VEHICLE AND INSURANCE</span><h3>Do not rebuild the history of a claim every time.</h3><p>A new insurer letter can be connected to the earlier claim, assessment or repair invoice, while the outstanding response remains visible.</p></article>
        <article class="keeper-example-card"><span class="micro">03 / PROPERTY AND WARRANTY</span><h3>Do not lose the warranty context after the invoice is paid.</h3><p>Keeper can recognize the contractor, date and warranty-relevant information and connect the new document to the work it belongs to.</p></article>
        <article class="keeper-example-card"><span class="micro">04 / SMALL BUSINESS</span><h3>Give incoming documents context immediately.</h3><p>Quotes, orders, invoices and letters should not require the same manual naming, filing and project linking every time.</p></article>
      </div>
    </section>

    <section class="keeper-background-order section-pad">
      <div class="keeper-background-copy"><p class="keeper-section-kicker">ORDER IN THE BACKGROUND</p><h2 class="keeper-section-title">Organization should be Keeper's job, not another chore for you.</h2><p>Folders and categories are useful, but they are not the product. The goal is for Keeper to prepare classification, recognize possible relationships and propose an organized state after a document arrives.</p></div>
      <div class="keeper-background-grid">
        <article><b>PROPOSE</b><h3>Where might it belong?</h3><p>A category, matter, contract or another related object.</p></article>
        <article><b>CONNECT</b><h3>What is related to it?</h3><p>Earlier documents and administrative history can stay connected.</p></article>
        <article><b>DO NOT FORCE IT</b><h3>If it is uncertain, say so.</h3><p>Suggestions can be reviewed and corrected; user corrections take priority.</p></article>
      </div>
    </section>

    <section class="keeper-trust section-pad">
      <div class="keeper-trust-head"><p class="keeper-section-kicker">TRUST AND CONTROL</p><h2 class="keeper-section-title">Help only matters if you can see what it is based on.</h2><p>Keeper is being built as a private, local-first system. The goal is not to make you blindly trust an automated answer, but to reduce the work while keeping important information checkable.</p></div>
      <div class="keeper-trust-grid">
        <article><span>SOURCE</span><h3>Important facts can be traced back to the original document.</h3><p>The extracted value stays connected to the source that supports it.</p></article>
        <article><span>UNCERTAINTY</span><h3>Uncertain output does not quietly become a fact.</h3><p>A result can be marked for review rather than presented with false certainty.</p></article>
        <article><span>APPROVAL</span><h3>Keeper can suggest; it does not act on your behalf.</h3><p>Reminders and other consequential actions require your approval.</p></article>
        <article><span>PRIVATE BY DESIGN</span><h3>The default direction is local processing without unnecessary data transfer.</h3><p>The architecture prioritizes on-device processing, protected storage and controlled access.</p></article>
      </div>
    </section>

    <section class="keeper-dev-status section-pad">
      <div><span class="micro">AXIONA KEEPER</span><h2>In development.</h2><p>The first release is planned for iPhone and iPad through the Apple App Store. Current development foundations include document import, local OCR, document understanding, checkable important facts and approval-based actions.</p></div>
      <div class="keeper-dev-side"><span>FIRST PLATFORM</span><strong>iPhone + iPad</strong><span>PLANNED DISTRIBUTION</span><strong>Apple App Store</strong><a class="button button-dark" href="/en/contact.html">Contact<span>→</span></a></div>
    </section>

''',
"de/keeper.html": r'''    <section class="keeper-page-hero keeper-page-hero--intelligence section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>AXIONA PRODUKT</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h1>Dokument hinein. <em>Keeper übernimmt einen großen Teil der Verwaltungsarbeit darum herum.</em></h1>
        <p class="keeper-hero-lead">Bei einer Rechnung, einem Schreiben oder Vertrag müssen Sie heute selbst lesen, verstehen, benennen, einordnen, Verbindungen zu anderen Unterlagen herstellen und im Kopf behalten, ob etwas zu tun ist. Keeper soll genau diese Verwaltungsarbeit vereinfachen: Das Dokument wird verarbeitet, wichtige Inhalte werden hervorgehoben, der passende Zusammenhang wird vorgeschlagen und möglicher Handlungsbedarf wird sichtbar.</p>
        <div class="keeper-hero-promise"><strong>Nicht nur ablegen.</strong><span>Verstehen · ordnen · verbinden · im Blick behalten.</span></div>
        <div class="actions"><a class="button button-dark" href="#so-arbeitet-keeper">Was macht Keeper?<span>↓</span></a><a class="text-link" href="/de/contact.html">Kontakt<span>→</span></a></div>
      </div>
      <aside class="keeper-work-demo" aria-label="Wie Keeper mit einem eingehenden Dokument arbeitet">
        <div class="keeper-work-demo-head"><span>EIN DOKUMENT</span><b>KEEPER ARBEIT</b></div>
        <div class="keeper-work-input"><span>EINGANG</span><div><b>PDF · BILD · FOTO</b><small>Originaldokument</small></div></div>
        <div class="keeper-work-steps">
          <div class="keeper-work-step"><span>01</span><div><b>Lesen</b><small>Text und Struktur des Dokuments werden verarbeitbar.</small></div><em>OCR</em></div>
          <div class="keeper-work-step"><span>02</span><div><b>Erkennen, worum es geht</b><small>Dokumentart, wichtige Namen, Beträge, Daten und Fristen können hervorgeholt werden.</small></div><em>VERSTEHEN</em></div>
          <div class="keeper-work-step"><span>03</span><div><b>Zusammenhang suchen</b><small>Keeper kann vorschlagen, zu welchem Vertrag, Vorgang, Gegenstand oder anderen vorhandenen Kontext das Dokument gehört.</small></div><em>KONTEXT</em></div>
          <div class="keeper-work-step"><span>04</span><div><b>Ordnen</b><small>Ein verständlicher Titel, Kategorie und Verknüpfungen bringen das Dokument an seinen Platz, ohne dass Sie eine Ordnerstruktur planen müssen.</small></div><em>ORDNUNG</em></div>
          <div class="keeper-work-step"><span>05</span><div><b>Aufmerksam machen</b><small>Frist, Prüfung oder Erinnerungsvorschlag können direkt beim Dokument sichtbar werden.</small></div><em>AUFMERKSAMKEIT</em></div>
        </div>
        <div class="keeper-work-control"><span>SIE BEHALTEN DIE KONTROLLE</span><strong>Wichtige Angaben sind prüfbar. Unsichere Vorschläge sind korrigierbar. Erinnerungen brauchen Ihre Freigabe.</strong></div>
      </aside>
    </section>

    <section class="keeper-value-section section-pad" id="so-arbeitet-keeper">
      <div class="keeper-value-head"><p class="keeper-section-kicker">WAS BRINGT DAS?</p><h2 class="keeper-section-title">Nicht noch ein Ablageort. Keeper arbeitet mit den Dokumenten.</h2><p>Viele Dokumenten-Apps hören dort auf, wo eine Datei gespeichert wurde. Keeper soll die Arbeit reduzieren, die danach erst beginnt.</p></div>
      <div class="keeper-value-grid">
        <article><span>01</span><h3>Sie müssen nicht selbst herausarbeiten, was wichtig ist.</h3><p>Wichtige Angaben, Daten und Fristen können aus langen oder schwer lesbaren Dokumenten hervorgeholt und kompakt sowie prüfbar dargestellt werden.</p></article>
        <article><span>02</span><h3>Sie müssen nicht jedes Mal neu entscheiden, wohin etwas gehört.</h3><p>Keeper kann anhand vorhandener Unterlagen, Verträge und Vorgänge eine Kategorie und einen Zusammenhang vorschlagen. Bei Unsicherheit soll nichts als Tatsache erfunden werden.</p></article>
        <article><span>03</span><h3>Sie müssen die Geschichte nicht im Kopf zusammensetzen.</h3><p>Ein neues Schreiben oder eine Rechnung bleibt nicht zwingend eine isolierte Datei: Zusammenhänge mit früheren Dokumenten können sichtbar werden.</p></article>
        <article><span>04</span><h3>Sie müssen nicht jeden Termin selbst im Kopf behalten.</h3><p>Enthält ein Dokument ein wichtiges Datum oder einen möglichen nächsten Schritt, kann Keeper darauf hinweisen und einen Vorschlag vorbereiten. Die Freigabe bleibt bei Ihnen.</p></article>
      </div>
    </section>

    <section class="keeper-lifecycle section-pad">
      <div class="keeper-lifecycle-head"><p class="keeper-section-kicker">WAS KOMMT DABEI HERAUS?</p><h2 class="keeper-section-title">Aus einem rohen Dokument wird eine verständliche Situation.</h2><p>Nicht der Dateiname ist entscheidend. Wichtig ist, schnell zu wissen: Was ist das, was ist darin wichtig, wozu gehört es und muss ich etwas tun?</p></div>
      <div class="keeper-lifecycle-grid">
        <div class="keeper-lifecycle-source"><span>EINGEHENDES DOKUMENT</span><strong>anbieter_hinweis_08.pdf</strong><small>8 Seiten · PDF</small><div class="keeper-lifecycle-lines"><i></i><i></i><i></i><i></i><i></i></div></div>
        <div class="keeper-lifecycle-arrow" aria-hidden="true">→</div>
        <div class="keeper-lifecycle-result">
          <span>KEEPER ZUSAMMENFASSUNG</span><h3>Anbieterhinweis</h3>
          <dl><div><dt>Worum geht es?</dt><dd>Änderung von Bedingungen und Preisen</dd></div><div><dt>Wichtiges Datum</dt><dd>Prüfung erforderlich</dd></div><div><dt>Wozu könnte es gehören?</dt><dd>Bestehender Dienstleistungsvertrag</dd></div><div><dt>Nächster Schritt</dt><dd>Vertrag prüfen · Vorschlag</dd></div></dl>
          <p>Die Darstellung veranschaulicht die geplante Produktlogik. Wichtige Aussagen werden mit ihrer Quelle verbunden; unsichere Ergebnisse bleiben zur Prüfung markiert.</p>
        </div>
      </div>
    </section>

    <section class="keeper-examples section-pad">
      <div class="keeper-examples-head"><p class="keeper-section-kicker">NUTZEN IM ALLTAG</p><h2 class="keeper-section-title">Die gleiche Hintergrundarbeit in ganz unterschiedlichen Situationen.</h2><p class="keeper-examples-lead">Keeper ist nicht deshalb nützlich, weil ein Ordner entsteht. Der Nutzen liegt darin, das Verstehen, Verbinden und Nachverfolgen von Unterlagen zu vereinfachen.</p></div>
      <div class="keeper-example-grid">
        <article class="keeper-example-card"><span class="micro">01 / VERTRAG</span><h3>Erkennen, wenn ein neues Dokument zu einem vorhandenen Vertrag gehört.</h3><p>Keeper kann eine Änderung erkennen, ein neues Datum oder eine neue Bedingung hervorheben und die Verbindung zum ursprünglichen Vertrag vorschlagen.</p></article>
        <article class="keeper-example-card"><span class="micro">02 / FAHRZEUG UND VERSICHERUNG</span><h3>Den Verlauf eines Schadenfalls nicht jedes Mal neu zusammensuchen.</h3><p>Ein neues Versicherungsschreiben kann mit Schadenmeldung, Gutachten oder Werkstattrechnung verbunden werden; offene Antworten bleiben sichtbar.</p></article>
        <article class="keeper-example-card"><span class="micro">03 / IMMOBILIE UND GARANTIE</span><h3>Garantieinformationen nach der Rechnung nicht verlieren.</h3><p>Keeper kann Handwerker, Datum und garantierelevante Angaben erkennen und das neue Dokument mit der zugehörigen Arbeit verbinden.</p></article>
        <article class="keeper-example-card"><span class="micro">04 / KLEINUNTERNEHMEN</span><h3>Eingehende Unterlagen sofort in einen Zusammenhang bringen.</h3><p>Angebot, Auftrag, Rechnung oder Schreiben sollen nicht jedes Mal manuell benannt, einsortiert und einem Projekt zugeordnet werden müssen.</p></article>
      </div>
    </section>

    <section class="keeper-background-order section-pad">
      <div class="keeper-background-copy"><p class="keeper-section-kicker">ORDNUNG IM HINTERGRUND</p><h2 class="keeper-section-title">Ordnung soll Keepers Aufgabe sein, nicht eine weitere Arbeit für Sie.</h2><p>Ordner und Kategorien sind nützlich, aber nicht der Kern des Produkts. Nach dem Eingang eines Dokuments soll Keeper die Einordnung vorbereiten, mögliche Beziehungen erkennen und einen geordneten Zustand vorschlagen.</p></div>
      <div class="keeper-background-grid">
        <article><b>VORSCHLAGEN</b><h3>Wozu könnte es gehören?</h3><p>Kategorie, Vorgang, Vertrag oder ein anderes verbundenes Element.</p></article>
        <article><b>VERBINDEN</b><h3>Was hängt damit zusammen?</h3><p>Frühere Unterlagen und administrative Vorgeschichte können verbunden bleiben.</p></article>
        <article><b>NICHT ERZWINGEN</b><h3>Bei Unsicherheit wird das sichtbar.</h3><p>Vorschläge bleiben prüf- und korrigierbar; Korrekturen des Nutzers haben Vorrang.</p></article>
      </div>
    </section>

    <section class="keeper-trust section-pad">
      <div class="keeper-trust-head"><p class="keeper-section-kicker">VERTRAUEN UND KONTROLLE</p><h2 class="keeper-section-title">Hilfe ist nur dann wertvoll, wenn nachvollziehbar bleibt, worauf sie basiert.</h2><p>Keeper wird als privates, local-first System entwickelt. Ziel ist nicht blindes Vertrauen in automatische Antworten, sondern weniger Verwaltungsarbeit bei weiterhin prüfbaren wichtigen Informationen.</p></div>
      <div class="keeper-trust-grid">
        <article><span>QUELLE</span><h3>Wichtige Angaben lassen sich zum Originaldokument zurückverfolgen.</h3><p>Der erkannte Wert bleibt mit der Quelle verbunden, die ihn stützt.</p></article>
        <article><span>UNSICHERHEIT</span><h3>Unsicherheit wird nicht stillschweigend zur Tatsache.</h3><p>Ein Ergebnis kann zur Prüfung markiert werden, statt mit falscher Sicherheit aufzutreten.</p></article>
        <article><span>FREIGABE</span><h3>Keeper kann vorschlagen, handelt aber nicht an Ihrer Stelle.</h3><p>Erinnerungen und andere folgenreiche Aktionen benötigen Ihre Freigabe.</p></article>
        <article><span>PRIVAT ENTWICKELT</span><h3>Die Grundrichtung ist lokale Verarbeitung ohne unnötige Datenübertragung.</h3><p>Die Architektur priorisiert Verarbeitung auf dem Gerät, geschützte Speicherung und kontrollierten Zugriff.</p></article>
      </div>
    </section>

    <section class="keeper-dev-status section-pad">
      <div><span class="micro">AXIONA KEEPER</span><h2>In Entwicklung.</h2><p>Die erste Version ist für iPhone und iPad über den Apple App Store geplant. Aktuelle Grundlagen sind Dokumentimport, lokales OCR, Dokumentverständnis, prüfbare wichtige Angaben und freigabebasierte Aktionen.</p></div>
      <div class="keeper-dev-side"><span>ERSTE PLATTFORM</span><strong>iPhone + iPad</strong><span>GEPLANTE VERTEILUNG</span><strong>Apple App Store</strong><a class="button button-dark" href="/de/contact.html">Kontakt<span>→</span></a></div>
    </section>

''',
}

OVERVIEW = {
"index.html": r'''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h2>AXIONA Keeper<span>Ne neked kelljen minden irattal ugyanazt az adminisztrációt végigcsinálni.</span></h2>
        <p class="keeper-preview-lead">A Keeper elolvassa a beérkező dokumentumot, kiemeli belőle a fontos adatokat és dátumokat, javasolja, mihez tartozik, majd jelzi, ha valami figyelmet kér. Nem egy újabb tárhelyet építünk, hanem egy olyan eszközt, amely a dokumentum körüli munkát egyszerűsíti le.</p>
        <div class="actions"><a class="button button-dark" href="/keeper.html">A Keeper megismerése<span>→</span></a><a class="text-link" href="/keeper.html#hogyan-dolgozik">Mit csinál egy irattal?<span>↗</span></a></div>
      </div>
      <aside class="keeper-benefit-panel" aria-label="Mit végez el a Keeper?">
        <div class="keeper-benefit-head"><span>MIT VÉGEZ EL?</span><b>A HÁTTÉRBEN</b></div>
        <div class="keeper-benefit-list">
          <article class="keeper-benefit-item"><span>01</span><div><strong>Elolvassa és érthetővé teszi.</strong><p>Dokumentumtípus, fontos adatok, dátumok és határidők kerülhetnek elő.</p></div></article>
          <article class="keeper-benefit-item"><span>02</span><div><strong>Javasolja, mihez tartozik.</strong><p>Kapcsolatot kereshet a már meglévő szerződések, ügyek és iratok között.</p></div></article>
          <article class="keeper-benefit-item"><span>03</span><div><strong>Rendezi és jelzi, ha dolgod van vele.</strong><p>A besorolás, kapcsolódások és következő lépés egy folyamat része lesz.</p></div></article>
        </div>
        <div class="keeper-benefit-outcome"><span>EREDMÉNY</span><strong>Kevesebb kézi rendszerezés. Kevesebb fejben tartott adminisztráció.</strong></div>
      </aside>
    </section>''',
"en/index.html": r'''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h2>AXIONA Keeper<span>Stop doing the same admin work for every document.</span></h2>
        <p class="keeper-preview-lead">Keeper reads an incoming document, brings important facts and dates forward, suggests what it belongs to and flags anything that may need attention. We are not building another storage space; we are building a tool that simplifies the work around documents.</p>
        <div class="actions"><a class="button button-dark" href="/en/keeper.html">Explore Keeper<span>→</span></a><a class="text-link" href="/en/keeper.html#how-keeper-works">What does it do with a document?<span>↗</span></a></div>
      </div>
      <aside class="keeper-benefit-panel" aria-label="What Keeper does">
        <div class="keeper-benefit-head"><span>WHAT DOES IT DO?</span><b>IN THE BACKGROUND</b></div>
        <div class="keeper-benefit-list">
          <article class="keeper-benefit-item"><span>01</span><div><strong>Reads it and makes it understandable.</strong><p>Document type, important facts, dates and deadlines can be surfaced.</p></div></article>
          <article class="keeper-benefit-item"><span>02</span><div><strong>Suggests what it belongs to.</strong><p>Keeper can look for context across existing contracts, matters and documents.</p></div></article>
          <article class="keeper-benefit-item"><span>03</span><div><strong>Organizes it and flags what needs attention.</strong><p>Classification, relationships and the next step become one flow.</p></div></article>
        </div>
        <div class="keeper-benefit-outcome"><span>RESULT</span><strong>Less manual filing. Less administration to keep in your head.</strong></div>
      </aside>
    </section>''',
"de/index.html": r'''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h2>AXIONA Keeper<span>Nicht bei jedem Dokument dieselbe Verwaltungsarbeit wiederholen.</span></h2>
        <p class="keeper-preview-lead">Keeper liest ein eingehendes Dokument, hebt wichtige Angaben und Daten hervor, schlägt den passenden Zusammenhang vor und macht möglichen Handlungsbedarf sichtbar. Wir bauen keinen weiteren Ablageort, sondern ein Werkzeug, das die Arbeit rund um Dokumente vereinfacht.</p>
        <div class="actions"><a class="button button-dark" href="/de/keeper.html">Keeper kennenlernen<span>→</span></a><a class="text-link" href="/de/keeper.html#so-arbeitet-keeper">Was macht Keeper mit einem Dokument?<span>↗</span></a></div>
      </div>
      <aside class="keeper-benefit-panel" aria-label="Was Keeper übernimmt">
        <div class="keeper-benefit-head"><span>WAS ÜBERNIMMT KEEPER?</span><b>IM HINTERGRUND</b></div>
        <div class="keeper-benefit-list">
          <article class="keeper-benefit-item"><span>01</span><div><strong>Lesen und verständlich machen.</strong><p>Dokumentart, wichtige Angaben, Daten und Fristen können hervorgeholt werden.</p></div></article>
          <article class="keeper-benefit-item"><span>02</span><div><strong>Den passenden Zusammenhang vorschlagen.</strong><p>Keeper kann Verbindungen zu vorhandenen Verträgen, Vorgängen und Unterlagen suchen.</p></div></article>
          <article class="keeper-benefit-item"><span>03</span><div><strong>Ordnen und auf Handlungsbedarf hinweisen.</strong><p>Einordnung, Verbindungen und nächster Schritt werden Teil eines Ablaufs.</p></div></article>
        </div>
        <div class="keeper-benefit-outcome"><span>ERGEBNIS</span><strong>Weniger manuelles Sortieren. Weniger Verwaltung im Kopf.</strong></div>
      </aside>
    </section>''',
}

SOLUTIONS = {
"solutions.html": r'''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">05 / SAJÁT FEJLESZTÉS</p><h2>AXIONA Keeper</h2><p>Dokumentum-intelligencia és mindennapi ügyintézés — privát, ellenőrizhető működéssel.</p></header>
      <article class="keeper-solutions-card">
        <div><div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Nem csak tárolja az iratot. Dolgozik vele.</h3><p>A Keeper elolvassa a dokumentumot, kiemeli a fontos adatokat és dátumokat, kapcsolatot javasol ahhoz, amihez tartozik, és jelzi, ha van következő teendő. A cél: kevesebb kézi besorolás, kevesebb keresgélés és kevesebb fejben tartott adminisztráció.</p><a class="text-link" href="/keeper.html">Részletes Keeper-bemutató<span>→</span></a></div>
        <aside class="keeper-solution-work" aria-label="Keeper feldolgozási folyamat"><span>IRAT</span><b>→</b><span>ELŐLVASSA</span><b>→</b><span>MEGÉRTI</span><b>→</b><span>RENDEZI</span><b>→</b><span>JELZI A TEENDŐT</span></aside>
      </article>
    </section>''',
"en/solutions.html": r'''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">05 / AXIONA PRODUCT</p><h2>AXIONA Keeper</h2><p>Document intelligence and everyday administration with private, checkable behavior.</p></header>
      <article class="keeper-solutions-card">
        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>It does more than store the document. It works on it.</h3><p>Keeper reads the document, surfaces important facts and dates, suggests the context it belongs to and flags a possible next step. The goal: less manual filing, less searching and less administration to keep in your head.</p><a class="text-link" href="/en/keeper.html">Detailed Keeper overview<span>→</span></a></div>
        <aside class="keeper-solution-work" aria-label="Keeper processing flow"><span>DOCUMENT</span><b>→</b><span>READ</span><b>→</b><span>UNDERSTAND</span><b>→</b><span>ORGANIZE</span><b>→</b><span>FLAG ACTION</span></aside>
      </article>
    </section>''',
"de/solutions.html": r'''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">05 / AXIONA PRODUKT</p><h2>AXIONA Keeper</h2><p>Dokumentenintelligenz und alltägliche Verwaltung mit privater, prüfbarer Arbeitsweise.</p></header>
      <article class="keeper-solutions-card">
        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Nicht nur speichern. Mit dem Dokument arbeiten.</h3><p>Keeper liest das Dokument, hebt wichtige Angaben und Daten hervor, schlägt den passenden Zusammenhang vor und macht einen möglichen nächsten Schritt sichtbar. Ziel: weniger manuelles Sortieren, weniger Suchen und weniger Verwaltung im Kopf.</p><a class="text-link" href="/de/keeper.html">Keeper im Detail<span>→</span></a></div>
        <aside class="keeper-solution-work" aria-label="Keeper Verarbeitungsablauf"><span>DOKUMENT</span><b>→</b><span>LESEN</span><b>→</b><span>VERSTEHEN</span><b>→</b><span>ORDNEN</span><b>→</b><span>HANDLUNGSBEDARF</span></aside>
      </article>
    </section>''',
}

META = {
"keeper.html": (
"AXIONA Keeper | Érthető dokumentumok, kevesebb adminisztráció",
"A Keeper elolvassa a dokumentumot, kiemeli a fontos adatokat és dátumokat, kapcsolatot javasol, rendezi és jelzi a következő teendőt — privát, ellenőrizhető működéssel.",
"AXIONA Keeper | Dokumentumból érthető teendő",
"A Keeper nem csak tárol: értelmezi, rendezi és követhetővé teszi a dokumentum körüli adminisztrációt."
),
"en/keeper.html": (
"AXIONA Keeper | Understand documents, reduce admin",
"Keeper reads documents, surfaces important facts and dates, suggests context, organizes them and flags possible next steps with private, checkable behavior.",
"AXIONA Keeper | From document to clear next step",
"Keeper does more than store documents: it helps understand, organize, connect and follow up on the administration around them."
),
"de/keeper.html": (
"AXIONA Keeper | Dokumente verstehen, Verwaltung vereinfachen",
"Keeper liest Dokumente, hebt wichtige Angaben und Daten hervor, schlägt Zusammenhänge vor, ordnet und macht mögliche nächste Schritte sichtbar — privat und prüfbar.",
"AXIONA Keeper | Vom Dokument zum klaren nächsten Schritt",
"Keeper speichert nicht nur: Dokumente werden verständlicher, geordnet, verbunden und in der weiteren Verwaltung leichter nachverfolgbar."
),
}

CSS = r'''

/* AXIONA R96 — Keeper document-intelligence story. */
.keeper-page-hero--intelligence{grid-template-columns:minmax(0,.92fr) minmax(470px,1.08fr);gap:clamp(52px,6vw,92px)}
.keeper-page-hero--intelligence h1{font-size:clamp(48px,5vw,82px)}
.keeper-hero-promise{display:flex;flex-wrap:wrap;gap:8px 18px;margin:24px 0 0;padding:15px 17px;border-left:4px solid var(--acid);background:#eff2ea}
.keeper-hero-promise strong{font-size:13px}.keeper-hero-promise span{color:#4b5754;font-size:13px}
.keeper-work-demo{background:#fbfaf6;border:1px solid #89999a;box-shadow:14px 14px 0 #0a1d20;overflow:hidden}
.keeper-work-demo-head,.keeper-work-input{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:16px 20px;border-bottom:1px solid #cbd1cd}
.keeper-work-demo-head{background:#f2f3ee}.keeper-work-demo-head span,.keeper-work-input>span{font:850 9px/1 monospace;letter-spacing:.14em;color:#4b5c60}.keeper-work-demo-head b{background:var(--navy);color:var(--acid);padding:7px 9px;font:850 9px/1 monospace;letter-spacing:.08em}
.keeper-work-input{background:#fffdf8}.keeper-work-input div{text-align:right}.keeper-work-input b{display:block;font-size:14px}.keeper-work-input small{display:block;margin-top:4px;color:#606864;font-size:10px}
.keeper-work-steps{padding:5px 20px 7px}.keeper-work-step{display:grid;grid-template-columns:34px minmax(0,1fr) auto;gap:14px;align-items:center;padding:16px 0;border-bottom:1px solid #ddd8cf}.keeper-work-step:last-child{border-bottom:0}.keeper-work-step>span{color:#9b3f24;font:900 11px/1 monospace}.keeper-work-step b{display:block;font-size:14px;line-height:1.3}.keeper-work-step small{display:block;margin-top:5px;color:#555f5b;font-size:11px;line-height:1.45}.keeper-work-step em{font:850 8px/1 monospace;letter-spacing:.08em;color:#52625e;border:1px solid #b8c3bf;padding:7px 8px;font-style:normal;background:#eef1ec}
.keeper-work-control{display:grid;gap:8px;padding:18px 20px;background:var(--navy);color:#fff}.keeper-work-control span{color:var(--acid);font:900 9px/1 monospace;letter-spacing:.14em}.keeper-work-control strong{font-size:13px;line-height:1.5}
.keeper-value-head,.keeper-lifecycle-head,.keeper-background-copy,.keeper-trust-head{max-width:900px}.keeper-value-head>p:last-child,.keeper-lifecycle-head>p:last-child,.keeper-background-copy>p:last-child,.keeper-trust-head>p:last-child{color:#5b554f;font-size:16px;line-height:1.7}
.keeper-value-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px;margin-top:34px;background:#bfc5c1;border:1px solid #bfc5c1}.keeper-value-grid article{background:#fbfaf6;padding:27px 25px;min-height:210px}.keeper-value-grid article>span{color:#9b3f24;font:900 10px/1 monospace}.keeper-value-grid h3{margin:15px 0 9px;font-size:22px;line-height:1.15}.keeper-value-grid p{margin:0;color:#535c58;font-size:13px;line-height:1.65}
.keeper-lifecycle{background:#f0ebe3}.keeper-lifecycle-grid{display:grid;grid-template-columns:minmax(0,.78fr) 54px minmax(0,1.22fr);gap:18px;align-items:stretch;margin-top:34px}.keeper-lifecycle-source,.keeper-lifecycle-result{border:1px solid #9ba7a3;background:#fffdf8;padding:24px}.keeper-lifecycle-source>span,.keeper-lifecycle-result>span{font:850 9px/1 monospace;letter-spacing:.13em;color:#4e6062}.keeper-lifecycle-source>strong{display:block;margin-top:18px;font-size:18px;word-break:break-word}.keeper-lifecycle-source>small{display:block;margin-top:7px;color:#606864;font-size:11px}.keeper-lifecycle-lines{display:grid;gap:9px;margin-top:28px}.keeper-lifecycle-lines i{height:7px;background:#dce1dc}.keeper-lifecycle-lines i:nth-child(2){width:83%}.keeper-lifecycle-lines i:nth-child(3){width:91%}.keeper-lifecycle-lines i:nth-child(4){width:68%}.keeper-lifecycle-lines i:nth-child(5){width:78%}.keeper-lifecycle-arrow{display:grid;place-items:center;font-size:28px;color:#31565a}.keeper-lifecycle-result h3{font-size:30px;margin:14px 0 18px}.keeper-lifecycle-result dl{margin:0;display:grid}.keeper-lifecycle-result dl>div{display:grid;grid-template-columns:minmax(120px,.42fr) 1fr;gap:18px;padding:12px 0;border-top:1px solid #d6d8d2}.keeper-lifecycle-result dt{font-size:11px;color:#5a6460;font-weight:800}.keeper-lifecycle-result dd{margin:0;font-size:13px;font-weight:750}.keeper-lifecycle-result>p{margin:18px 0 0;padding-top:15px;border-top:1px solid #d6d8d2;color:#5d6661;font-size:11px;line-height:1.55}
.keeper-background-order{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(40px,6vw,86px);align-items:start}.keeper-background-grid{display:grid;gap:1px;background:#bcc4c0;border:1px solid #bcc4c0}.keeper-background-grid article{background:#fbfaf6;padding:22px 23px}.keeper-background-grid b{color:#9b3f24;font:900 9px/1 monospace;letter-spacing:.1em}.keeper-background-grid h3{margin:10px 0 7px;font-size:20px}.keeper-background-grid p{margin:0;color:#55605b;font-size:12px;line-height:1.55}
.keeper-trust-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:32px}.keeper-trust-grid article{border:1px solid #9eaaa5;background:#fbfaf6;padding:23px}.keeper-trust-grid span{color:#31565a;font:900 9px/1 monospace;letter-spacing:.12em}.keeper-trust-grid h3{font-size:19px;margin:12px 0 8px}.keeper-trust-grid p{margin:0;color:#57615d;font-size:12px;line-height:1.6}
.keeper-solution-work{min-height:220px;display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr auto 1.25fr;align-items:center;gap:8px;padding:24px;border:1px solid #8fa0a2;background:#fbfaf6;box-shadow:12px 12px 0 #d2c6b8}.keeper-solution-work span{display:grid;place-items:center;min-height:64px;padding:10px;border:1px solid #bbc6c2;background:#edf1ed;color:#31565a;text-align:center;font:900 8px/1.25 monospace;letter-spacing:.07em}.keeper-solution-work b{color:#9b3f24}
@media (max-width:1100px){.keeper-page-hero--intelligence{grid-template-columns:1fr}.keeper-work-demo{max-width:850px}.keeper-background-order{grid-template-columns:1fr}.keeper-solution-work{min-height:0}}
@media (max-width:760px){.keeper-work-demo{box-shadow:9px 9px 0 #0a1d20}.keeper-work-step{grid-template-columns:28px minmax(0,1fr)}.keeper-work-step em{grid-column:2;justify-self:start}.keeper-value-grid,.keeper-trust-grid{grid-template-columns:1fr}.keeper-lifecycle-grid{grid-template-columns:1fr}.keeper-lifecycle-arrow{transform:rotate(90deg);min-height:32px}.keeper-lifecycle-result dl>div{grid-template-columns:1fr;gap:5px}.keeper-solution-work{grid-template-columns:1fr}.keeper-solution-work b{transform:rotate(90deg);justify-self:center}}
'''


def replace_one(text: str, pattern: str, replacement: str, label: str) -> str:
    new, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"STOP_R96_{label}_COUNT={count}")
    return new


def set_meta(text: str, title: str, desc: str, social_title: str, social_desc: str) -> str:
    text = replace_one(text, r"<title>.*?</title>", f"<title>{title}</title>", "TITLE")
    text = replace_one(text, r'<meta content="[^"]*" name="description"/>', f'<meta content="{desc}" name="description"/>', "DESC")
    text = replace_one(text, r'<meta content="[^"]*" property="og:title"/>', f'<meta content="{social_title}" property="og:title"/>', "OG_TITLE")
    text = replace_one(text, r'<meta content="[^"]*" property="og:description"/>', f'<meta content="{social_desc}" property="og:description"/>', "OG_DESC")
    text = replace_one(text, r'<meta content="[^"]*" name="twitter:title"/>', f'<meta content="{social_title}" name="twitter:title"/>', "TW_TITLE")
    text = replace_one(text, r'<meta content="[^"]*" name="twitter:description"/>', f'<meta content="{social_desc}" name="twitter:description"/>', "TW_DESC")
    return text

for rel, body in KEEPER.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    text = replace_one(text, r'(?<=<main id="content">\n).*?(?=    <section class="ax-share )', body, f"KEEPER_MAIN_{rel}")
    title, desc, st, sd = META[rel]
    text = set_meta(text, title, desc, st, sd)
    text = text.replace('<meta content="R94" name="axiona-release"/>', '<meta content="R96" name="axiona-release"/>')
    path.write_text(text, encoding="utf-8")

for rel, section in OVERVIEW.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    text = replace_one(text, r'    <section class="keeper-preview section-pad">.*?</section>', section, f"OVERVIEW_{rel}")
    text = text.replace('<meta content="R94" name="axiona-release"/>', '<meta content="R96" name="axiona-release"/>')
    path.write_text(text, encoding="utf-8")

for rel, section in SOLUTIONS.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    text = replace_one(text, r'    <section class="development section-pad">.*?</section>', section, f"SOLUTIONS_{rel}")
    text = text.replace('<meta content="R94" name="axiona-release"/>', '<meta content="R96" name="axiona-release"/>')
    path.write_text(text, encoding="utf-8")

css = ROOT / "assets/keeper-r94.css"
css_text = css.read_text(encoding="utf-8")
if "AXIONA R96 — Keeper document-intelligence story." in css_text:
    raise SystemExit("STOP_R96_CSS_ALREADY_PRESENT")
css.write_text(css_text.rstrip() + CSS + "\n", encoding="utf-8")

quality = ROOT / "scripts/verify_public_quality.py"
q = quality.read_text(encoding="utf-8")
old_markers = '''KEEPER_REQUIRED_MARKERS = (\n    'class="keeper-status-badge"',\n    'class="keeper-matter-demo keeper-matter-demo--full"',\n    'class="keeper-scatter-map"',\n    'class="keeper-planned-note"',\n    'class="keeper-folder-tree"',\n    'class="keeper-dev-status section-pad"',\n)'''
new_markers = '''KEEPER_REQUIRED_MARKERS = (\n    'class="keeper-status-badge"',\n    'class="keeper-work-demo"',\n    'class="keeper-value-grid"',\n    'class="keeper-lifecycle-grid"',\n    'class="keeper-background-order section-pad"',\n    'class="keeper-trust-grid"',\n    'class="keeper-dev-status section-pad"',\n)'''
if old_markers not in q:
    raise SystemExit("STOP_R96_QUALITY_MARKERS_NOT_FOUND")
q = q.replace(old_markers, new_markers, 1)
old_solution = '''        solutions_text = solutions.read_text(encoding="utf-8") if solutions.is_file() else ""\n        if 'class="keeper-matter-demo keeper-matter-demo--compact"' not in solutions_text:\n            errors.append(f"Keeper R94 matter demo missing from solutions page: {solutions}")'''
new_solution = '''        solutions_text = solutions.read_text(encoding="utf-8") if solutions.is_file() else ""\n        if 'class="keeper-solution-work"' not in solutions_text:\n            errors.append(f"Keeper R96 processing summary missing from solutions page: {solutions}")\n        if 'class="keeper-matter-demo keeper-matter-demo--compact"' in solutions_text:\n            errors.append(f"Legacy Keeper matter demo remains on solutions page: {solutions}")'''
if old_solution not in q:
    raise SystemExit("STOP_R96_QUALITY_SOLUTION_NOT_FOUND")
q = q.replace(old_solution, new_solution, 1)
old_keeper_css = '''        if "/assets/keeper-r94.css" not in keeper_text:\n            errors.append(f"Keeper R94 product-story stylesheet missing from product page: {keeper}")'''
new_keeper_css = '''        if "/assets/keeper-r94.css" not in keeper_text:\n            errors.append(f"Keeper product-story stylesheet missing from product page: {keeper}")\n        for legacy_marker in ('class="keeper-matter-demo keeper-matter-demo--full"', 'class="keeper-scatter-map"', 'class="keeper-folder-tree"'):\n            if legacy_marker in keeper_text:\n                errors.append(f"Legacy storage-first Keeper story remains in {keeper}: {legacy_marker}")'''
if old_keeper_css not in q:
    raise SystemExit("STOP_R96_QUALITY_KEEPER_NOT_FOUND")
q = q.replace(old_keeper_css, new_keeper_css, 1)
quality.write_text(q, encoding="utf-8")

workflow = ROOT / ".github/workflows/axiona-pages-rebuild.yml"
w = workflow.read_text(encoding="utf-8")
w = w.replace("Verify live social previews and Keeper product story", "Verify live social previews and Keeper R96 product story")
w = w.replace("'keeper-matter-demo keeper-matter-demo--full' <<<\"$KEEPER_HU\"", "'keeper-work-demo' <<<\"$KEEPER_HU\"")
w = w.replace("'melyik ügyhöz tartozik' <<<\"$KEEPER_HU\"", "'A Keeper dolgozik velük' <<<\"$KEEPER_HU\"")
w = w.replace("'which matter it belongs to' <<<\"$KEEPER_EN\"", "'Keeper works on them' <<<\"$KEEPER_EN\"")
w = w.replace("'zu welchem Vorgang es gehört' <<<\"$KEEPER_DE\"", "'Keeper arbeitet mit den Dokumenten' <<<\"$KEEPER_DE\"")
w = w.replace("OK_AXIONA_LIVE_SOCIAL_AND_KEEPER_R94", "OK_AXIONA_LIVE_SOCIAL_AND_KEEPER_R96")
w = w.replace("LIVE_R94_NOT_READY_ATTEMPT", "LIVE_R96_NOT_READY_ATTEMPT")
w = w.replace("STOP_AXIONA_LIVE_R94_NOT_PUBLISHED", "STOP_AXIONA_LIVE_R96_NOT_PUBLISHED")
w = w.replace('"keeper_story": "R94"', '"keeper_story": "R96"')
workflow.write_text(w, encoding="utf-8")

print("OK_KEEPER_INTELLIGENCE_STORY_R96_PATCHED")
