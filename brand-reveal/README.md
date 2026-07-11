# Brand reveal frames

Four invented brands, each shown as a reveal frame: a pure white lockup
centered on a full-bleed generative background, in the style of a set of
reference frames. Everything is drawn in code: SVG marks, canvas-painted
backgrounds, Google Fonts wordmarks (embedded as woff2 data URIs, so the
page renders fully offline). No stock images, no AI image generation.

## The brands

| Brand | Mark construction | Wordmark | Background |
|-------|-------------------|----------|------------|
| **Kestrel** | one swept wing blade rotated 4x90, pinwheel negative center | Schibsted Grotesk 500, sentence case | duotone stipple: a falcon in a banking dive rendered as ultramarine dot density on paper white, with a pale carved motion corridor |
| **halcyon** | one lens petal rotated 8x45, eight-point star negative center | Fraunces 600, lowercase | soft aura: three ultra-soft warm fields (coral, peach, blush) melting into white at every edge |
| **voltra** | lowercase v knocked out of a rounded container | Hanken Grotesk 600, lowercase | grain airbrush: colliding sprayed fields of vermilion, coral red, ultramarine, sand, peach and near-black under dense film grain and a halftone hint |
| **Vesper** (TM) | one thin kite shard rotated 8x45, star-hole negative center | Inter 500, sentence case | dark glitch waveform: a spiked ribbon sweeping to a high crest, gray-blue body with an amber light edge, faint vertical streaks |

## Palettes

- Kestrel: paper `#EEF1F7`, dots `#2A44C8` to `#17298F`
- halcyon: white, coral `#F0837E`, peach `#F59E56`, blush `#F7B08B`
- voltra: vermilion `#F1481F`, coral red `#EF3E33`, ultramarine `#4152F0`,
  sand `#EBCF79`, peach `#F5C994`, near-black `#1A0E08`
- Vesper: field `#04070C`, spike body `#2E3C4C` to `#9FB2C6`,
  amber edge `#F2AE72`

## Lockup rules

Horizontal lockup, mark left, wordmark right, optically centered, total
width 25 to 30 percent of the 1920x1080 frame, solid white only. Each mark
is one geometric unit repeated by rotation into 4- or 8-fold symmetry (or
a letterform in a rounded container) and stays legible at 32 px; the page
renders that small test next to each frame. Subtle film grain on every
frame, including the soft ones.

## Files

- `index.html` self contained page rendering the four frames plus 32 px
  mark tests
- `export.cjs` headless export script (Playwright plus system Chromium)
- `kestrel.png`, `halcyon.png`, `voltra.png`, `vesper.png` frames at
  3840x2160
- `*-preview.png` the same frames at 1920x1080, `bench-*.png` the 32 px
  mark tests

## Rendering

```bash
node export.cjs            # four 3840x2160 frames
node export.cjs --preview  # 1920x1080 previews, bench shots, lockup widths
```

The script waits for `window.__ready`, set once fonts are loaded and all
four canvases are painted. Backgrounds are deterministic (seeded PRNG), so
exports are reproducible.
