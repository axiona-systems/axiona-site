// AXIONA Systems — v4 oldalszkript. Követés, süti és hálózati hívás nélkül.
(() => {
  const root = document.documentElement;
  root.classList.add("js");
  const calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // A hero nyugtája soronként „kinyomtatódik”, a végén felvillan az ELLENŐRIZVE.
  document.querySelectorAll(".receipt[data-print]").forEach((card) => {
    card.querySelectorAll(".receipt__row, .receipt__stamp").forEach((row, i) => {
      row.style.setProperty("--i", String(i));
    });
    if (calm) {
      card.classList.add("is-printed");
    } else {
      requestAnimationFrame(() => requestAnimationFrame(() => card.classList.add("is-printed")));
    }
  });

  // Finom megjelenés görgetéskor; csökkentett mozgásnál azonnal a végállapot.
  const targets = document.querySelectorAll(".reveal, .product");
  if (calm || !("IntersectionObserver" in window)) {
    targets.forEach((el) => el.classList.add("is-in"));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.08 });
    targets.forEach((el) => io.observe(el));
  }

  // Napló-szűrő termék szerint.
  const filters = document.querySelector("[data-filters]");
  if (filters) {
    const entries = document.querySelectorAll("[data-kind]");
    filters.hidden = false;
    filters.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-filter]");
      if (!button) return;
      const value = button.dataset.filter;
      filters.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
      entries.forEach((entry) => {
        entry.hidden = value !== "all" && entry.dataset.kind !== value;
      });
    });
  }

  // A Kapcsolat oldalon a ?tema= paraméter előre kiválasztja a témát.
  const topic = new URLSearchParams(location.search).get("tema");
  if (topic) {
    const option = document.querySelector(`select[name="tema"] option[data-key="${CSS.escape(topic)}"]`);
    if (option) option.selected = true;
  }

  // Levél-előkészítő: a mezőkből e-mailt állít össze a látogató saját levelezőjében.
  document.querySelectorAll("form[data-mailto]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const message = form.uzenet.value.trim();
      if (!message) {
        form.uzenet.focus();
        return;
      }
      const name = form.nev ? form.nev.value.trim() : "";
      const topic = form.tema ? form.tema.value : "Kérdés";
      const body = name ? `${message}\n\n${name}` : message;
      window.location.href =
        `mailto:${form.dataset.mailto}` +
        `?subject=${encodeURIComponent(topic)}` +
        `&body=${encodeURIComponent(body)}`;
    });
  });
})();
