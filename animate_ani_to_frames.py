from PIL import Image
import os

ANI_DIR = r"E:\Bowling Game\TENPIN\ANIMATE"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_animate"

os.makedirs(OUT, exist_ok=True)

pal = open(PAL, "rb").read()[:768]

W, H = 320, 200
FRAME_SIZE = W * H

def extract_frames(ani_path, name):
    data = open(ani_path, "rb").read()
    out_dir = os.path.join(OUT, name.replace(".ANI", ""))
    os.makedirs(out_dir, exist_ok=True)

    count = 0
    for off in range(0, len(data) - FRAME_SIZE, 1024):
        chunk = data[off:off + FRAME_SIZE]
        if len(chunk) != FRAME_SIZE:
            continue

        try:
            img = Image.frombytes("P", (W, H), chunk)
            img.putpalette(pal)

            out = os.path.join(out_dir, f"frame_{count:03d}.png")
            img.save(out)
            count += 1

            if count >= 120:  # safety limit
                break
        except:
            pass

    print(f"{name}: extracted {count} frames")
    return out_dir, count

for f in os.listdir(ANI_DIR):
    if f.upper().endswith(".ANI"):
        extract_frames(os.path.join(ANI_DIR, f), f)

print("✅ ALL ANI FRAME EXTRACTION DONE")
