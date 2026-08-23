/* AXIONA R108 — native share + cross-browser motion bootstrap. */
(() => {
  const motionStyleId = 'axiona-motion-r108';
  if (!document.getElementById(motionStyleId)) {
    const link = document.createElement('link');
    link.id = motionStyleId;
    link.rel = 'stylesheet';
    link.href = '/assets/motion-r108.css';
    document.head.appendChild(link);
  }

  const reduceMotion = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const revealSelectors = [
      '.fact-strip > div',
      '.section-intro',
      '.problem-spectrum-intro',
      '.problem-card',
      '.lifecycle-story-intro',
      '.lifecycle-board li',
      '.lifecycle-principle',
      '.keeper-preview-copy',
      '.keeper96-preview-row',
      '.system-board',
      '.service-copy',
      '.system-layer',
      '.control-depth-card',
      '.system-outcome-card',
      '.stage-list article',
      '.status-sheet',
      '.process-signal',
      '.process-clarity-copy',
      '.process-clarity-list article',
      '.process-handoff-grid article',
      '.method-list article',
      '.credit-card',
      '.security-baseline',
      '.security-trust-card',
      '.security-layer',
      '.solution-fit-card',
      '.solution-form',
      '.product-chain article',
      '.ax-share-copy',
      '.ax-share-controls'
    ].join(',');

    const boardSelectors = [
      '.system-board',
      '.status-sheet',
      '.lifecycle-board',
      '.problem-spectrum-board',
      '.keeper96-preview-panel',
      '.security-baseline'
    ].join(',');

    document.querySelectorAll(boardSelectors).forEach((element) => {
      element.classList.add('ax-motion-board');
    });

    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in-view');
        currentObserver.unobserve(entry.target);
      });
    }, { root: null, rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

    document.querySelectorAll(revealSelectors).forEach((element) => {
      element.classList.add('ax-motion-node');
      const siblings = Array.from(element.parentElement?.children || []);
      const siblingIndex = Math.max(0, siblings.indexOf(element));
      element.style.setProperty('--ax-order', String(Math.min(siblingIndex, 6)));
      if (element.matches('.system-board,.status-sheet,.lifecycle-board,.problem-spectrum-board,.keeper96-preview-panel,.security-baseline')) {
        element.classList.add('ax-from-left');
      } else if (element.matches('.service-copy,.lifecycle-principle,.credit-card,.ax-share-controls')) {
        element.classList.add('ax-from-right');
      }
      observer.observe(element);
    });
  }

  const sections = document.querySelectorAll('.ax-share');
  if (!sections.length) return;

  const copyText = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const area = document.createElement('textarea');
    area.value = text;
    area.setAttribute('readonly', '');
    area.style.position = 'fixed';
    area.style.opacity = '0';
    document.body.appendChild(area);
    area.select();
    document.execCommand('copy');
    area.remove();
  };

  sections.forEach((section) => {
    const title = section.dataset.shareTitle || document.title;
    const text = section.dataset.shareText || '';
    const url = section.dataset.shareUrl || window.location.href;
    const copied = section.dataset.shareCopied || 'Link copied.';
    const failed = section.dataset.shareFailed || 'Could not copy the link.';
    const shareButton = section.querySelector('[data-share-native]');
    const copyButton = section.querySelector('[data-share-copy]');
    const fallback = section.querySelector('[data-share-fallback]');
    const email = section.querySelector('[data-share-email]');
    const linkedin = section.querySelector('[data-share-linkedin]');
    const whatsapp = section.querySelector('[data-share-whatsapp]');
    const status = section.querySelector('[data-share-status]');

    const message = text ? `${text}\n\n${url}` : url;
    if (email) email.href = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(message)}`;
    if (linkedin) linkedin.href = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
    if (whatsapp) whatsapp.href = `https://wa.me/?text=${encodeURIComponent(message)}`;

    const showFallback = () => {
      if (!fallback) return;
      fallback.hidden = false;
      fallback.querySelector('a,button')?.focus();
    };

    shareButton?.addEventListener('click', async () => {
      if (navigator.share) {
        try {
          await navigator.share({ title, text, url });
          return;
        } catch (error) {
          if (error && error.name === 'AbortError') return;
        }
      }
      showFallback();
    });

    copyButton?.addEventListener('click', async () => {
      try {
        await copyText(url);
        if (status) status.textContent = copied;
      } catch (_) {
        if (status) status.textContent = failed;
      }
    });
  });
})();
