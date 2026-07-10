/* Renders index.html headless and saves brand-board.png at 4800 px wide.
   Usage: node export.cjs [--preview]  (preview writes a 1200 px preview.png) */

const path = require("path");

function loadPlaywright() {
  try {
    return require("playwright");
  } catch (err) {
    return require("/opt/node22/lib/node_modules/playwright");
  }
}

const preview = process.argv.includes("--preview");
const outfile = preview ? "preview.png" : "brand-board.png";
const scale = preview ? 0.5 : 2;

(async () => {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 2400, height: 2076 },
    deviceScaleFactor: scale,
  });
  await page.goto("file://" + path.join(__dirname, "index.html"));
  await page.waitForFunction("window.__ready === true", null, { timeout: 30000 });
  await page.screenshot({ path: path.join(__dirname, outfile) });
  await browser.close();
  console.log("wrote " + outfile);
})();
