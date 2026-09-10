# Visual and structural checking

## Required checks

1. Slide dimensions and aspect ratio are correct.
2. Master-owned logo, header line, footer, and page number remain correct.
3. No residual `REFERENCE_GUIDE` exists.
4. No whole slide or text-heavy module is flattened into an image.
5. Required text, scientific symbols, English terms, formulas, and data are exact.
6. Text has no overlap, clipping, character-by-character wrapping, or edge contact.
7. Repeated cards have consistent geometry and baselines.
8. Connectors do not cross labels or node interiors unexpectedly.
9. Controlled raster assets use the correct source and are not translated or redrawn.
10. Each slide has a PNG preview; corresponding references have overlay/diff output.

## 0–5 rubric

Score scientific correctness, layout fidelity, color/style fidelity, typography fidelity, asset-use correctness, editability, readability, formula handling, and PowerPoint maintainability.

## Mandatory REVISE conditions

- wrong scientific content or required data;
- supplied complex figure redrawn, translated, or replaced without authorization;
- entire slide or major text module rasterized;
- unreadable formula or missing formula source;
- major regions visibly shifted;
- text overlap or abnormal wrapping remains;
- preview, coordinate table, or check report missing;
- temporary guide layer remains.

## Checker response template

```text
overall_score: /100
pass_items:
critical_errors:
geometry_errors:
typography_errors:
asset_errors:
formula_or_data_errors:
next_iteration_tasks:
decision: PASS / REVISE
```
