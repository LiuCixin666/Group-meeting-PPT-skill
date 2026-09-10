# Execution workflow

## 1. Intake and target definition

Record the reference image/PPT and pixel dimensions, slide size, exact text, template-owned background objects, required editable objects, allowed raster assets, formula requirements, output names, and review mode. If a reference image is missing, do not describe the result as 1:1 reconstruction.

## 2. Standard task tree

```text
tasks/<task_name>/
  task_spec.json
  asset_decision_table.md
  coordinate_table.md
  style_summary.md
  generation_script.py
  check_report.md
  equations.md
  manual_actions.md

figures/<task_name>/
  reference/
  assets/
  preview/
  overlays/

result/<task_name>/
  <task_name>.pptx
  <task_name>_preview_<n>.png
```

Initialize this tree with `scripts/init_task.py`.

## 3. Segment and classify

Give every element a stable ID. Classify it as `editable_ppt_object`, `cropped_reference_image`, `retained_template_object`, or `manual_action`. Use controlled raster only when internal detail cannot be reproduced reliably and does not need editing. Do not crop text-heavy modules.

## 4. Geometry reconstruction

Insert the reference at exact slide bounds as `REFERENCE_GUIDE`. Place reconstructed objects above it. Use a centralized dictionary, JSON layout file, or coordinate table as the source of truth.

Recommended z-order:

```text
0 temporary reference guide
10 background panels
20 borders and separators
30 connectors
40 images and icons
50 text
60 highlights and annotations
```

Delete `REFERENCE_GUIDE` before saving.

## 5. Build and export

Clone the supplied template rather than rebuilding master content. On Windows, PowerPoint COM gives the most faithful rendering. Export each slide to the same pixel dimensions as the reference when possible.

## 6. Compare

Create a generated-page montage, side-by-side reference/preview, 50% alpha overlay, and enhanced absolute-difference image when a true corresponding reference exists. Do not generate a misleading diff when the reference is missing or duplicated; record the limitation.

## 7. Iterate

Each iteration should normally repair 3–5 concrete defects. Freeze correct regions. Prioritize wrong content/data, source-asset misuse, text overlap, major geometry drift, typography/icon details, then cosmetic pixel refinements.

When an urgent usable version is requested, stop after blocking defects pass and save a versioned copy such as `_usable_v1.pptx` or `_iconfix_v1.pptx`.
