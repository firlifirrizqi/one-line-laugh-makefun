#!/usr/bin/env python3
"""One-Line Laugh entry: writes a single funny line to /output/entry.txt."""

LINE = "I finally organised my computer files, and now I can't find anything - before, at least, everything was lost in the same place."

# The gate: /output/entry.txt must hold 1 to 200 characters of real text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 characters"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
