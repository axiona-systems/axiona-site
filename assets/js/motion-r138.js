/* AXIONA R141 — minimal bidirectional scroll reveal coordinator. */
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

  const distance = () => window.matchMedia('(max-width: 680px)').matches ? 5 : 7;
  const setEntrySide = (node, side) => {
    const y = side === 'top' ? -distance() : distance();
    node.style.setProperty('--ax-r141-entry-y', `${y}px`);
  };
  const activate = (node) => {
    node.classList.remove('ax-reveal-armed');
    node.classList.add('ax-reveal-active');
    node.dataset.axR141Seen = '1';
  };
  const arm = (node, side) => {
    setEntrySide(node, side);
    node.classList.remove('ax-reveal-active');
    node.classList.add('ax-reveal-armed');
  };

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
      arm(node, rect.bottom <= 0 ? 'top' : 'bottom');
    }
  }

  document.documentElement.classList.add('ax-motion-r141-ready');

  const enterObserver = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      activate(entry.target);
    }
  }, {
    threshold: 0.035,
    rootMargin: '-2% 0px -2% 0px'
  });

  /* 14% hysteresis: enough separation to prevent viewport-edge chatter while
     still allowing near-bottom sections to re-arm before the user scrolls back. */
  const resetObserver = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      const node = entry.target;
      if (entry.isIntersecting || node.dataset.axR141Seen !== '1') continue;

      const rect = node.getBoundingClientRect();
      if (rect.bottom < -window.innerHeight * 0.14) {
        arm(node, 'top');
      } else if (rect.top > window.innerHeight * 1.14) {
        arm(node, 'bottom');
      }
    }
  }, {
    threshold: 0,
    rootMargin: '14% 0px 14% 0px'
  });

  nodes.forEach((node) => {
    enterObserver.observe(node);
    resetObserver.observe(node);
  });
})();
