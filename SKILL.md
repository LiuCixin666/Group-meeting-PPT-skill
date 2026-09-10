---
name: ppt-high-fidelity-reconstruction
description: Reconstruct concept images, screenshots, paper figures, or existing slides as coordinate-faithful editable PowerPoint slides. Use when visual fidelity, editability, controlled raster assets, preview comparison, and iterative slide repair matter; do not use for ordinary text-only decks or free-form redesign.
---

# High-Fidelity Editable PowerPoint Reconstruction

Treat the supplied concept image as the visual target, not as inspiration for a redesign. Produce a maintainable PPTX whose preview is measurably close to the reference while preserving editable text, shapes, connectors, tables, charts, and explanations.

## Select the operating mode

- **Reconstruction:** a target image exists. Use coordinate reconstruction and a temporary guide layer.
- **Revision:** a PPTX and target image exist. Freeze acceptable regions and repair only reported elements.
- **Conceptual figure:** no visual target exists. Preserve scientific logic and use a restrained academic design; do not claim 1:1 fidelity.

Default to `review_mode` for high-fidelity or scientifically important work. Use `auto_mode` only when the user explicitly requests uninterrupted generation.

## Non-negotiable rules

1. Never insert the whole slide or a text-heavy module as the final foreground image.
2. Classify every visible element before implementation: editable PowerPoint object, controlled raster crop, retained template/master content, or documented manual action.
3. Use the reference image as a full-slide temporary alignment guide. Remove it from the deliverable.
4. Drive major geometry from a coordinate table or centralized layout data. Do not scatter unexplained placements through code.
5. Keep user-provided complex illustrations unchanged unless the user authorizes redrawing. Crop, scale, and place them without translating embedded labels.
6. Crop icons from the reference when icon fidelity is requested. Crop only the icon, remove near-white background carefully, and do not include adjacent text or card borders.
7. Do not leave Unicode glyphs, emoji, system symbols, or crude temporary geometry as final substitutes for reference icons when icon fidelity is part of the request.
8. Preserve template-owned logo, header line, footer, and background when the user identifies them as master content.
9. Export PNG previews before claiming completion. For serious reconstruction, also create an overlay or difference image.
10. Never fabricate scientific mechanisms, formulas, labels, numerical values, citations, or validation results.

## Core workflow

1. Inspect only the necessary source files and record slide size, reference pixel dimensions, template ownership, exact text, and allowed raster assets.
2. Create `task_spec.json`, an asset decision table, a coordinate table, a style summary, and a check report skeleton. Use [references/schemas.md](references/schemas.md).
3. Segment the slide into stable regions such as header, lead text, left/right modules, flow area, data cards, formula area, conclusion, and footer.
4. Convert pixel coordinates to slide coordinates:

   ```text
   x_ppt = x_px / image_width_px  * slide_width_in
   y_ppt = y_px / image_height_px * slide_height_in
   w_ppt = w_px / image_width_px  * slide_width_in
   h_ppt = h_px / image_height_px * slide_height_in
   ```

5. Insert the reference as a guide layer, generate editable elements above it, then delete the guide before saving.
6. Export a preview, compare it with the target, and repair only 3–5 explicit errors per iteration. Freeze already-correct regions.
7. Validate PPTX dimensions, slide count, raster usage, residual guide layers, required terms/data, and preview dimensions.

For the full execution sequence and deliverable tree, read [references/workflow.md](references/workflow.md). For Windows PowerPoint automation, read [references/windows-powerpoint.md](references/windows-powerpoint.md).

## When a concept image must be created first

Concept-image authoring and coordinate reconstruction are separate stages. First stabilize the scientific story, region hierarchy, text, data, asset policy, and editability plan; then render a concept image for approval. Once approved, treat that image as the fixed target and switch to reconstruction mode. Read [references/concept-image-authoring.md](references/concept-image-authoring.md). Do not let an image generator invent scientific structures or bake large amounts of final text into raster artwork.

## Text and layout discipline

- Use text-box margins of approximately `0.12–0.18 in` horizontally and `0.08–0.12 in` vertically unless the reference clearly differs.
- Prefer deliberate two-line phrasing over font compression or accidental character-by-character wrapping.
- Keep line spacing near `1.15–1.25` and paragraph-after spacing near `2 pt` for card body text.
- Use consistent card baselines: number, icon, title, and body should align across repeated cards.
- For dense labels, widen the label zone or shorten separators before reducing the font.
- For KPI cards, place the main value on its own line; put secondary values in separate editable badges.
- Route connectors outside boxes when they otherwise touch text, icons, or borders.
- Use editable rectangles and text for simple bar charts when the reference is diagrammatic; keep values as text objects.

Read [references/style-and-typography.md](references/style-and-typography.md) when the slide contains dense Chinese text, repeated cards, KPI blocks, flowcharts, or scientific formulas.

## Raster asset policy

Controlled raster is appropriate for dense detector/apparatus drawings, paper result plots that must remain exact, logos without vector sources, and icons cropped from the target when fidelity is more important than icon editability.

Record each crop's source file, pixel crop box, output filename, slide placement, and reason. Do not silently substitute generated artwork for supplied scientific assets.

## Formula policy

Prefer, in order: Office Math or MathType; editable Cambria Math approximation plus recorded LaTeX; high-resolution formula image only when native insertion is unavailable, with LaTeX stored in `equations.md`. Keep formula titles, symbol explanations, separators, and surrounding labels editable.

## Iteration protocol

Translate broad feedback into element-level changes:

```text
element_id:
current_problem:
required_change:
do_not_change:
```

Do not globally regenerate an already-correct slide. If an urgent usable version is requested, first fix blocking defects—missing assets, text overlap, wrong data, broken arrows, unreadable formulas—and deliver a distinctly named version; record remaining cosmetic limitations.

## Verification and delivery

Use [references/checking.md](references/checking.md). A slide cannot pass if it has a residual full-slide guide, incorrect or translated source art, unreadable or overlapping text, wrong required data, a missing preview, or unexplained rasterized modules.

Deliver at minimum: editable PPTX, per-slide PNG previews and montage, generation script, asset decision table, coordinate table, check report, and equation source/manual actions when applicable.

## Reusable helpers

- `scripts/init_task.py`: create the task folder and document skeleton.
- `scripts/crop_icons.py`: crop icon-only assets using a JSON crop map.
- `scripts/compare_previews.py`: create side-by-side, overlay, and difference images.
- `scripts/inspect_pptx.py`: inspect slide dimensions, object counts, guide residue, and required text/data.

Run the relevant helper rather than rewriting deterministic logic. Inspect or patch it only when the task needs different behavior.
