(() => {
  const form = document.querySelector("[data-intake-form]");
  if (!form) return;

  const language = form.getAttribute("data-intake-lang") || "hu";
  const email = form.getAttribute("data-email") || "hello@axiona.systems";
  const status = form.querySelector("[data-intake-status]");
  const fallback = form.querySelector("[data-mailto-link]");

  const copy = {
    hu: {
      title: "AXIONA Systems — projekt egyeztetés",
      subject: "AXIONA projekt — első egyeztetés",
      safety: "Megjegyzés: az első kapcsolatfelvételnél nem szükséges érzékeny adatot küldeni.",
      ready: "Az e-mail elkészült. Ha a levelező nem nyílt meg automatikusan, használd az „E-mail megnyitása” linket."
    },
    en: {
      title: "AXIONA Systems — project enquiry",
      subject: "AXIONA project — first review",
      safety: "Note: sensitive information is not needed in the first message.",
      ready: "The email is ready. If your mail application did not open automatically, use the “Open email” link."
    },
    de: {
      title: "AXIONA Systems — Projektanfrage",
      subject: "AXIONA Projekt — erste Klärung",
      safety: "Hinweis: Für die erste Kontaktaufnahme sind keine sensiblen Daten erforderlich.",
      ready: "Die E-Mail ist vorbereitet. Falls sich Ihr Mailprogramm nicht automatisch geöffnet hat, verwenden Sie den Link „E-Mail öffnen“."
    }
  };

  const strings = copy[language] || copy.hu;

  const buildBody = () => {
    const lines = [strings.title, ""];
    form.querySelectorAll("[data-intake-field]").forEach((field) => {
      const value = (field.value || "").trim();
      if (!value) return;
      const label = field.getAttribute("data-intake-label") || field.name;
      lines.push(`${label}: ${value}`);
    });
    lines.push("", strings.safety);
    return lines.join("\n");
  };

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const href = `mailto:${email}?subject=${encodeURIComponent(strings.subject)}&body=${encodeURIComponent(buildBody())}`;
    if (fallback) {
      fallback.href = href;
      fallback.hidden = false;
    }
    if (status) status.textContent = strings.ready;

    window.location.href = href;
  });
})();
