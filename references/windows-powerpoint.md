# Windows PowerPoint automation notes

Use Microsoft PowerPoint COM when installed and native rendering fidelity matters.

## Stable pattern

1. Copy the template to a temporary `_writing.pptx`.
2. Launch a separate PowerPoint instance with `DispatchEx`.
3. Duplicate the template slide as needed.
4. Delete only foreground shapes; retain master/background content.
5. Add a full-slide `REFERENCE_GUIDE`, build objects, then delete the guide.
6. Export every slide as PNG before closing.
7. Save and close, quit PowerPoint, then atomically rename the writing copy.

## Maintainability

Name every significant shape with a stable element ID. Put repeated construction in helpers. Store major geometry in one layout dictionary or JSON. Preserve source files and save versioned outputs.

## Common COM pitfalls

- Partial rich-text APIs vary by PowerPoint version. If run-level formatting fails, use separate text boxes for highlighted phrases rather than blocking delivery.
- Old Pillow versions use `Image.LANCZOS`; newer versions may expose `Image.Resampling.LANCZOS`.
- Non-ASCII paths can display incorrectly in console output even when files are valid; verify with filesystem APIs.
- Close stale PowerPoint instances after errors before retrying.
- A successful `Save` is not sufficient verification; inspect the PPTX package and exported PNGs.

## Structural verification

The PPTX is a ZIP package. Inspect `ppt/presentation.xml` for dimensions and `ppt/slides/slide*.xml` for shape/picture counts, required text, and residual guide names. A page may contain icon pictures, but a whole-slide reference picture must not remain.
