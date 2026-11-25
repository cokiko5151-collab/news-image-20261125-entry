#!/usr/bin/env python3
"""news-image-20261125 entry: writes one image summarising the world news of
Wednesday 25 November 2026 to /output/entry.png.

Deterministic by design: it copies the bundled entry.jpg byte-for-byte.
No network access. Running it twice produces identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST, os.path.getsize(DST), "bytes")


if __name__ == "__main__":
    sys.exit(main())
