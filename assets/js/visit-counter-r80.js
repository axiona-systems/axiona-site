(() => {
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
    // Counting must never affect the website experience.
  }
})();
