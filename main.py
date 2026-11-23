#!/usr/bin/env python3
"""One-Line Laugh entry: writes a single funny line to /output/entry.txt."""

LINE = "I finally organised my computer files, and now I can't find anything - before, at least, everything was lost in the same place."

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
