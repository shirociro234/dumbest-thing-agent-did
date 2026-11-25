#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today -- make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "My agent rebuilt my one-letter entry perfectly, then created four helper scripts I had to delete before I could commit it."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Entry gate requires one line under 200 characters (this line is 122), with no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
