#!/usr/bin/env python3
# capture_calibrated_csv_V2.py
# Appends to the CSV instead of overwriting, and flushes more frequently so
# KST (or any file-tailing viewer) sees new rows appear while capture runs.
#
# KST side: in the Data Manager / vector properties for this CSV source,
# look for an auto-update / poll-interval setting (Kst is built for exactly
# this live-tailing use case) -- set it to a couple seconds and it should
# pick up new rows as they're flushed here. If a plot still looks frozen,
# try Data -> Reload once to confirm the file itself is updating, which
# tells you whether it's a KST refresh-timer setting vs. a real capture issue.

import os
import struct
import time
import csv
import serial  # pip install pyserial

COM_PORT = "COM3"
BAUD_RATE = 115200
OUT_CSV_PATH = "capture.csv"
FLUSH_INTERVAL_S = 0.5     # how often to flush to disk / print status
APPEND = False              # False = always start a fresh file (old 'w' behavior)

OUTPUT_FORMAT = 1  # 1=Ax/Ay/Az(g)  2=roll/pitch(rad)+Az(g)  3=roll/pitch(deg)+Zup(g)  4=roll/pitch(deg)

HEADERS = {
    1: ["t_us", "Ax_g", "Ay_g", "Az_g"],
    2: ["t_us", "roll_rad", "pitch_rad", "Az_g"],
    3: ["t_us", "roll_deg", "pitch_deg", "Zup_g"],
    4: ["t_us", "roll_deg", "pitch_deg", "unused"],
}

PACKET_STRUCT = struct.Struct("<IfffH")  # t_us, v1, v2, v3, crc16 = 18 bytes
PACKET_SIZE = PACKET_STRUCT.size


def crc16_ccitt(data, poly=0x1021, init=0xFFFF):
    crc = init
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ poly) & 0xFFFF if (crc & 0x8000) else (crc << 1) & 0xFFFF
    return crc


def run_capture():
    print(f"Opening port {COM_PORT}...")
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=0.05)
    ser.reset_input_buffer()

    file_exists = os.path.exists(OUT_CSV_PATH)
    mode = "a" if (APPEND and file_exists) else "w"
    csv_file = open(OUT_CSV_PATH, mode, newline="")
    writer = csv.writer(csv_file)
    if mode == "w":
        writer.writerow(HEADERS.get(OUTPUT_FORMAT, ["t_us", "v1", "v2", "v3"]))
        csv_file.flush()

    print(f"Sending 'run'... ({'appending to' if mode == 'a' else 'writing'} {OUT_CSV_PATH})")
    ser.write(b"run\n")
    ser.flush()

    print(f"Capturing verified samples to {OUT_CSV_PATH}. Press Ctrl+C to stop.")

    buf = bytearray()
    good = 0
    crc_errors = 0
    last_report = time.time()
    start_time = time.time()

    try:
        while True:
            n = ser.in_waiting or 1
            data = ser.read(n)
            if data:
                buf.extend(data)

            while len(buf) >= PACKET_SIZE:
                chunk = bytes(buf[:PACKET_SIZE])
                crc_calc = crc16_ccitt(chunk[:-2])
                t_us, v1, v2, v3, crc_read = PACKET_STRUCT.unpack(chunk)

                if crc_calc == crc_read:
                    writer.writerow([t_us, f"{v1:.6f}", f"{v2:.6f}", f"{v3:.6f}"])
                    good += 1
                    del buf[:PACKET_SIZE]
                else:
                    crc_errors += 1
                    del buf[:1]

            now = time.time()
            if now - last_report >= FLUSH_INTERVAL_S:
                elapsed = now - start_time
                rate = good / elapsed if elapsed > 0 else 0
                print(f"Captured: {good} | CRC fails: {crc_errors} | Rate: {rate:.1f} samples/sec")
                last_report = now
                csv_file.flush()
                os.fsync(csv_file.fileno())  # force it out of the OS cache immediately

    except KeyboardInterrupt:
        print("\nStopping. Sending 'stop'...")
        ser.write(b"stop\n")
        ser.flush()
        time.sleep(0.2)
    finally:
        ser.close()
        csv_file.close()
        print("\n--- Capture Report ---")
        print(f"Samples written: {good}")
        print(f"CRC failures:    {crc_errors}")
        print(f"Output file:     {OUT_CSV_PATH} ({'appended' if mode == 'a' else 'new file'})")


if __name__ == "__main__":
    run_capture()
