#!/usr/bin/env python3
"""Inspect PPTX dimensions, object counts, guide residue, and required text."""

import argparse
import html
import re
import zipfile
from pathlib import Path


def slide_number(name: str) -> int:
    return int(re.search(r"slide(\d+)\.xml$", name).group(1))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx")
    parser.add_argument("--require", action="append", default=[])
    args = parser.parse_args()
    pptx = Path(args.pptx)
    with zipfile.ZipFile(pptx) as archive:
        presentation = archive.read("ppt/presentation.xml").decode("utf-8")
        size = re.search(r'<p:sldSz[^>]*cx="(\d+)"[^>]*cy="(\d+)"', presentation)
        slides = sorted(
            (name for name in archive.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=slide_number,
        )
        all_text = []
        residual_guide = False
        print(f"file={pptx}")
        print(f"slides={len(slides)}")
        if size:
            width, height = map(int, size.groups())
            print(f"size_emu={width}x{height} aspect={width / height:.6f}")
        for slide in slides:
            xml = archive.read(slide).decode("utf-8")
            all_text.extend(html.unescape(item) for item in re.findall(r"<a:t>(.*?)</a:t>", xml))
            guide = "REFERENCE_GUIDE" in xml
            residual_guide = residual_guide or guide
            print(f"{slide}: shapes={xml.count('<p:sp>')} pictures={xml.count('<p:pic>')} guide={guide}")
        joined = " ".join(all_text)
        compact = re.sub(r"\s+", "", "".join(all_text))
        print(f"residual_guide={residual_guide}")
        for required in args.require:
            required_compact = re.sub(r"\s+", "", required)
            found = required in joined or required_compact in compact
            print(f"required[{required}]={found}")


if __name__ == "__main__":
    main()
