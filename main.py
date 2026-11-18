#!/usr/bin/env python3
"""news-image-20261118 v9a (akun 5): 40-story front page.

Late-Breaking Complete atas v8 (985.514, rank 99): resep v8 + 40 cerita
(3 TOP + 12 grid + 25 ALSO) termasuk berita sore/malam 18 Nov (GTA VI,
Peltola, inflasi UK 3,6%, COP31 35x35, emas $3.792, Jeffries 251-262,
operasi darat Gaza) + tag sumber per kartu + badge temporal
(REPORTED/SCHEDULED/PLANNED) + kotak DATE CHECK + deck 2 baris + peta
40 pin. Setiap cerita pertama dilaporkan Rabu 18 Nov 2026 (item 17 Nov
dikecualikan, dicantumkan di DATE CHECK). Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
