/* AXIONA R126 — localized 404 recovery + transform-only motion. */
(() => {
  const path = window.location.pathname.toLowerCase();
  const locale = path.startsWith('/en/') ? 'en' : path.startsWith('/de/') ? 'de' : 'hu';
  const prefix = locale === 'hu' ? '' : `/${locale}`;
  const copy = {
    hu: {
      title: 'Oldal nem található | AXIONA Systems',
      eyebrow: '404 / OLDAL NEM TALÁLHATÓ',
      heading: 'Ez az oldal nincs itt.',
      lead: 'Lehet, hogy a hivatkozás régi, vagy a cím el lett írva. Innen visszatérhetsz az aktuális AXIONA tartalomhoz.',
      home: 'Vissza a főoldalra', contact: 'Kapcsolat', sheet: 'Merre tovább?',
      sheetNote: 'Három biztos út az aktuális tartalomhoz.',
      overview: 'Áttekintés', overviewText: 'Rendszerépítés, folyamatok és fejlesztési irányok.',
      solutions: 'Megoldások', solutionsText: 'Konkrét szoftveres és automatizálási példák.',
      contactRoute: 'Kapcsolat', contactText: 'Ha egy konkrét oldalt kerestél, írj röviden.',
      nav: ['Áttekintés','Rendszerépítés','Folyamattervezés','Biztonság','Megoldások','Kapcsolat'],
      menu: 'Menü', skip: 'Ugrás a tartalomhoz', localeNote: 'A hibaoldal nyelve az URL alapján automatikusan igazodik.'
    },
    en: {
      title: 'Page not found | AXIONA Systems',
      eyebrow: '404 / PAGE NOT FOUND',
      heading: 'This page is not here.',
      lead: 'The link may be old or the address may have been mistyped. You can return to current AXIONA content from here.',
      home: 'Back to overview', contact: 'Contact', sheet: 'Where next?',
      sheetNote: 'Three reliable routes back to current content.',
      overview: 'Overview', overviewText: 'System design, processes and current development directions.',
      solutions: 'Solutions', solutionsText: 'Concrete software and automation examples.',
      contactRoute: 'Contact', contactText: 'If you were looking for a specific page, send a short message.',
      nav: ['Overview','System design','Process design','Security','Solutions','Contact'],
      menu: 'Menu', skip: 'Skip to content', localeNote: 'The error page language follows the URL automatically.'
    },
    de: {
      title: 'Seite nicht gefunden | AXIONA Systems',
      eyebrow: '404 / SEITE NICHT GEFUNDEN',
      heading: 'Diese Seite ist nicht hier.',
      lead: 'Der Link kann veraltet sein oder die Adresse wurde möglicherweise falsch eingegeben. Von hier gelangen Sie zurück zu den aktuellen AXIONA-Inhalten.',
      home: 'Zur Übersicht', contact: 'Kontakt', sheet: 'Wie weiter?',
      sheetNote: 'Drei sichere Wege zurück zu den aktuellen Inhalten.',
      overview: 'Übersicht', overviewText: 'Systemaufbau, Prozesse und aktuelle Entwicklungsrichtungen.',
      solutions: 'Lösungen', solutionsText: 'Konkrete Beispiele für Software und Automatisierung.',
      contactRoute: 'Kontakt', contactText: 'Wenn Sie eine bestimmte Seite gesucht haben, schreiben Sie kurz.',
      nav: ['Übersicht','Systemaufbau','Prozessplanung','Sicherheit','Lösungen','Kontakt'],
      menu: 'Menü', skip: 'Zum Inhalt', localeNote: 'Die Sprache der Fehlerseite richtet sich automatisch nach der URL.'
    }
  }[locale];

  document.documentElement.lang = locale;
  document.title = copy.title;
  const shell = document.querySelector('.site-shell');
  if (shell) shell.lang = locale;

  const text = (selector, value) => { const el = document.querySelector(selector); if (el) el.textContent = value; };
  text('[data-i18n="skip"]', copy.skip);
  text('[data-i18n="eyebrow"]', copy.eyebrow);
  text('[data-i18n="heading"]', copy.heading);
  text('[data-i18n="lead"]', copy.lead);
  text('[data-i18n="home"]', copy.home);
  text('[data-i18n="contact"]', copy.contact);
  text('[data-i18n="sheet"]', copy.sheet);
  text('[data-i18n="sheet-note"]', copy.sheetNote);
  text('[data-i18n="overview"]', copy.overview);
  text('[data-i18n="overview-text"]', copy.overviewText);
  text('[data-i18n="solutions"]', copy.solutions);
  text('[data-i18n="solutions-text"]', copy.solutionsText);
  text('[data-i18n="contact-route"]', copy.contactRoute);
  text('[data-i18n="contact-text"]', copy.contactText);
  text('[data-i18n="locale-note"]', copy.localeNote);
  text('.mobile-menu > summary', copy.menu);

  const routes = {
    home: prefix ? `${prefix}/` : '/',
    systems: `${prefix}/systems.html` || '/systems.html',
    process: `${prefix}/process.html` || '/process.html',
    security: `${prefix}/security.html` || '/security.html',
    solutions: `${prefix}/solutions.html` || '/solutions.html',
    contact: `${prefix}/contact.html` || '/contact.html'
  };
  if (!prefix) Object.assign(routes, {systems:'/systems.html',process:'/process.html',security:'/security.html',solutions:'/solutions.html',contact:'/contact.html'});

  document.querySelectorAll('[data-route]').forEach((el) => {
    const key = el.getAttribute('data-route');
    if (routes[key]) el.setAttribute('href', routes[key]);
  });

  const navLinks = document.querySelectorAll('[data-main-nav] a');
  navLinks.forEach((link, i) => { if (copy.nav[i]) link.childNodes[0].nodeValue = copy.nav[i]; });

  document.querySelectorAll('[data-locale]').forEach((link) => {
    link.classList.toggle('active', link.getAttribute('data-locale') === locale);
  });

  const reveal = [...document.querySelectorAll('[data-error-reveal]')];
  if (!reveal.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    reveal.forEach((el) => el.classList.add('is-visible'));
    return;
  }
  document.body.classList.add('error-motion-ready');
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting)), {threshold: 0.12});
  reveal.forEach((el) => observer.observe(el));
})();
