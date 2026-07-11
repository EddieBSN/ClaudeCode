/* Renders index.html headless and saves each 1920x1080 frame as a PNG.
   Usage: node export.cjs [--preview]
   Default writes kestrel.png, halcyon.png, voltra.png, vesper.png at
   3840x2160. --preview writes *-preview.png at 1920x1080 plus bench.png
   with the 32 px mark tests. */

const path = require("path");

function loadPlaywright() {
  try {
    return require("playwright");
  } catch (err) {
    return require("/opt/node22/lib/node_modules/playwright");
  }
}

const preview = process.argv.includes("--preview");
const brands = ["kestrel", "halcyon", "voltra", "vesper"];

(async () => {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 2020, height: 1240 },
    deviceScaleFactor: preview ? 1 : 2,
  });
  await page.goto("file://" + path.join(__dirname, "index.html"));
  await page.waitForFunction("window.__ready === true", null, { timeout: 60000 });

  for (const b of brands) {
    const out = b + (preview ? "-preview" : "") + ".png";
    await page.locator("#frame-" + b).screenshot({ path: path.join(__dirname, out) });
    console.log("wrote " + out);
  }

  if (preview) {
    for (const b of brands) {
      await page.locator("#bench-" + b).screenshot({ path: path.join(__dirname, "bench-" + b + ".png") });
    }
    console.log("wrote bench-*.png");
    const widths = await page.evaluate(() =>
      Array.from(document.querySelectorAll(".frame")).map(f => ({
        id: f.id,
        pct: Math.round(f.querySelector(".lockup").getBoundingClientRect().width / 1920 * 1000) / 10,
      })));
    console.log("lockup widths (% of frame):", JSON.stringify(widths));
  }

  await browser.close();
})();
