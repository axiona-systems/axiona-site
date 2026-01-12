/* site.js — AXIONA x SENTRA shared (footer + lastUpdated + HU/EN toggle)
   - No storage, hash only (#lang=hu|en)
   - Footer injected into #siteFooter (if present)
*/
(function () {
  function pad2(n){ return String(n).padStart(2, '0'); }

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

  function escapeHtml(s){
    return String(s)
      .replaceAll('&','&amp;')
      .replaceAll('<','&lt;')
      .replaceAll('>','&gt;')
      .replaceAll('"','&quot;')
      .replaceAll("'","&#39;");
  }

  function initLangToggle(){
    const HU = document.getElementById('HU');
    const EN = document.getElementById('EN');
    const btn = document.getElementById('langToggle');
    if (!HU || !EN || !btn) return;

    function setLang(code){
      if (code === 'EN'){
        EN.classList.add('isOn');
        HU.classList.remove('isOn');
        btn.textContent = 'EN';
      } else {
        HU.classList.add('isOn');
        EN.classList.remove('isOn');
        btn.textContent = 'HU';
      }
      try { location.hash = (code === 'EN') ? '#lang=en' : '#lang=hu'; } catch(e){}
    }

    const h = (location.hash || '').toLowerCase();
    if (h.includes('lang=en')) setLang('EN'); else setLang('HU');

    btn.addEventListener('click', function(){
      const now = (btn.textContent || 'HU').trim().toUpperCase();
      setLang(now === 'HU' ? 'EN' : 'HU');
    });
  }

  function boot(){
    injectFooter();
    const stamp = buildStamp();
    setLastUpdated(stamp);
    initLangToggle();
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
