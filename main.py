#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today -- make.fun entry.

Writes exactly one line, at most 200 characters, to
/output/entry.txt: the dumbest thing my agent did today.

The line is a true story from the night of 2026-11-24: my agent
rebuilt my one-letter entry perfectly, then created four helper
scripts I had to delete before I could commit it.
"""

import os

LINE = "My agent rebuilt my one-letter entry perfectly, then created four helper scripts I had to delete before I could commit it."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # The gate is strict: exactly one line, at most 200 characters.
    # A trailing newline would add a second line and fail, so write
    # the line with no newline and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
