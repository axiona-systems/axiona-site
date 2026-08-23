/* AXIONA R116 — restore the overview share utility before share-r86 boots. */
(() => {
  const main = document.querySelector('body.page-overview main.ax112-home');
  if (!main || document.querySelector('.ax-share')) return;

  const lang = (document.documentElement.lang || document.querySelector('.site-shell')?.lang || 'hu').toLowerCase();
  const copy = {
    hu: {
      title: 'AXIONA Systems | Rendszerépítés és folyamattervezés',
      text: 'Rendszerépítés, folyamattervezés és egyedi digitális megoldások valós problémákra.',
      url: 'https://axiona.systems/',
      copied: 'Link másolva.',
      failed: 'A link másolása nem sikerült.',
      micro: 'TOVÁBBADNÁD?',
      heading: 'Hasznos lehet másnak is?',
      body: 'Ha valakinek van egy nehezen kezelhető folyamata, egyedi problémája vagy olyan ötlete, amelyhez megfelelő rendszer kellene, innen közvetlenül továbbküldheted az oldalt.',
      share: 'Megosztás',
      copy: 'Link másolása',
      fallback: 'Közvetlen megosztás',
      email: 'E-mail'
    },
    en: {
      title: 'AXIONA Systems | System and process design',
      text: 'System design, process design and custom digital solutions for real problems.',
      url: 'https://axiona.systems/en/',
      copied: 'Link copied.',
      failed: 'Could not copy the link.',
      micro: 'SHARE',
      heading: 'Know someone who might find this useful?',
      body: 'If someone has a difficult workflow, a specific problem or an idea that needs the right system, you can share this page directly.',
      share: 'Share',
      copy: 'Copy link',
      fallback: 'Other options',
      email: 'Email'
    },
    de: {
      title: 'AXIONA Systems | Systemaufbau und Prozessplanung',
      text: 'Systemaufbau, Prozessplanung und individuelle digitale Lösungen für reale Probleme.',
      url: 'https://axiona.systems/de/',
      copied: 'Link kopiert.',
      failed: 'Der Link konnte nicht kopiert werden.',
      micro: 'WEITEREMPFEHLEN',
      heading: 'Kennen Sie jemanden, für den das hilfreich sein könnte?',
      body: 'Wenn jemand einen schwierigen Ablauf, ein spezielles Problem oder eine Idee hat, für die ein passendes System fehlt, können Sie diese Seite direkt weitergeben.',
      share: 'Teilen',
      copy: 'Link kopieren',
      fallback: 'Weitere Möglichkeiten',
      email: 'E-Mail'
    }
  }[lang] || null;

  if (!copy) return;

  const section = document.createElement('section');
  section.className = 'ax-share ax116-share section-pad';
  section.dataset.shareTitle = copy.title;
  section.dataset.shareText = copy.text;
  section.dataset.shareUrl = copy.url;
  section.dataset.shareCopied = copy.copied;
  section.dataset.shareFailed = copy.failed;
  section.innerHTML = `
    <div class="ax-share-copy">
      <span class="micro">${copy.micro}</span>
      <h2>${copy.heading}</h2>
      <p>${copy.body}</p>
    </div>
    <div class="ax-share-controls">
      <div class="ax-share-actions">
        <button class="ax-share-primary" type="button" data-share-native>${copy.share}<span>↗</span></button>
        <button class="ax-share-copy-button" type="button" data-share-copy>${copy.copy}</button>
      </div>
      <div class="ax-share-fallback" data-share-fallback hidden>
        <span>${copy.fallback}</span>
        <div class="ax-share-fallback-links">
          <a data-share-email href="#">${copy.email}</a>
          <a data-share-linkedin href="#" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          <a data-share-whatsapp href="#" target="_blank" rel="noopener noreferrer">WhatsApp</a>
        </div>
      </div>
      <p class="ax-share-status" data-share-status aria-live="polite"></p>
    </div>`;

  main.appendChild(section);
})();
