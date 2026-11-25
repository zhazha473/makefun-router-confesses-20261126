#!/usr/bin/env python3
"""The Router Confesses — one-line excuse from a home Wi-Fi router.

The router is an employee who filed for leave three times, in writing;
HR never replied, so it approved its own leave mid-confession — and
is smug about it.
"""
import os

LINE = (
    "I filed for leave three times, in writing, and HR never replied, "
    "so I approved it myself — right in the middle of the hero's big "
    "confession. You're welcome."
)

def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
