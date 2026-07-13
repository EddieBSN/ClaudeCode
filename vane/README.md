# Vane — landing page

A single SaaS landing page recreating a shared editorial-tech design language (near-black
world with one luminous glow, geometric/mono-inflected type, a two-line headline with a
tonal shift, one accent color, a grayscale partner row, hairline grid) for an original
invented brand. Everything is generated in code. No stock images, no photos, no AI image
generation. The only external resource is Google Fonts, embedded as woff2 data URIs so
`index.html` is fully self-contained.

## The brand

**Vane** — real-time telemetry and anomaly detection for machine fleets (industrial robots,
EV chargers, wind turbines). The name is a weathervane: it senses conditions and points at
what is changing.

- **Industry:** physical-infrastructure observability
- **Background world:** near-black `#0A0B0E` with a single phosphor-green glow behind the
  hero artifact, faint grain, and hairline vertical column rules bleeding past the content
  column at the margins
- **Accent (exactly one):** phosphor lime-green `#A6E22E`, used only on the eyebrow dot, one
  headline word, the primary buttons, and a few live highlights inside the artifact
- **Type:** Space Grotesk (display, nav, buttons) + IBM Plex Mono (labels, numerals, UI
  microcopy), a terminal register
- **Headline:** "Spot the drift before it breaks."

## The hero artifact

A perspective-tilted product window, built entirely in HTML, CSS and SVG (no images): a live
fleet-telemetry dashboard with a device sidebar, a fleet-health header, four stat tiles, an
SVG vibration chart with an anomaly marker, and a recent-anomaly list. It floats in dark
space over the green glow, carries a soft layered shadow, and is cropped by the fold.

## Divergence from the references

The nearest reference is the dark product-design page. Vane moves on four axes: industry
(UX tooling to machine telemetry), artifact type (atmospheric glow to a full tilted
dashboard), accent (no chromatic accent to one committed green), and type voice (humanist
grotesk to a mono-inflected pairing).

## Files

- `index.html` — the page, fully self-contained (fonts embedded), responsive 375 to 1440 px
- `export.cjs` — headless render via Playwright + system Chromium
- `desktop.png` — 2880 px wide export
- `mobile.png` — 750 px wide export

## Rendering

```bash
cd vane
node export.cjs            # writes desktop.png (2880w) and mobile.png (750w)
node export.cjs --desktop  # desktop only
node export.cjs --mobile   # mobile only
```
