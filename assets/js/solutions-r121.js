/* AXIONA R121 — repeatable, progressive-enhancement solutions reveal motion. */
(() => {
  const root = document.body;
  if (!root?.classList.contains('page-solutions-r121')) return;

  const selector = [
    '.services > .section-intro',
    '.service-editorial.website-service',
    '.solution-fit > .section-intro',
    '.solution-fit-card',
    '.solution-stack-copy',
    '.solution-layer-list article',
    '.solution-choice-copy',
    '.solution-choice-panel',
    '.development > .section-intro',
    '.keeper-solutions-card'
  ].join(',');

  const items = [...document.querySelectorAll(selector)];
  if (!items.length) return;
  items.forEach((item) => item.setAttribute('data-solutions-reveal', ''));

  const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  root.classList.add('solutions-motion-ready');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      entry.target.classList.toggle('is-visible', entry.isIntersecting);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -4% 0px' });

  items.forEach((item) => observer.observe(item));
})();
