/* AXIONA R120 — repeatable, progressive-enhancement security reveal motion. */
(() => {
  const root = document.documentElement;
  const selector = [
    '.security > .section-intro',
    '.security-layout',
    '.security-principles article',
    '.security-pledge',
    '.security-trust > .section-intro',
    '.security-trust-card',
    '.security-threats > .section-intro',
    '.security-threat',
    '.security-trust-proof-copy',
    '.security-proof-list article'
  ].join(',');
  const nodes = [...document.querySelectorAll(selector)];
  if (!nodes.length) return;

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('security-motion-ready');
  nodes.forEach((node) => node.setAttribute('data-security-reveal', ''));

  if (reduced || !('IntersectionObserver' in window)) {
    nodes.forEach((node) => node.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      entry.target.classList.toggle('is-visible', entry.isIntersecting);
    }
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -5% 0px'
  });

  nodes.forEach((node) => observer.observe(node));
})();
