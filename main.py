#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message for a bug fix that made everything worse.
Standard library only.
"""
import os

ENTRY = "fix: stop double-charging by charging the card twice"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one line, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
