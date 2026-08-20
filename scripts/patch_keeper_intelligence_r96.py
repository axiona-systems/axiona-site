#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('.')

R96_CSS = r'''/* AXIONA R96 — Keeper intelligence-first product story. */
.keeper96-hero{
  display:grid;
  grid-template-columns:minmax(0,.95fr) minmax(430px,1.05fr);
  gap:clamp(48px,6vw,92px);
  align-items:center;
}
.keeper96-hero h1{
  margin:26px 0 0;
  max-width:930px;
  font-size:clamp(48px,5.1vw,84px);
  line-height:.96;
  letter-spacing:-.055em;
}
.keeper96-hero-lead{
  max-width:820px;
  margin:26px 0 0;
  color:#4d514d;
  font-size:clamp(17px,1.25vw,20px);
  line-height:1.68;
}
.keeper96-hero-note{
  margin:18px 0 0;
  max-width:760px;
  color:#626760;
  font-size:13px;
  line-height:1.6;
}
.keeper96-workcard{
  background:#fbfaf6;
  color:var(--ink);
  border:1px solid #89999a;
  box-shadow:14px 14px 0 #d2c6b8;
  overflow:hidden;
}
.keeper96-workcard-head,
.keeper96-preview-head,
.keeper96-mini-head{
  min-height:54px;
  padding:0 20px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:18px;
  border-bottom:1px solid #c9cfca;
  background:#f3f5ef;
}
.keeper96-workcard-head span,
.keeper96-preview-head span,
.keeper96-mini-head span{
  color:#40555a;
  font:900 9px/1 monospace;
  letter-spacing:.15em;
}
.keeper96-workcard-head b,
.keeper96-preview-head b,
.keeper96-mini-head b{
  padding:7px 9px;
  background:var(--navy);
  color:var(--acid);
  font:900 9px/1 monospace;
  letter-spacing:.08em;
}
.keeper96-incoming{
  padding:22px 22px 18px;
  display:grid;
  grid-template-columns:auto 1fr;
  gap:14px;
  align-items:center;
  border-bottom:1px solid #d4d0c8;
  background:#fffdf8;
}
.keeper96-incoming-icon{
  width:48px;
  height:58px;
  display:grid;
  place-items:center;
  border:1px solid #9aa8a6;
  background:#edf1ed;
  color:#31565a;
  font:900 9px/1 monospace;
  letter-spacing:.08em;
}
.keeper96-incoming small{display:block;color:#666e69;font:850 9px/1 monospace;letter-spacing:.11em}
.keeper96-incoming strong{display:block;margin-top:5px;font-size:17px;line-height:1.25}
.keeper96-worklist{padding:7px 20px 8px}
.keeper96-workrow{
  display:grid;
  grid-template-columns:86px minmax(0,1fr);
  gap:14px;
  padding:17px 2px;
  border-bottom:1px solid #ded9d0;
}
.keeper96-workrow:last-child{border-bottom:0}
.keeper96-workrow>span{
  color:#934126;
  font:900 9px/1.35 monospace;
  letter-spacing:.1em;
}
.keeper96-workrow strong{display:block;font-size:15px;line-height:1.32}
.keeper96-workrow p{margin:6px 0 0;color:#59615c;font-size:11px;line-height:1.52}
.keeper96-control{
  padding:17px 20px 19px;
  display:grid;
  grid-template-columns:auto minmax(0,1fr);
  gap:14px;
  align-items:start;
  background:var(--navy);
  color:var(--white);
}
.keeper96-control span{color:var(--acid);font:900 9px/1.35 monospace;letter-spacing:.13em}
.keeper96-control strong{display:block;font-size:14px;line-height:1.38}
.keeper96-control p{margin:5px 0 0;color:#c8d3d3;font-size:11px;line-height:1.5}

.keeper96-core{background:#f3eee6;border-top:1px solid #cfc6bb;border-bottom:1px solid #cfc6bb}
.keeper96-core-head{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:44px;align-items:end}
.keeper96-kicker{margin:0 0 12px;color:#7a3e29;font:900 10px/1 monospace;letter-spacing:.15em}
.keeper96-title{margin:0;font-size:clamp(34px,4vw,62px);line-height:1.02;letter-spacing:-.045em}
.keeper96-core-head>p:last-child{margin:0;color:#535650;font-size:17px;line-height:1.72}
.keeper96-question-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;margin-top:38px;background:#aeb8b4;border:1px solid #aeb8b4}
.keeper96-question{background:#fbfaf6;padding:25px 21px 27px;min-height:190px}
.keeper96-question span{color:#934126;font:900 10px/1 monospace;letter-spacing:.1em}
.keeper96-question h3{margin:18px 0 0;font-size:21px;line-height:1.15;letter-spacing:-.025em}
.keeper96-question p{margin:12px 0 0;color:#555c57;font-size:13px;line-height:1.62}

.keeper96-process-head{max-width:880px}
.keeper96-process-head>p:last-child{margin:18px 0 0;color:#565b56;font-size:17px;line-height:1.7}
.keeper96-process-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:36px}
.keeper96-process-step{border:1px solid #a7b2ae;background:#fbfaf6;padding:24px;min-height:230px}
.keeper96-process-step>span{color:#934126;font:900 11px/1 monospace;letter-spacing:.1em}
.keeper96-process-step h3{margin:18px 0 0;font-size:22px;line-height:1.16;letter-spacing:-.025em}
.keeper96-process-step p{margin:12px 0 0;color:#555c58;font-size:13px;line-height:1.66}
.keeper96-process-step small{display:block;margin-top:16px;padding-top:14px;border-top:1px solid #ddd7ce;color:#596964;font:800 9px/1.45 monospace;letter-spacing:.055em}

.keeper96-contrast{background:var(--navy);color:var(--white)}
.keeper96-contrast .keeper96-kicker{color:var(--acid)}
.keeper96-contrast-head{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:48px;align-items:end}
.keeper96-contrast-head>p:last-child{margin:0;color:#c4d0d0;font-size:17px;line-height:1.72}
.keeper96-compare{margin-top:36px;border:1px solid #476368}
.keeper96-compare-head,.keeper96-compare-row{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}
.keeper96-compare-head{background:#102a2e}
.keeper96-compare-head span{padding:14px 18px;color:#9eb1b3;font:900 9px/1 monospace;letter-spacing:.13em}
.keeper96-compare-head span:last-child{color:var(--acid);border-left:1px solid #476368}
.keeper96-compare-row{border-top:1px solid #476368}
.keeper96-compare-row>div{padding:19px 18px}
.keeper96-compare-row>div:last-child{border-left:1px solid #476368;background:#0d2226}
.keeper96-compare-row strong{display:block;font-size:14px;line-height:1.35}
.keeper96-compare-row p{margin:7px 0 0;color:#aebfc0;font-size:12px;line-height:1.55}
.keeper96-compare-row>div:last-child p{color:#cbd5d5}

.keeper96-examples-head{max-width:930px}
.keeper96-examples-note{margin:16px 0 0;color:#5c625c;font-size:14px;line-height:1.65}
.keeper96-example-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:34px}
.keeper96-example{border:1px solid #a8b2ae;background:#fbfaf6;padding:24px}
.keeper96-example>span{color:#7a3e29;font:900 9px/1 monospace;letter-spacing:.13em}
.keeper96-example h3{margin:17px 0 0;font-size:24px;line-height:1.14;letter-spacing:-.025em}
.keeper96-example p{margin:11px 0 0;color:#555d58;font-size:13px;line-height:1.65}
.keeper96-example-work{margin-top:18px;padding-top:16px;border-top:1px solid #d9d4cb}
.keeper96-example-work b{display:block;margin-bottom:8px;color:#31565a;font:900 9px/1 monospace;letter-spacing:.12em}
.keeper96-example-work ul{margin:0;padding-left:18px;color:#3f4844;font-size:12px;line-height:1.65}

.keeper96-trust{background:#f3eee6;border-top:1px solid #cfc6bb;border-bottom:1px solid #cfc6bb}
.keeper96-trust-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:34px}
.keeper96-trust-card{background:#fbfaf6;border:1px solid #a7b2ae;padding:22px;min-height:190px}
.keeper96-trust-card span{color:#934126;font:900 10px/1 monospace;letter-spacing:.1em}
.keeper96-trust-card h3{margin:16px 0 0;font-size:19px;line-height:1.18}
.keeper96-trust-card p{margin:10px 0 0;color:#555d58;font-size:12px;line-height:1.62}

.keeper96-dev{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:36px;align-items:center}
.keeper96-dev p{max-width:850px;margin:13px 0 0;color:#535a55;font-size:15px;line-height:1.68}
.keeper96-dev-badge{padding:18px 20px;border:1px solid #829294;background:var(--navy);color:var(--white);min-width:260px}
.keeper96-dev-badge span{display:block;color:var(--acid);font:900 9px/1 monospace;letter-spacing:.12em}
.keeper96-dev-badge strong{display:block;margin-top:8px;font-size:16px;line-height:1.35}

.keeper96-preview-panel,.keeper96-mini-process{background:#fbfaf6;color:var(--ink);border:1px solid #89999a;box-shadow:14px 14px 0 #08181b;overflow:hidden}
.keeper96-preview-list,.keeper96-mini-list{padding:7px 20px 8px}
.keeper96-preview-row,.keeper96-mini-row{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;padding:17px 2px;border-bottom:1px solid #ded9d0}
.keeper96-preview-row:last-child,.keeper96-mini-row:last-child{border-bottom:0}
.keeper96-preview-row>span,.keeper96-mini-row>span{color:#934126;font:900 10px/1.35 monospace}
.keeper96-preview-row strong,.keeper96-mini-row strong{display:block;font-size:14px;line-height:1.35}
.keeper96-preview-row p,.keeper96-mini-row p{margin:5px 0 0;color:#59615c;font-size:11px;line-height:1.5}
.keeper96-preview-result,.keeper96-mini-result{padding:17px 20px;background:var(--navy);color:var(--white)}
.keeper96-preview-result span,.keeper96-mini-result span{display:block;color:var(--acid);font:900 9px/1 monospace;letter-spacing:.13em}
.keeper96-preview-result strong,.keeper96-mini-result strong{display:block;margin-top:7px;font-size:15px;line-height:1.4}

@media(max-width:1100px){
  .keeper96-hero{grid-template-columns:1fr}
  .keeper96-workcard{max-width:820px}
  .keeper96-core-head,.keeper96-contrast-head{grid-template-columns:1fr;gap:20px}
  .keeper96-question-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .keeper96-trust-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media(max-width:820px){
  .keeper96-process-grid{grid-template-columns:1fr}
  .keeper96-example-grid{grid-template-columns:1fr}
  .keeper96-dev{grid-template-columns:1fr}
  .keeper96-dev-badge{min-width:0}
}
@media(max-width:620px){
  .keeper96-hero h1{font-size:clamp(42px,12vw,64px)}
  .keeper96-question-grid,.keeper96-trust-grid{grid-template-columns:1fr}
  .keeper96-workrow{grid-template-columns:1fr;gap:7px}
  .keeper96-control{grid-template-columns:1fr;gap:7px}
  .keeper96-compare-head,.keeper96-compare-row{grid-template-columns:1fr}
  .keeper96-compare-head span:last-child,.keeper96-compare-row>div:last-child{border-left:0;border-top:1px solid #476368}
  .keeper96-preview-panel,.keeper96-mini-process,.keeper96-workcard{box-shadow:9px 9px 0 #08181b}
}
'''

SHARE_HU = '''    <section class="ax-share section-pad" data-share-title="AXIONA Keeper | Privát dokumentum-asszisztens" data-share-text="A Keeper célja, hogy a beérkező iratokat felismerje, a fontos adatokat kiemelje, segítsen besorolni, és jelezze a következő teendőt." data-share-url="https://axiona.systems/keeper.html" data-share-copied="Link másolva." data-share-failed="A link másolása nem sikerült."><div class="ax-share-copy"><span class="micro">TOVÁBBADNÁD?</span><h2>Hasznos lehet másnak is?</h2><p>Ha valaki sok irattal, határidővel és hétköznapi ügyintézéssel küzd, innen közvetlenül továbbküldheted a Keeper bemutatóját.</p></div><div class="ax-share-controls"><div class="ax-share-actions"><button class="ax-share-primary" type="button" data-share-native>Megosztás<span>↗</span></button><button class="ax-share-copy-button" type="button" data-share-copy>Link másolása</button></div><div class="ax-share-fallback" data-share-fallback hidden><span>Közvetlen megosztás</span><div class="ax-share-fallback-links"><a data-share-email href="#">E-mail</a><a data-share-linkedin href="#" target="_blank" rel="noopener noreferrer">LinkedIn</a><a data-share-whatsapp href="#" target="_blank" rel="noopener noreferrer">WhatsApp</a></div></div><p class="ax-share-status" data-share-status aria-live="polite"></p></div></section>'''
SHARE_EN = '''    <section class="ax-share section-pad" data-share-title="AXIONA Keeper | Private document assistant" data-share-text="Keeper is designed to recognize incoming documents, surface important information, help classify them and show what needs attention next." data-share-url="https://axiona.systems/en/keeper.html" data-share-copied="Link copied." data-share-failed="Could not copy the link."><div class="ax-share-copy"><span class="micro">SHARE</span><h2>Know someone who might find this useful?</h2><p>If someone you know is dealing with too many documents, deadlines and everyday admin, you can send them the Keeper overview directly.</p></div><div class="ax-share-controls"><div class="ax-share-actions"><button class="ax-share-primary" type="button" data-share-native>Share<span>↗</span></button><button class="ax-share-copy-button" type="button" data-share-copy>Copy link</button></div><div class="ax-share-fallback" data-share-fallback hidden><span>Other options</span><div class="ax-share-fallback-links"><a data-share-email href="#">Email</a><a data-share-linkedin href="#" target="_blank" rel="noopener noreferrer">LinkedIn</a><a data-share-whatsapp href="#" target="_blank" rel="noopener noreferrer">WhatsApp</a></div></div><p class="ax-share-status" data-share-status aria-live="polite"></p></div></section>'''
SHARE_DE = '''    <section class="ax-share section-pad" data-share-title="AXIONA Keeper | Privater Dokumentenassistent" data-share-text="Keeper soll eingehende Dokumente erkennen, wichtige Angaben hervorheben, bei der Zuordnung helfen und den nächsten Handlungsbedarf sichtbar machen." data-share-url="https://axiona.systems/de/keeper.html" data-share-copied="Link kopiert." data-share-failed="Der Link konnte nicht kopiert werden."><div class="ax-share-copy"><span class="micro">WEITEREMPFEHLEN</span><h2>Kennen Sie jemanden, für den das hilfreich sein könnte?</h2><p>Wenn jemand viele Unterlagen, Fristen und alltägliche Verwaltung im Blick behalten muss, können Sie die Keeper-Seite direkt weitergeben.</p></div><div class="ax-share-controls"><div class="ax-share-actions"><button class="ax-share-primary" type="button" data-share-native>Teilen<span>↗</span></button><button class="ax-share-copy-button" type="button" data-share-copy>Link kopieren</button></div><div class="ax-share-fallback" data-share-fallback hidden><span>Weitere Möglichkeiten</span><div class="ax-share-fallback-links"><a data-share-email href="#">E-Mail</a><a data-share-linkedin href="#" target="_blank" rel="noopener noreferrer">LinkedIn</a><a data-share-whatsapp href="#" target="_blank" rel="noopener noreferrer">WhatsApp</a></div></div><p class="ax-share-status" data-share-status aria-live="polite"></p></div></section>'''

KEEPER_MAINS = {
'keeper.html': f'''  <main id="content">
    <section class="keeper96-hero section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>SAJÁT FEJLESZTÉS</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h1>Behozod az iratot. A Keeper elvégzi a rendrakás nagy részét.</h1>
        <p class="keeper96-hero-lead">PDF, kép vagy fotó érkezik. A Keeper célja, hogy elolvassa, felismerje, milyen dokumentumról van szó, kiemelje a fontos adatokat és dátumokat, majd javaslatot tegyen arra, mihez tartozik és van-e vele teendőd. Nem neked kell minden fájlt kézzel végigolvasni, elnevezni és besorolni.</p>
        <p class="keeper96-hero-note">A Keeper javasol és előkészít. A bizonytalan adatokat ellenőrizheted, a következménnyel járó lépések pedig csak a jóváhagyásoddal történhetnek meg.</p>
        <div class="actions"><a class="button button-dark" href="#mit-csinal">Mit csinál a Keeper?<span>↓</span></a><a class="text-link" href="/contact.html">Kapcsolat<span>→</span></a></div>
      </div>
      <aside class="keeper96-workcard" aria-label="Egy beérkező dokumentum feldolgozásának tervezett Keeper-folyamata">
        <div class="keeper96-workcard-head"><span>EGY IRAT ÚTJA A KEEPERBEN</span><b>TERVEZETT MŰKÖDÉS</b></div>
        <div class="keeper96-incoming"><span class="keeper96-incoming-icon">PDF</span><div><small>BEÉRKEZETT</small><strong>Dokumentum.pdf</strong></div></div>
        <div class="keeper96-worklist">
          <div class="keeper96-workrow"><span>01 / ELOLVASSA</span><div><strong>Szöveggé alakítja és feldolgozza.</strong><p>Nem csak a fájlnevet látja: a dokumentum tartalma lesz az alap.</p></div></div>
          <div class="keeper96-workrow"><span>02 / FELISMERI</span><div><strong>Javaslatot készít arra, milyen irat érkezett.</strong><p>Például számla, szerződés, értesítő vagy levél.</p></div></div>
          <div class="keeper96-workrow"><span>03 / KIEMELI</span><div><strong>Kiszedi, ami az ügyintézéshez fontos lehet.</strong><p>Dátum, összeg, azonosító, kibocsátó, határidő — ahol a forrás ezt alátámasztja.</p></div></div>
          <div class="keeper96-workrow"><span>04 / RENDBE TESZI</span><div><strong>Javasolja a kategóriát és a kapcsolatokat.</strong><p>Mihez, kihez vagy melyik ügyhöz tartozhat az irat; a bizonytalan kapcsolat visszakérdezhető.</p></div></div>
          <div class="keeper96-workrow"><span>05 / JELEZ</span><div><strong>Megmutatja, ha valami figyelmet kér.</strong><p>Lehetséges határidő, ellenőrizendő adat vagy következő teendő.</p></div></div>
        </div>
        <div class="keeper96-control"><span>TE DÖNTESZ</span><div><strong>A Keeper nem intéz el következménnyel járó lépést a háttérben.</strong><p>Emlékeztető és más gyakorlati lépés csak ellenőrzés és jóváhagyás után készülhet.</p></div></div>
      </aside>
    </section>

    <section class="keeper96-core section-pad">
      <div class="keeper96-core-head"><div><p class="keeper96-kicker">MIÉRT JÓ EZ NEKED?</p><h2 class="keeper96-title">Nem az a lényeg, hogy megvan a fájl. Hanem hogy értsd is, mi van benne.</h2></div><p>Egy digitális irattár elteszi a dokumentumot. A valódi adminisztráció viszont ezután kezdődik: meg kell érteni, mi érkezett, ki kell szedni belőle a fontos adatot, el kell dönteni, mihez tartozik, és észben kell tartani, ha tenni kell valamit. A Keeper ebből a kézi munkából akar minél többet levenni rólad.</p></div>
      <div class="keeper96-question-grid">
        <article class="keeper96-question"><span>01</span><h3>Mi ez?</h3><p>A Keeper dokumentumtípus-javaslatot készít, hogy ne neked kelljen a fájlnévből kitalálni.</p></article>
        <article class="keeper96-question"><span>02</span><h3>Mi fontos benne?</h3><p>A lényeges adatokat és dátumokat kiemeli, a fontos értékeket pedig forráshoz köti.</p></article>
        <article class="keeper96-question"><span>03</span><h3>Mihez tartozik?</h3><p>Kategóriát és kapcsolatot javasolhat személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy ügyhöz.</p></article>
        <article class="keeper96-question"><span>04</span><h3>Kell vele valamit tennem?</h3><p>Ha határidő vagy következő lépés látszik, a Keeper ezt külön jelzi és teendőt javasolhat.</p></article>
      </div>
    </section>

    <section class="section-pad" id="mit-csinal">
      <div class="keeper96-process-head"><p class="keeper96-kicker">MIT VESZ LE RÓLAD A KEEPER?</p><h2 class="keeper96-title">Te behozod. A feldolgozás nagy részét a rendszer végzi.</h2><p>A tervezett felhasználói út nem mappák építésével kezdődik. Egy dokumentummal kezdődik, amelyből a Keeper lépésről lépésre használható adminisztrációs információt készít.</p></div>
      <div class="keeper96-process-grid">
        <article class="keeper96-process-step"><span>01 / BEHOZATAL</span><h3>PDF, kép, fotó vagy megosztott irat.</h3><p>Nem kell előtte átnevezni, kategóriát választani vagy külön mappát létrehozni.</p><small>TE MŰVELETED: BEHOZOD AZ IRATOT</small></article>
        <article class="keeper96-process-step"><span>02 / HELYI OCR</span><h3>Elolvassa a dokumentumot.</h3><p>A szöveget helyben kinyeri, így a további feldolgozás nem pusztán a fájlnévre támaszkodik.</p><small>KEEPER MUNKÁJA: TARTALOMFELISMERÉS</small></article>
        <article class="keeper96-process-step"><span>03 / MEGÉRTÉS</span><h3>Felismeri, milyen iratról lehet szó.</h3><p>Dokumentumtípus-, kategória- és fontosadat-javaslat készülhet. A bizonytalan eredmény nem válik csendben biztos adattá.</p><small>KEEPER MUNKÁJA: OSZTÁLYOZÁSI JAVASLAT</small></article>
        <article class="keeper96-process-step"><span>04 / FONTOS ADATOK</span><h3>Kiemeli, ami számít.</h3><p>Dátumok, határidők, összegek és más lényeges értékek külön megjelenhetnek, az eredeti forrás visszanézhető.</p><small>KEEPER MUNKÁJA: KINYERÉS + FORRÁS</small></article>
        <article class="keeper96-process-step"><span>05 / RENDEZÉS</span><h3>Javasolja a helyét és a kapcsolatait.</h3><p>A cél nem egyetlen merev mappa, hanem annak felismerése, hogy az irat mihez, kihez vagy melyik ügyhöz tartozik. Az automatikus javaslat javítható és visszafordítható.</p><small>KEEPER MUNKÁJA: KONTEXTUS + BESOROLÁS</small></article>
        <article class="keeper96-process-step"><span>06 / KÖVETKEZŐ LÉPÉS</span><h3>Szól, ha dolgod lehet vele.</h3><p>Határidő, várakozás vagy teendő esetén javaslat jelenhet meg. Emlékeztető csak a jóváhagyásod után készül.</p><small>TE DÖNTESZ: JÓVÁHAGYÁS VAGY JAVÍTÁS</small></article>
      </div>
    </section>

    <section class="keeper96-contrast section-pad">
      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">A KÜLÖNBSÉG</p><h2 class="keeper96-title">Nem a tárolás a termék lényege.</h2></div><p>A fájl megőrzése csak az alap. A Keeper értéke ott kezdődik, amikor a dokumentumból érthető, kereshető és használható ügyintézési információ lesz.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>EGYSZERŰ TÁRHELY</span><span>KEEPER FEJLESZTÉSI IRÁNY</span></div>
        <div class="keeper96-compare-row"><div><strong>Megőrzi a fájlt.</strong><p>A dokumentum ott van, de továbbra is neked kell elolvasni és értelmezni.</p></div><div><strong>Feldolgozza a tartalmát.</strong><p>Felismerési és adatkinyerési javaslatot készít, hogy ne nulláról indulj.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Mappát és fájlnevet mutat.</strong><p>A rend attól függ, mennyire következetesen rendezed kézzel.</p></div><div><strong>Jelentést és kapcsolatot ad a dokumentumnak.</strong><p>Típus, kategória, kapcsolódó személy, szerződés, eszköz vagy ügy lehet a kontextus.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>A fontos dátum bent marad a PDF-ben.</strong><p>Neked kell észrevenni és átírni valahová.</p></div><div><strong>Kiemeli a lehetséges határidőt.</strong><p>A forrás visszanézhető, és emlékeztető csak jóváhagyás után készül.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Keresel egy fájlt.</strong><p>Fájlnévre, helyre vagy saját emlékezetre támaszkodsz.</p></div><div><strong>A dokumentum tartalma is kereshetővé válik.</strong><p>A cél, hogy később ne azt kelljen felidézni, hová mentetted.</p></div></div>
      </div>
    </section>

    <section class="section-pad">
      <div class="keeper96-examples-head"><p class="keeper96-kicker">MIT JELENT EZ A GYAKORLATBAN?</p><h2 class="keeper96-title">Ugyanaz a Keeper-munka, egészen különböző iratoknál.</h2><p class="keeper96-examples-note">Az alábbiak a tervezett termékműködés szemléltető példái. Nem kész felhasználói adatok és nem automatikus döntések.</p></div>
      <div class="keeper96-example-grid">
        <article class="keeper96-example"><span>BIZTOSÍTÓI LEVÉL</span><h3>Ne neked kelljen kibányászni az ügyszámot és a határidőt.</h3><p>Beérkezik egy levél a biztosítótól. A dokumentum önmagában még csak egy PDF.</p><div class="keeper96-example-work"><b>KEEPER MUNKÁJA</b><ul><li>felismeri a dokumentum jellegét</li><li>kiemeli az ügyszámot és a lehetséges határidőt</li><li>javasolja a kapcsolódó kárügyet vagy járművet</li><li>jelzi, ha válasz vagy követés lehet szükséges</li></ul></div></article>
        <article class="keeper96-example"><span>SZÁMLA / FIZETÉSI ÉRTESÍTŐ</span><h3>A határidő ne csak egy sor legyen a dokumentumban.</h3><p>A Keeper a dokumentumból strukturált, ellenőrizhető adatot próbál készíteni.</p><div class="keeper96-example-work"><b>KEEPER MUNKÁJA</b><ul><li>kibocsátó, összeg és dátum javasolt felismerése</li><li>dokumentumtípus és kategória javaslata</li><li>határidő forrásának megmutatása</li><li>emlékeztető-javaslat, amelyet te hagysz jóvá</li></ul></div></article>
        <article class="keeper96-example"><span>SZERZŐDÉS / ELŐFIZETÉS</span><h3>Ne neked kelljen fejben összekötni a régi és az új iratokat.</h3><p>Egy szerződéshez később módosítás, számla vagy új értesítés érkezhet.</p><div class="keeper96-example-work"><b>KEEPER MUNKÁJA</b><ul><li>felismeri a szerződés jellegét és a feleket</li><li>kiemeli a releváns dátumokat</li><li>kapcsolatot javasol a korábbi iratokhoz</li><li>jelzi, ha felülvizsgálat vagy lejárat közeledhet</li></ul></div></article>
        <article class="keeper96-example"><span>INGATLAN / FELÚJÍTÁS</span><h3>Sok különböző iratból egy érthető adminisztrációs kép.</h3><p>Ajánlat, számla, fotó és garancia ugyanahhoz a munkához tartozhat, még ha más formátumban is érkezik.</p><div class="keeper96-example-work"><b>KEEPER MUNKÁJA</b><ul><li>felismeri az eltérő dokumentumtípusokat</li><li>javasolja a közös projekt- vagy ügykapcsolatot</li><li>kiemeli a fontos dátumokat és azonosítókat</li><li>segít később ugyanabból a kontextusból folytatni</li></ul></div></article>
      </div>
    </section>

    <section class="keeper96-trust section-pad">
      <div><p class="keeper96-kicker">BIZALOM ÉS KONTROLL</p><h2 class="keeper96-title">A Keeper segít. Nem dönt helyetted.</h2></div>
      <div class="keeper96-trust-grid">
        <article class="keeper96-trust-card"><span>01</span><h3>Helyi működés az alap.</h3><p>A termék local-first irányra épül: a dokumentumfeldolgozás elsődleges helye a saját készülék.</p></article>
        <article class="keeper96-trust-card"><span>02</span><h3>A fontos adatnak legyen forrása.</h3><p>A cél, hogy lásd, melyik rész alapján került elő egy dátum vagy más fontos érték.</p></article>
        <article class="keeper96-trust-card"><span>03</span><h3>A bizonytalanság látszódjon.</h3><p>Ha valami nem biztos, a Keeper ne tegyen úgy, mintha az lenne. Ellenőrzést kérhet.</p></article>
        <article class="keeper96-trust-card"><span>04</span><h3>A te javításod az első.</h3><p>A felhasználói korrekciót a rendszer nem írhatja felül csendben egy későbbi automatikus javaslattal.</p></article>
      </div>
    </section>

    <section class="keeper-dev-status keeper96-dev section-pad">
      <div><p class="keeper96-kicker">FEJLESZTÉSI STÁTUSZ</p><h2 class="keeper96-title">Elsőként iPhone-ra és iPadre készül.</h2><p>Az AXIONA Keeper fejlesztés alatt áll, jelenleg nem tölthető le. Az első tervezett nyilvános kiadás az Apple App Store-ban jelenik meg. A weboldal a termék célját és tervezett működését mutatja; nem kész alkalmazásként mutatja be.</p></div>
      <div class="keeper96-dev-badge"><span>ELSŐ CÉLPLATFORM</span><strong>iPhone + iPad<br/>Apple App Store</strong></div>
    </section>

{SHARE_HU}
  </main>''',
'en/keeper.html': f'''  <main id="content">
    <section class="keeper96-hero section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>AXIONA PRODUCT</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h1>Bring in the document. Keeper does most of the organising work around it.</h1>
        <p class="keeper96-hero-lead">A PDF, image or photo comes in. Keeper is designed to read it, recognize what kind of document it may be, surface important facts and dates, then suggest what it relates to and whether it needs your attention. You should not have to read, name and classify every file by hand before it becomes useful.</p>
        <p class="keeper96-hero-note">Keeper proposes and prepares. You can review uncertain information, and anything with a real-world consequence remains under your approval.</p>
        <div class="actions"><a class="button button-dark" href="#what-keeper-does">What does Keeper do?<span>↓</span></a><a class="text-link" href="/en/contact.html">Contact<span>→</span></a></div>
      </div>
      <aside class="keeper96-workcard" aria-label="Planned Keeper processing flow for one incoming document">
        <div class="keeper96-workcard-head"><span>ONE DOCUMENT THROUGH KEEPER</span><b>PLANNED EXPERIENCE</b></div>
        <div class="keeper96-incoming"><span class="keeper96-incoming-icon">PDF</span><div><small>ARRIVED</small><strong>Document.pdf</strong></div></div>
        <div class="keeper96-worklist">
          <div class="keeper96-workrow"><span>01 / READ</span><div><strong>Turn the document into usable text.</strong><p>The content, not just the filename, becomes the basis for what happens next.</p></div></div>
          <div class="keeper96-workrow"><span>02 / RECOGNIZE</span><div><strong>Suggest what kind of document arrived.</strong><p>For example an invoice, contract, notice or letter.</p></div></div>
          <div class="keeper96-workrow"><span>03 / EXTRACT</span><div><strong>Surface what may matter for the admin task.</strong><p>Dates, amounts, references, issuer and deadlines where the source supports them.</p></div></div>
          <div class="keeper96-workrow"><span>04 / ORGANIZE</span><div><strong>Suggest category and context.</strong><p>What person, provider, contract, asset or matter the document may belong to; ambiguous links stay reviewable.</p></div></div>
          <div class="keeper96-workrow"><span>05 / FLAG</span><div><strong>Show when something may need attention.</strong><p>A possible deadline, uncertain fact or next action.</p></div></div>
        </div>
        <div class="keeper96-control"><span>YOU DECIDE</span><div><strong>Keeper does not quietly execute consequential actions for you.</strong><p>Reminders and other practical actions require review and approval.</p></div></div>
      </aside>
    </section>

    <section class="keeper96-core section-pad">
      <div class="keeper96-core-head"><div><p class="keeper96-kicker">WHY THIS MATTERS</p><h2 class="keeper96-title">Having the file is not enough. You still need to understand what it means.</h2></div><p>A digital archive can store a document. The admin work starts after that: understand what arrived, pick out the important facts, decide what it belongs to and remember whether something needs to happen. Keeper is designed to remove as much of that manual work as possible.</p></div>
      <div class="keeper96-question-grid">
        <article class="keeper96-question"><span>01</span><h3>What is it?</h3><p>Keeper can propose a document type so you do not have to infer it from a filename.</p></article>
        <article class="keeper96-question"><span>02</span><h3>What matters in it?</h3><p>Important facts and dates can be surfaced, with source evidence behind important values.</p></article>
        <article class="keeper96-question"><span>03</span><h3>What does it belong to?</h3><p>Keeper can suggest category and relationships to a person, provider, contract, asset or matter.</p></article>
        <article class="keeper96-question"><span>04</span><h3>Do I need to do anything?</h3><p>If a deadline or next step is detected, Keeper can flag it separately and propose an action.</p></article>
      </div>
    </section>

    <section class="section-pad" id="what-keeper-does">
      <div class="keeper96-process-head"><p class="keeper96-kicker">WHAT KEEPER TAKES OFF YOUR HANDS</p><h2 class="keeper96-title">You bring the document in. The system does most of the processing.</h2><p>The intended user journey does not begin with building folders. It begins with a document, which Keeper gradually turns into useful, reviewable administrative information.</p></div>
      <div class="keeper96-process-grid">
        <article class="keeper96-process-step"><span>01 / IMPORT</span><h3>PDF, image, photo or shared document.</h3><p>No renaming, pre-classifying or folder building should be required before import.</p><small>YOUR STEP: BRING IN THE DOCUMENT</small></article>
        <article class="keeper96-process-step"><span>02 / LOCAL OCR</span><h3>Read the document.</h3><p>Text is extracted locally so later processing can work from document content rather than filename alone.</p><small>KEEPER WORK: CONTENT RECOGNITION</small></article>
        <article class="keeper96-process-step"><span>03 / UNDERSTAND</span><h3>Recognize what kind of document it may be.</h3><p>Keeper can prepare document-type, category and key-field candidates. Uncertainty must not be silently promoted to certainty.</p><small>KEEPER WORK: CLASSIFICATION PROPOSAL</small></article>
        <article class="keeper96-process-step"><span>04 / IMPORTANT FACTS</span><h3>Surface what matters.</h3><p>Dates, deadlines, amounts and other useful values can be presented separately, with the original source available for review.</p><small>KEEPER WORK: EXTRACTION + SOURCE</small></article>
        <article class="keeper96-process-step"><span>05 / ORGANIZE</span><h3>Suggest where it belongs and what it relates to.</h3><p>The goal is not one rigid folder tree. It is to understand what person, provider, contract, asset or matter gives the document context. Automatic proposals remain editable and reversible.</p><small>KEEPER WORK: CONTEXT + CLASSIFICATION</small></article>
        <article class="keeper96-process-step"><span>06 / NEXT STEP</span><h3>Flag when it may need your attention.</h3><p>A deadline, waiting state or action can become a proposal. A reminder is created only after you approve it.</p><small>YOU DECIDE: APPROVE OR CORRECT</small></article>
      </div>
    </section>

    <section class="keeper96-contrast section-pad">
      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">THE DIFFERENCE</p><h2 class="keeper96-title">Storage is not the product.</h2></div><p>Keeping the file is only the foundation. Keeper becomes useful when a document turns into understandable, searchable and actionable administrative information.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>BASIC STORAGE</span><span>KEEPER PRODUCT DIRECTION</span></div>
        <div class="keeper96-compare-row"><div><strong>Keeps the file.</strong><p>The document exists, but you still have to read and interpret it yourself.</p></div><div><strong>Processes the content.</strong><p>Recognition and extraction proposals help you start from something useful rather than from zero.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Shows folders and filenames.</strong><p>Order depends on how consistently you maintain it by hand.</p></div><div><strong>Gives the document meaning and context.</strong><p>Type, category, related person, contract, asset or matter can become part of the structure.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>The date stays buried in the PDF.</strong><p>You have to notice it and copy it somewhere else.</p></div><div><strong>Surfaces a possible deadline.</strong><p>The source can be reviewed, and reminders remain approval-first.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>You search for a file.</strong><p>You rely on filename, location or memory.</p></div><div><strong>The document content becomes searchable too.</strong><p>The aim is to stop requiring you to remember where you saved it.</p></div></div>
      </div>
    </section>

    <section class="section-pad">
      <div class="keeper96-examples-head"><p class="keeper96-kicker">WHAT THIS LOOKS LIKE IN PRACTICE</p><h2 class="keeper96-title">The same Keeper work across very different documents.</h2><p class="keeper96-examples-note">These are illustrative examples of the planned product experience, not real user data and not automatic decisions.</p></div>
      <div class="keeper96-example-grid">
        <article class="keeper96-example"><span>INSURANCE LETTER</span><h3>Do not make the user dig out the claim number and deadline.</h3><p>An insurer sends a letter. On its own it is still just a PDF.</p><div class="keeper96-example-work"><b>KEEPER WORK</b><ul><li>recognize the kind of document</li><li>surface the reference and possible deadline</li><li>suggest the related claim or vehicle</li><li>flag when a reply or follow-up may be needed</li></ul></div></article>
        <article class="keeper96-example"><span>INVOICE / PAYMENT NOTICE</span><h3>A deadline should not remain just another line in a document.</h3><p>Keeper tries to turn the document into structured, reviewable information.</p><div class="keeper96-example-work"><b>KEEPER WORK</b><ul><li>propose issuer, amount and date recognition</li><li>suggest document type and category</li><li>show where the deadline came from</li><li>propose a reminder that you approve</li></ul></div></article>
        <article class="keeper96-example"><span>CONTRACT / SUBSCRIPTION</span><h3>Do not rely on memory to connect old and new documents.</h3><p>A contract may later receive amendments, invoices or fresh notices.</p><div class="keeper96-example-work"><b>KEEPER WORK</b><ul><li>recognize contract characteristics and parties</li><li>surface relevant dates</li><li>suggest relationships to earlier documents</li><li>flag when review or expiry may be approaching</li></ul></div></article>
        <article class="keeper96-example"><span>PROPERTY / RENOVATION</span><h3>Turn mixed documents into a clearer administrative picture.</h3><p>Quotes, invoices, photos and warranties may belong to the same work even when they arrive in different formats.</p><div class="keeper96-example-work"><b>KEEPER WORK</b><ul><li>recognize different document types</li><li>suggest a shared project or matter context</li><li>surface important dates and references</li><li>help you return later without rebuilding the context</li></ul></div></article>
      </div>
    </section>

    <section class="keeper96-trust section-pad">
      <div><p class="keeper96-kicker">TRUST AND CONTROL</p><h2 class="keeper96-title">Keeper helps. It does not decide for you.</h2></div>
      <div class="keeper96-trust-grid">
        <article class="keeper96-trust-card"><span>01</span><h3>Local-first by design.</h3><p>The product direction puts the device at the centre of document processing rather than treating remote processing as the default.</p></article>
        <article class="keeper96-trust-card"><span>02</span><h3>Important facts need a source.</h3><p>The aim is to show what part of the document supports an extracted date or other important value.</p></article>
        <article class="keeper96-trust-card"><span>03</span><h3>Uncertainty should be visible.</h3><p>If something is not reliable enough, Keeper should ask for review rather than pretend certainty.</p></article>
        <article class="keeper96-trust-card"><span>04</span><h3>Your correction comes first.</h3><p>A later automatic proposal must not quietly overwrite a correction you already made.</p></article>
      </div>
    </section>

    <section class="keeper-dev-status keeper96-dev section-pad">
      <div><p class="keeper96-kicker">DEVELOPMENT STATUS</p><h2 class="keeper96-title">Built first for iPhone and iPad.</h2><p>AXIONA Keeper is in development and is not available for download yet. The first planned public release is through the Apple App Store. This page describes the intended product experience; it does not present the app as finished.</p></div>
      <div class="keeper96-dev-badge"><span>FIRST TARGET PLATFORM</span><strong>iPhone + iPad<br/>Apple App Store</strong></div>
    </section>

{SHARE_EN}
  </main>''',
'de/keeper.html': f'''  <main id="content">
    <section class="keeper96-hero section-pad">
      <div>
        <div class="keeper-product-lockup"><img alt="" height="42" src="/assets/axiona-mark.png" width="42"/><div><strong>AXIONA KEEPER</strong><span>AXIONA PRODUKT</span></div></div>
        <div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h1>Sie geben das Dokument hinein. Keeper liest es, erkennt es und ordnet die Verwaltung vor.</h1>
        <p class="keeper96-hero-lead">Ein PDF, Bild oder Foto kommt herein. Keeper soll den Inhalt lesen, erkennen, um welche Art Dokument es sich handeln könnte, wichtige Angaben und Termine hervorheben und anschließend vorschlagen, wozu es gehört und ob etwas zu tun ist. Sie sollen nicht jede Datei erst vollständig lesen, benennen und manuell einsortieren müssen.</p>
        <p class="keeper96-hero-note">Keeper schlägt vor und bereitet vor. Unsichere Angaben können Sie prüfen; Schritte mit tatsächlichen Folgen bleiben unter Ihrer Freigabe.</p>
        <div class="actions"><a class="button button-dark" href="#was-keeper-macht">Was macht Keeper?<span>↓</span></a><a class="text-link" href="/de/contact.html">Kontakt<span>→</span></a></div>
      </div>
      <aside class="keeper96-workcard" aria-label="Geplanter Keeper-Verarbeitungsweg für ein eingehendes Dokument">
        <div class="keeper96-workcard-head"><span>EIN DOKUMENT DURCH KEEPER</span><b>GEPLANTER ABLAUF</b></div>
        <div class="keeper96-incoming"><span class="keeper96-incoming-icon">PDF</span><div><small>EINGEGANGEN</small><strong>Dokument.pdf</strong></div></div>
        <div class="keeper96-worklist">
          <div class="keeper96-workrow"><span>01 / LESEN</span><div><strong>Inhalt in nutzbaren Text umwandeln.</strong><p>Die Grundlage ist der Dokumentinhalt, nicht nur der Dateiname.</p></div></div>
          <div class="keeper96-workrow"><span>02 / ERKENNEN</span><div><strong>Vorschlagen, welche Dokumentart eingegangen ist.</strong><p>Zum Beispiel Rechnung, Vertrag, Mitteilung oder Schreiben.</p></div></div>
          <div class="keeper96-workrow"><span>03 / HERVORHEBEN</span><div><strong>Wichtige Verwaltungsdaten herausziehen.</strong><p>Datum, Betrag, Referenz, Absender oder Frist — sofern die Quelle dies trägt.</p></div></div>
          <div class="keeper96-workrow"><span>04 / ORDNEN</span><div><strong>Kategorie und Zusammenhang vorschlagen.</strong><p>Zu welcher Person, welchem Anbieter, Vertrag, Gegenstand oder Vorgang das Dokument gehören könnte; unklare Zuordnungen bleiben prüfbar.</p></div></div>
          <div class="keeper96-workrow"><span>05 / HINWEIS</span><div><strong>Zeigen, wenn etwas Aufmerksamkeit braucht.</strong><p>Eine mögliche Frist, unsichere Angabe oder ein nächster Schritt.</p></div></div>
        </div>
        <div class="keeper96-control"><span>SIE ENTSCHEIDEN</span><div><strong>Keeper führt keine folgenreichen Schritte unbemerkt im Hintergrund aus.</strong><p>Erinnerungen und andere praktische Schritte benötigen Prüfung und Freigabe.</p></div></div>
      </aside>
    </section>

    <section class="keeper96-core section-pad">
      <div class="keeper96-core-head"><div><p class="keeper96-kicker">WARUM DAS HILFT</p><h2 class="keeper96-title">Dass die Datei gespeichert ist, reicht nicht. Sie müssen auch verstehen, was darin steckt.</h2></div><p>Ein digitales Archiv kann ein Dokument aufbewahren. Die eigentliche Verwaltung beginnt danach: verstehen, was eingegangen ist, wichtige Angaben herausziehen, den Zusammenhang erkennen und daran denken, ob etwas zu tun ist. Keeper soll Ihnen möglichst viel dieser Handarbeit abnehmen.</p></div>
      <div class="keeper96-question-grid">
        <article class="keeper96-question"><span>01</span><h3>Was ist das?</h3><p>Keeper kann eine Dokumentart vorschlagen, damit Sie sie nicht aus dem Dateinamen erraten müssen.</p></article>
        <article class="keeper96-question"><span>02</span><h3>Was ist wichtig?</h3><p>Wichtige Angaben und Termine können hervorgehoben und wichtige Werte mit ihrer Quelle verbunden werden.</p></article>
        <article class="keeper96-question"><span>03</span><h3>Wozu gehört es?</h3><p>Keeper kann Kategorie und Beziehungen zu Person, Anbieter, Vertrag, Gegenstand oder Vorgang vorschlagen.</p></article>
        <article class="keeper96-question"><span>04</span><h3>Muss ich etwas tun?</h3><p>Wenn eine Frist oder ein nächster Schritt erkannt wird, kann Keeper darauf gesondert hinweisen.</p></article>
      </div>
    </section>

    <section class="section-pad" id="was-keeper-macht">
      <div class="keeper96-process-head"><p class="keeper96-kicker">WAS KEEPER IHNEN ABNIMMT</p><h2 class="keeper96-title">Sie bringen das Dokument hinein. Das System übernimmt den größten Teil der Verarbeitung.</h2><p>Der geplante Nutzerweg beginnt nicht mit dem Anlegen von Ordnern. Er beginnt mit einem Dokument, das Keeper Schritt für Schritt in nutzbare, prüfbare Verwaltungsinformation überführt.</p></div>
      <div class="keeper96-process-grid">
        <article class="keeper96-process-step"><span>01 / IMPORT</span><h3>PDF, Bild, Foto oder geteiltes Dokument.</h3><p>Vorheriges Umbenennen, Vorkategorisieren oder Anlegen eines Ordners soll nicht nötig sein.</p><small>IHR SCHRITT: DOKUMENT HINZUFÜGEN</small></article>
        <article class="keeper96-process-step"><span>02 / LOKALE OCR</span><h3>Dokument lesen.</h3><p>Text wird lokal extrahiert, damit die weitere Verarbeitung auf dem Inhalt und nicht nur auf dem Dateinamen basiert.</p><small>KEEPER-ARBEIT: INHALTSERKENNUNG</small></article>
        <article class="keeper96-process-step"><span>03 / VERSTEHEN</span><h3>Erkennen, welche Art Dokument vorliegen könnte.</h3><p>Keeper kann Vorschläge zu Dokumentart, Kategorie und wichtigen Feldern vorbereiten. Unsicherheit darf nicht stillschweigend zu Gewissheit werden.</p><small>KEEPER-ARBEIT: KLASSIFIZIERUNGSVORSCHLAG</small></article>
        <article class="keeper96-process-step"><span>04 / WICHTIGE ANGABEN</span><h3>Hervorheben, was zählt.</h3><p>Daten, Fristen, Beträge und andere relevante Werte können getrennt angezeigt werden; die Originalquelle bleibt prüfbar.</p><small>KEEPER-ARBEIT: EXTRAKTION + QUELLE</small></article>
        <article class="keeper96-process-step"><span>05 / ORDNEN</span><h3>Vorschlagen, wohin es gehört und womit es zusammenhängt.</h3><p>Ziel ist nicht ein starres Ordnersystem, sondern der richtige Kontext: Person, Anbieter, Vertrag, Gegenstand oder Vorgang. Automatische Vorschläge bleiben änderbar und umkehrbar.</p><small>KEEPER-ARBEIT: KONTEXT + ZUORDNUNG</small></article>
        <article class="keeper96-process-step"><span>06 / NÄCHSTER SCHRITT</span><h3>Zeigen, wenn Handlungsbedarf bestehen könnte.</h3><p>Frist, Wartezustand oder Aufgabe können als Vorschlag erscheinen. Eine Erinnerung entsteht erst nach Ihrer Freigabe.</p><small>SIE ENTSCHEIDEN: FREIGEBEN ODER KORRIGIEREN</small></article>
      </div>
    </section>

    <section class="keeper96-contrast section-pad">
      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">DER UNTERSCHIED</p><h2 class="keeper96-title">Speichern ist nicht der Kern des Produkts.</h2></div><p>Die Datei aufzubewahren ist nur die Grundlage. Keeper wird dort wertvoll, wo aus einem Dokument verständliche, durchsuchbare und nutzbare Verwaltungsinformation wird.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>EINFACHER SPEICHER</span><span>KEEPER PRODUKTRICHTUNG</span></div>
        <div class="keeper96-compare-row"><div><strong>Bewahrt die Datei auf.</strong><p>Das Dokument ist vorhanden, aber Sie müssen es weiterhin selbst lesen und einordnen.</p></div><div><strong>Verarbeitet den Inhalt.</strong><p>Erkennungs- und Extraktionsvorschläge geben Ihnen einen brauchbaren Ausgangspunkt.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Zeigt Ordner und Dateinamen.</strong><p>Die Ordnung hängt davon ab, wie konsequent Sie sie manuell pflegen.</p></div><div><strong>Gibt dem Dokument Bedeutung und Kontext.</strong><p>Dokumentart, Kategorie und Bezug zu Person, Vertrag, Gegenstand oder Vorgang können Teil der Struktur werden.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Das wichtige Datum bleibt im PDF verborgen.</strong><p>Sie müssen es bemerken und separat übertragen.</p></div><div><strong>Hebt eine mögliche Frist hervor.</strong><p>Die Quelle bleibt prüfbar; Erinnerungen bleiben freigabepflichtig.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Sie suchen eine Datei.</strong><p>Sie verlassen sich auf Dateiname, Speicherort oder Erinnerung.</p></div><div><strong>Auch der Dokumentinhalt wird auffindbar.</strong><p>Ziel ist, dass Sie später nicht mehr wissen müssen, wo Sie etwas abgelegt haben.</p></div></div>
      </div>
    </section>

    <section class="section-pad">
      <div class="keeper96-examples-head"><p class="keeper96-kicker">WIE DAS PRAKTISCH AUSSIEHT</p><h2 class="keeper96-title">Die gleiche Keeper-Arbeit bei ganz unterschiedlichen Dokumenten.</h2><p class="keeper96-examples-note">Die folgenden Beispiele veranschaulichen die geplante Produktfunktion. Es sind keine echten Nutzerdaten und keine automatischen Entscheidungen.</p></div>
      <div class="keeper96-example-grid">
        <article class="keeper96-example"><span>VERSICHERUNGSSCHREIBEN</span><h3>Nicht selbst Aktenzeichen und Frist aus dem Schreiben herausziehen müssen.</h3><p>Ein Schreiben der Versicherung kommt an. Zunächst ist es nur eine PDF-Datei.</p><div class="keeper96-example-work"><b>KEEPER-ARBEIT</b><ul><li>Art des Dokuments erkennen</li><li>Referenz und mögliche Frist hervorheben</li><li>zugehörigen Schadenfall oder Fahrzeug vorschlagen</li><li>auf mögliche Antwort oder Nachverfolgung hinweisen</li></ul></div></article>
        <article class="keeper96-example"><span>RECHNUNG / ZAHLUNGSHINWEIS</span><h3>Eine Frist soll nicht nur eine Zeile im Dokument bleiben.</h3><p>Keeper versucht, aus dem Dokument strukturierte, prüfbare Information zu machen.</p><div class="keeper96-example-work"><b>KEEPER-ARBEIT</b><ul><li>Absender, Betrag und Datum als Kandidaten erkennen</li><li>Dokumentart und Kategorie vorschlagen</li><li>Quelle der Frist sichtbar machen</li><li>Erinnerung vorschlagen, die Sie freigeben</li></ul></div></article>
        <article class="keeper96-example"><span>VERTRAG / ABONNEMENT</span><h3>Alte und neue Unterlagen nicht im Kopf zusammenführen müssen.</h3><p>Zu einem Vertrag können später Änderungen, Rechnungen oder neue Mitteilungen kommen.</p><div class="keeper96-example-work"><b>KEEPER-ARBEIT</b><ul><li>Vertragsmerkmale und Parteien erkennen</li><li>relevante Termine hervorheben</li><li>Beziehungen zu früheren Dokumenten vorschlagen</li><li>auf mögliche Prüfung oder Ablauf hinweisen</li></ul></div></article>
        <article class="keeper96-example"><span>IMMOBILIE / RENOVIERUNG</span><h3>Aus verschiedenen Unterlagen ein verständlicheres Verwaltungsbild machen.</h3><p>Angebote, Rechnungen, Fotos und Garantien können zur gleichen Arbeit gehören, obwohl sie in verschiedenen Formaten eintreffen.</p><div class="keeper96-example-work"><b>KEEPER-ARBEIT</b><ul><li>unterschiedliche Dokumentarten erkennen</li><li>gemeinsamen Projekt- oder Vorgangskontext vorschlagen</li><li>wichtige Termine und Referenzen hervorheben</li><li>später im vorhandenen Kontext weiterarbeiten helfen</li></ul></div></article>
      </div>
    </section>

    <section class="keeper96-trust section-pad">
      <div><p class="keeper96-kicker">VERTRAUEN UND KONTROLLE</p><h2 class="keeper96-title">Keeper hilft. Entscheiden tun Sie.</h2></div>
      <div class="keeper96-trust-grid">
        <article class="keeper96-trust-card"><span>01</span><h3>Local-first als Grundlage.</h3><p>Die Produktrichtung stellt das eigene Gerät in den Mittelpunkt der Dokumentverarbeitung, statt entfernte Verarbeitung zum Standard zu machen.</p></article>
        <article class="keeper96-trust-card"><span>02</span><h3>Wichtige Angaben brauchen eine Quelle.</h3><p>Ziel ist, sichtbar zu machen, welcher Teil des Dokuments ein extrahiertes Datum oder einen anderen wichtigen Wert stützt.</p></article>
        <article class="keeper96-trust-card"><span>03</span><h3>Unsicherheit muss sichtbar bleiben.</h3><p>Wenn etwas nicht zuverlässig genug ist, soll Keeper eine Prüfung verlangen statt Sicherheit vorzutäuschen.</p></article>
        <article class="keeper96-trust-card"><span>04</span><h3>Ihre Korrektur hat Vorrang.</h3><p>Ein späterer automatischer Vorschlag darf eine bereits von Ihnen korrigierte Angabe nicht still überschreiben.</p></article>
      </div>
    </section>

    <section class="keeper-dev-status keeper96-dev section-pad">
      <div><p class="keeper96-kicker">ENTWICKLUNGSSTATUS</p><h2 class="keeper96-title">Zuerst für iPhone und iPad.</h2><p>AXIONA Keeper befindet sich in Entwicklung und kann noch nicht heruntergeladen werden. Die erste geplante öffentliche Veröffentlichung erfolgt über den Apple App Store. Diese Seite beschreibt die angestrebte Produkterfahrung und stellt die App nicht als fertig dar.</p></div>
      <div class="keeper96-dev-badge"><span>ERSTE ZIELPLATTFORM</span><strong>iPhone + iPad<br/>Apple App Store</strong></div>
    </section>

{SHARE_DE}
  </main>'''
}

OVERVIEWS = {
'index.html': '''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h2>AXIONA Keeper<span>Nem neked kell minden iratot kibogarászni és kézzel elrendezni.</span></h2>
        <p class="keeper-preview-lead">Behozol egy PDF-et, képet vagy fotót. A Keeper célja, hogy elolvassa, felismerje, milyen iratról van szó, kiemelje a fontos adatokat, segítsen besorolni és összekapcsolni azzal, amihez tartozik, majd jelezze, ha valami figyelmet kér. A fontos döntés nálad marad.</p>
        <div class="actions"><a class="button button-dark" href="/keeper.html">A Keeper megismerése<span>→</span></a><a class="text-link" href="/keeper.html#mit-csinal">Mit csinál a háttérben?<span>↗</span></a></div>
      </div>
      <aside class="keeper96-preview-panel" aria-label="Mit vesz le a Keeper a felhasználóról?">
        <div class="keeper96-preview-head"><span>MIT VESZ LE RÓLAD?</span><b>RÖVIDEN</b></div>
        <div class="keeper96-preview-list">
          <div class="keeper96-preview-row"><span>01</span><div><strong>Elolvassa.</strong><p>A tartalommal dolgozik, nem csak a fájlnévvel.</p></div></div>
          <div class="keeper96-preview-row"><span>02</span><div><strong>Felismeri és kiemeli.</strong><p>Dokumentumtípus, fontos adatok, dátumok és lehetséges határidők.</p></div></div>
          <div class="keeper96-preview-row"><span>03</span><div><strong>Rendbe teszi.</strong><p>Kategóriát és kapcsolatot javasol ahhoz, amihez az irat tartozik.</p></div></div>
          <div class="keeper96-preview-row"><span>04</span><div><strong>Jelzi, ha dolgod lehet vele.</strong><p>A következő lépés javaslat marad; te ellenőrzöd és hagyod jóvá.</p></div></div>
        </div>
        <div class="keeper96-preview-result"><span>EREDMÉNY</span><strong>Kevesebb kézi adminisztráció. Kevesebb bizonytalanság.</strong></div>
      </aside>
    </section>''',
'en/index.html': '''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h2>AXIONA Keeper<span>You should not have to decode and organize every document by hand.</span></h2>
        <p class="keeper-preview-lead">Bring in a PDF, image or photo. Keeper is designed to read it, recognize what kind of document it may be, surface important information, help classify and connect it to the right context, then flag when something may need your attention. Important decisions remain yours.</p>
        <div class="actions"><a class="button button-dark" href="/en/keeper.html">Explore Keeper<span>→</span></a><a class="text-link" href="/en/keeper.html#what-keeper-does">What happens behind the scenes?<span>↗</span></a></div>
      </div>
      <aside class="keeper96-preview-panel" aria-label="What work Keeper takes off your hands">
        <div class="keeper96-preview-head"><span>WHAT IT TAKES OFF YOUR HANDS</span><b>IN SHORT</b></div>
        <div class="keeper96-preview-list">
          <div class="keeper96-preview-row"><span>01</span><div><strong>Reads it.</strong><p>Works from the content, not just the filename.</p></div></div>
          <div class="keeper96-preview-row"><span>02</span><div><strong>Recognizes and surfaces.</strong><p>Document type, key facts, dates and possible deadlines.</p></div></div>
          <div class="keeper96-preview-row"><span>03</span><div><strong>Organizes it.</strong><p>Suggests category and relationships to the context the document belongs to.</p></div></div>
          <div class="keeper96-preview-row"><span>04</span><div><strong>Flags when it may need action.</strong><p>The next step remains a proposal for you to review and approve.</p></div></div>
        </div>
        <div class="keeper96-preview-result"><span>RESULT</span><strong>Less manual admin. Less uncertainty.</strong></div>
      </aside>
    </section>''',
'de/index.html': '''    <section class="keeper-preview section-pad">
      <div class="keeper-preview-copy">
        <div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div>
        <h2>AXIONA Keeper<span>Sie sollten nicht jedes Dokument selbst lesen, verstehen und manuell einsortieren müssen.</span></h2>
        <p class="keeper-preview-lead">Sie bringen ein PDF, Bild oder Foto hinein. Keeper soll den Inhalt lesen, die Dokumentart erkennen, wichtige Angaben hervorheben, bei Zuordnung und Zusammenhang helfen und zeigen, wenn etwas Aufmerksamkeit braucht. Wichtige Entscheidungen bleiben bei Ihnen.</p>
        <div class="actions"><a class="button button-dark" href="/de/keeper.html">Keeper kennenlernen<span>→</span></a><a class="text-link" href="/de/keeper.html#was-keeper-macht">Was passiert im Hintergrund?<span>↗</span></a></div>
      </div>
      <aside class="keeper96-preview-panel" aria-label="Welche Arbeit Keeper Ihnen abnimmt">
        <div class="keeper96-preview-head"><span>WAS KEEPER IHNEN ABNIMMT</span><b>KURZ</b></div>
        <div class="keeper96-preview-list">
          <div class="keeper96-preview-row"><span>01</span><div><strong>Lesen.</strong><p>Der Inhalt zählt, nicht nur der Dateiname.</p></div></div>
          <div class="keeper96-preview-row"><span>02</span><div><strong>Erkennen und hervorheben.</strong><p>Dokumentart, wichtige Angaben, Termine und mögliche Fristen.</p></div></div>
          <div class="keeper96-preview-row"><span>03</span><div><strong>Ordnen.</strong><p>Kategorie und Beziehungen zum passenden Kontext vorschlagen.</p></div></div>
          <div class="keeper96-preview-row"><span>04</span><div><strong>Handlungsbedarf sichtbar machen.</strong><p>Der nächste Schritt bleibt ein Vorschlag, den Sie prüfen und freigeben.</p></div></div>
        </div>
        <div class="keeper96-preview-result"><span>ERGEBNIS</span><strong>Weniger manuelle Verwaltung. Weniger Unsicherheit.</strong></div>
      </aside>
    </section>'''
}

SOLUTIONS = {
'solutions.html': '''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">05 / SAJÁT FEJLESZTÉS</p><h2>AXIONA Keeper</h2><p>Privát dokumentum-asszisztens, amely nem csak megőrzi az iratot, hanem segít megérteni és elrendezni.</p></header>
      <article class="keeper-solutions-card">
        <div><div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Behozod az iratot. A Keeper dolgozik rajta.</h3><p>A cél: elolvasni a dokumentumot, felismerni a típusát, kiemelni a fontos adatokat és határidőket, javasolni a megfelelő kategóriát és kapcsolatot, majd megmutatni, ha teendő van vele. Nem egyszerű tárhely, hanem a kézi adminisztráció csökkentésére épülő rendszer.</p><a class="text-link" href="/keeper.html">Részletes Keeper-bemutató<span>→</span></a></div>
        <aside class="keeper96-mini-process" aria-label="A Keeper tervezett dokumentumfeldolgozási munkája"><div class="keeper96-mini-head"><span>MIT CSINÁL A KEEPER?</span><b>5 LÉPÉS</b></div><div class="keeper96-mini-list"><div class="keeper96-mini-row"><span>01</span><div><strong>Elolvassa</strong><p>helyi OCR-rel feldolgozza a tartalmat</p></div></div><div class="keeper96-mini-row"><span>02</span><div><strong>Felismeri</strong><p>dokumentumtípus- és kategóriajavaslat</p></div></div><div class="keeper96-mini-row"><span>03</span><div><strong>Kiemeli</strong><p>fontos adatok, dátumok, lehetséges határidők</p></div></div><div class="keeper96-mini-row"><span>04</span><div><strong>Rendbe teszi</strong><p>kapcsolatot és kontextust javasol</p></div></div><div class="keeper96-mini-row"><span>05</span><div><strong>Jelez</strong><p>ha valami ellenőrzést vagy teendőt kér</p></div></div></div><div class="keeper96-mini-result"><span>KONTROLL</span><strong>A fontos lépéseket te hagyod jóvá.</strong></div></aside>
      </article>
    </section>''',
'en/solutions.html': '''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">05 / OWN PRODUCT</p><h2>AXIONA Keeper</h2><p>A private document assistant designed to understand and organize documents, not merely store them.</p></header>
      <article class="keeper-solutions-card">
        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Bring in the document. Keeper works on it.</h3><p>The goal is to read the document, recognize its type, surface important facts and deadlines, suggest the right category and context, then show when something may need attention. It is designed to reduce manual admin rather than behave like another storage service.</p><a class="text-link" href="/en/keeper.html">Detailed Keeper overview<span>→</span></a></div>
        <aside class="keeper96-mini-process" aria-label="Keeper planned document-processing work"><div class="keeper96-mini-head"><span>WHAT DOES KEEPER DO?</span><b>5 STEPS</b></div><div class="keeper96-mini-list"><div class="keeper96-mini-row"><span>01</span><div><strong>Reads</strong><p>processes document content locally</p></div></div><div class="keeper96-mini-row"><span>02</span><div><strong>Recognizes</strong><p>document-type and category proposals</p></div></div><div class="keeper96-mini-row"><span>03</span><div><strong>Surfaces</strong><p>important facts, dates and possible deadlines</p></div></div><div class="keeper96-mini-row"><span>04</span><div><strong>Organizes</strong><p>suggests relationships and context</p></div></div><div class="keeper96-mini-row"><span>05</span><div><strong>Flags</strong><p>when something may need review or action</p></div></div></div><div class="keeper96-mini-result"><span>CONTROL</span><strong>You approve the important steps.</strong></div></aside>
      </article>
    </section>''',
'de/solutions.html': '''    <section class="development section-pad">
      <header class="section-intro"><p class="eyebrow">05 / EIGENE ENTWICKLUNG</p><h2>AXIONA Keeper</h2><p>Ein privater Dokumentenassistent, der Unterlagen verstehen und einordnen soll — nicht nur speichern.</p></header>
      <article class="keeper-solutions-card">
        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Dokument hinein. Keeper arbeitet damit.</h3><p>Ziel ist, das Dokument zu lesen, die Art zu erkennen, wichtige Angaben und Fristen hervorzuheben, Kategorie und Kontext vorzuschlagen und zu zeigen, wenn etwas Aufmerksamkeit braucht. Keeper soll manuelle Verwaltung reduzieren, statt nur ein weiterer Speicherort zu sein.</p><a class="text-link" href="/de/keeper.html">Keeper im Detail<span>→</span></a></div>
        <aside class="keeper96-mini-process" aria-label="Geplante Dokumentenverarbeitung durch Keeper"><div class="keeper96-mini-head"><span>WAS MACHT KEEPER?</span><b>5 SCHRITTE</b></div><div class="keeper96-mini-list"><div class="keeper96-mini-row"><span>01</span><div><strong>Lesen</strong><p>Dokumentinhalt lokal verarbeiten</p></div></div><div class="keeper96-mini-row"><span>02</span><div><strong>Erkennen</strong><p>Dokumentart und Kategorie vorschlagen</p></div></div><div class="keeper96-mini-row"><span>03</span><div><strong>Hervorheben</strong><p>wichtige Angaben, Termine und mögliche Fristen</p></div></div><div class="keeper96-mini-row"><span>04</span><div><strong>Ordnen</strong><p>Beziehungen und Kontext vorschlagen</p></div></div><div class="keeper96-mini-row"><span>05</span><div><strong>Hinweisen</strong><p>wenn Prüfung oder Handlung nötig sein könnte</p></div></div></div><div class="keeper96-mini-result"><span>KONTROLLE</span><strong>Wichtige Schritte geben Sie frei.</strong></div></aside>
      </article>
    </section>'''
}

META = {
'keeper.html': {
 'title':'AXIONA Keeper | Privát dokumentum-asszisztens',
 'description':'Az AXIONA Keeper fejlesztés alatt álló, local-first dokumentum-asszisztens: iratfelismerés, fontos adatok és határidők kiemelése, besorolási és teendő-javaslatok.',
 'og_title':'AXIONA Keeper | Privát dokumentum-asszisztens',
 'og_description':'A Keeper célja, hogy a beérkező iratokat felismerje, a fontos adatokat kiemelje, segítsen besorolni, és jelezze a következő teendőt.'
},
'en/keeper.html': {
 'title':'AXIONA Keeper | Private document assistant',
 'description':'AXIONA Keeper is a local-first document assistant in development for document recognition, important facts and deadlines, classification and reviewable next-step proposals.',
 'og_title':'AXIONA Keeper | Private document assistant',
 'og_description':'Keeper is designed to recognize incoming documents, surface important information, help classify them and show what may need attention next.'
},
'de/keeper.html': {
 'title':'AXIONA Keeper | Privater Dokumentenassistent',
 'description':'AXIONA Keeper ist ein local-first Dokumentenassistent in Entwicklung: Dokumenterkennung, wichtige Angaben und Fristen, Zuordnung und prüfbare Vorschläge für nächste Schritte.',
 'og_title':'AXIONA Keeper | Privater Dokumentenassistent',
 'og_description':'Keeper soll eingehende Dokumente erkennen, wichtige Angaben hervorheben, bei der Zuordnung helfen und den nächsten Handlungsbedarf sichtbar machen.'
}
}


def replace_once(text, pattern, replacement, label, flags=re.S):
    out, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise SystemExit(f'STOP_R96_REPLACE {label} count={count}')
    return out

# Create R96 stylesheet.
css_path = ROOT / 'assets/keeper-r96.css'
if css_path.exists():
    raise SystemExit('STOP_R96_CSS_ALREADY_EXISTS')
css_path.write_text(R96_CSS, encoding='utf-8')

# Keeper product pages: complete main-story replacement + metadata.
for rel, main_html in KEEPER_MAINS.items():
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    text = replace_once(text, r'  <main id="content">.*?  </main>', main_html, f'{rel}:main')
    meta = META[rel]
    text = replace_once(text, r'<title>.*?</title>', f'<title>{meta["title"]}</title>', f'{rel}:title')
    text = replace_once(text, r'<meta content="[^"]*" name="description"/>', f'<meta content="{meta["description"]}" name="description"/>', f'{rel}:description')
    text = replace_once(text, r'<meta content="[^"]*" property="og:title"/>', f'<meta content="{meta["og_title"]}" property="og:title"/>', f'{rel}:og-title')
    text = replace_once(text, r'<meta content="[^"]*" property="og:description"/>', f'<meta content="{meta["og_description"]}" property="og:description"/>', f'{rel}:og-description')
    text = replace_once(text, r'<meta content="[^"]*" name="twitter:title"/>', f'<meta content="{meta["og_title"]}" name="twitter:title"/>', f'{rel}:tw-title')
    text = replace_once(text, r'<meta content="[^"]*" name="twitter:description"/>', f'<meta content="{meta["og_description"]}" name="twitter:description"/>', f'{rel}:tw-description')
    path.write_text(text, encoding='utf-8')

# Overview and Solutions entry points.
section_pattern = r'    <section class="keeper-preview section-pad">.*?    </section>'
for rel, replacement in OVERVIEWS.items():
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    text = replace_once(text, section_pattern, replacement, f'{rel}:overview')
    path.write_text(text, encoding='utf-8')

solutions_pattern = r'    <section class="development section-pad">.*?    </section>'
for rel, replacement in SOLUTIONS.items():
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    text = replace_once(text, solutions_pattern, replacement, f'{rel}:solutions')
    path.write_text(text, encoding='utf-8')

PUBLIC_ENTRY_FILES = list(KEEPER_MAINS) + list(OVERVIEWS) + list(SOLUTIONS)
for rel in PUBLIC_ENTRY_FILES:
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    if '/assets/keeper-r96.css' not in text:
        text = replace_once(text, r'(<link href="/assets/keeper-r94.css" rel="stylesheet"/>)', r'\1\n  <link href="/assets/keeper-r96.css" rel="stylesheet"/>', f'{rel}:css-link')
    text = re.sub(r'<meta content="R9[45]" name="axiona-release"/>', '<meta content="R96" name="axiona-release"/>', text, count=1)
    path.write_text(text, encoding='utf-8')

# Quality gate: R96 is now the public Keeper story authority.
gate_path = ROOT / 'scripts/verify_public_quality.py'
gate = gate_path.read_text(encoding='utf-8')
gate = replace_once(
    gate,
    r'KEEPER_REQUIRED_MARKERS = \(.*?\)\nKEEPER_PLATFORM_MARKERS',
    '''KEEPER_REQUIRED_MARKERS = (\n    'class="keeper-status-badge"',\n    'class="keeper96-workcard"',\n    'class="keeper96-process-grid"',\n    'class="keeper96-compare"',\n    'class="keeper96-example-grid"',\n    'class="keeper96-trust-grid"',\n    'class="keeper-dev-status keeper96-dev section-pad"',\n)\nKEEPER_PLATFORM_MARKERS''',
    'gate:markers'
)
entry_pattern = r'''        for source in \(homepage, solutions\):.*?        keeper_text = keeper\.read_text\(encoding="utf-8"\) if keeper\.is_file\(\) else ""'''
entry_replacement = '''        for source in (homepage, solutions):\n            text = source.read_text(encoding="utf-8") if source.is_file() else ""\n            if f'href="{keeper_href}"' not in text:\n                errors.append(f"Keeper product entry link missing in {source}: {keeper_href}")\n            for stylesheet in ("/assets/keeper-r87.css", "/assets/keeper-r94.css", "/assets/keeper-r96.css"):\n                if stylesheet not in text:\n                    errors.append(f"Keeper stylesheet missing from product entry page: {source}: {stylesheet}")\n            for marker in KEEPER_PLATFORM_MARKERS:\n                if marker not in text:\n                    errors.append(f"Keeper platform marker missing in {source}: {marker}")\n\n        homepage_text = homepage.read_text(encoding="utf-8") if homepage.is_file() else ""\n        if 'class="keeper96-preview-panel"' not in homepage_text:\n            errors.append(f"Keeper R96 intelligence preview missing from overview page: {homepage}")\n        if 'keeper-matter-demo' in homepage_text:\n            errors.append(f"Legacy Keeper matter demo must remain off overview page: {homepage}")\n\n        solutions_text = solutions.read_text(encoding="utf-8") if solutions.is_file() else ""\n        if 'class="keeper96-mini-process"' not in solutions_text:\n            errors.append(f"Keeper R96 mini process missing from solutions page: {solutions}")\n        if 'keeper-matter-demo' in solutions_text:\n            errors.append(f"Legacy Keeper matter demo must remain off solutions page: {solutions}")\n\n        keeper_text = keeper.read_text(encoding="utf-8") if keeper.is_file() else ""'''
gate = replace_once(gate, entry_pattern, entry_replacement, 'gate:entry-block')
if 'if "/assets/keeper-r96.css" not in keeper_text:' not in gate:
    gate = gate.replace(
        '        if "/assets/keeper-r94.css" not in keeper_text:\n            errors.append(f"Keeper R94 product-story stylesheet missing from product page: {keeper}")\n',
        '        if "/assets/keeper-r94.css" not in keeper_text:\n            errors.append(f"Keeper R94 compatibility stylesheet missing from product page: {keeper}")\n        if "/assets/keeper-r96.css" not in keeper_text:\n            errors.append(f"Keeper R96 product-story stylesheet missing from product page: {keeper}")\n'
    )
gate_path.write_text(gate, encoding='utf-8')

# Live deployment proof: require the intelligence-first R96 story in all locales and overview.
workflow_path = ROOT / '.github/workflows/axiona-pages-rebuild.yml'
workflow = workflow_path.read_text(encoding='utf-8')
verify_step_pattern = r'''      - name: Verify live social previews and Keeper product story\n.*?      - name: Record live deployment proof'''
verify_step = '''      - name: Verify live social previews and Keeper R96 intelligence story\n        id: live\n        shell: bash\n        run: |\n          set -euo pipefail\n          for attempt in $(seq 1 24); do\n            HU="$(curl --fail --silent --show-error --location https://axiona.systems/systems.html || true)"\n            EN="$(curl --fail --silent --show-error --location https://axiona.systems/en/systems.html || true)"\n            DE="$(curl --fail --silent --show-error --location https://axiona.systems/de/systems.html || true)"\n            HOME_HU="$(curl --fail --silent --show-error --location https://axiona.systems/ || true)"\n            HOME_EN="$(curl --fail --silent --show-error --location https://axiona.systems/en/ || true)"\n            HOME_DE="$(curl --fail --silent --show-error --location https://axiona.systems/de/ || true)"\n            KEEPER_HU="$(curl --fail --silent --show-error --location https://axiona.systems/keeper.html || true)"\n            KEEPER_EN="$(curl --fail --silent --show-error --location https://axiona.systems/en/keeper.html || true)"\n            KEEPER_DE="$(curl --fail --silent --show-error --location https://axiona.systems/de/keeper.html || true)"\n            if grep -Fq 'axiona-social-preview-r92-hu.png' <<<"$HU" \\\n              && grep -Fq 'axiona-social-preview-r92-en.png' <<<"$EN" \\\n              && grep -Fq 'axiona-social-preview-r92-de.png' <<<"$DE" \\\n              && grep -Fq 'axiona-keeper-social-preview-r92-hu.png' <<<"$KEEPER_HU" \\\n              && grep -Fq '/assets/keeper-r96.css' <<<"$HOME_HU" \\\n              && grep -Fq 'keeper96-preview-panel' <<<"$HOME_HU" \\\n              && grep -Fq 'Kevesebb kézi adminisztráció' <<<"$HOME_HU" \\\n              && grep -Fq 'keeper96-preview-panel' <<<"$HOME_EN" \\\n              && grep -Fq 'Less manual admin' <<<"$HOME_EN" \\\n              && grep -Fq 'keeper96-preview-panel' <<<"$HOME_DE" \\\n              && grep -Fq 'Weniger manuelle Verwaltung' <<<"$HOME_DE" \\\n              && grep -Fq '/assets/keeper-r96.css' <<<"$KEEPER_HU" \\\n              && grep -Fq 'keeper96-workcard' <<<"$KEEPER_HU" \\\n              && grep -Fq 'elvégzi a rendrakás nagy részét' <<<"$KEEPER_HU" \\\n              && grep -Fq 'keeper96-process-grid' <<<"$KEEPER_HU" \\\n              && grep -Fq '/assets/keeper-r96.css' <<<"$KEEPER_EN" \\\n              && grep -Fq 'does most of the organising work' <<<"$KEEPER_EN" \\\n              && grep -Fq '/assets/keeper-r96.css' <<<"$KEEPER_DE" \\\n              && grep -Fq 'liest es, erkennt es und ordnet' <<<"$KEEPER_DE" \\\n              && curl --fail --silent --show-error --head https://axiona.systems/assets/social/axiona-social-preview-r92-hu.png >/dev/null \\\n              && curl --fail --silent --show-error --head https://axiona.systems/assets/social/axiona-keeper-social-preview-r92-hu.png >/dev/null \\\n              && curl --fail --silent --show-error --head https://axiona.systems/assets/keeper-r96.css >/dev/null; then\n              echo "OK_AXIONA_LIVE_SOCIAL_AND_KEEPER_R96"\n              exit 0\n            fi\n            echo "LIVE_R96_NOT_READY_ATTEMPT=${attempt}"\n            sleep 5\n          done\n          echo "STOP_AXIONA_LIVE_R96_NOT_PUBLISHED"\n          exit 1\n\n      - name: Record live deployment proof'''
workflow = replace_once(workflow, verify_step_pattern, verify_step, 'workflow:verify-step')
workflow = workflow.replace('"keeper_story": "R94",\n                  "keeper_stylesheet": "assets/keeper-r94.css",', '"keeper_story": "R96",\n                  "keeper_stylesheet": "assets/keeper-r96.css",')
workflow_path.write_text(workflow, encoding='utf-8')

print('OK_KEEPER_INTELLIGENCE_R96_PATCHED')
