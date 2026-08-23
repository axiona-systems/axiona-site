/* AXIONA R124 — repeatable, progressive-enhancement policy reveal motion. */
(() => {
  const root = document.body;
  if (!root?.classList.contains('policy-r124')) return;

  const selector = [
    '.policy-hero > div',
    '.policy-summary',
    '.policy-intro',
    '.policy-card',
    '.policy-wide',
    '.policy-meta'
  ].join(',');
  const items = [...document.querySelectorAll(selector)];
  if (!items.length) return;

  items.forEach((item) => item.setAttribute('data-policy-reveal', ''));
  root.classList.add('policy-motion-ready');

  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting));
  }, { threshold: 0.1, rootMargin: '0px 0px -7% 0px' });

  items.forEach((item) => observer.observe(item));
})();
