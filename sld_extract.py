from PIL import Image
import os

SLD = r"E:\Bowling Game\TENPIN\STILLS\SPMLANE.SLD"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\SLD_TEST"

os.makedirs(OUT, exist_ok=True)

data = open(SLD, "rb").read()
pal = open(PAL, "rb").read()[:768]

W, H = 320, 200
frame_size = W * H

# SLDs usually ARE raw full frames
chunk = data[:frame_size]

img = Image.frombytes("P", (W, H), chunk)
img.putpalette(pal)

out = os.path.join(OUT, "SPMLANE.png")
img.save(out)

print("Saved:", out)
