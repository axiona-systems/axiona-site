(() => {
  const form = document.querySelector('[data-intake-form]');
  if (!form) return;
  const output = form.querySelector('[data-summary-output]');
  const mailLink = form.querySelector('[data-mailto-link]');
  const email = form.getAttribute('data-email') || 'hello@axiona.systems';
  const getLabel = (field) => {
    const label = field.closest('label');
    if (!label) return field.name;
    return (label.childNodes[0]?.textContent || field.name).trim();
  };
  const build = () => {
    const fields = Array.from(form.querySelectorAll('input, select, textarea')).filter(el => el.name);
    const lines = ['AXIONA Systems intake', ''];
    fields.forEach(field => {
      const value = (field.value || '').trim();
      if (value) lines.push(`${getLabel(field)}: ${value}`);
    });
    lines.push('', 'Megjegyzés / Note: első kapcsolatfelvételnél nem szükséges érzékeny adatot küldeni.');
    return lines.join('\n');
  };
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const summary = build();
    if (output) output.value = summary;
    const subject = encodeURIComponent('AXIONA Systems intake');
    const body = encodeURIComponent(summary);
    if (mailLink) {
      mailLink.href = `mailto:${email}?subject=${subject}&body=${body}`;
      mailLink.classList.remove('disabled');
    }
  });
})();
