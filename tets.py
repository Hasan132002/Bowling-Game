import struct
from PIL import Image
import os

ANI = r"E:\Bowling Game\TENPIN\ANIMATE\STRIKE1.ANI"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\STRIKE1"

os.makedirs(OUT, exist_ok=True)

data = open(ANI, "rb").read()
pal = open(PAL, "rb").read()[:768]

W, H = 320, 200

# simple brute-force scan for real frames
frame_size = W * H
count = 0

for i in range(0, len(data) - frame_size, 1024):
    chunk = data[i:i+frame_size]
    if len(chunk) != frame_size:
        continue

    img = Image.frombytes("P", (W, H), chunk)
    img.putpalette(pal)

    out = os.path.join(OUT, f"frame_{count:04d}.png")
    img.save(out)
    count += 1

    if count == 20:
        break

print("Extracted", count, "test frames")
