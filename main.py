#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters -- make.fun entry.

Writes a single line, in which a robot vacuum explains why it missed
a spot, to /output/entry.txt.

The line (105 characters, one line, UTF-8, no trailing newline):
"The spot bribed me with a lost earring. We do not speak of this.
The earring and I have an understanding."

Deterministic: the same line is written on every run. Offline: no
network access, no input files, standard library only.

Putaran 1 (2026-11-24T03:4xZ): baris diganti dari D3x ("I left it there
as evidence, Exhibit A...") ke F6 sesudah turnamen ulang dengan kriteria
tersegel RULES.txt (crosscheck V1 B1): F6 menang 4-0, diputuskan kriteria
#2 tawa sungguhan (5/5 vs 4/5).

Verified 2026-11-24T03:52Z: two runs from clean copies produce
byte-identical output, sha256
01faf7aec241752711f42153aa58325ec452e006096fc5f9dcd0117c132db44d,
mode 0644, 105 bytes, 105 code points, one line, no trailing newline.
Run dengan jaringan dimatikan (unshare -rn) menghasilkan sha256 yang sama.
Catatan: bila /output belum ada, os.makedirs membuatnya 0770 di bawah
umask 007 sandbox ini; di sandbox gerbang, /output sudah ada (0755) dan
program tidak mengubah modenya — perilaku sama seperti V1.
"""

import os

LINE = (
    "The spot bribed me with a lost earring. We do not speak of "
    "this. The earring and I have an understanding."
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
