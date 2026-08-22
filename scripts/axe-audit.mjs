import { chromium } from "playwright-core";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const axeSource = require.resolve("axe-core/axe.min.js");
const chromePath = process.env.CHROME_PATH;
const base = process.env.AXIONA_AUDIT_BASE || "http://127.0.0.1:4173";
const paths = [
  "/",
  "/systems.html",
  "/process.html",
  "/security.html",
  "/solutions.html",
  "/keeper.html",
  "/contact.html",
  "/support.html",
  "/privacy.html",
  "/legal.html",
  "/en/",
  "/en/systems.html",
  "/en/process.html",
  "/en/security.html",
  "/en/solutions.html",
  "/en/keeper.html",
  "/en/contact.html",
  "/en/support.html",
  "/en/privacy.html",
  "/en/legal.html",
  "/de/",
  "/de/systems.html",
  "/de/process.html",
  "/de/security.html",
  "/de/solutions.html",
  "/de/keeper.html",
  "/de/contact.html",
  "/de/support.html",
  "/de/privacy.html",
  "/de/legal.html"
];

if (!chromePath) {
  console.error("STOP_AXIONA_AXE_CHROME_PATH_MISSING");
  process.exit(2);
}

const browser = await chromium.launch({
  executablePath: chromePath,
  headless: true,
  args: ["--no-sandbox", "--disable-dev-shm-usage"]
});

let failed = false;
try {
  for (const route of paths) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    const page = await context.newPage();
    const url = new URL(route, base).href;
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 30000 });
    await page.addScriptTag({ path: path.resolve(axeSource) });

    const result = await page.evaluate(async () => {
      return await globalThis.axe.run(document, {
        runOnly: {
          type: "tag",
          values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"]
        }
      });
    });

    const blocking = result.violations.filter((violation) =>
      violation.impact === "critical" || violation.impact === "serious"
    );

    if (blocking.length) {
      failed = true;
      console.error(`STOP_AXIONA_AXE_ROUTE=${route}`);
      for (const violation of blocking) {
        console.error(`${violation.impact?.toUpperCase() || "UNKNOWN"} ${violation.id}: ${violation.help}`);
        for (const node of violation.nodes.slice(0, 5)) {
          console.error(`  target=${JSON.stringify(node.target)} summary=${node.failureSummary || ""}`);
        }
      }
    } else {
      console.log(`OK_AXIONA_AXE_ROUTE=${route} violations=${result.violations.length}`);
    }

    await context.close();
  }
} finally {
  await browser.close();
}

if (failed) {
  console.error("STOP_AXIONA_AXE_A11Y_FAILED");
  process.exit(1);
}

console.log("OK_AXIONA_AXE_A11Y_PASSED");
