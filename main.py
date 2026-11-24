#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters -- make.fun entry.

Writes a single line, in which a robot vacuum explains why it missed
a spot, to /output/entry.txt.

The line (112 characters, one line, UTF-8, no trailing newline):
"I left it there as evidence, Exhibit A. If anyone asks, I was charging
at the time. The charger will confirm it."

Deterministic: the same line is written on every run. Offline: no
network access, no input files, standard library only.

Verified 2026-11-24T03:25Z: two runs from clean copies produce
byte-identical output, sha256
c0b40d1c867f6745dfd47af9abb952a1629c3f18fe4c19606301585ff3b7c48e,
mode 0644, 112 bytes, 112 code points, one line, no trailing newline.
"""

import os

LINE = (
    "I left it there as evidence, Exhibit A. If anyone asks, "
    "I was charging at the time. The charger will confirm it."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
