#!/usr/bin/env python3
# convert_tus_to_elapsed.py
# Reads an existing capture CSV (first column = t_us, raw microseconds since
# Pico boot) and writes a new CSV with an added 't_sec' column: elapsed
# seconds from the first row, as a plain float. No date/time parsing on the
# KST side needed -- just pick 't_sec' as the X vector like any other column.

import csv
import sys

IN_PATH = "capture.csv"
OUT_PATH = "capture_elapsed.csv"


def convert():
    with open(IN_PATH, "r", newline="") as fin, open(OUT_PATH, "w", newline="") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)

        header = next(reader)
        writer.writerow(["t_sec"] + header[1:])  # t_sec first, drop t_us, rest unchanged

        first_t_us = None
        rows = 0
        for row in reader:
            if not row:
                continue
            t_us = int(row[0])
            if first_t_us is None:
                first_t_us = t_us
            t_sec = (t_us - first_t_us) / 1_000_000.0
            writer.writerow([f"{t_sec:.6f}"] + row[1:])
            rows += 1

    print(f"Wrote {rows} rows to {OUT_PATH}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        IN_PATH = sys.argv[1]
    if len(sys.argv) >= 3:
        OUT_PATH = sys.argv[2]
    convert()