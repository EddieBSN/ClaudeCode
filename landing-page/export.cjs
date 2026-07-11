/* Renders index.html headless and saves full-page PNGs.
   Usage: node export.cjs [--preview]
   Writes desktop.png (2880 px wide) and mobile.png (750 px wide).
   --preview writes half-resolution desktop-preview.png / mobile-preview.png. */

const path = require("path");

function loadPlaywright() {
  try {
    return require("playwright");
  } catch (err) {
    return require("/opt/node22/lib/node_modules/playwright");
  }
}

const preview = process.argv.includes("--preview");

const shots = [
  { width: 1440, height: 900, scale: 2, out: "desktop.png" },
  { width: 375, height: 760, scale: 2, out: "mobile.png" },
];

(async () => {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  for (const shot of shots) {
    const scale = preview ? shot.scale / 2 : shot.scale;
    const out = preview ? shot.out.replace(".png", "-preview.png") : shot.out;
    const page = await browser.newPage({
      viewport: { width: shot.width, height: shot.height },
      deviceScaleFactor: scale,
    });
    // reveal everything and freeze transitions so the full-page shot is clean
    await page.addInitScript(() => {
      document.addEventListener("DOMContentLoaded", () => {
        document.documentElement.classList.add("no-anim");
      });
    });
    await page.goto("file://" + path.join(__dirname, "index.html"));
    await page.waitForFunction("window.__ready === true", null, { timeout: 30000 });
    await page.screenshot({ path: path.join(__dirname, out), fullPage: true });
    await page.close();
    console.log("wrote " + out);
  }
  await browser.close();
})();
