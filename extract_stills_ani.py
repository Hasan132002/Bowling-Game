from PIL import Image
import os

ANI_DIR = r"E:\Bowling Game\TENPIN\STILLS"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\STILLS_PNG"

os.makedirs(OUT, exist_ok=True)

pal = open(PAL, "rb").read()[:768]

W, H = 320, 200   # confirmed arcade resolution
FRAME_SIZE = W * H

def extract_first_frame(path, name):
    data = open(path, "rb").read()

    # STILLS ANI usually store raw frame right after small header
    for offset in [64, 128, 256, 512, 1024, 2048]:
        chunk = data[offset:offset + FRAME_SIZE]
        if len(chunk) != FRAME_SIZE:
            continue

        try:
            img = Image.frombytes("P", (W, H), chunk)
            img.putpalette(pal)

            out = os.path.join(OUT, name.replace(".ANI", ".png"))
            img.save(out)
            print("✔ Extracted:", out)
            return
        except:
            pass

    print("❌ Failed:", name)

for f in os.listdir(ANI_DIR):
    if f.upper().endswith(".ANI"):
        extract_first_frame(os.path.join(ANI_DIR, f), f)

print("✅ DONE: STILLS extraction complete")
