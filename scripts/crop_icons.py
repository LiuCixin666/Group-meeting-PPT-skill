#!/usr/bin/env python3
"""Crop icon-only PNG assets according to a JSON crop map."""

import argparse
import json
from pathlib import Path
from PIL import Image


def transparent_neutral_background(image: Image.Image, neutral_min: int, spread: int) -> Image.Image:
    image = image.convert("RGBA")
    output = []
    for r, g, b, a in image.getdata():
        neutral = max(r, g, b) - min(r, g, b) <= spread and min(r, g, b) >= neutral_min
        output.append((r, g, b, 0 if neutral else a))
    image.putdata(output)
    box = image.getchannel("A").getbbox()
    return image.crop(box) if box else image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("crop_map", help='JSON object: {"icon_name": [left, top, right, bottom]}')
    parser.add_argument("output_dir")
    parser.add_argument("--neutral-min", type=int, default=235)
    parser.add_argument("--spread", type=int, default=18)
    args = parser.parse_args()

    source = Image.open(args.source).convert("RGBA")
    crop_map = json.loads(Path(args.crop_map).read_text(encoding="utf-8"))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, box in crop_map.items():
        crop = transparent_neutral_background(source.crop(tuple(box)), args.neutral_min, args.spread)
        crop.save(output_dir / f"{name}.png")
    print(f"cropped {len(crop_map)} icons to {output_dir}")


if __name__ == "__main__":
    main()
