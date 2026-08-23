/* AXIONA R126 — localized 404 recovery + transform-only motion. */
(() => {
  const path = window.location.pathname.toLowerCase();
  const locale = path.startsWith('/en/') ? 'en' : path.startsWith('/de/') ? 'de' : 'hu';
  const prefix = locale === 'hu' ? '' : `/${locale}`;
  const copy = {
    hu: {
      title:'Oldal nem található | AXIONA Systems', eyebrow:'404 / OLDAL NEM TALÁLHATÓ', heading:'Ez az oldal nincs itt.',
      lead:'Lehet, hogy a hivatkozás régi, vagy a cím el lett írva. Innen visszatérhetsz az aktuális AXIONA tartalomhoz.',
      home:'Vissza a főoldalra', contact:'Kapcsolat', sheet:'Merre tovább?', sheetNote:'Három biztos út az aktuális tartalomhoz.',
      overview:'Áttekintés', overviewText:'Rendszerépítés, folyamatok és fejlesztési irányok.', solutions:'Megoldások', solutionsText:'Konkrét szoftveres és automatizálási példák.',
      contactRoute:'Kapcsolat', contactText:'Ha egy konkrét oldalt kerestél, írj röviden.', nav:['Áttekintés','Rendszerépítés','Folyamattervezés','Biztonság','Megoldások','Kapcsolat'],
      menu:'Menü', skip:'Ugrás a tartalomhoz', localeNote:'A hibaoldal nyelve az URL alapján automatikusan igazodik.', navAria:'Fő navigáció', sheetAria:'Tovább az AXIONA oldalaira',
      footerCredit:'Tervezés és fejlesztés — Asztalos Zoltán', support:'Támogatás', privacy:'Adatvédelem', legal:'Jogi információk', security:'Biztonság'
    },
    en: {
      title:'Page not found | AXIONA Systems', eyebrow:'404 / PAGE NOT FOUND', heading:'This page is not here.',
      lead:'The link may be old or the address may have been mistyped. You can return to current AXIONA content from here.',
      home:'Back to overview', contact:'Contact', sheet:'Where next?', sheetNote:'Three reliable routes back to current content.',
      overview:'Overview', overviewText:'System design, processes and current development directions.', solutions:'Solutions', solutionsText:'Concrete software and automation examples.',
      contactRoute:'Contact', contactText:'If you were looking for a specific page, send a short message.', nav:['Overview','System design','Process design','Security','Solutions','Contact'],
      menu:'Menu', skip:'Skip to content', localeNote:'The error page language follows the URL automatically.', navAria:'Main navigation', sheetAria:'Continue to AXIONA pages',
      footerCredit:'Design and development — Asztalos Zoltán', support:'Support', privacy:'Privacy', legal:'Legal information', security:'Security'
    },
    de: {
      title:'Seite nicht gefunden | AXIONA Systems', eyebrow:'404 / SEITE NICHT GEFUNDEN', heading:'Diese Seite ist nicht hier.',
      lead:'Der Link kann veraltet sein oder die Adresse wurde möglicherweise falsch eingegeben. Von hier gelangen Sie zurück zu den aktuellen AXIONA-Inhalten.',
      home:'Zur Übersicht', contact:'Kontakt', sheet:'Wie weiter?', sheetNote:'Drei sichere Wege zurück zu den aktuellen Inhalten.',
      overview:'Übersicht', overviewText:'Systemaufbau, Prozesse und aktuelle Entwicklungsrichtungen.', solutions:'Lösungen', solutionsText:'Konkrete Beispiele für Software und Automatisierung.',
      contactRoute:'Kontakt', contactText:'Wenn Sie eine bestimmte Seite gesucht haben, schreiben Sie kurz.', nav:['Übersicht','Systemaufbau','Prozessplanung','Sicherheit','Lösungen','Kontakt'],
      menu:'Menü', skip:'Zum Inhalt', localeNote:'Die Sprache der Fehlerseite richtet sich automatisch nach der URL.', navAria:'Hauptnavigation', sheetAria:'Weiter zu den AXIONA-Seiten',
      footerCredit:'Planung und Entwicklung — Asztalos Zoltán', support:'Support', privacy:'Datenschutz', legal:'Rechtliche Hinweise', security:'Sicherheit'
    }
  }[locale];

  document.documentElement.lang = locale;
  document.title = copy.title;
  const shell = document.querySelector('.site-shell');
  if (shell) shell.lang = locale;

  const text = (selector, value) => { const el = document.querySelector(selector); if (el) el.textContent = value; };
  Object.entries({
    skip:copy.skip, eyebrow:copy.eyebrow, heading:copy.heading, lead:copy.lead, home:copy.home, contact:copy.contact,
    sheet:copy.sheet, 'sheet-note':copy.sheetNote, overview:copy.overview, 'overview-text':copy.overviewText,
    solutions:copy.solutions, 'solutions-text':copy.solutionsText, 'contact-route':copy.contactRoute, 'contact-text':copy.contactText,
    'locale-note':copy.localeNote, 'footer-credit':copy.footerCredit, support:copy.support, privacy:copy.privacy, legal:copy.legal, security:copy.security
  }).forEach(([key,value]) => text(`[data-i18n="${key}"]`, value));
  text('.mobile-menu > summary', copy.menu);
  document.querySelectorAll('nav[data-main-nav]').forEach((nav) => nav.setAttribute('aria-label', copy.navAria));
  const sheet = document.querySelector('.not-found-sheet');
  if (sheet) sheet.setAttribute('aria-label', copy.sheetAria);

  const route = (name) => prefix ? `${prefix}/${name}` : `/${name}`;
  const routes = {
    home: prefix ? `${prefix}/` : '/',
    systems:route('systems.html'), process:route('process.html'), security:route('security.html'), solutions:route('solutions.html'), contact:route('contact.html'),
    support:route('support.html'), privacy:route('privacy.html'), legal:route('legal.html')
  };
  document.querySelectorAll('[data-route]').forEach((el) => {
    const key = el.getAttribute('data-route');
    if (routes[key]) el.setAttribute('href', routes[key]);
  });

  document.querySelectorAll('[data-main-nav]').forEach((container) => {
    container.querySelectorAll('a').forEach((link, i) => {
      if (copy.nav[i]) link.textContent = copy.nav[i];
    });
  });

  document.querySelectorAll('[data-locale]').forEach((link) => link.classList.toggle('active', link.getAttribute('data-locale') === locale));

  const reveal = [...document.querySelectorAll('[data-error-reveal]')];
  if (!reveal.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    reveal.forEach((el) => el.classList.add('is-visible'));
    return;
  }
  document.body.classList.add('error-motion-ready');
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting)), {threshold:0.12});
  reveal.forEach((el) => observer.observe(el));
})();
