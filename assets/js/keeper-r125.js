/* AXIONA R125 — repeatable, progressive-enhancement Keeper reveal motion. */
(() => {
  const root = document.body;
  if (!root?.classList.contains('page-keeper-r125')) return;
  const selector = [
    '.keeper96-hero > div',
    '.keeper96-workcard',
    '.keeper96-core-head',
    '.keeper96-question',
    '.keeper96-process-head',
    '.keeper96-process-step',
    '.keeper96-contrast-head',
    '.keeper96-compare',
    '.keeper96-examples-head',
    '.keeper96-example',
    '.keeper96-trust > div:first-child',
    '.keeper96-trust-card',
    '.keeper96-dev > div'
  ].join(',');
  const items = [...document.querySelectorAll(selector)];
  if (!items.length) return;
  items.forEach((item) => item.setAttribute('data-keeper125-reveal', ''));
  root.classList.add('keeper125-motion-ready');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting));
  }, { threshold: 0.1, rootMargin: '0px 0px -7% 0px' });
  items.forEach((item) => observer.observe(item));
})();
