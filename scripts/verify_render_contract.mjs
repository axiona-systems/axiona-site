// v4 megjelenítési szerződés: valódi böngészőben ellenőrzi az oldalakat.
// Minden sitemap-oldalon asztali és mobil nézetben: nincs vízszintes kilógás,
// egy h1, látható fejléc, nincs konzolhiba és nincs külső hálózati kérés.
// Ezen felül: a mobilmenü nyílik, a hero nyugtája végigfut, a Napló-szűrő szűr,
// és a lazy képek betöltődnek.
import { chromium } from "playwright-core";
import { readFileSync } from "node:fs";

const base = process.env.AXIONA_BASE || "http://127.0.0.1:4176";
const chromePath = process.env.CHROME_PATH;
if (!chromePath) throw new Error("STOP_AXIONA_RENDER_CHROME_MISSING");

const sitemap = readFileSync(new URL("../sitemap.xml", import.meta.url), "utf8");
const routes = [...sitemap.matchAll(/<loc>https:\/\/axiona\.systems([^<]*)<\/loc>/g)].map((m) => m[1] || "/");
if (routes.length < 15) throw new Error(`STOP_AXIONA_RENDER_ROUTES=${routes.length}`);

const browser = await chromium.launch({ executablePath: chromePath, headless: true, args: ["--no-sandbox"] });
const failures = [];
const fail = (msg) => failures.push(msg);

async function open(route, width, height, { reducedMotion = "no-preference" } = {}) {
  const context = await browser.newContext({ viewport: { width, height }, reducedMotion });
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", (e) => errors.push(String(e)));
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  await page.route("**/*", (req) => {
    const url = new URL(req.request().url());
    if (url.origin !== new URL(base).origin) { errors.push(`external request: ${url.href}`); return req.abort(); }
    return req.continue();
  });
  await page.goto(`${base}${route}`, { waitUntil: "networkidle" });
  return { page, context, errors };
}

for (const route of routes) {
  for (const [width, height, label] of [[1440, 900, "desktop"], [375, 812, "mobile"]]) {
    const { page, context, errors } = await open(route, width, height);
    const facts = await page.evaluate(() => ({
      overflow: document.documentElement.scrollWidth - window.innerWidth,
      h1: document.querySelectorAll("h1").length,
      header: !!document.querySelector(".site-header") && document.querySelector(".site-header").getBoundingClientRect().height > 0,
      main: !!document.querySelector("main#tartalom"),
    }));
    if (facts.overflow > 0) fail(`${route} ${label}: vízszintes kilógás ${facts.overflow}px`);
    if (facts.h1 !== 1) fail(`${route} ${label}: ${facts.h1} h1`);
    if (!facts.header || !facts.main) fail(`${route} ${label}: hiányzó fejléc vagy fő tartalom`);
    await page.evaluate(async () => {
      for (const img of document.images) img.loading = "eager";
      await Promise.all([...document.images].map((i) => i.complete ? 0 : new Promise((r) => { i.onload = i.onerror = r; })));
    });
    const broken = await page.evaluate(() => [...document.images].filter((i) => !i.naturalWidth).map((i) => i.getAttribute("src")));
    if (broken.length) fail(`${route} ${label}: be nem töltött kép: ${broken.join(", ")}`);
    if (label === "mobile") {
      const menu = page.locator("details.menu summary");
      if (await menu.isVisible()) {
        await menu.click();
        if (!(await page.locator("details.menu .menu__panel").isVisible())) fail(`${route}: a mobilmenü nem nyílik`);
      } else fail(`${route}: a mobilmenü nem látszik`);
    }
    for (const e of errors) fail(`${route} ${label}: ${e}`);
    await context.close();
  }
}

// A hero nyugtája végigfut, csökkentett mozgásnál azonnal kész.
for (const reducedMotion of ["no-preference", "reduce"]) {
  const { page, context } = await open("/", 1440, 900, { reducedMotion });
  await page.waitForTimeout(reducedMotion === "reduce" ? 100 : 3500);
  if (!(await page.locator(".receipt[data-print].is-printed").count())) fail(`hero nyugta nem fut végig (${reducedMotion})`);
  await context.close();
}

// A Napló-szűrő csak a kiválasztott terméket mutatja.
{
  const { page, context } = await open("/naplo/", 1440, 900);
  await page.click('button[data-filter="kockalmar"]');
  const kinds = await page.$$eval(".mslist > li", (els) => els.filter((e) => getComputedStyle(e).display !== "none").map((e) => e.dataset.kind));
  if (!kinds.length || kinds.some((k) => k !== "kockalmar")) fail(`Napló-szűrő hibás: ${kinds.join(",")}`);
  await context.close();
}

await browser.close();
if (failures.length) {
  for (const f of failures) console.error(`STOP_AXIONA_RENDER: ${f}`);
  process.exit(1);
}
console.log(`OK_AXIONA_RENDER_CONTRACT routes=${routes.length} viewports=2`);
