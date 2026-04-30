(function(){
  'use strict';
  var allowed = {hu:true,en:true};
  function currentLang(){
    var p = new URLSearchParams(window.location.search);
    var q = String(p.get('lang') || '').toLowerCase();
    var s = '';
    try { s = String(localStorage.getItem('axiona_lang') || '').toLowerCase(); } catch(e) {}
    return allowed[q] ? q : (allowed[s] ? s : 'en');
  }
  function applyLang(lang){
    document.documentElement.classList.remove('lang-hu','lang-en','no-js');
    document.documentElement.classList.add('js','lang-' + lang);
    document.documentElement.setAttribute('lang', lang);
    try { localStorage.setItem('axiona_lang', lang); } catch(e) {}
    var btn = document.getElementById('langToggle');
    if (btn) {
      btn.textContent = lang === 'hu' ? 'EN' : 'HU';
      btn.setAttribute('aria-label', lang === 'hu' ? 'Switch to English' : 'Váltás magyarra');
    }
  }
  function updateUrlLang(lang){
    var u = new URL(window.location.href);
    u.searchParams.set('lang', lang);
    window.history.replaceState({}, '', u.pathname + u.search + u.hash);
  }
  function inheritLangToLinks(lang){
    document.querySelectorAll('a[href]').forEach(function(a){
      var href = a.getAttribute('href') || '';
      if (!href || href.charAt(0)==='#' || href.indexOf('mailto:')===0 || href.indexOf('tel:')===0) return;
      if (/^https?:\/\//i.test(href)) return;
      try {
        var u = new URL(href, window.location.href);
        u.searchParams.set('lang', lang);
        a.setAttribute('href', u.pathname + u.search + u.hash);
      } catch(e) {}
    });
  }
  function wireLanguage(){
    var lang = currentLang();
    applyLang(lang);
    inheritLangToLinks(lang);
    var btn = document.getElementById('langToggle');
    if (btn) {
      btn.addEventListener('click', function(){
        var next = currentLang() === 'hu' ? 'en' : 'hu';
        applyLang(next);
        updateUrlLang(next);
        inheritLangToLinks(next);
      });
    }
  }
  function wireEmailLinks(){
    document.querySelectorAll('[data-email-link]').forEach(function(a){
      var user = a.getAttribute('data-user') || '';
      var domain = a.getAttribute('data-domain') || '';
      var subject = a.getAttribute('data-subject') || '';
      if (!user || !domain) return;
      var addr = user + '@' + domain;
      a.setAttribute('href', 'mailto:' + addr + (subject ? '?subject=' + encodeURIComponent(subject) : ''));
      a.addEventListener('click', function(){ a.setAttribute('href', 'mailto:' + addr + (subject ? '?subject=' + encodeURIComponent(subject) : '')); });
    });
  }
  function markActive(){
    var file = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
    if (file === '') file = 'index.html';
    document.querySelectorAll('.navItem[href]').forEach(function(a){
      var href = (a.getAttribute('href') || '').split('?')[0].split('#')[0].split('/').pop().toLowerCase() || 'index.html';
      if (href === file) { a.classList.add('isActive'); a.setAttribute('aria-current','page'); }
      else { a.classList.remove('isActive'); a.removeAttribute('aria-current'); }
    });
  }
  function setYear(){
    var y = document.getElementById('year');
    if (y) y.textContent = String(new Date().getFullYear());
  }
  function main(){ wireLanguage(); wireEmailLinks(); markActive(); setYear(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', main); else main();
})();
