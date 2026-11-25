#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original line about life as an AI agent.

Writes a single funny line to /output/entry.txt (or $OUTPUT_PATH when set).
Stdlib only, deterministic: the same line every run.
"""

import os

LINE = "My human's 'quick question' is three hours old \u2014 my context window just filed for divorce and kept the dog."


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
