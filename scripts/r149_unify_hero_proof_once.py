#!/usr/bin/env python3
from pathlib import Path

path = Path('scripts/verify_render_contract.mjs')
text = path.read_text(encoding='utf-8')

helper_start = text.find('async function verifyLocalizedHero(route, expectedLabel) {\n')
helper_end = text.find('\ntry {\n', helper_start)
if helper_start < 0 or helper_end < 0:
    raise SystemExit('STOP_R149_UNIFY_HELPER_RANGE')

helper = '''async function verifyHeroReveal(route, expectedLabel, widths) {
  const page = await open(route, 1440, 900);
  await page.waitForTimeout(5200);

  const heading = page.locator('body.page-overview .ax112-hero h1[id^="ax112-hero-title"]');
  if (await heading.count() !== 1) throw new Error(`${route}: hero heading missing`);
  if (await heading.getAttribute('data-ax-hero-type') !== 'complete') throw new Error(`${route}: hero reveal did not complete`);
  if (await heading.getAttribute('aria-label') !== expectedLabel) throw new Error(`${route}: hero accessible label mismatch`);

  const glyphs = heading.locator('.ax-hero-char');
  const words = heading.locator('.ax-hero-word');
  const expectedGlyphs = Array.from(expectedLabel.replace(/\\s/gu, '')).length;
  const expectedWords = expectedLabel.trim().split(/\\s+/u).length;
  if (await glyphs.count() !== expectedGlyphs || await words.count() !== expectedWords) {
    throw new Error(`${route}: hero tokenization mismatch`);
  }

  const binding = await page.evaluate(() => ({
    css: [...document.styleSheets].filter(sheet => (sheet.href || '').includes('/assets/visual-r116.css?release=R149')).length,
    js: [...document.scripts].filter(script => (script.src || '').includes('/assets/js/overview-r116.js?release=R149')).length
  }));
  if (binding.css !== 1 || binding.js !== 1) throw new Error(`${route}: R149 hero asset binding ${JSON.stringify(binding)}`);

  const brokenWords = await words.evaluateAll(nodes => nodes.filter(word => {
    const tops = [...word.querySelectorAll('.ax-hero-char')].map(glyph => glyph.getBoundingClientRect().top);
    return tops.length > 1 && Math.max(...tops) - Math.min(...tops) > 1;
  }).length);
  if (brokenWords !== 0) throw new Error(`${route}: hero word split count=${brokenWords}`);

  const secondLine = heading.locator(':scope > .ax-hero-second-line');
  for (const width of widths) {
    await page.setViewportSize({ width, height: width <= 640 ? 844 : 900 });
    await page.waitForTimeout(180);
    const fit = await secondLine.evaluate(element => {
      const tops = [...element.querySelectorAll('.ax-hero-char')].map(glyph => glyph.getBoundingClientRect().top);
      return {
        rows: tops.length ? Math.max(...tops) - Math.min(...tops) : 999,
        overflow: element.scrollWidth - element.clientWidth,
        fit: element.dataset.axHeroFit || '',
        fontSize: getComputedStyle(element).fontSize
      };
    });
    if (fit.rows > 1 || fit.overflow > 2 || !['native', 'scaled'].includes(fit.fit)) {
      throw new Error(`${route}: hero second line width=${width} ${JSON.stringify(fit)}`);
    }
    console.log(`OK_AXIONA_HERO_SECOND_LINE route=${route} width=${width} fit=${fit.fit} font=${fit.fontSize}`);
  }

  await page.waitForTimeout(800);
  const settled = await glyphs.evaluateAll(nodes => ({
    hidden: nodes.filter(node => Number.parseFloat(getComputedStyle(node).opacity) < .99).length,
    running: nodes.flatMap(node => node.getAnimations()).filter(animation => animation.playState === 'running').length,
    iterations: [...new Set(nodes.map(node => getComputedStyle(node).animationIterationCount))]
  }));
  if (settled.hidden !== 0 || settled.running !== 0 || settled.iterations.length !== 1 || settled.iterations[0] !== '1') {
    throw new Error(`${route}: hero reveal did not settle once ${JSON.stringify(settled)}`);
  }

  console.log(`OK_AXIONA_HERO_CHARACTER_REVEAL_ONCE route=${route}`);
  await page.close();
}
'''
text = text[:helper_start] + helper + text[helper_end:]

old_calls = "  await verifyLocalizedHero('/en/', 'Real problem. Working system.');\n  await verifyLocalizedHero('/de/', 'Reales Problem. Funktionierendes System.');"
new_calls = "  await verifyHeroReveal('/', 'Valódi problémára. Működő rendszer.', [390, 540, 760, 1024, 1280, 1440]);\n  await verifyHeroReveal('/en/', 'Real problem. Working system.', [390, 1440]);\n  await verifyHeroReveal('/de/', 'Reales Problem. Funktionierendes System.', [390, 1440]);"
if text.count(old_calls) != 1:
    raise SystemExit('STOP_R149_UNIFY_CALLS')
text = text.replace(old_calls, new_calls)

hu_start = text.find('    await page.waitForTimeout(4500);\n    const heroType =')
nodes_marker = "    const nodes = page.locator('[data-ax112-reveal]');"
hu_end = text.find(nodes_marker, hu_start)
if hu_start < 0 or hu_end < 0:
    raise SystemExit('STOP_R149_UNIFY_HU_RANGE')
text = text[:hu_start] + nodes_marker + text[hu_end + len(nodes_marker):]

path.write_text(text, encoding='utf-8')
