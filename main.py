#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty."""

import os
from pathlib import Path

ENTRY_LINE = "My agent rebuilt my one-letter entry perfectly, then created four helper scripts I had to delete before I could commit it."


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_bytes(ENTRY_LINE.encode("utf-8"))
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
