import { chromium } from 'playwright-core';

const base = process.env.AXIONA_BASE || 'http://127.0.0.1:4176';
const chromePath = process.env.CHROME_PATH;
if (!chromePath) throw new Error('STOP_AXIONA_RENDER_CHROME_MISSING');

const browser = await chromium.launch({
  executablePath: chromePath,
  headless: true,
  args: ['--no-sandbox']
});

const primary = ['/', '/systems.html', '/process.html', '/security.html', '/solutions.html', '/contact.html'];
const auxiliary = ['/support.html', '/keeper.html', '/privacy.html', '/legal.html', '/en/', '/de/'];
const allRoutes = [...primary, ...auxiliary];

async function open(route, width, height) {
  const page = await browser.newPage({ viewport: { width, height } });
  await page.route('https://**/*', request => request.abort());
  await page.goto(`${base}${route}`, { waitUntil: 'networkidle' });
  return page;
}

try {
  for (const route of allRoutes) {
    for (const [label, width, height] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
      const page = await open(route, width, height);
      const result = await page.evaluate(() => {
        const styles = [...document.styleSheets].map(sheet => sheet.href || '');
        const scripts = [...document.scripts].map(script => script.src || '');
        const root = getComputedStyle(document.documentElement);
        const active = document.querySelector('.topbar nav a.active');
        return {
          main: document.querySelectorAll('main').length,
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          r137: styles.filter(url => url.includes('/assets/r137-ux-fixes.css?release=R137')).length,
          motionCss: styles.filter(url => url.includes('/assets/motion-r138.css?release=R142')).length,
          motionJs: scripts.filter(url => url.includes('/assets/js/motion-r138.js?release=R142')).length,
          stale: [...styles, ...scripts].filter(url => /r13[56]-ux-fixes/.test(url)).length,
          distance: root.getPropertyValue('--ax-r141-reveal-y').trim(),
          duration: root.getPropertyValue('--ax-r141-reveal-transform-duration').trim(),
          activeNav: document.querySelectorAll('.topbar nav a.active').length,
          activeAfter: active ? getComputedStyle(active, '::after').display : null
        };
      });

      if (result.main !== 1) throw new Error(`${route} ${label}: main count ${result.main}`);
      if (result.scrollWidth > result.clientWidth + 2) throw new Error(`${route} ${label}: horizontal overflow ${result.scrollWidth}/${result.clientWidth}`);
      if (result.r137 !== 1 || result.motionCss !== 1 || result.motionJs !== 1 || result.stale !== 0) {
        throw new Error(`${route} ${label}: canonical binding mismatch ${JSON.stringify(result)}`);
      }
      if (label === 'desktop' && (result.distance !== '7px' || result.duration !== '900ms')) {
        throw new Error(`${route}: desktop motion tuning ${result.distance}/${result.duration}`);
      }
      if (label === 'mobile' && (result.distance !== '5px' || result.duration !== '760ms')) {
        throw new Error(`${route}: mobile motion tuning ${result.distance}/${result.duration}`);
      }
      if (primary.includes(route) && label === 'desktop') {
        if (result.activeNav !== 1) throw new Error(`${route}: active desktop nav count ${result.activeNav}`);
        if (result.activeAfter !== 'none') throw new Error(`${route}: active nav pseudo still renders (${result.activeAfter})`);
      }
      console.log(`OK_RENDER route=${route} viewport=${label}`);
      await page.close();
    }
  }

  for (const width of [1280, 1440, 1728, 1920]) {
    const page = await open('/systems.html', width, 1000);
    const geometry = await page.evaluate(() => {
      const intro = document.querySelector('.services > .section-intro')?.getBoundingClientRect();
      const service = document.querySelector('.services > .system-service')?.getBoundingClientRect();
      if (!intro || !service) return null;
      const overlapX = Math.max(0, Math.min(intro.right, service.right) - Math.max(intro.left, service.left));
      const overlapY = Math.max(0, Math.min(intro.bottom, service.bottom) - Math.max(intro.top, service.top));
      return {
        overlap: overlapX * overlapY,
        clearance: service.top - intro.bottom,
        intro: { top: intro.top, bottom: intro.bottom },
        service: { top: service.top, bottom: service.bottom }
      };
    });
    if (!geometry) throw new Error(`systems ${width}: geometry nodes missing`);
    if (geometry.overlap > .5) throw new Error(`systems ${width}: overlap ${JSON.stringify(geometry)}`);
    if (width < 1800 && geometry.clearance < 30) throw new Error(`systems ${width}: clearance ${geometry.clearance}`);
    console.log(`OK_SYSTEMS_GEOMETRY width=${width} clearance=${geometry.clearance}`);
    await page.close();
  }

  {
    const page = await open('/', 1440, 900);
    const nodes = page.locator('[data-ax112-reveal]');
    const count = await nodes.count();
    let target = null;
    for (let index = 0; index < count; index++) {
      const box = await nodes.nth(index).boundingBox();
      if (box && box.y > 1300 && box.y < 2800) {
        target = nodes.nth(index);
        break;
      }
    }
    if (!target) throw new Error('overview: no mid-page reveal target');

    const armedBefore = await target.evaluate(element => {
      const matrix = new DOMMatrixReadOnly(getComputedStyle(element).transform);
      return {
        armed: element.classList.contains('ax-reveal-armed'),
        active: element.classList.contains('ax-reveal-active'),
        y: matrix.m42
      };
    });
    if (!armedBefore.armed || armedBefore.active || Math.abs(Math.abs(armedBefore.y) - 7) > .6) {
      throw new Error(`overview: initial armed state ${JSON.stringify(armedBefore)}`);
    }

    await target.scrollIntoViewIfNeeded();
    await page.waitForTimeout(1050);
    if (!(await target.evaluate(element => element.classList.contains('ax-reveal-active')))) {
      throw new Error('overview: first reveal did not activate');
    }

    const absoluteTop = await target.evaluate(element => element.getBoundingClientRect().top + window.scrollY);
    const far = await page.evaluate(y => Math.min(document.documentElement.scrollHeight - innerHeight, y + 1800), absoluteTop);
    await page.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), far);
    await page.waitForTimeout(450);
    const rearmed = await target.evaluate(element => {
      const matrix = new DOMMatrixReadOnly(getComputedStyle(element).transform);
      const rect = element.getBoundingClientRect();
      return {
        armed: element.classList.contains('ax-reveal-armed'),
        active: element.classList.contains('ax-reveal-active'),
        y: matrix.m42,
        bottom: rect.bottom
      };
    });
    if (!rearmed.armed || rearmed.active || Math.abs(Math.abs(rearmed.y) - 7) > .6) {
      throw new Error(`overview: return rearm failed ${JSON.stringify(rearmed)}`);
    }

    await target.scrollIntoViewIfNeeded();
    await page.waitForTimeout(1050);
    if (!(await target.evaluate(element => element.classList.contains('ax-reveal-active')))) {
      throw new Error('overview: return reveal did not activate');
    }
    console.log('OK_AXIONA_BIDIRECTIONAL_MOTION');
    await page.close();
  }

  console.log('OK_AXIONA_CURRENT_RENDER_CONTRACT');
} finally {
  await browser.close();
}
