/* site.js — AXIONA x SENTRA shared
   - Language persistence via URL query param: ?lang=hu|en
   - No storage.
   - Auto-propagates ?lang=... to all internal links (AXIONA <-> SENTRA)
   - Footer injected into #siteFooter (if present)
*/
(function () {
  function pad2(n){ return String(n).padStart(2, '0'); }

  function escapeHtml(s){
    return String(s)
      .replaceAll('&','&amp;')
      .replaceAll('<','&lt;')
      .replaceAll('>','&gt;')
      .replaceAll('"','&quot;')
      .replaceAll("'","&#39;");
  }

  function getLangFromUrl(){
    try {
      const u = new URL(location.href);
      const q = (u.searchParams.get('lang') || '').toLowerCase();
      if (q === 'en') return 'EN';
      if (q === 'hu') return 'HU';
    } catch(e){}

    // fallback: old hash format (#lang=en|hu)
    const h = (location.hash || '').toLowerCase();
    if (h.includes('lang=en')) return 'EN';
    return 'HU';
  }

  function setLangInUrl(code){
    try {
      const u = new URL(location.href);
      u.searchParams.set('lang', (code === 'EN') ? 'en' : 'hu');
      // keep existing hash (anchors)
      history.replaceState(null, '', u.toString());
    } catch(e){}
  }

  function buildStamp(){
    const d = new Date(document.lastModified);
    return `${d.getFullYear()}-${pad2(d.getMonth()+1)}-${pad2(d.getDate())} ${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
  }

  function setLastUpdated(stamp){
    const nodes = document.querySelectorAll('[data-last-updated], #lastUpdated');
    nodes.forEach(n => { n.textContent = stamp; });
  }

  function injectFooter(){
    const host = document.getElementById('siteFooter');
    if (!host) return;

    const text = host.getAttribute('data-footer-text') || '© AXIONA Systems — SENTRA design baseline';

    host.innerHTML = `
      <footer class="footer">
        <div class="muted">${escapeHtml(text)}</div>
        <div class="muted small">
          Last updated: <span data-last-updated></span>
        </div>
      </footer>
    `;
  }

  function applyLangUI(code){
    const HU = document.getElementById('HU');
    const EN = document.getElementById('EN');
    const btn = document.getElementById('langToggle');
    if (!HU || !EN || !btn) return;

    if (code === 'EN'){
      EN.classList.add('isOn');
      HU.classList.remove('isOn');
      btn.textContent = 'EN';
      document.documentElement.setAttribute('lang', 'en');
    } else {
      HU.classList.add('isOn');
      EN.classList.remove('isOn');
      btn.textContent = 'HU';
      document.documentElement.setAttribute('lang', 'hu');
    }
  }

  function updateInternalLinks(code){
    const lang = (code === 'EN') ? 'en' : 'hu';

    document.querySelectorAll('a[href]').forEach(a => {
      const href = a.getAttribute('href');
      if (!href) return;

      // skip anchors, mailto, tel, javascript
      const low = href.toLowerCase();
      if (low.startsWith('#') || low.startsWith('mailto:') || low.startsWith('tel:') || low.startsWith('javascript:')) return;

      try {
        const u = new URL(href, location.href);

        // only same-origin
        if (u.origin !== location.origin) return;

        // set/override lang
        u.searchParams.set('lang', lang);

        // keep any existing hash
        a.setAttribute('href', u.pathname + (u.search ? u.search : '') + (u.hash ? u.hash : ''));
      } catch(e){}
    });
  }

  function initLangToggle(codeInitial){
    const btn = document.getElementById('langToggle');
    if (!btn) return;

    btn.addEventListener('click', function(){
      const now = (btn.textContent || 'HU').trim().toUpperCase();
      const next = (now === 'HU') ? 'EN' : 'HU';
      setLangInUrl(next);
      applyLangUI(next);
      updateInternalLinks(next);
    });

    // initial apply
    setLangInUrl(codeInitial);
    applyLangUI(codeInitial);
    updateInternalLinks(codeInitial);
  }

  function boot(){
    injectFooter();
    const stamp = buildStamp();
    setLastUpdated(stamp);

    const code = getLangFromUrl();
    initLangToggle(code);
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
