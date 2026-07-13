# Waitlist Hero — Understory

Screen 1 of an editorial product-screen series: a split waitlist hero recreating a
shared design language (paper backgrounds, an editorial serif over a quiet grotesk,
hairline UI, one handcrafted image carrying the whole identity) with an original
invented brand. Everything is generated in code. No stock images, no photos, no AI
image generation. The only external resource is Google Fonts, embedded as woff2 data
URIs so the HTML is fully self-contained.

## The brand

**Understory** — a calm workspace for tending long-term, hand-made projects (the name
is the forest layer beneath the canopy, where things quietly grow). Glyph: a two-leaf
sprout beside the wordmark.

- **Paper** `#F3EEE4` · **body ink** `#2A2A24` · **accent** `#1C3B2A` deep forest green
- **Type:** Fraunces (editorial serif) for wordmark + headline; Inter (grotesk) for copy,
  labels, button, trust line
- **Headline:** "Something good is growing."

## The image

The right half carries the identity: a flat-vector editorial illustration of a person
absorbed in their phone among oversized foliage, a cropped classical building fragment,
coral poppies and a dawn sky, with real back-to-front depth and a cool phone-screen glow
on the hands and chin. It is generated externally (GPT Image 2) to prompts authored in
`asset-prompts.md` using the palette sampled from this page, then dropped in full bleed
(`object-fit: cover`, centered). A hand-built SVG version of the same scene remains in the
markup as a fallback if the raster fails to load, and the feTurbulence film grain stays in
code, layered on top of the image so it matches the rest of the page.

## Files

- `screen-1-waitlist.html` — 1600x1000 frame (fonts embedded; references `art/`)
- `art/hero-illustration.png` — generated hero illustration (1254x1254)
- `asset-prompts.md` — GPT Image 2 generation prompts + sampled palette
- `export.cjs` — headless render via Playwright + system Chromium
- `screen-1-waitlist.png` — 3200x2000 export

## Rendering

```bash
cd waitlist-hero
node export.cjs            # writes screen-1-waitlist.png at 3200x2000
node export.cjs --preview  # writes screen-1-preview.png at 1600x1000
```
