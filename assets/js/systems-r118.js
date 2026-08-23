/* AXIONA R118 — repeatable, progressive-enhancement reveal motion. */
(() => {
  const root = document.documentElement;
  const nodes = [...document.querySelectorAll('[data-system-reveal]')];
  if (!nodes.length) return;

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('systems-motion-ready');

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
