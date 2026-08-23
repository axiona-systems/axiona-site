/* AXIONA R138 — one-shot scroll reveal coordinator. */
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

  const settle = (node) => {
    node.classList.add('is-visible', 'ax-reveal-settled');
  };

  if (reduced || !('IntersectionObserver' in window)) {
    nodes.forEach(settle);
    return;
  }

  const viewportCutoff = window.innerHeight * 0.92;
  const pending = [];
  for (const node of nodes) {
    const rect = node.getBoundingClientRect();
    if (rect.bottom > 0 && rect.top < viewportCutoff) settle(node);
    else pending.push(node);
  }

  document.documentElement.classList.add('ax-motion-r138-ready');

  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      settle(entry.target);
      observer.unobserve(entry.target);
    }
  }, {
    threshold: 0.08,
    rootMargin: '0px 0px -8% 0px'
  });

  pending.forEach((node) => observer.observe(node));
})();
