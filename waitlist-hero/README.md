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

The right half is a single composed SVG scene (viewBox 880x1000) with real back-to-front
depth: a graduated dawn sky and soft top-left light; a cropped classical building
fragment; a canopy of desaturated fronds hanging from the top edge (atmospheric
perspective); midground foliage with per-leaf gradient modelling and veins, mixing
almond and tropical split-leaf shapes; a figure absorbed in their phone with a warm
screen-glow lighting the hands and chin; coral poppies; and oversized, darker,
higher-contrast foreground leaves. An feTurbulence film grain sits over everything.

## Files

- `screen-1-waitlist.html` — self-contained 1600x1000 frame (fonts embedded)
- `export.cjs` — headless render via Playwright + system Chromium
- `screen-1-waitlist.png` — 3200x2000 export

## Rendering

```bash
cd waitlist-hero
node export.cjs            # writes screen-1-waitlist.png at 3200x2000
node export.cjs --preview  # writes screen-1-preview.png at 1600x1000
```
