/* AXIONA R122 — repeatable, progressive-enhancement contact reveal motion. */
(() => {
  const root = document.body;
  if (!root?.classList.contains('page-contact-r122')) return;

  const items = [...document.querySelectorAll([
    '.contact-intake-copy > .eyebrow',
    '.contact-intake-copy > h1',
    '.contact-intake-copy > .contact-lead',
    '.contact-fit',
    '.contact-support-link',
    '.contact-direct',
    '.intake-form'
  ].join(','))];
  if (!items.length) return;
  items.forEach((item) => item.setAttribute('data-contact-reveal', ''));

  const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  root.classList.add('contact-motion-ready');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting));
  }, { threshold: 0.12, rootMargin: '0px 0px -4% 0px' });
  items.forEach((item) => observer.observe(item));
})();
