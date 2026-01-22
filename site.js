(function () {
  "use strict";

  const DEFAULT_LANG = "hu";
  const ALLOWED = new Set(["hu", "en"]);

  function getLang() {
    const u = new URL(window.location.href);
    const raw = (u.searchParams.get("lang") || "").toLowerCase();
    return ALLOWED.has(raw) ? raw : DEFAULT_LANG;
  }

  function setLang(lang) {
    const u = new URL(window.location.href);
    u.searchParams.set("lang", lang);
    window.location.href = u.toString();
  }

  function forcedDisplayFor(el) {
    const tag = (el.tagName || "").toUpperCase();
    if (tag === "SPAN" || tag === "B" || tag === "I" || tag === "EM" || tag === "STRONG") return "inline";
    if (tag === "LI") return "list-item";
    return "block";
  }

  function toggleLangBlocks(lang) {
    document.querySelectorAll("[data-lang]").forEach((el) => {
      const v = (el.getAttribute("data-lang") || "").toLowerCase();
      if (!ALLOWED.has(v)) return;

      if (v === lang) {
        el.style.display = forcedDisplayFor(el);
        el.style.visibility = "visible";
        el.style.opacity = "1";
        el.removeAttribute("aria-hidden");
      } else {
        el.style.display = "none";
        el.setAttribute("aria-hidden", "true");
      }
    });

    document.documentElement.setAttribute("lang", lang);
  }

  function inheritLangToLinks(lang) {
    document.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href");
      if (!href) return;
      if (href.startsWith("#")) return;
      if (href.startsWith("mailto:") || href.startsWith("tel:")) return;
      if (href.startsWith("http://") || href.startsWith("https://")) return;

      try {
        const u = new URL(href, window.location.href);
        u.searchParams.set("lang", lang);
        a.setAttribute("href", u.pathname + u.search + u.hash);
      } catch (_) { }
    });
  }

  function markActiveNav() {
    const nav = document.querySelector("nav.nav");
    if (!nav) return;

    const raw = (location.pathname || "").split("/").pop() || "";
    const page = ((raw.trim() === "") ? "index.html" : raw.trim()).toLowerCase();

    const items = Array.from(nav.querySelectorAll(".navItem"));
    if (!items.length) return;

    // clear ALL
    items.forEach((el) => {
      el.classList.remove("isActive");
      el.removeAttribute("aria-current");
    });

    const links = items.filter((el) => el.tagName && el.tagName.toUpperCase() === "A");
    const match = links.find((a) => {
      const href = (a.getAttribute("href") || "").split("?")[0].split("#")[0].trim();
      const base = (href.split("/").pop() || "").toLowerCase();
      return base === page;
    });

    const fallback = match || links.find((a) => ((a.getAttribute("href") || "").split("?")[0].split("#")[0].toLowerCase().endsWith("index.html")));

    if (fallback) {
      fallback.classList.add("isActive");
      fallback.setAttribute("aria-current", "page");
    }
  }

  function normalizeProofDisabled(lang) {
    const msg =
      lang === "hu"
        ? "Disabled (publikus-safe összefoglaló még nincs kint)"
        : "Disabled (public-safe summary not published yet)";

    document.querySelectorAll("[data-proof='disabled']").forEach((el) => {
      if (el.tagName && el.tagName.toUpperCase() === "SPAN") {
        el.setAttribute("title", msg);
        return;
      }
      el.textContent = msg;
      el.setAttribute("title", msg);
    });
  }

  function wireLangToggle(lang) {
    const btn = document.getElementById("langToggle");
    if (!btn) return;

    btn.textContent = lang.toUpperCase();

    btn.addEventListener("click", () => {
      const next = lang === "hu" ? "en" : "hu";
      setLang(next);
    });
  }

  function escapeHtml(s) {
    return String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function injectFooter(lang) {
    const host = document.getElementById("siteFooter");
    if (!host) return;

    const brand = host.getAttribute("data-footer-brand") || "© AXIONA Systems — engineering baseline";
    const email = host.getAttribute("data-footer-email") || "hello@axiona.systems";

    const now = new Date();
    const pad = (n) => String(n).padStart(2, "0");
    const lastUpdated = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())} ${pad(
      now.getHours()
    )}:${pad(now.getMinutes())}`;

    const credit =
      lang === "hu"
        ? `Fejlesztés / kivitelezés: Asztalos Zoltán • ${email}`
        : `Built by: Zoltán Asztalos • ${email}`;

    host.innerHTML = `
      <footer class="site-footer">
        <div class="footer-row">${escapeHtml(brand)}</div>
        <div class="footer-row">${escapeHtml(credit)}</div>
        <div class="footer-row">Last updated: ${escapeHtml(lastUpdated)}</div>
      </footer>
    `;
  }

  function getTopbarOffsetPx() {
    const top = document.querySelector(".topbar");
    if (!top) return 0;
    const r = top.getBoundingClientRect();
    // small breathing room
    return Math.round(r.height + 10);
  }

  function scrollToHashIfAny() {
    const hash = (location.hash || "").trim();
    if (!hash || hash.length < 2) return;

    const id = decodeURIComponent(hash.slice(1));
    const el = document.getElementById(id);
    if (!el) return;

    const offset = getTopbarOffsetPx();
    const y = window.scrollY + el.getBoundingClientRect().top - offset;

    window.scrollTo({ top: y, behavior: "auto" });
  }

  function wireHashClicks() {
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener("click", (e) => {
        const href = a.getAttribute("href") || "";
        if (!href.startsWith("#") || href.length < 2) return;

        const id = decodeURIComponent(href.slice(1));
        const el = document.getElementById(id);
        if (!el) return;

        e.preventDefault();

        history.replaceState(null, "", href);
        const offset = getTopbarOffsetPx();
        const y = window.scrollY + el.getBoundingClientRect().top - offset;

        window.scrollTo({ top: y, behavior: "smooth" });
      });
    });
  }

  function main() {
    const lang = getLang();
    toggleLangBlocks(lang);
    inheritLangToLinks(lang);
    wireLangToggle(lang);
    markActiveNav();
    normalizeProofDisabled(lang);
    injectFooter(lang);

    // hash offset handling
    wireHashClicks();
    // after layout settles
    setTimeout(scrollToHashIfAny, 0);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", main);
  } else {
    main();
  }
})();

