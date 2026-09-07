#!/usr/bin/env python3
from pathlib import Path

path = Path('scripts/verify_render_contract.mjs')
text = path.read_text(encoding='utf-8')

open_anchor = "async function open(route, width, height) {\n  const page = await browser.newPage({ viewport: { width, height } });\n  await page.route('https://**/*', request => request.abort());\n  await page.goto(`${base}${route}`, { waitUntil: 'networkidle' });\n  return page;\n}\n"
if text.count(open_anchor) != 1:
    raise SystemExit('STOP_R149_DEDUPE_OPEN_ANCHOR')

helper = '''
async function verifyLocalizedHero(route, expectedLabel) {
  const page = await open(route, 1440, 900);
  await page.waitForTimeout(5200);

  const heading = page.locator('body.page-overview .ax112-hero h1[id^="ax112-hero-title"]');
  if (await heading.count() !== 1) throw new Error(`${route}: localized hero heading missing`);
  if (await heading.getAttribute('data-ax-hero-type') !== 'complete') {
    throw new Error(`${route}: localized hero did not complete`);
  }
  if (await heading.getAttribute('aria-label') !== expectedLabel) {
    throw new Error(`${route}: localized hero accessible label mismatch`);
  }

  const glyphs = heading.locator('.ax-hero-char');
  const expectedGlyphs = Array.from(expectedLabel.replace(/\\s/gu, '')).length;
  if (await glyphs.count() !== expectedGlyphs) {
    throw new Error(`${route}: localized hero glyph count mismatch`);
  }

  const assetBinding = await page.evaluate(() => ({
    css: [...document.styleSheets].filter(sheet => (sheet.href || '').includes('/assets/visual-r116.css?release=R149')).length,
    js: [...document.scripts].filter(script => (script.src || '').includes('/assets/js/overview-r116.js?release=R149')).length
  }));
  if (assetBinding.css !== 1 || assetBinding.js !== 1) {
    throw new Error(`${route}: localized R149 asset binding ${JSON.stringify(assetBinding)}`);
  }

  const secondLine = heading.locator(':scope > .ax-hero-second-line');
  const assertSecondLine = async label => {
    const fit = await secondLine.evaluate(element => {
      const tops = [...element.querySelectorAll('.ax-hero-char')].map(glyph => glyph.getBoundingClientRect().top);
      return {
        rows: tops.length ? Math.max(...tops) - Math.min(...tops) : 999,
        overflow: element.scrollWidth - element.clientWidth,
        fit: element.dataset.axHeroFit || ''
      };
    });
    if (fit.rows > 1 || fit.overflow > 2 || !['native', 'scaled'].includes(fit.fit)) {
      throw new Error(`${route}: localized hero ${label} fit ${JSON.stringify(fit)}`);
    }
  };

  await assertSecondLine('desktop');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(180);
  await assertSecondLine('mobile');
  await page.waitForTimeout(800);

  const settled = await glyphs.evaluateAll(nodes => ({
    hidden: nodes.filter(node => Number.parseFloat(getComputedStyle(node).opacity) < .99).length,
    running: nodes.flatMap(node => node.getAnimations()).filter(animation => animation.playState === 'running').length,
    iterations: [...new Set(nodes.map(node => getComputedStyle(node).animationIterationCount))]
  }));
  if (settled.hidden !== 0 || settled.running !== 0 || settled.iterations.length !== 1 || settled.iterations[0] !== '1') {
    throw new Error(`${route}: localized hero did not settle once ${JSON.stringify(settled)}`);
  }

  console.log(`OK_AXIONA_LOCALIZED_HERO_REVEAL_ONCE route=${route}`);
  await page.close();
}
'''
text = text.replace(open_anchor, open_anchor + helper)

start = "  for (const [route, expectedLabel] of [['/en/', 'Real problem. Working system.'], ['/de/', 'Reales Problem. Funktionierendes System.']]) {\n"
end = "\n\n  {\n    const page = await open('/', 1440, 900);\n"
start_index = text.find(start)
end_index = text.find(end, start_index)
if start_index < 0 or end_index < 0:
    raise SystemExit('STOP_R149_DEDUPE_LOOP_RANGE')
replacement = "  await verifyLocalizedHero('/en/', 'Real problem. Working system.');\n  await verifyLocalizedHero('/de/', 'Reales Problem. Funktionierendes System.');"
text = text[:start_index] + replacement + text[end_index:]
path.write_text(text, encoding='utf-8')
