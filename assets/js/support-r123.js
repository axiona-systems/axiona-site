/* AXIONA R123 — repeatable, progressive-enhancement support reveal motion. */
(() => {
  const root = document.body;
  if (!root?.classList.contains('page-support-r123')) return;

  const selector = [
    '.method > .section-intro',
    '.method-list article',
    '.credit-card',
    '.anatomy > .section-intro',
    '.stage-list article',
    '.contact.standalone-contact > div',
    '.contact.standalone-contact > aside'
  ].join(',');
  const items = [...document.querySelectorAll(selector)];
  if (!items.length) return;

  items.forEach((item) => item.setAttribute('data-support-reveal', ''));
  root.classList.add('support-motion-ready');

  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting));
  }, { threshold: 0.12, rootMargin: '0px 0px -7% 0px' });

  items.forEach((item) => observer.observe(item));
})();
