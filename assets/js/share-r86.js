/* AXIONA R86 — native share with privacy-minimal fallbacks. */
(() => {
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
