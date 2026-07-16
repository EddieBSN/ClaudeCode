/* Renders index.html headless and saves screenshots.
   desktop.png : 1440px viewport @2x  -> 2880px wide, full page
   mobile.png  :  375px viewport @2x  ->  750px wide, full page
   Usage: node export.cjs [--desktop] [--mobile]   (default: both) */

const path = require("path");

function loadPlaywright() {
  try { return require("playwright"); }
  catch (err) { return require("/opt/node22/lib/node_modules/playwright"); }
}

const only = process.argv.slice(2);
const doDesktop = only.length === 0 || only.includes("--desktop");
const doMobile = only.length === 0 || only.includes("--mobile");
const FILE = "file://" + path.join(__dirname, "index.html");

async function shoot(browser, { width, dsf, out }) {
  const page = await browser.newPage({
    viewport: { width, height: 900 },
    deviceScaleFactor: dsf,
  });
  await page.goto(FILE, { waitUntil: "load" });
  await page.waitForFunction("window.__ready === true", null, { timeout: 60000 });
  // Expand the viewport to the full content height and capture in a single
  // shot. This brings every reveal element into view so the
  // IntersectionObserver fires without a scroll sweep.
  const h = await page.evaluate(() => document.body.scrollHeight);
  await page.setViewportSize({ width, height: h });
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(900);
  await page.screenshot({ path: path.join(__dirname, out) });
  console.log("wrote " + out);
  await page.close();
}

(async () => {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  if (doDesktop) await shoot(browser, { width: 1440, dsf: 2, out: "desktop.png" });
  if (doMobile) await shoot(browser, { width: 375, dsf: 2, out: "mobile.png" });
  await browser.close();
})();
