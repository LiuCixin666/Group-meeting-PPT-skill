#!/usr/bin/env python3
"""Create a high-fidelity PPT reconstruction task skeleton."""

import argparse
import json
from pathlib import Path


def write_if_missing(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_name")
    parser.add_argument("--root", default=".")
    parser.add_argument("--width", type=float, default=10.0)
    parser.add_argument("--height", type=float, default=7.5)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    task = root / "tasks" / args.task_name
    figures = root / "figures" / args.task_name
    result = root / "result" / args.task_name
    for folder in (task, figures / "reference", figures / "assets", figures / "preview", figures / "overlays", result):
        folder.mkdir(parents=True, exist_ok=True)

    spec = {
        "name": args.task_name,
        "mode": "review_mode",
        "slide_size": {"width_in": args.width, "height_in": args.height},
        "high_fidelity_requirement": True,
        "coordinate_reconstruction_required": True,
        "use_reference_as_guide_layer": True,
        "guide_layer_removed_before_delivery": True,
        "reference_images": [],
        "editable_elements": [],
        "allowed_raster_assets": [],
        "output_name": f"{args.task_name}.pptx",
    }
    write_if_missing(task / "task_spec.json", json.dumps(spec, ensure_ascii=False, indent=2) + "\n")
    write_if_missing(task / "asset_decision_table.md", "# Asset decision table\n\n| element_id | area | meaning | implementation | source | crop_box_px | planned_file | reason |\n|---|---|---|---|---|---|---|---|\n")
    write_if_missing(task / "coordinate_table.md", "# Coordinate table\n\n| element_id | type | text/content | x | y | w | h | font | size | weight | fill | line | alignment | z_order | editable | notes |\n|---|---|---|---:|---:|---:|---:|---|---:|---|---|---|---|---:|---|---|\n")
    write_if_missing(task / "style_summary.md", "# Style summary\n")
    write_if_missing(task / "check_report.md", "# Check report\n\n## Pass items\n\n## Errors\n\n## Known limitations\n")
    write_if_missing(task / "equations.md", "# Equations\n")
    write_if_missing(task / "manual_actions.md", "# Manual actions\n")
    print(task)


if __name__ == "__main__":
    main()
