from PIL import Image
import os

ANI = r"E:\Bowling Game\TENPIN\STILLS\STRIKE1.ANI"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\STILLS_STRIKE1"

os.makedirs(OUT, exist_ok=True)

data = open(ANI, "rb").read()
pal = open(PAL, "rb").read()[:768]

W, H = 320, 200
frame_size = W * H

# STILLS usually start frame data very early
possible_offsets = [64, 128, 256, 512, 1024]

for off in possible_offsets:
    chunk = data[off:off+frame_size]
    if len(chunk) != frame_size:
        continue

    img = Image.frombytes("P", (W, H), chunk)
    img.putpalette(pal)

    out = os.path.join(OUT, f"frame_at_{off}.png")
    img.save(out)
    print("Saved:", out)
