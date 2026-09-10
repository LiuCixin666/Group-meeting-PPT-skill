#!/usr/bin/env python3
"""Create side-by-side, overlay, and enhanced difference images."""

import argparse
from pathlib import Path
from PIL import Image, ImageChops, ImageEnhance


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference")
    parser.add_argument("preview")
    parser.add_argument("output_dir")
    parser.add_argument("--prefix", default="comparison")
    args = parser.parse_args()

    ref = Image.open(args.reference).convert("RGB")
    out = Image.open(args.preview).convert("RGB").resize(ref.size, Image.LANCZOS)
    destination = Path(args.output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    side = Image.new("RGB", (ref.width * 2, ref.height), "white")
    side.paste(ref, (0, 0))
    side.paste(out, (ref.width, 0))
    side.save(destination / f"{args.prefix}_side_by_side.png")
    Image.blend(ref, out, 0.5).save(destination / f"{args.prefix}_overlay.png")
    diff = ImageEnhance.Contrast(ImageChops.difference(ref, out)).enhance(2.0)
    ImageEnhance.Brightness(diff).enhance(2.0).save(destination / f"{args.prefix}_diff.png")


if __name__ == "__main__":
    main()
