/* AXIONA R140 — restrained bidirectional scroll reveal coordinator. */
(() => {
  const selector = [
    '[data-ax112-reveal]',
    '[data-system-reveal]',
    '[data-process-reveal]',
    '[data-security-reveal]',
    '[data-solutions-reveal]',
    '[data-contact-reveal]',
    '[data-support-reveal]',
    '[data-keeper125-reveal]',
    '[data-policy-reveal]'
  ].join(',');

  const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const nodes = [...document.querySelectorAll(selector)];
  if (!nodes.length) return;

  const distance = () => window.matchMedia('(max-width: 680px)').matches ? 6 : 9;
  const setEntrySide = (node, side) => {
    const y = side === 'top' ? -distance() : distance();
    node.style.setProperty('--ax-r140-entry-y', `${y}px`);
  };
  const activate = (node) => {
    node.classList.add('ax-reveal-active');
    node.dataset.axR140Seen = '1';
  };
  const deactivate = (node) => node.classList.remove('ax-reveal-active');

  if (reduced || !('IntersectionObserver' in window)) {
    nodes.forEach(activate);
    return;
  }

  const viewportCutoff = window.innerHeight * 0.96;
  for (const node of nodes) {
    const rect = node.getBoundingClientRect();
    if (rect.bottom > 0 && rect.top < viewportCutoff) {
      activate(node);
    } else {
      setEntrySide(node, rect.bottom <= 0 ? 'top' : 'bottom');
    }
  }

  document.documentElement.classList.add('ax-motion-r140-ready');

  /* Entrance observer: animation starts only after the element is genuinely
     inside the viewport. It never owns the reset state. */
  const enterObserver = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      activate(entry.target);
    }
  }, {
    threshold: 0.04,
    rootMargin: '-2% 0px -3% 0px'
  });

  /* Reset observer: an already shown element is only armed for another glide
     after it has travelled well beyond the viewport. This wide hysteresis band
     prevents edge flicker while allowing a subtle return animation later. */
  const resetObserver = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      const node = entry.target;
      if (entry.isIntersecting || node.dataset.axR140Seen !== '1') continue;

      const rect = node.getBoundingClientRect();
      if (rect.bottom < -window.innerHeight * 0.28) {
        setEntrySide(node, 'top');
        deactivate(node);
      } else if (rect.top > window.innerHeight * 1.28) {
        setEntrySide(node, 'bottom');
        deactivate(node);
      }
    }
  }, {
    threshold: 0,
    rootMargin: '28% 0px 28% 0px'
  });

  nodes.forEach((node) => {
    enterObserver.observe(node);
    resetObserver.observe(node);
  });
})();
