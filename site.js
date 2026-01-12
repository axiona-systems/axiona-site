/* site.js — AXIONA x SENTRA shared
   - Language persistence via URL query param: ?lang=hu|en
   - No storage.
   - Auto-propagates ?lang=... to internal links
   - Footer injected into #siteFooter (developer/execution + email + last updated), localized
*/

(function () {
  function pad2(n) { return String(n).padStart(2, "0"); }

  function escapeHtml(s) {
    return String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  function getLangFromUrl() {
    try {
      const u = new URL(location.href);
      const q = (u.searchParams.get("lang") || "").toLowerCase();
      if (q === "en") return "EN";
      if (q === "hu") return "HU";
    } catch (e) {}
    return "HU";
  }

  function setLangInUrl(code) {
    try {
      const u = new URL(location.href);
      u.searchParams.set("lang", code === "EN" ? "en" : "hu");
      history.replaceState(null, "", u.toString());
    } catch (e) {}
  }

  function buildStamp() {
    const d = new Date(document.lastModified);
    return `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())} ${pad2(
      d.getHours()
    )}:${pad2(d.getMinutes())}`;
  }

  function applyLangUI(code) {
    const HU = document.getElementById("HU");
    const EN = document.getElementById("EN");
    const btn = document.getElementById("langToggle");
    if (!HU || !EN || !btn) return;

    if (code === "EN") {
      EN.classList.add("isOn");
      HU.classList.remove("isOn");
      btn.textContent = "EN";
      document.documentElement.setAttribute("lang", "en");
    } else {
      HU.classList.add("isOn");
      EN.classList.remove("isOn");
      btn.textContent = "HU";
      document.documentElement.setAttribute("lang", "hu");
    }
  }

  function updateInternalLinks(code) {
    const lang = code === "EN" ? "en" : "hu";

    document.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href");
      if (!href) return;

      const low = href.toLowerCase();
      if (
        low.startsWith("#") ||
        low.startsWith("mailto:") ||
        low.startsWith("tel:") ||
        low.startsWith("javascript:")
      )
        return;

      try {
        const u = new URL(href, location.href);
        if (u.origin !== location.origin) return;
        u.searchParams.set("lang", lang);
        a.setAttribute("href", u.pathname + (u.search ? u.search : "") + (u.hash ? u.hash : ""));
      } catch (e) {}
    });
  }

  function setLastUpdated(stamp) {
    document.querySelectorAll("[data-last-updated], #lastUpdated").forEach((n) => {
      n.textContent = stamp;
    });
  }

  function injectFooter(code) {
    const host = document.getElementById("siteFooter");
    if (!host) return;

    const email = host.getAttribute("data-footer-email") || "hello@axiona.systems";
    const brand = host.getAttribute("data-footer-brand") || "© AXIONA Systems — SENTRA design baseline";
    const name = host.getAttribute("data-footer-name") || "Asztalos Zoltán";

    const t = {
      HU: {
        dev: "Fejlesztés / kivitelezés",
        updated: "Last updated",
      },
      EN: {
        dev: "Developer / Execution",
        updated: "Last updated",
      },
    }[code === "EN" ? "EN" : "HU"];

    host.innerHTML = `
      <footer class="footer">
        <div class="muted">
          ${escapeHtml(brand)}
        </div>

        <div class="muted small" style="margin-top:6px;">
          ${escapeHtml(t.dev)}: ${escapeHtml(name)} ·
          <a href="mailto:${escapeHtml(email)}" style="color: rgba(134,163,255,0.92); text-decoration:none;">
            ${escapeHtml(email)}
          </a>
        </div>

        <div class="muted small" style="margin-top:6px;">
          ${escapeHtml(t.updated)}: <span data-last-updated></span>
        </div>
      </footer>
    `;
  }

  function initLangToggle(codeInitial) {
    const btn = document.getElementById("langToggle");
    if (!btn) return;

    btn.addEventListener("click", function () {
      const now = (btn.textContent || "HU").trim().toUpperCase();
      const next = now === "HU" ? "EN" : "HU";
      setLangInUrl(next);
      applyLangUI(next);
      updateInternalLinks(next);
      injectFooter(next);
      setLastUpdated(buildStamp());
    });

    setLangInUrl(codeInitial);
    applyLangUI(codeInitial);
    updateInternalLinks(codeInitial);
    injectFooter(codeInitial);
  }

  function boot() {
    const lang = getLangFromUrl();
    initLangToggle(lang);
    setLastUpdated(buildStamp());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
