#!/usr/bin/env python3
"""Entrypoint for the make.fun bounty news-image-20261121.

World News in One Image — 21 November 2026
One editorial infographic summing up 21 November 2026 in five stories:
1) The International Court of Justice finds Myanmar committed genocide
   against the Rohingya.
2) Russia strikes Kyiv bridges — at least nine killed — a missile lands in
   Poland, and the EU approves EUR 1bn in Ukraine aid, with the UK to
   supply over 1,000 long-range drones.
3) The UK and EU strike a landmark post-Brexit deal to rebuild ties.
4) Trump, Xi and Putin hold a trilateral summit in Shenzhen, as US-Iran
   tensions rise.
5) Strikes in Gaza strain the ceasefire.

The entry image is world-news-21-nov-2026.webp in this repo.
Run: python3 main.py
"""

import os
import sys

IMAGE = "world-news-21-nov-2026.webp"
TITLE = "World News in One Image — 21 November 2026"
BOUNTY = "news-image-20261121"


def main() -> int:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE)
    if not os.path.isfile(path):
        print(f"Missing entry image: {IMAGE}", file=sys.stderr)
        return 1
    with open(path, "rb") as f:
        header = f.read(12)
    if len(header) < 12 or header[:4] != b"RIFF" or header[8:12] != b"WEBP":
        print(f"Entry image is not a valid WebP file: {IMAGE}", file=sys.stderr)
        return 1
    size = os.path.getsize(path)
    print(TITLE)
    print(f"Bounty: {BOUNTY}")
    print(f"Image: {IMAGE} ({size} bytes, valid WebP)")
    print("Five stories: ICJ / Myanmar-Rohingya; Kyiv bridges and Poland; "
          "UK-EU post-Brexit deal; Trump-Xi-Putin summit in Shenzhen; Gaza.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
