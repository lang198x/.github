# Lang198x initial and wordmark

Steve requested an L matching the sibling initial tiles. Use the binding family
identity's real Oxanium Extra Bold outlines; no mascot or new symbol system.

1. Inspect the umbrella identity decision and existing vector generator.
2. Build `branding/` with the licensed, hash-checked existing font, a reproducible
   generator, four wordmarks and three initial tiles. Keep source files small.
3. Derive a candidate colour from the largest unused hue gap without changing
   siblings. Label the palette as proposed until Steve reviews the artwork.
4. Render a comparison sheet and 128/512px PNG icons using existing rsvg-convert
   and ImageMagick. Inspect actual small sizes and SVG bounds, then verify a
   missing glyph fails rather than producing incomplete lettering.
5. Commit and push the reviewable assets. Do not upload the publisher logo or
   alter account branding before the candidate is reviewed.

Verification: source-font SHA-256, valid SVG XML, glyph bounds inside viewBoxes,
centred L ink, complete expected variants and rendered visual inspection.

Outcome: seven SVG variants and 128/512px PNG tiles prepared, with a rendered
light/dark preview. Source hash, XML, bounds, centring and missing-glyph negative
control pass. The preview was visually inspected, including actual small icons.
The 97.5-degree golden palette remains a review candidate. No account or
extension branding was changed, and no temporary process or workspace was used.
