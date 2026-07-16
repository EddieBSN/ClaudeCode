# Keelson · landing page

A single SaaS landing page recreating a shared blueprint-style design language (a ruled
layout frame whose hairlines run to the viewport edges, diagonal hatch filler bands, warm
paper with near-black ink, one accent, mono-voiced type, terminal-strip feature cards) for
an original invented brand. Everything is generated in code. No stock images, no photos,
no AI image generation. The only external resource is Google Fonts, embedded as woff2 data
URIs so `index.html` is fully self-contained.

## The brand

**Keelson** · operations control for ocean freight. Forwarders track bookings, containers,
vessels and port calls; rollings and missed cutoffs surface the hour they happen; demurrage
risk is priced before it invoices. The name is the structural beam that runs along a ship's
keel, which suits a page drawn like an engineering sheet.

- **Industry:** ocean freight operations
- **Paper / ink:** warm ivory `#F5F3EE`, warm near-black `#151410`
- **Accent (exactly one):** deep viridian `#0E7A5B`, used only on the eyebrow, the flagged
  and live states inside the board, checkmarks, and the terminal status lines
- **Type:** Geist Mono (headlines, labels, numerals, buttons, terminals) + Instrument Sans
  (body copy, nav), a machined-terminal voice over a warm grotesk
- **Headline:** "Vessel schedules slip. / Your margins shouldn't." with the tonal shift on
  line two

## The hero artifact

A straight-on product window seated inside the blueprint frame itself: its side edges land
exactly on the page rules, and it is annotated like a drawing sheet with a dimension line
and oblique end ticks, numbered leader callouts, corner registration crosses, construction
lines extending its edges to the viewport, and sheet notes (drawing number, revision, issue
date). Inside is a live freight operations board built entirely in HTML/CSS/SVG: workspace
sidebar, KPI strip, a sailings table with status pills, a cutoffs list, and a per-container
demurrage clock.

## Divergence from the references

The nearest reference is the blueprint-styled work-OS page. Keelson moves on four axes:
industry (AI workspace to ocean freight), artifact type (tilted overlapping windows on a
textile slab to a straight-on engineering-drawing window aligned to the rules), color
temperature (cool gray paper to warm ivory), and accent (orange to deep viridian), plus a
shifted type voice (typewriter-flavored mono to a machined mono over a humanist grotesk).

## Files

- `index.html` · the page, fully self-contained (fonts embedded), responsive 375 to 1440 px;
  the ruled frame simplifies on mobile instead of disappearing
- `export.cjs` · headless render via Playwright + system Chromium
- `desktop.png` · 2880 px wide export
- `mobile.png` · 750 px wide export

## Rendering

```bash
cd keelson
node export.cjs            # writes desktop.png (2880w) and mobile.png (750w)
node export.cjs --desktop  # desktop only
node export.cjs --mobile   # mobile only
```
