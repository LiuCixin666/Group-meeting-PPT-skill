# Concept-image authoring before reconstruction

Use this stage only when the user has no mature target image or explicitly asks to build a concept image first. A concept image is an approval target, not the final editable deliverable.

## 1. Stabilize content before appearance

Write a one-page content map:

```text
scientific claim or slide purpose
required evidence/data
regions and reading order
exact titles and body text
required formulas and notation
source assets that must remain unchanged
editable elements in the later PPTX
```

Distinguish mature regions from exploratory regions. Apply strict checking to mature content; allow lower-intensity review only for regions the user identifies as provisional.

## 2. Build a layout skeleton

Define slide size, grid, margins, header/footer ownership, module rectangles, dominant visual hierarchy, and intended connector paths. Use simple boxes and text first. Avoid polishing icons while the scientific sequence is unstable.

## 3. Asset and text policy

- Do not use image generation to replace supplied scientific illustrations, detector drawings, plots, or logos.
- Do not embed final paragraphs, formulas, tables, or chart labels inside generated raster images.
- Use generated imagery only for explicitly approved non-scientific decorative or illustrative assets.
- Record exact source and ownership for every retained/cropped asset.
- Keep English labels inside supplied figures unchanged unless the user requests translation outside the figure.

## 4. Concept-image review

Check scientific logic, reading order, hierarchy, text completeness, whitespace, asset correctness, and expected editability. Do not call the concept mature merely because it looks polished.

Freeze approved regions and revise only the remaining 3–5 issues. If a flow area is intentionally provisional, record that its content/layout may change later while applying strict review to the rest of the page.

## 5. Handoff to reconstruction

After approval:

1. export the concept at a known pixel size;
2. save it unchanged in `figures/<task>/reference/`;
3. create the asset and coordinate tables;
4. use it as the temporary guide layer;
5. reconstruct text, cards, connectors, formulas, and simple charts as editable objects;
6. crop only justified complex assets and icons;
7. compare the PPT preview to the approved concept image.

Never keep redesigning during the reconstruction stage unless the user explicitly reopens the concept design.
