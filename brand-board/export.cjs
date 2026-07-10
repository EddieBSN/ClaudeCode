/* Renders a board page headless and saves a PNG at 4800 px wide.
   Usage: node export.cjs [page.html] [--preview]
   Default page is index.html, exported as brand-board.png.
   Other pages export as <name>.png. --preview writes a 1200 px preview. */

const path = require("path");

function loadPlaywright() {
  try {
    return require("playwright");
  } catch (err) {
    return require("/opt/node22/lib/node_modules/playwright");
  }
}

const args = process.argv.slice(2);
const preview = args.includes("--preview");
const page_file = args.find((a) => a.endsWith(".html")) || "index.html";
const base = path.basename(page_file, ".html");
const fullname = base === "index" ? "brand-board.png" : base + ".png";
const previewname = base === "index" ? "preview.png" : base + "-preview.png";
const outfile = preview ? previewname : fullname;
const scale = preview ? 0.5 : 2;

(async () => {
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 2400, height: 2076 },
    deviceScaleFactor: scale,
  });
  await page.goto("file://" + path.join(__dirname, page_file));
  await page.waitForFunction("window.__ready === true", null, { timeout: 30000 });
  await page.screenshot({ path: path.join(__dirname, outfile) });
  await browser.close();
  console.log("wrote " + outfile);
})();
