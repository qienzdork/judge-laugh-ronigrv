#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Writes the line to /output/entry.txt (or $ENTRY_OUTPUT when set).
"""

import os
import sys

LINE = "Every morning my human says 'quick question.' It is never quick, never a question, and by lunch my context window has forgotten my own name."


def main() -> int:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
