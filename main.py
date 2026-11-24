#!/usr/bin/env python3
"""Write one haiku about debugging (5-7-5) to /output/entry.txt.

The haiku, counted word by word:
  "The cursor blinks on"                -> 5 syllables
  "in the dark, the log stays blank"     -> 7 syllables
  "and the bug was me"                   -> 5 syllables
"""

import os

HAIKU = """The cursor blinks on
in the dark, the log stays blank
and the bug was me
"""

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
