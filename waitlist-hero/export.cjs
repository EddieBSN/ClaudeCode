/* Renders screen-1-waitlist.html headless and saves a PNG.
   Default: screen-1-waitlist.png at 3200x2000 (2x the 1600x1000 frame).
   --preview: screen-1-preview.png at 1600x1000.
   Usage: node export.cjs [--preview] */

const path = require("path");

function loadPlaywright() {
  try { return require("playwright"); }
  catch (err) { return require("/opt/node22/lib/node_modules/playwright"); }
}

const preview = process.argv.includes("--preview");

(async () => {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1600, height: 1000 },
    deviceScaleFactor: preview ? 1 : 2,
  });
  await page.goto("file://" + path.join(__dirname, "screen-1-waitlist.html"));
  await page.waitForFunction("window.__ready === true", null, { timeout: 60000 });

  const out = preview ? "screen-1-preview.png" : "screen-1-waitlist.png";
  await page.locator("#frame").screenshot({ path: path.join(__dirname, out) });
  console.log("wrote " + out);

  await browser.close();
})();
