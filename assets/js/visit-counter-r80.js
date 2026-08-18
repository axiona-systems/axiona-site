(() => {
  const compactMobileMenu = () => {
    if (!window.matchMedia("(max-width: 920px)").matches) return;
    document.querySelectorAll(".mobile-menu[open]").forEach((menu) => {
      menu.removeAttribute("open");
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", compactMobileMenu, { once: true });
  } else {
    compactMobileMenu();
  }

  try {
    const navigation = performance.getEntriesByType("navigation")[0];
    if (navigation && navigation.type !== "navigate") return;

    if (document.referrer) {
      const referrer = new URL(document.referrer);
      if (referrer.origin === window.location.origin) return;
    }

    fetch("https://yzhmqygbqitfqdabqkqr.supabase.co/functions/v1/visitor-count", {
      method: "POST",
      mode: "cors",
      credentials: "omit",
      cache: "no-store",
      referrerPolicy: "no-referrer",
      keepalive: true,
    }).catch(() => {});
  } catch (_) {
    // Site runtime helpers must never affect the website experience.
  }
})();
