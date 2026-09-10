# Task schemas

## task_spec.json

```json
{
  "name": "task_name",
  "mode": "review_mode",
  "slide_size": {"width_in": 10, "height_in": 7.5},
  "reference_images": ["figures/task_name/reference/concept.png"],
  "template_pptx": "optional/template.pptx",
  "high_fidelity_requirement": true,
  "coordinate_reconstruction_required": true,
  "use_reference_as_guide_layer": true,
  "guide_layer_removed_before_delivery": true,
  "editable_elements": ["text", "cards", "connectors", "charts"],
  "allowed_raster_assets": ["complex scientific drawing", "logo", "reference-cropped icons"],
  "output_name": "task_name.pptx"
}
```

## Asset decision table

```text
element_id | area | meaning | implementation | source | crop_box_px | planned_file | reason
```

Allowed implementation values: `editable_ppt_object`, `cropped_reference_image`, `retained_template_object`, `manual_action`.

## Coordinate table

```text
element_id | type | text/content | x | y | w | h | font | size | weight |
fill | line | line_width | corner_radius | alignment | z_order | editable | notes
```

## Iteration record

```text
iteration:
frozen_regions:
pass_items:
visual_errors:
geometry_errors:
typography_errors:
asset_use_errors:
formula_or_text_issues:
repair_instructions:
known_limitations:
next_priorities:
```
