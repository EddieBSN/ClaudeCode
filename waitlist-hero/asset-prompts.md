# Screen 1 — Generated art prompts (GPT Image 2)

Frame: 1600 x 1000. Left column (x 0–720) is coded UI and stays fully in code.
Right column (x 720–1600, i.e. 880 x 1000) is the illustration slot. Per the rule
change, only raster **artwork** is generated externally; UI, layout, type and grain
remain code. Grain will be re-applied in code on top of any returned image.

---

## Step 1 — Asset audit

| Graphic | Current build | Verdict | Reason |
|---|---|---|---|
| Right-hand illustration panel | hand-built SVG scene | **GENERATE** | The one asset that carries the whole identity; generated flat-vector art can hold richer light, depth and shape variety than hand-laid SVG paths. |
| Five trust avatars (34×34) | coded flat figures | keep in code | At 34px (68px @2x) a generated portrait would read muddy and drift off-palette; crisp coded silhouettes match the editorial restraint. |
| Cream column background | flat fill + code grain | keep in code | Must stay code per the rule (UI + grain). |
| Paper / grain texture | feTurbulence in code | keep in code | Grain explicitly stays in code and is layered over the returned art. |

Only one asset is generated: the hero illustration panel.

### Slot spec — hero illustration
- **Pixel slot:** x 720 → 1600, y 0 → 1000 inside the 1600×1000 frame → **880 × 1000**.
- **Aspect ratio of slot:** 0.88 (upright, near-square).
- **Placement:** full bleed, `object-fit: cover`, `object-position: center`. The figure is
  centered, so covering trims left/right evenly.
- **Requested source:** 1024 × 1024 (square, ratio 1.00 — the model ratio closest to 0.88;
  covering the slot trims only ~6% off each of the left and right edges, full height kept).
- **Must not:** it never overlaps the headline (headline lives on the separate cream column),
  but its **left ~8% butts the seam with the cream panel**, so that band must stay quiet and
  low-contrast; the figure/face/phone must not drift into the outer 8% left/right that gets cropped.

---

## Step 2 — Palette sampled from the built page

Verbatim hexes (these go into the prompt so the art lives in the same color world):

**UI (context only, not for the art):** cream paper `#F3EEE4`, body ink `#2A2A24`,
accent forest green `#1C3B2A`, input hairline `#CBBCA2`, input fill `#FBF8F1`,
muted text `#5B5B50`, headline second line `#2F5540`.

**Illustration (drive the art):**
- Sky: cool blue `#C4D8E2` → mid `#D8DFDA` → warm cream `#ECE1CE`; sunlight `#FBF3DF`
- Building: wall `#E3CEA6`→`#CBB088`, cornice `#EFE0C2`, trim `#B79A70`, windows `#5E6E78`, sill `#C7AE86`
- Background / canopy leaves (light, desaturated blue-green): `#AEC3AA` `#9FBBA6` `#8AAE97` `#7FA08C`
- Midground leaves: `#6FA07E` `#5E9070` `#4E8064` `#437A66` `#396A50` `#2C5A42`
- Foreground leaves (dark, high-contrast): `#2C5240` `#2A5A50` `#14301F` `#123028`; deepest shadow `#1C3B2A`
- Coat blue: `#496A90` `#3B5A80` `#2E486A` `#274465` `#26405F`
- Skin: `#E6B98E` (light) `#D6A074` (shadow) `#DCAD80` (hands)
- Hair: `#2B2A31`
- Coral poppy: petals `#F49A6A` `#E87646` `#DE5C36` `#C64826`, dark center `#2B2018`
- Cool phone glow: `#EAF2FB`

---

## Asset 1 — Hero illustration panel

Requested output: **1024 × 1024** PNG. Hard color cap: **18** flat colors.

```
A flat vector editorial illustration of a single calm person absorbed in a phone in a sunlit courtyard garden full of oversized houseplants, rendered as hard edged shapes with no outlines, each shape filled with flat matte color in at most two or three tonal steps, no smooth photographic blends and no mesh gradients, a clean matte finish with only the very faintest fine grain so the color reads essentially flat. Subject and staging: one person only, seated upright and relaxed and seen from the front, head tilted gently downward with a soft calm expression and eyes lowered, both hands holding a small phone at chest height, shoulders loose; the figure wears a buttoned deep blue coat over a simple collar, has chin length dark hair falling just past the jaw, and warm medium skin; the phone emits a small localized cool glow that lights only the palms, the fingertips and the underside of the chin and nothing else. Foreground, the largest and darkest and crispest layer: two or three oversized leaves rising from the very bottom edge and overlapping the person's lap and lower body, one broad almond shaped leaf and one fingered split tropical leaf, plus a single coral orange poppy flower with a dark center sitting low in the left foreground. Midground: the seated figure, a cluster of medium sized green leaves framing the person on both sides, and two more coral poppies on slender stems near the waist. Background, small and soft and cool: a cropped fragment of a warm ochre classical apartment building with three tall shuttered windows in the upper left, a soft graduated dawn sky above going from cool pale blue at the top to warm cream near an unseen horizon, and a hanging canopy of lighter desaturated blue green leaves drooping down into the frame from the top edge. Composition and crop: place the figure centered left to right with the head at about forty percent down from the top and occupying the central vertical third, and leave a calmer quieter pocket of soft sky and wall immediately around the head and shoulders so that area stays uncluttered and low contrast; hide the base of the building behind the midground foliage at roughly fifty five percent down; keep every important element, the whole figure and face and phone and all the framing foliage and flowers, inside the central eighty four percent of the width and the central eighty percent of the height, and treat the outer eight percent of the left and right edges and a thin sliver of the top and bottom as sacrificial margin, and specifically keep the left eight percent quiet and simple because it will butt against a plain cream panel. Palette, use only these flat colors and derive at most three tonal steps per material from within this set, hard capped at eighteen distinct colors total: deep forest green 1C3B2A as the very deepest leaf shadow and darkest accent, foreground leaf greens 2C5240 and 14301F and 123028, midground leaf greens 5E9070 and 4E8064 and 6FA07E and 396A50 and 2C5A42, background and canopy blue greens AEC3AA and 9FBBA6 and 8AAE97 and 7FA08C, coat blues 496A90 and 3B5A80 and 2E486A and 274465, near black hair 2B2A31, warm skin E6B98E with shadow D6A074, coral poppy petals F49A6A and E87646 and DE5C36 with dark center 2B2018, building ochre E3CEA6 and CBB088 with cream cornice EFE0C2 and slate windows 5E6E78, sky cool blue C4D8E2 fading to warm cream ECE1CE, warm sunlight FBF3DF, and a single cool phone glow EAF2FB used only on the hands and chin. Light: soft warm early morning sun coming from the upper left at a low angle, gentle and diffuse with no harsh highlights; the background building and sky are the brightest and coolest, the midground foliage catches warm light on its upper left faces and turns cooler and darker on the shaded undersides, and the foreground leaves sit in the deepest shade as the darkest and highest contrast shapes; the only other light is the tiny cool phone glow on the hands and chin. Depth: strong overlapping layers with a clear scale jump, foreground leaves enormous and dark, the midground figure and medium leaves at human scale, the background building and canopy small and soft, and a gentle atmospheric fade toward the back so the distant leaves and the building read lighter and cooler and less saturated and lower contrast while the foreground stays crisp and saturated dark. Texture and finish: flat matte fills, crisp hard edges everywhere, no outlines, at most one soft directional tonal step inside the largest leaves and the coat, absolutely no smooth photographic gradients and no mesh gradients, only the faintest hint of fine matte grain so the surface stays essentially clean flat color that a separate grain layer can be laid over later, and no gloss anywhere. Output as a one thousand twenty four by one thousand twenty four square image; the composition is centered so it survives being cropped into a slightly narrower upright slot, and I expect to lose roughly the outer six to eight percent of the left and right edges and only a thin sliver of the top and bottom, so nothing important may sit in those outer margins. Do not include any text, letters, numbers, words, logos, wordmarks, watermarks, signatures, captions, user interface elements, buttons, input fields, frames, borders, vignettes, drop shadows, cast card shadows, photorealism, three dimensional rendering, glossy highlights, specular reflections, lens flare, bokeh, or mesh gradients, and do not add any second person, extra hands, or extra faces.
```

**Variant levers** (append one line when regenerating):
- Denser foliage: add two more oversized leaves crowding the lower left and lower right corners and thicken the midground so less sky shows.
- Tighter crop on the figure: scale the person up so the shoulders and phone fill more of the middle of the frame and the head sits a little higher.
- Warmer late afternoon light: shift the sky and building toward amber and gold, warm every highlight, and let the shadows grow longer and a touch deeper.

---

## Step 6 — Where the returned file goes

- **Folder:** `waitlist-hero/art/` (created)
- **Filename:** `hero-illustration.png`
- **Dimensions:** 1024 × 1024, RGB PNG (highest square resolution GPT Image 2 offers; if a
  larger square is available, hand it back and it will be used as-is).
- On return: placed full bleed in the 880×1000 slot, `object-fit: cover`,
  `object-position: center`, at 2x for retina; the coded feTurbulence grain stays layered on top.
