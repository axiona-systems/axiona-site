#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one match in {path}, got {count}: {old[:120]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


def replace_all(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"missing expected text in {path}: {old!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


# Release marker on the public Keeper entry surfaces.
for path in (
    "keeper.html", "index.html", "solutions.html",
    "en/keeper.html", "en/index.html", "en/solutions.html",
    "de/keeper.html", "de/index.html", "de/solutions.html",
):
    replace(path, '<meta content="R97" name="axiona-release"/>', '<meta content="R98" name="axiona-release"/>')

# ---------------------------------------------------------------------------
# HU — semantic ownership: what Keeper does vs what remains for the user.
# ---------------------------------------------------------------------------
replace(
    "keeper.html",
    '        <p class="keeper96-hero-lead">Legyen az PDF vagy egy iratról készült kép, a Keeper elolvassa, megpróbálja felismerni, mi az, röviden összefoglalja, kiemeli a fontos adatokat és dátumokat, majd megmutatja, mihez tartozhat és kell-e vele foglalkoznod. Nem neked kell minden dokumentumot külön végigolvasni, elnevezni, besorolni és fejben tartani.</p>',
    '        <p class="keeper96-hero-lead">Legyen az PDF vagy egy iratról készült kép, a Keeper elolvassa, megpróbálja felismerni, mi az, röviden összefoglalja, kiemeli a fontos adatokat és dátumokat, majd megkeresi, mihez tartozhat, és jelzi, ha van vele teendő. Nem neked kell minden dokumentumot külön végigolvasni, kiszedni belőle a fontos adatokat, kitalálni, mihez tartozik és fejben tartani a határidőket.</p>',
)
replace(
    "keeper.html",
    '          <div class="keeper96-workrow"><span>04 / RENDBE TESZI</span><div><strong>Megkeresi, mihez tartozhat.</strong><p>Javasolhat kapcsolatot személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy egy ügyhöz. Ha nem biztos benne, rákérdezhet.</p></div></div>',
    '          <div class="keeper96-workrow"><span>04 / RENDBE TESZI</span><div><strong>Megkeresi, mihez tartozik, és javasolja a helyét.</strong><p>Kapcsolatot kereshet a megfelelő személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy ügyhöz. Ha a javaslat rendben van, jóváhagyás után a Keeper elrendezheti; ha bizonytalan, rákérdez.</p></div></div>',
)
replace(
    "keeper.html",
    '        <div class="keeper96-control"><span>TE DÖNTESZ</span><div><strong>A Keeper segít előkészíteni a következő lépést, de nem dönt helyetted.</strong><p>A bizonytalan részeket te ellenőrzöd. Emlékeztető vagy más teendő csak a jóváhagyásoddal készül.</p></div></div>',
    '        <div class="keeper96-control"><span>TE DÖNTESZ</span><div><strong>A Keeper előkészíti a munkát; neked ott kell döntened, ahol valóban döntés kell.</strong><p>A bizonytalan adatokat ellenőrizheted. Rendezés, emlékeztető vagy más következő lépés csak a jóváhagyásoddal történik.</p></div></div>',
)
replace(
    "keeper.html",
    '      <div class="keeper96-core-head"><div><p class="keeper96-kicker">MIÉRT JÓ EZ NEKED?</p><h2 class="keeper96-title">Nem elég, hogy megvan az irat. Jó lenne rögtön tudni, mi van benne és mi a dolgod vele.</h2></div><p>Egy tárhely megőrzi a fájlt. De attól még neked kell elolvasni, kiszedni belőle a fontos adatokat, kitalálni, mihez tartozik, és észben tartani a határidőket. A Keeper pont ebből a munkából vesz le minél többet.</p></div>',
    '      <div class="keeper96-core-head"><div><p class="keeper96-kicker">MIÉRT JÓ EZ NEKED?</p><h2 class="keeper96-title">Nem az a segítség, hogy megvan az irat. Az a segítség, hogy ne neked kelljen újra végigdolgoznod.</h2></div><p>Egy sima tárhely csak megőrzi a fájlt. Ott neked kell elolvasni, kiszedni a fontos adatokat, kitalálni, mihez tartozik és észben tartani a határidőket. A Keeper célja, hogy ezeknek a lépéseknek a nagy részét elvégezze helyetted, és csak ott kérjen tőled ellenőrzést vagy döntést, ahol valóban szükség van rá.</p></div>',
)
replace(
    "keeper.html",
    '      <div class="keeper96-process-head"><p class="keeper96-kicker">MIT VESZ LE RÓLAD A KEEPER?</p><h2 class="keeper96-title">Te behozod az iratot. A Keeper végigmegy rajta.</h2><p>Nem kell előre kitalálnod, hová mentsd vagy hogyan nevezd el. Elég behozni az iratot; a Keeper lépésről lépésre feldolgozza.</p></div>',
    '      <div class="keeper96-process-head"><p class="keeper96-kicker">MIT VESZ LE RÓLAD A KEEPER?</p><h2 class="keeper96-title">Te behozod az iratot. A Keeper elvégzi a feldolgozás nagy részét.</h2><p>Nem kell előre végigolvasnod, átnevezned, mappát választanod vagy kézzel összekapcsolnod a korábbi iratokkal. Elég behozni; a Keeper lépésről lépésre feldolgozza, és csak ott kér ellenőrzést vagy jóváhagyást, ahol szükséges.</p></div>',
)
replace(
    "keeper.html",
    '        <article class="keeper96-process-step"><span>02 / SZÖVEGFELISMERÉS</span><h3>Elolvassa a dokumentumot.</h3><p>A szöveget lehetőleg a készüléken olvassa ki, így később nem csak a fájlnévből kell dolgoznia.</p><small>KEEPER: ELOLVASSA</small></article>',
    '        <article class="keeper96-process-step"><span>02 / SZÖVEGFELISMERÉS</span><h3>Elolvassa a dokumentumot.</h3><p>A szöveget lehetőleg a készüléken olvassa ki. Így a Keeper a dokumentum tényleges tartalmával tud dolgozni, nem csak a fájlnévvel.</p><small>KEEPER: ELOLVASSA</small></article>',
)
replace(
    "keeper.html",
    '        <article class="keeper96-process-step"><span>03 / ÉRTELMEZÉS</span><h3>Megpróbálja megérteni, milyen iratról van szó.</h3><p>Készíthet rövid összefoglalót, és javaslatot adhat arra, milyen dokumentumról van szó. Ha valamiben nem biztos, azt jelzi.</p><small>KEEPER: ÉRTELMEZI ÉS ÖSSZEFOGLALJA</small></article>',
    '        <article class="keeper96-process-step"><span>03 / ÉRTELMEZÉS</span><h3>Megpróbálja megérteni, milyen iratról van szó.</h3><p>Rövid összefoglalót készíthet, és felismerheti, hogy például számla, szerződés vagy értesítő érkezett. Ha valamiben nem biztos, azt jelzi.</p><small>KEEPER: ÉRTELMEZI ÉS ÖSSZEFOGLALJA</small></article>',
)
replace(
    "keeper.html",
    '        <article class="keeper96-process-step"><span>04 / FONTOS ADATOK</span><h3>Kiemeli, amit érdemes észrevenni.</h3><p>Dátumok, határidők, összegek és más fontos adatok külön megjelenhetnek. Az eredeti irat bármikor visszanézhető.</p><small>KEEPER: KIEMELI A FONTOS ADATOKAT</small></article>',
    '        <article class="keeper96-process-step"><span>04 / FONTOS ADATOK</span><h3>Kiemeli, amit fontos lehet tudnod.</h3><p>Nem neked kell újra végigolvasni az egész iratot azért, hogy megtaláld a dátumot, összeget, azonosítót vagy határidőt. A Keeper ezeket külön kiemelheti, az eredeti helyük pedig visszanézhető.</p><small>KEEPER: KIEMELI A FONTOS ADATOKAT</small></article>',
)
replace(
    "keeper.html",
    '        <article class="keeper96-process-step"><span>05 / RENDEZÉS</span><h3>Megkeresi a helyét a többi irat között.</h3><p>Javasolhat kategóriát és kapcsolatot ahhoz a személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy ügyhöz, amihez az irat tartozik. A javaslatot bármikor javíthatod.</p><small>KEEPER: MEGKERESI, MIHEZ TARTOZHAT</small></article>',
    '        <article class="keeper96-process-step"><span>05 / RENDEZÉS</span><h3>Rendbe teszi, ami összetartozik.</h3><p>Nem neked kell fejben vagy mappák között összerakni a kapcsolatokat. A Keeper javasolhatja, melyik személyhez, szolgáltatóhoz, szerződéshez, eszközhöz vagy ügyhöz tartozik az irat, és jóváhagyás után a helyére rendezheti. Ha téved, javíthatod.</p><small>KEEPER: KAPCSOLATOT ÉS HELYET JAVASOL</small></article>',
)
replace(
    "keeper.html",
    '        <article class="keeper96-process-step"><span>06 / KÖVETKEZŐ LÉPÉS</span><h3>Szól, ha valami következik.</h3><p>Ha határidőt vagy tennivalót talál, jelzi. Emlékeztető csak akkor készül, ha jóváhagyod.</p><small>TE: ELLENŐRZÖD ÉS JÓVÁHAGYOD</small></article>',
    '        <article class="keeper96-process-step"><span>06 / KÖVETKEZŐ LÉPÉS</span><h3>Szól, ha van vele dolgod.</h3><p>Nem neked kell minden iratból külön felírni a határidőt. Ha a Keeper teendőt vagy határidőt talál, kiemeli és emlékeztetőt javasolhat; az emlékeztető csak jóváhagyás után készül.</p><small>TE: ELLENŐRZÖD ÉS JÓVÁHAGYOD</small></article>',
)

old_hu_compare = '''      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">A KÜLÖNBSÉG</p><h2 class="keeper96-title">Több annál, mint hogy elteszi a fájlokat.</h2></div><p>A tárolás csak az első lépés. A Keeper attól lesz hasznos, hogy segít értelmezni az iratot, összekötni azzal, amihez tartozik, és észrevenni, ha teendőd van vele.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>EGYSZERŰ TÁRHELY</span><span>KEEPER</span></div>
        <div class="keeper96-compare-row"><div><strong>Elteszi a fájlt.</strong><p>Megvan, de továbbra is neked kell elolvasni és értelmezni.</p></div><div><strong>Elolvassa és kiemeli a lényeget.</strong><p>Nem egy ismeretlen fájlból kell elindulnod: a fontos részek már előkerülhetnek.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Mappát és fájlnevet mutat.</strong><p>A rend attól függ, mennyire következetesen rendezed kézzel.</p></div><div><strong>Segít megmutatni, mihez tartozik.</strong><p>Javasolhat kategóriát, és összekötheti az iratot a kapcsolódó személlyel, szerződéssel, eszközzel vagy üggyel.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>A határidő bent marad a dokumentumban.</strong><p>Neked kell észrevenni és átírni valahová.</p></div><div><strong>Kiemelheti a határidőt.</strong><p>Az eredeti rész visszanézhető, emlékeztető pedig csak a jóváhagyásoddal készül.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Neked kell emlékezned, hol keresd.</strong><p>Fájlnévre, mappára vagy arra hagyatkozol, hogy emlékszel, hová tetted.</p></div><div><strong>A tartalmában is kereshetsz.</strong><p>Így később nem feltétlenül kell tudnod, milyen néven vagy hová mentetted.</p></div></div>
      </div>'''
new_hu_compare = '''      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">A KÜLÖNBSÉG</p><h2 class="keeper96-title">A különbség az, mennyi munka marad rád.</h2></div><p>Egy sima tárhelyen az irat megvan, de az értelmezés, rendezés és utánkövetés továbbra is a te feladatod. A Keeper célja, hogy ezekből minél többet elvégezzen helyetted.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>SIMA TÁRHELY</span><span>KEEPERREL</span></div>
        <div class="keeper96-compare-row"><div><strong>Neked kell végigolvasni és kiszedni, ami fontos.</strong><p>A fájl megvan, de az értelmezés rád marad.</p></div><div><strong>Nem neked kell minden iratot végigolvasni.</strong><p>A Keeper összefoglalhatja a tartalmát, és külön kiemelheti a fontos adatokat.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Neked kell rendben tartani, mi hová tartozik.</strong><p>Te sorolod be és kapcsolod össze kézzel a dokumentumokat.</p></div><div><strong>Nem neked kell egyedül összerakni a kapcsolatokat.</strong><p>A Keeper felismerheti, mihez tartozik az irat, helyet és kapcsolatot javasolhat, majd jóváhagyás után elrendezheti.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Neked kell észrevenni és külön felírni a határidőt.</strong><p>Ha átsiklasz fölötte, a tárhely nem szól.</p></div><div><strong>Nem neked kell minden dátumot külön figyelni.</strong><p>A Keeper kiemelheti a határidőt, és jóváhagyható emlékeztetőt javasolhat.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Neked kell emlékezned, hol és milyen néven keresd.</strong><p>A keresés a fájlnévre, mappára és a saját emlékezetedre támaszkodik.</p></div><div><strong>Nem kell emlékezned a fájlnévre vagy a mappára.</strong><p>A Keeper a dokumentum tartalmát és kapcsolatait is felhasználhatja a kereséshez.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Neked kell észben tartani, mi a következő lépés.</strong><p>A tárhely nem tudja, hogy válaszolni, fizetni vagy utánanézni kell.</p></div><div><strong>A Keeper külön jelezheti, ha teendőt talál.</strong><p>A következő lépést előkészítheti, de csak a jóváhagyásoddal lesz belőle emlékeztető vagy más művelet.</p></div></div>
      </div>'''
replace("keeper.html", old_hu_compare, new_hu_compare)

replace(
    "keeper.html",
    '<article class="keeper96-example"><span>SZÁMLA / FIZETÉSI ÉRTESÍTŐ</span><h3>A fizetési határidő ne vesszen el a sorok között.</h3><p>Egy számlánál nem csak az számít, hogy megvan, hanem az is, mennyi, mikorra és ki állította ki.</p>',
    '<article class="keeper96-example"><span>SZÁMLA / FIZETÉSI ÉRTESÍTŐ</span><h3>Ne neked kelljen kibányászni az összeget és a fizetési határidőt.</h3><p>A Keeper kiemelheti, mennyit, mikorra és kinek kell fizetni, így ezekért nem kell újra végigolvasnod a számlát.</p>',
)
replace(
    "keeper.html",
    '<article class="keeper96-example"><span>SZERZŐDÉS / ELŐFIZETÉS</span><h3>Az új irat találja meg a régi szerződést, ne neked kelljen emlékezned rá.</h3>',
    '<article class="keeper96-example"><span>SZERZŐDÉS / ELŐFIZETÉS</span><h3>Ne neked kelljen emlékezned, melyik régi szerződéshez tartozik az új irat.</h3>',
)
replace(
    "keeper.html",
    '<article class="keeper96-example"><span>INGATLAN / FELÚJÍTÁS</span><h3>Sokféle irat, mégis ugyanahhoz a munkához tartoznak.</h3>',
    '<article class="keeper96-example"><span>INGATLAN / FELÚJÍTÁS</span><h3>Ne neked kelljen külön összeválogatni az ugyanahhoz a munkához tartozó iratokat.</h3>',
)

# HU overview and Solutions.
replace(
    "index.html",
    '        <h2>AXIONA Keeper<span>Ne az iratok rendezése vigye el az idődet.</span></h2>',
    '        <h2>AXIONA Keeper<span>Ne neked kelljen minden iratot végigolvasni, rendezni és fejben tartani.</span></h2>',
)
replace(
    "index.html",
    '        <p class="keeper-preview-lead">Behozol egy PDF-et vagy egy iratról készült képet. A Keeper elolvassa, megpróbálja felismerni, mi az, kiemeli a fontos adatokat, megkeresi, mihez tartozhat, és szól, ha dolgod lehet vele. A döntés nálad marad.</p>',
    '        <p class="keeper-preview-lead">Behozol egy PDF-et vagy egy iratról készült képet. A Keeper elolvassa, megpróbálja felismerni, mi az, összefoglalja, kiemeli a fontos adatokat, megkeresi, mihez tartozhat, és szól, ha van vele teendő. Így a munka nagy részét nem neked kell kézzel elvégezni; a döntés ott marad nálad, ahol tényleg dönteni kell.</p>',
)
replace(
    "index.html",
    '          <div class="keeper96-preview-row"><span>02</span><div><strong>Megérti és kiemeli.</strong><p>Röviden összefoglalja, és előveszi a fontos adatokat, dátumokat, határidőket.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>02</span><div><strong>Felismeri és kiemeli a lényeget.</strong><p>Röviden összefoglalja, és előveszi a fontos adatokat, dátumokat, határidőket.</p></div></div>',
)
replace(
    "index.html",
    '          <div class="keeper96-preview-row"><span>03</span><div><strong>Megkeresi, mihez tartozik.</strong><p>Kapcsolatot javasol a megfelelő személyhez, szerződéshez, eszközhöz vagy ügyhöz.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>03</span><div><strong>Rendbe teszi, ami összetartozik.</strong><p>Megkeresi, mihez tartozhat az irat, és helyet vagy kapcsolatot javasol; a jóváhagyott rendezést elvégezheti.</p></div></div>',
)
replace(
    "index.html",
    '          <div class="keeper96-preview-row"><span>04</span><div><strong>Szól, ha dolgod van vele.</strong><p>Ha teendőt vagy határidőt talál, jelzi. A következő lépést te hagyod jóvá.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>04</span><div><strong>Szól, ha teendőt talál.</strong><p>Nem neked kell minden határidőt külön észben tartani; a következő lépést viszont te hagyod jóvá.</p></div></div>',
)
replace(
    "solutions.html",
    '        <div><div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Behozod az iratot. A Keeper végigmegy rajta.</h3><p>Elolvassa, megpróbálja felismerni, mi az, kiemeli a fontos adatokat és határidőket, megkeresi, mihez tartozhat, és szól, ha valamit intézned kell. A cél egyszerű: kevesebb idő menjen el az iratok kézi rendezésére és újraolvasására.</p><a class="text-link" href="/keeper.html">Részletes Keeper-bemutató<span>→</span></a></div>',
    '        <div><div class="keeper-status-line"><b class="keeper-status-badge">FEJLESZTÉS ALATT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Behozod az iratot. A Keeper elvégzi a feldolgozás nagy részét.</h3><p>Elolvassa, megpróbálja felismerni, mi az, kiemeli a fontos adatokat és határidőket, megkeresi, mihez tartozhat, és szól, ha van vele teendő. Így nem neked kell minden iratot külön végigolvasni, kézzel besorolni és fejben tartani.</p><a class="text-link" href="/keeper.html">Részletes Keeper-bemutató<span>→</span></a></div>',
)
replace(
    "solutions.html",
    '<div class="keeper96-mini-row"><span>04</span><div><strong>Rendbe teszi</strong><p>megkeresi, mihez tartozhat</p></div></div>',
    '<div class="keeper96-mini-row"><span>04</span><div><strong>Rendbe teszi</strong><p>helyet és kapcsolatot javasol; jóváhagyás után elrendezheti</p></div></div>',
)
replace(
    "solutions.html",
    '<div class="keeper96-mini-row"><span>05</span><div><strong>Jelez</strong><p>ha ellenőrizni vagy intézni kell valamit</p></div></div>',
    '<div class="keeper96-mini-row"><span>05</span><div><strong>Jelez</strong><p>ha határidőt, bizonytalan adatot vagy teendőt talál</p></div></div>',
)

# ---------------------------------------------------------------------------
# EN — same semantics, natural English.
# ---------------------------------------------------------------------------
replace(
    "en/keeper.html",
    '        <p class="keeper96-hero-lead">Whether it is a PDF or a photo of a document, Keeper reads it, tries to understand what it is, gives you a short summary, pulls out important facts and dates, then shows what it may belong to and whether you need to do anything with it. You should not have to read, name, sort and remember every document by hand.</p>',
    '        <p class="keeper96-hero-lead">Whether it is a PDF or a photo of a document, Keeper reads it, tries to identify what it is, gives you a short summary, pulls out important facts and dates, works out what it may belong to and flags anything that may need action. You should not have to read every document end to end, extract the important details, piece together the relationships and remember every deadline yourself.</p>',
)
replace(
    "en/keeper.html",
    '          <div class="keeper96-workrow"><span>04 / ORGANIZE</span><div><strong>Work out what it may belong to.</strong><p>It can suggest a link to the right person, provider, contract, asset or matter. If the match is uncertain, you can review it.</p></div></div>',
    '          <div class="keeper96-workrow"><span>04 / ORGANIZE</span><div><strong>Work out what it belongs with and suggest where it should go.</strong><p>Keeper can look for a link to the right person, provider, contract, asset or matter. Once you approve the suggestion, Keeper can organize it; if the match is uncertain, it asks for review.</p></div></div>',
)
replace(
    "en/keeper.html",
    '        <div class="keeper96-control"><span>YOU DECIDE</span><div><strong>Keeper can prepare the next step, but it does not decide for you.</strong><p>You review uncertain details, and reminders or other actions only happen after you approve them.</p></div></div>',
    '        <div class="keeper96-control"><span>YOU DECIDE</span><div><strong>Keeper prepares the work; you step in where an actual decision is needed.</strong><p>You can review uncertain details. Filing changes, reminders and other next steps only happen after you approve them.</p></div></div>',
)
replace(
    "en/keeper.html",
    '      <div class="keeper96-core-head"><div><p class="keeper96-kicker">WHY THIS MATTERS</p><h2 class="keeper96-title">Having the document is not enough. You also need to know what is in it and what to do with it.</h2></div><p>Storage keeps the file. You still have to read it, find the important details, work out what it belongs to and remember the deadlines. Keeper is designed to take as much of that work off your hands as possible.</p></div>',
    '      <div class="keeper96-core-head"><div><p class="keeper96-kicker">WHY THIS MATTERS</p><h2 class="keeper96-title">The useful part is not simply having the document. It is not having to do all the work around it yourself.</h2></div><p>With basic storage, the file is kept but the admin is still yours: reading it, finding the important details, working out what it belongs to and remembering deadlines. Keeper is designed to do most of those steps for you and ask for your review only where it is actually needed.</p></div>',
)
replace(
    "en/keeper.html",
    '      <div class="keeper96-process-head"><p class="keeper96-kicker">WHAT KEEPER TAKES OFF YOUR HANDS</p><h2 class="keeper96-title">You bring in the document. Keeper works through it.</h2><p>You do not need to decide on folders or filenames first. Bring in the document and Keeper works through it step by step.</p></div>',
    '      <div class="keeper96-process-head"><p class="keeper96-kicker">WHAT KEEPER TAKES OFF YOUR HANDS</p><h2 class="keeper96-title">You bring in the document. Keeper does most of the processing.</h2><p>You do not need to read it first, rename it, choose a folder or manually connect it to earlier documents. Bring it in and Keeper works through the steps, asking for review or approval only where necessary.</p></div>',
)
replace(
    "en/keeper.html",
    '        <article class="keeper96-process-step"><span>04 / IMPORTANT FACTS</span><h3>Pull out what is worth noticing.</h3><p>Dates, deadlines, amounts and other important details can be shown separately. You can always go back to the original document.</p><small>KEEPER: PULLS OUT IMPORTANT DETAILS</small></article>',
    '        <article class="keeper96-process-step"><span>04 / IMPORTANT FACTS</span><h3>Pull out what matters.</h3><p>You should not have to reread the whole document just to find a date, amount, reference or deadline. Keeper can bring those details forward while keeping the original passage available to check.</p><small>KEEPER: PULLS OUT IMPORTANT DETAILS</small></article>',
)
replace(
    "en/keeper.html",
    '        <article class="keeper96-process-step"><span>05 / ORGANIZE</span><h3>Find where it fits with your other documents.</h3><p>Keeper can suggest a category and a link to the person, provider, contract, asset or matter the document belongs to. You can correct the suggestion at any time.</p><small>KEEPER: FINDS WHAT IT MAY BELONG TO</small></article>',
    '        <article class="keeper96-process-step"><span>05 / ORGANIZE</span><h3>Organize what belongs together.</h3><p>You should not have to piece the relationships together in your head or across folders. Keeper can suggest the person, provider, contract, asset or matter the document belongs to and, after approval, organize it accordingly. You can correct a wrong suggestion at any time.</p><small>KEEPER: SUGGESTS THE RIGHT PLACE AND RELATIONSHIPS</small></article>',
)
replace(
    "en/keeper.html",
    '        <article class="keeper96-process-step"><span>06 / NEXT STEP</span><h3>Tell you when something comes next.</h3><p>If Keeper finds a deadline or something you may need to do, it tells you. A reminder is only created after you approve it.</p><small>YOU: REVIEW AND APPROVE</small></article>',
    '        <article class="keeper96-process-step"><span>06 / NEXT STEP</span><h3>Tell you when something needs attention.</h3><p>You should not have to copy every deadline somewhere else by hand. If Keeper finds a deadline or task, it can flag it and suggest a reminder; the reminder is only created after you approve it.</p><small>YOU: REVIEW AND APPROVE</small></article>',
)
old_en_compare = '''      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">THE DIFFERENCE</p><h2 class="keeper96-title">It does more than store files.</h2></div><p>Storage is only the first step. Keeper becomes useful when it helps you understand the document, connect it to what it belongs to and notice when something needs doing.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>BASIC STORAGE</span><span>KEEPER</span></div>
        <div class="keeper96-compare-row"><div><strong>Stores the file.</strong><p>The document exists, but you still have to read and interpret it yourself.</p></div><div><strong>Reads it and pulls out the important parts.</strong><p>The useful details can already be in front of you instead of staying buried in the document.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Shows folders and filenames.</strong><p>Order depends on how consistently you maintain it by hand.</p></div><div><strong>Helps show what the document belongs to.</strong><p>It can suggest a category and connect the document to the right person, contract, asset or matter.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>The deadline stays buried in the document.</strong><p>You have to notice it and copy it somewhere else.</p></div><div><strong>Can bring the deadline forward.</strong><p>You can check the original passage, and reminders only happen after you approve them.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>You have to remember where to look.</strong><p>You rely on the filename, folder or your memory of where you put it.</p></div><div><strong>You can search by what is inside the document too.</strong><p>You do not necessarily need to remember the filename or where you saved it.</p></div></div>
      </div>'''
new_en_compare = '''      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">THE DIFFERENCE</p><h2 class="keeper96-title">The difference is how much work is still left for you.</h2></div><p>With basic storage the document is there, but reading, organizing and following it up are still your job. Keeper is designed to do as much of that work for you as possible.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>BASIC STORAGE</span><span>WITH KEEPER</span></div>
        <div class="keeper96-compare-row"><div><strong>You still have to read the document and pull out what matters.</strong><p>The file is stored, but the interpretation is still yours.</p></div><div><strong>You do not have to read every document end to end.</strong><p>Keeper can summarize it and bring the important details forward.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>You still have to keep track of what belongs where.</strong><p>You classify and connect documents by hand.</p></div><div><strong>You do not have to piece all the relationships together yourself.</strong><p>Keeper can work out what the document may belong to, suggest the right place and relationships, then organize it after approval.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>You still have to notice the deadline and copy it somewhere else.</strong><p>If you miss it, basic storage will not tell you.</p></div><div><strong>You do not have to watch every date manually.</strong><p>Keeper can surface a deadline and suggest a reminder for you to approve.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>You still have to remember where and under what name to look.</strong><p>Search depends on filenames, folders and your own memory.</p></div><div><strong>You do not have to remember the filename or folder.</strong><p>Keeper can use document content and relationships to help you find it again.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>You still have to remember what needs to happen next.</strong><p>Basic storage does not know that something may need a reply, payment or follow-up.</p></div><div><strong>Keeper can flag when it finds a possible next step.</strong><p>It can prepare the next action, while reminders and other actions still require your approval.</p></div></div>
      </div>'''
replace("en/keeper.html", old_en_compare, new_en_compare)
replace(
    "en/keeper.html",
    '<article class="keeper96-example"><span>INVOICE / PAYMENT NOTICE</span><h3>A payment deadline should not disappear among the other lines.</h3><p>With an invoice, it is not enough to have the file. You want the amount, due date and issuer at a glance.</p>',
    '<article class="keeper96-example"><span>INVOICE / PAYMENT NOTICE</span><h3>You should not have to dig out the amount and due date yourself.</h3><p>Keeper can bring the issuer, amount and payment deadline forward so you do not have to reread the invoice to find them.</p>',
)
replace(
    "en/keeper.html",
    '<article class="keeper96-example"><span>CONTRACT / SUBSCRIPTION</span><h3>Let the new document find the old contract instead of relying on your memory.</h3>',
    '<article class="keeper96-example"><span>CONTRACT / SUBSCRIPTION</span><h3>You should not have to remember which old contract a new document belongs to.</h3>',
)
replace(
    "en/keeper.html",
    '<article class="keeper96-example"><span>PROPERTY / RENOVATION</span><h3>Different documents, but all part of the same job.</h3>',
    '<article class="keeper96-example"><span>PROPERTY / RENOVATION</span><h3>You should not have to gather the documents for the same job by hand.</h3>',
)
replace(
    "en/index.html",
    '        <h2>AXIONA Keeper<span>Your time should not disappear into sorting documents.</span></h2>',
    '        <h2>AXIONA Keeper<span>You should not have to read, organize and remember every document yourself.</span></h2>',
)
replace(
    "en/index.html",
    '        <p class="keeper-preview-lead">Bring in a PDF or a photo of a document. Keeper reads it, tries to understand what it is, pulls out the important details, works out what it may belong to and tells you if something needs your attention. The decision stays with you.</p>',
    '        <p class="keeper-preview-lead">Bring in a PDF or a photo of a document. Keeper reads it, tries to identify what it is, summarizes it, pulls out the important details, works out what it may belong to and flags anything that may need action. Most of that work should not be yours to do by hand; you step in where a real decision is needed.</p>',
)
replace(
    "en/index.html",
    '          <div class="keeper96-preview-row"><span>02</span><div><strong>Makes sense of it and pulls out what matters.</strong><p>A short summary, important details, dates and possible deadlines.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>02</span><div><strong>Identifies it and pulls out what matters.</strong><p>A short summary, important details, dates and possible deadlines.</p></div></div>',
)
replace(
    "en/index.html",
    '          <div class="keeper96-preview-row"><span>03</span><div><strong>Finds what it may belong to.</strong><p>Suggests a link to the right person, contract, asset or matter.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>03</span><div><strong>Organizes what belongs together.</strong><p>Works out what the document may belong to, suggests the right place or relationship, and can organize it after approval.</p></div></div>',
)
replace(
    "en/index.html",
    '          <div class="keeper96-preview-row"><span>04</span><div><strong>Tells you when you may need to act.</strong><p>If it finds a deadline or task, it tells you. You approve the next step.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>04</span><div><strong>Flags when it finds something to do.</strong><p>You do not have to remember every deadline yourself; you still approve the next step.</p></div></div>',
)
replace(
    "en/solutions.html",
    '        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Bring in the document. Keeper works through it.</h3><p>Keeper reads the document, tries to understand what it is, pulls out important details and deadlines, works out what it may belong to and tells you if something needs doing. The goal is simple: less time spent sorting and rereading documents by hand.</p><a class="text-link" href="/en/keeper.html">Detailed Keeper overview<span>→</span></a></div>',
    '        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN DEVELOPMENT</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Bring in the document. Keeper does most of the processing.</h3><p>Keeper reads it, tries to identify what it is, pulls out important details and deadlines, works out what it may belong to and flags anything that may need action. You should not have to read every document end to end, classify it by hand and remember every deadline yourself.</p><a class="text-link" href="/en/keeper.html">Detailed Keeper overview<span>→</span></a></div>',
)
replace(
    "en/solutions.html",
    '<div class="keeper96-mini-row"><span>04</span><div><strong>Organizes</strong><p>finds what it may belong to</p></div></div>',
    '<div class="keeper96-mini-row"><span>04</span><div><strong>Organizes</strong><p>suggests the right place and relationships; can organize after approval</p></div></div>',
)
replace(
    "en/solutions.html",
    '<div class="keeper96-mini-row"><span>05</span><div><strong>Flags</strong><p>when something may need checking or doing</p></div></div>',
    '<div class="keeper96-mini-row"><span>05</span><div><strong>Flags</strong><p>when it finds a deadline, uncertain detail or possible task</p></div></div>',
)

# ---------------------------------------------------------------------------
# DE — same semantics, natural German.
# ---------------------------------------------------------------------------
replace(
    "de/keeper.html",
    '        <h1>Sie fügen das Dokument hinzu. Keeper übernimmt einen großen Teil der Arbeit, die sonst daran hängen bleibt.</h1>',
    '        <h1>Sie fügen das Dokument hinzu. Keeper übernimmt einen großen Teil der Arbeit, die sonst bei Ihnen bleibt.</h1>',
)
replace(
    "de/keeper.html",
    '        <p class="keeper96-hero-lead">Ob PDF oder Foto eines Dokuments: Keeper liest den Inhalt, versucht zu erkennen, worum es geht, fasst ihn kurz zusammen, hebt wichtige Angaben und Termine hervor und zeigt anschließend, wozu das Dokument gehören könnte und ob Sie etwas damit tun müssen. Sie sollen nicht jede Unterlage erst selbst vollständig lesen, benennen, sortieren und im Kopf behalten müssen.</p>',
    '        <p class="keeper96-hero-lead">Ob PDF oder Foto eines Dokuments: Keeper liest den Inhalt, versucht zu erkennen, worum es geht, fasst ihn kurz zusammen, hebt wichtige Angaben und Termine hervor, sucht den passenden Zusammenhang und weist auf mögliche Aufgaben hin. Sie sollen nicht jede Unterlage selbst vollständig lesen, wichtige Angaben heraussuchen, Zusammenhänge herstellen und Fristen im Kopf behalten müssen.</p>',
)
replace(
    "de/keeper.html",
    '          <div class="keeper96-workrow"><span>04 / ORDNEN</span><div><strong>Prüfen, wozu es gehören könnte.</strong><p>Keeper kann eine Verbindung zu Person, Anbieter, Vertrag, Gegenstand oder Vorgang vorschlagen. Ist die Zuordnung unsicher, können Sie sie prüfen.</p></div></div>',
    '          <div class="keeper96-workrow"><span>04 / ORDNEN</span><div><strong>Zuordnen und den passenden Platz vorschlagen.</strong><p>Keeper kann eine Verbindung zu Person, Anbieter, Vertrag, Gegenstand oder Vorgang suchen. Nach Ihrer Freigabe kann Keeper die Zuordnung übernehmen; ist sie unsicher, bittet es um Prüfung.</p></div></div>',
)
replace(
    "de/keeper.html",
    '        <div class="keeper96-control"><span>SIE ENTSCHEIDEN</span><div><strong>Keeper kann den nächsten Schritt vorbereiten, entscheidet aber nicht für Sie.</strong><p>Unsichere Angaben prüfen Sie selbst; Erinnerungen oder andere Schritte entstehen erst nach Ihrer Freigabe.</p></div></div>',
    '        <div class="keeper96-control"><span>SIE ENTSCHEIDEN</span><div><strong>Keeper bereitet die Arbeit vor; Sie greifen dort ein, wo wirklich eine Entscheidung nötig ist.</strong><p>Unsichere Angaben können Sie prüfen. Zuordnung, Erinnerung oder andere nächste Schritte erfolgen erst nach Ihrer Freigabe.</p></div></div>',
)
replace(
    "de/keeper.html",
    '      <div class="keeper96-core-head"><div><p class="keeper96-kicker">WARUM DAS HILFT</p><h2 class="keeper96-title">Dass das Dokument gespeichert ist, reicht nicht. Sie möchten auch wissen, was darin steht und was damit zu tun ist.</h2></div><p>Ein Speicher bewahrt die Datei auf. Lesen, wichtige Angaben finden, den Zusammenhang erkennen und Fristen im Kopf behalten müssen Sie trotzdem selbst. Genau von dieser Arbeit soll Keeper Ihnen möglichst viel abnehmen.</p></div>',
    '      <div class="keeper96-core-head"><div><p class="keeper96-kicker">WARUM DAS HILFT</p><h2 class="keeper96-title">Die Hilfe besteht nicht nur darin, dass das Dokument gespeichert ist. Entscheidend ist, dass Sie die Arbeit darum nicht selbst erledigen müssen.</h2></div><p>Bei einem einfachen Speicher bleibt die Verwaltung bei Ihnen: lesen, wichtige Angaben finden, den Zusammenhang erkennen und Fristen im Kopf behalten. Keeper soll den größten Teil dieser Schritte übernehmen und nur dort Ihre Prüfung oder Entscheidung verlangen, wo sie wirklich nötig ist.</p></div>',
)
replace(
    "de/keeper.html",
    '      <div class="keeper96-process-head"><p class="keeper96-kicker">WAS KEEPER IHNEN ABNIMMT</p><h2 class="keeper96-title">Sie fügen das Dokument hinzu. Keeper arbeitet es Schritt für Schritt durch.</h2><p>Sie müssen vorher weder Ordner noch Dateinamen festlegen. Fügen Sie das Dokument hinzu, und Keeper arbeitet es Schritt für Schritt durch.</p></div>',
    '      <div class="keeper96-process-head"><p class="keeper96-kicker">WAS KEEPER IHNEN ABNIMMT</p><h2 class="keeper96-title">Sie fügen das Dokument hinzu. Keeper übernimmt den größten Teil der Verarbeitung.</h2><p>Sie müssen es vorher nicht vollständig lesen, umbenennen, einem Ordner zuweisen oder von Hand mit älteren Unterlagen verknüpfen. Keeper arbeitet die Schritte durch und fragt nur dort nach Prüfung oder Freigabe, wo sie nötig ist.</p></div>',
)
replace(
    "de/keeper.html",
    '        <article class="keeper96-process-step"><span>04 / WICHTIGE ANGABEN</span><h3>Hervorheben, was Sie wissen sollten.</h3><p>Daten, Fristen, Beträge und andere wichtige Angaben können separat erscheinen. Das Originaldokument bleibt jederzeit einsehbar.</p><small>KEEPER: HEBT WICHTIGE ANGABEN HERVOR</small></article>',
    '        <article class="keeper96-process-step"><span>04 / WICHTIGE ANGABEN</span><h3>Hervorheben, was wichtig sein kann.</h3><p>Sie müssen nicht das ganze Dokument erneut lesen, nur um Datum, Betrag, Referenz oder Frist zu finden. Keeper kann diese Angaben separat hervorheben; die ursprüngliche Stelle bleibt einsehbar.</p><small>KEEPER: HEBT WICHTIGE ANGABEN HERVOR</small></article>',
)
replace(
    "de/keeper.html",
    '        <article class="keeper96-process-step"><span>05 / ORDNEN</span><h3>Den Platz zwischen den anderen Unterlagen finden.</h3><p>Keeper kann eine Kategorie und eine Verbindung zu Person, Anbieter, Vertrag, Gegenstand oder Vorgang vorschlagen. Den Vorschlag können Sie jederzeit ändern.</p><small>KEEPER: FINDET, WOZU ES GEHÖREN KÖNNTE</small></article>',
    '        <article class="keeper96-process-step"><span>05 / ORDNEN</span><h3>Zusammenbringen, was zusammengehört.</h3><p>Sie müssen die Zusammenhänge nicht selbst im Kopf oder zwischen Ordnern zusammensetzen. Keeper kann Person, Anbieter, Vertrag, Gegenstand oder Vorgang vorschlagen und das Dokument nach Ihrer Freigabe entsprechend zuordnen. Einen falschen Vorschlag können Sie jederzeit korrigieren.</p><small>KEEPER: SCHLÄGT ZUORDNUNG UND PASSENDEN PLATZ VOR</small></article>',
)
replace(
    "de/keeper.html",
    '        <article class="keeper96-process-step"><span>06 / NÄCHSTER SCHRITT</span><h3>Hinweisen, wenn etwas ansteht.</h3><p>Findet Keeper eine Frist oder eine mögliche Aufgabe, weist es Sie darauf hin. Eine Erinnerung entsteht erst nach Ihrer Freigabe.</p><small>SIE: PRÜFEN UND GEBEN FREI</small></article>',
    '        <article class="keeper96-process-step"><span>06 / NÄCHSTER SCHRITT</span><h3>Hinweisen, wenn etwas zu tun ist.</h3><p>Sie müssen nicht jede Frist von Hand irgendwo übertragen. Findet Keeper eine Frist oder Aufgabe, kann es darauf hinweisen und eine Erinnerung vorschlagen; diese entsteht erst nach Ihrer Freigabe.</p><small>SIE: PRÜFEN UND GEBEN FREI</small></article>',
)
old_de_compare = '''      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">DER UNTERSCHIED</p><h2 class="keeper96-title">Keeper soll mehr können als Dateien speichern.</h2></div><p>Speichern ist nur der erste Schritt. Keeper wird dann hilfreich, wenn es das Dokument verständlicher macht, den Zusammenhang findet und Sie rechtzeitig auf Aufgaben hinweist.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>EINFACHER SPEICHER</span><span>KEEPER</span></div>
        <div class="keeper96-compare-row"><div><strong>Bewahrt die Datei auf.</strong><p>Das Dokument ist vorhanden, aber Sie müssen es weiterhin selbst lesen und einordnen.</p></div><div><strong>Liest den Inhalt und hebt Wichtiges hervor.</strong><p>Wichtige Angaben können bereits sichtbar sein, statt im Dokument verborgen zu bleiben.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Zeigt Ordner und Dateinamen.</strong><p>Die Ordnung hängt davon ab, wie konsequent Sie sie manuell pflegen.</p></div><div><strong>Hilft zu erkennen, wozu das Dokument gehört.</strong><p>Keeper kann eine Kategorie vorschlagen und das Dokument mit Person, Vertrag, Gegenstand oder Vorgang verknüpfen.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Die Frist bleibt im Dokument verborgen.</strong><p>Sie müssen es bemerken und separat übertragen.</p></div><div><strong>Kann die Frist hervorheben.</strong><p>Die ursprüngliche Stelle bleibt einsehbar; eine Erinnerung entsteht erst nach Ihrer Freigabe.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Sie müssen wissen, wo Sie suchen sollen.</strong><p>Sie verlassen sich auf Dateiname, Ordner oder Ihre Erinnerung daran, wo Sie die Datei abgelegt haben.</p></div><div><strong>Sie können auch nach dem Inhalt suchen.</strong><p>So müssen Sie später nicht unbedingt wissen, wie die Datei heißt oder wo Sie sie abgelegt haben.</p></div></div>
      </div>'''
new_de_compare = '''      <div class="keeper96-contrast-head"><div><p class="keeper96-kicker">DER UNTERSCHIED</p><h2 class="keeper96-title">Der Unterschied ist, wie viel Arbeit bei Ihnen bleibt.</h2></div><p>Bei einem einfachen Speicher ist das Dokument vorhanden, aber Lesen, Zuordnen und Nachverfolgen bleiben Ihre Aufgabe. Keeper soll möglichst viel davon für Sie übernehmen.</p></div>
      <div class="keeper96-compare">
        <div class="keeper96-compare-head"><span>EINFACHER SPEICHER</span><span>MIT KEEPER</span></div>
        <div class="keeper96-compare-row"><div><strong>Sie müssen das Dokument selbst lesen und Wichtiges heraussuchen.</strong><p>Die Datei ist gespeichert, aber die Auswertung bleibt bei Ihnen.</p></div><div><strong>Sie müssen nicht jedes Dokument vollständig lesen.</strong><p>Keeper kann den Inhalt zusammenfassen und wichtige Angaben hervorheben.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Sie müssen selbst im Blick behalten, was wohin gehört.</strong><p>Sie ordnen und verknüpfen die Unterlagen von Hand.</p></div><div><strong>Sie müssen die Zusammenhänge nicht allein zusammensetzen.</strong><p>Keeper kann erkennen, wozu das Dokument gehören könnte, den passenden Platz und Verbindungen vorschlagen und es nach Ihrer Freigabe zuordnen.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Sie müssen die Frist selbst bemerken und separat notieren.</strong><p>Wenn Sie sie übersehen, meldet sich ein einfacher Speicher nicht.</p></div><div><strong>Sie müssen nicht jedes Datum selbst überwachen.</strong><p>Keeper kann eine Frist hervorheben und eine Erinnerung zur Freigabe vorschlagen.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Sie müssen wissen, wo und unter welchem Namen Sie suchen.</strong><p>Die Suche hängt von Dateiname, Ordner und Ihrer Erinnerung ab.</p></div><div><strong>Sie müssen Dateiname oder Ordner nicht im Kopf behalten.</strong><p>Keeper kann Dokumentinhalt und Beziehungen nutzen, um die Unterlage wiederzufinden.</p></div></div>
        <div class="keeper96-compare-row"><div><strong>Sie müssen selbst im Kopf behalten, was als Nächstes zu tun ist.</strong><p>Ein einfacher Speicher weiß nicht, ob eine Antwort, Zahlung oder Nachfrage ansteht.</p></div><div><strong>Keeper kann auf einen möglichen nächsten Schritt hinweisen.</strong><p>Es kann den Schritt vorbereiten; Erinnerungen und andere Aktionen brauchen weiterhin Ihre Freigabe.</p></div></div>
      </div>'''
replace("de/keeper.html", old_de_compare, new_de_compare)
replace(
    "de/keeper.html",
    '<article class="keeper96-example"><span>RECHNUNG / ZAHLUNGSHINWEIS</span><h3>Die Zahlungsfrist soll nicht zwischen anderen Zeilen untergehen.</h3><p>Bei einer Rechnung möchten Sie Betrag, Fälligkeit und Absender auf einen Blick sehen — nicht nur die Datei besitzen.</p>',
    '<article class="keeper96-example"><span>RECHNUNG / ZAHLUNGSHINWEIS</span><h3>Sie sollen Betrag und Zahlungsfrist nicht selbst aus dem Dokument heraussuchen müssen.</h3><p>Keeper kann Absender, Betrag und Fälligkeit hervorheben, damit Sie die Rechnung dafür nicht erneut vollständig lesen müssen.</p>',
)
replace(
    "de/keeper.html",
    '<article class="keeper96-example"><span>VERTRAG / ABONNEMENT</span><h3>Neue Unterlagen sollen den alten Vertrag finden — nicht Ihre Erinnerung.</h3>',
    '<article class="keeper96-example"><span>VERTRAG / ABONNEMENT</span><h3>Sie sollen nicht selbst im Kopf behalten müssen, zu welchem alten Vertrag eine neue Unterlage gehört.</h3>',
)
replace(
    "de/keeper.html",
    '<article class="keeper96-example"><span>IMMOBILIE / RENOVIERUNG</span><h3>Verschiedene Unterlagen, aber sie gehören zur gleichen Arbeit.</h3>',
    '<article class="keeper96-example"><span>IMMOBILIE / RENOVIERUNG</span><h3>Sie sollen Unterlagen zur gleichen Arbeit nicht selbst zusammensuchen müssen.</h3>',
)
replace(
    "de/index.html",
    '        <h2>AXIONA Keeper<span>Ihre Zeit sollte nicht für das Sortieren von Unterlagen draufgehen.</span></h2>',
    '        <h2>AXIONA Keeper<span>Sie sollten nicht jedes Dokument selbst lesen, ordnen und im Kopf behalten müssen.</span></h2>',
)
replace(
    "de/index.html",
    '        <p class="keeper-preview-lead">Sie fügen ein PDF oder ein Foto eines Dokuments hinzu. Keeper liest den Inhalt, versucht zu erkennen, worum es geht, hebt wichtige Angaben hervor, sucht den passenden Zusammenhang und weist Sie darauf hin, wenn etwas zu tun ist. Die Entscheidung bleibt bei Ihnen.</p>',
    '        <p class="keeper-preview-lead">Sie fügen ein PDF oder ein Foto eines Dokuments hinzu. Keeper liest den Inhalt, versucht zu erkennen, worum es geht, fasst ihn kurz zusammen, hebt wichtige Angaben hervor, sucht den passenden Zusammenhang und weist auf mögliche Aufgaben hin. Den größten Teil dieser Arbeit sollen Sie nicht von Hand erledigen müssen; Sie greifen dort ein, wo eine echte Entscheidung nötig ist.</p>',
)
replace(
    "de/index.html",
    '          <div class="keeper96-preview-row"><span>02</span><div><strong>Einordnen und Wichtiges hervorheben.</strong><p>Kurze Zusammenfassung, wichtige Angaben, Termine und mögliche Fristen.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>02</span><div><strong>Erkennen und Wichtiges hervorheben.</strong><p>Kurze Zusammenfassung, wichtige Angaben, Termine und mögliche Fristen.</p></div></div>',
)
replace(
    "de/index.html",
    '          <div class="keeper96-preview-row"><span>03</span><div><strong>Finden, wozu es gehört.</strong><p>Eine Verbindung zu Person, Vertrag, Gegenstand oder Vorgang vorschlagen.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>03</span><div><strong>Zusammenbringen, was zusammengehört.</strong><p>Keeper sucht den passenden Zusammenhang, schlägt Platz oder Verbindung vor und kann nach Ihrer Freigabe zuordnen.</p></div></div>',
)
replace(
    "de/index.html",
    '          <div class="keeper96-preview-row"><span>04</span><div><strong>Hinweisen, wenn etwas zu tun ist.</strong><p>Findet Keeper eine Frist oder Aufgabe, weist es Sie darauf hin. Den nächsten Schritt geben Sie frei.</p></div></div>',
    '          <div class="keeper96-preview-row"><span>04</span><div><strong>Hinweisen, wenn Keeper eine Aufgabe findet.</strong><p>Sie müssen nicht jede Frist selbst im Kopf behalten; den nächsten Schritt geben Sie weiterhin frei.</p></div></div>',
)
replace(
    "de/solutions.html",
    '        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Dokument hinzufügen. Keeper arbeitet es durch.</h3><p>Keeper liest das Dokument, versucht zu erkennen, worum es geht, hebt wichtige Angaben und Fristen hervor, sucht den passenden Zusammenhang und weist Sie darauf hin, wenn etwas zu tun ist. Ziel ist einfach: weniger Zeit für manuelles Sortieren und erneutes Lesen.</p><a class="text-link" href="/de/keeper.html">Keeper im Detail<span>→</span></a></div>',
    '        <div><div class="keeper-status-line"><b class="keeper-status-badge">IN ENTWICKLUNG</b><span class="micro">iPhone + iPad · Apple App Store</span></div><h3>Dokument hinzufügen. Keeper übernimmt den größten Teil der Verarbeitung.</h3><p>Keeper liest es, versucht zu erkennen, worum es geht, hebt wichtige Angaben und Fristen hervor, sucht den passenden Zusammenhang und weist auf mögliche Aufgaben hin. Sie sollen nicht jede Unterlage vollständig lesen, von Hand zuordnen und jede Frist selbst im Kopf behalten müssen.</p><a class="text-link" href="/de/keeper.html">Keeper im Detail<span>→</span></a></div>',
)
replace(
    "de/solutions.html",
    '<div class="keeper96-mini-row"><span>04</span><div><strong>Ordnen</strong><p>finden, wozu es gehören könnte</p></div></div>',
    '<div class="keeper96-mini-row"><span>04</span><div><strong>Ordnen</strong><p>passenden Platz und Verbindungen vorschlagen; nach Freigabe zuordnen</p></div></div>',
)
replace(
    "de/solutions.html",
    '<div class="keeper96-mini-row"><span>05</span><div><strong>Hinweisen</strong><p>wenn etwas geprüft oder erledigt werden muss</p></div></div>',
    '<div class="keeper96-mini-row"><span>05</span><div><strong>Hinweisen</strong><p>wenn eine Frist, unsichere Angabe oder mögliche Aufgabe erkannt wird</p></div></div>',
)

# ---------------------------------------------------------------------------
# Regression gates: require semantic ownership markers and forbid ambiguous R97 copy.
# ---------------------------------------------------------------------------
verify = ROOT / "scripts/verify_public_quality.py"
text = verify.read_text(encoding="utf-8")
anchor = '''KEEPER_HUMAN_COPY_FORBIDDEN = {
'''
if anchor not in text:
    raise SystemExit("verify_public_quality.py anchor missing")

semantic_block = '''KEEPER_SEMANTIC_REQUIRED = {
    "": {
        "keeper": (
            "A különbség az, mennyi munka marad rád.",
            "Nem neked kell egyedül összerakni a kapcsolatokat.",
            "Nem neked kell minden dátumot külön figyelni.",
            "A Keeper célja, hogy ezeknek a lépéseknek a nagy részét elvégezze helyetted",
        ),
        "home": (
            "Ne neked kelljen minden iratot végigolvasni, rendezni és fejben tartani.",
            "a munka nagy részét nem neked kell kézzel elvégezni",
        ),
        "solutions": (
            "Így nem neked kell minden iratot külön végigolvasni, kézzel besorolni és fejben tartani.",
        ),
    },
    "en/": {
        "keeper": (
            "The difference is how much work is still left for you.",
            "You do not have to piece all the relationships together yourself.",
            "You do not have to watch every date manually.",
            "Keeper is designed to do most of those steps for you",
        ),
        "home": (
            "You should not have to read, organize and remember every document yourself.",
            "Most of that work should not be yours to do by hand",
        ),
        "solutions": (
            "You should not have to read every document end to end, classify it by hand and remember every deadline yourself.",
        ),
    },
    "de/": {
        "keeper": (
            "Der Unterschied ist, wie viel Arbeit bei Ihnen bleibt.",
            "Sie müssen die Zusammenhänge nicht allein zusammensetzen.",
            "Sie müssen nicht jedes Datum selbst überwachen.",
            "Keeper soll den größten Teil dieser Schritte übernehmen",
        ),
        "home": (
            "Sie sollten nicht jedes Dokument selbst lesen, ordnen und im Kopf behalten müssen.",
            "Den größten Teil dieser Arbeit sollen Sie nicht von Hand erledigen müssen",
        ),
        "solutions": (
            "Sie sollen nicht jede Unterlage vollständig lesen, von Hand zuordnen und jede Frist selbst im Kopf behalten müssen.",
        ),
    },
}
KEEPER_SEMANTIC_FORBIDDEN = {
    "": (
        "A rend attól függ, mennyire következetesen rendezed kézzel.",
        "Neked kell észrevenni és átírni valahová.",
        "Megkeresi a helyét a többi irat között.",
    ),
    "en/": (
        "Order depends on how consistently you maintain it by hand.",
        "You have to notice it and copy it somewhere else.",
        "Find where it fits with your other documents.",
    ),
    "de/": (
        "Die Ordnung hängt davon ab, wie konsequent Sie sie manuell pflegen.",
        "Sie müssen es bemerken und separat übertragen.",
        "Den Platz zwischen den anderen Unterlagen finden.",
    ),
}

'''
if "KEEPER_SEMANTIC_REQUIRED =" in text:
    raise SystemExit("semantic gate already present")
text = text.replace(anchor, semantic_block + anchor, 1)

needle = '''        for forbidden in KEEPER_HUMAN_COPY_FORBIDDEN[prefix]:
            if forbidden in keeper_text:
                errors.append(f"Keeper human-copy regression in {keeper}: {forbidden}")
'''
replacement = needle + '''        for required in KEEPER_SEMANTIC_REQUIRED[prefix]["keeper"]:
            if required not in keeper_text:
                errors.append(f"Keeper semantic ownership marker missing in {keeper}: {required}")
        for required in KEEPER_SEMANTIC_REQUIRED[prefix]["home"]:
            if required not in homepage_text:
                errors.append(f"Keeper semantic ownership marker missing in {homepage}: {required}")
        for required in KEEPER_SEMANTIC_REQUIRED[prefix]["solutions"]:
            if required not in solutions_text:
                errors.append(f"Keeper semantic ownership marker missing in {solutions}: {required}")
        for forbidden in KEEPER_SEMANTIC_FORBIDDEN[prefix]:
            for source, source_text in ((keeper, keeper_text), (homepage, homepage_text), (solutions, solutions_text)):
                if forbidden in source_text:
                    errors.append(f"ambiguous Keeper semantic copy remains in {source}: {forbidden}")
'''
if needle not in text:
    raise SystemExit("keeper verification insertion point missing")
text = text.replace(needle, replacement, 1)
verify.write_text(text, encoding="utf-8")

print("OK_KEEPER_SEMANTICS_R98_PATCHED")
