/* AXIONA R115 — repeatable structural interaction layer. */
(() => {
  const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

  const revealNodes = document.querySelectorAll('[data-ax112-reveal]');
  if (!reduced && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        entry.target.classList.toggle('is-visible', entry.isIntersecting);
      }
    }, { threshold: 0.12, rootMargin: '0px 0px -7% 0px' });
    revealNodes.forEach((node) => revealObserver.observe(node));
  } else {
    revealNodes.forEach((node) => node.classList.add('is-visible'));
  }

  const steps = [...document.querySelectorAll('.ax112-step')];
  if (steps.length && 'IntersectionObserver' in window) {
    const stepObserver = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

      if (!visible) return;
      steps.forEach((step) => step.classList.toggle('is-current', step === visible.target));
    }, { threshold: [0.22, 0.45, 0.68], rootMargin: '-16% 0px -35% 0px' });
    steps.forEach((step) => stepObserver.observe(step));
  } else if (steps[0]) {
    steps[0].classList.add('is-current');
  }
})();
