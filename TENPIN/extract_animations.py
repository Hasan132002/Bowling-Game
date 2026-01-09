import os
import png
import numpy as np

ANI_DIR = r"E:\Bowling Game\TENPIN\ANIMATE"
OUT_BASE = r"E:\Bowling Game\TENPIN\extracted"

def extract_ani(filepath):
    with open(filepath, "rb") as f:
        if f.read(4) != b'*ANI':
            print("Skipping:", filepath)
            return

        # ---- HEADER ----
        f.read(4)  # magic/unk
        f.read(4)  # unk0
        frame_count     = int.from_bytes(f.read(4), "little")
        f.read(4)  # unk ptr
        pal_offset      = int.from_bytes(f.read(4), "little")
        frameptr_offset = int.from_bytes(f.read(4), "little")
        f.read(4)  # unk
        f.read(4)  # unk
        f.read(4)  # file type
        res_x           = int.from_bytes(f.read(4), "little")
        res_y           = int.from_bytes(f.read(4), "little")

        # ---- PALETTE ----
        f.seek(pal_offset)
        palette = []
        for _ in range(256):
            r = int.from_bytes(f.read(1), "little")
            g = int.from_bytes(f.read(1), "little")
            b = int.from_bytes(f.read(1), "little")
            palette.append((
                int(r * 255 / 63),
                int(g * 255 / 63),
                int(b * 255 / 63)
            ))

        # ---- FRAME POINTERS ----
        f.seek(frameptr_offset)
        frame_ptrs = [int.from_bytes(f.read(4), "little") for _ in range(frame_count)]

        # ---- OUTPUT ----
        name = os.path.splitext(os.path.basename(filepath))[0]
        out_dir = os.path.join(OUT_BASE, name)
        os.makedirs(out_dir, exist_ok=True)

        prev_frame = [0] * (res_x * res_y)

        def decompress_frame(offset):
            f.seek(offset)
            out = []
            while True:
                b = int.from_bytes(f.read(1), "little")
                if b == 0:
                    break
                elif b <= 0x3F:
                    val = f.read(1)[0]
                    out.extend([val] * b)
                elif b <= 0x7F:
                    lo = int.from_bytes(f.read(1), "little")
                    val = f.read(1)[0]
                    out.extend([val] * (((b & 0x3F) << 8) | lo))
                elif b <= 0xBF:
                    for _ in range(b - 0x80):
                        out.append(f.read(1)[0])
                else:
                    lo = int.from_bytes(f.read(1), "little")
                    count = lo + ((b & 0x3F) << 8)
                    for _ in range(count):
                        out.append(f.read(1)[0])
            return out

        for i, ptr in enumerate(frame_ptrs):
            raw = decompress_frame(ptr)

            # ---- SAFE FRAME BUILD ----
            frame = prev_frame.copy()
            limit = min(len(raw), len(frame))

            for p in range(limit):
                if raw[p] != 0:
                    frame[p] = raw[p]

            prev_frame = frame

            img = np.reshape(frame, (res_y, res_x))
            out_png = os.path.join(out_dir, f"{name}_{str(i).zfill(3)}.png")

            with open(out_png, "wb") as imgfile:
                png.Writer(res_x, res_y, palette=palette).write(imgfile, img)

        print(f"✔ Extracted {name} ({frame_count} frames)")

# ---- BATCH ----
os.makedirs(OUT_BASE, exist_ok=True)

for file in os.listdir(ANI_DIR):
    if file.lower().endswith((".ani", ".sld")):
        extract_ani(os.path.join(ANI_DIR, file))

print("✅ ALL ANI / SLD FILES EXTRACTED SAFELY")
