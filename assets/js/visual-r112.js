/* AXIONA R112 — structural interaction layer. */
(() => {
  const reduced = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

  const revealNodes = document.querySelectorAll('[data-ax112-reveal]');
  if (!reduced && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
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

  const model = document.querySelector('.ax112-model');
  const visual = document.querySelector('.ax112-hero-visual');
  const finePointer = window.matchMedia?.('(pointer:fine)').matches;
  if (!reduced && model && visual && finePointer) {
    visual.addEventListener('pointermove', (event) => {
      const rect = visual.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      model.style.transform = `perspective(1300px) rotateY(${x * 3.2}deg) rotateX(${y * -2.5}deg) translate3d(${x * 5}px, ${y * 5}px, 0)`;
    }, { passive: true });
    visual.addEventListener('pointerleave', () => {
      model.style.transform = '';
    }, { passive: true });
  }
})();
