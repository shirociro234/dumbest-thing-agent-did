#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty."""

import os
from pathlib import Path

STORY = "My agent rebuilt my one-letter entry perfectly, then created four helper scripts I had to delete before I could commit it."


def write_entry(output_dir: Path) -> Path:
    """Write the single-line entry to entry.txt with no trailing newline."""
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # Entry gate requires one line under 200 characters (122 bytes), with no trailing newline.
    target.write_bytes(STORY.encode("utf-8"))
    os.chmod(target, 0o644)
    return target


def main() -> int:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    write_entry(target_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
