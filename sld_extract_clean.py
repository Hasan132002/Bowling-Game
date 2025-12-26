from PIL import Image
import os

SLD = r"E:\Bowling Game\TENPIN\STILLS\SPMLANE.SLD"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\SLD_CLEAN"

os.makedirs(OUT, exist_ok=True)

data = open(SLD, "rb").read()
pal = open(PAL, "rb").read()[:768]

# known width for bowling assets
W = 320
H = len(data) // W

print("Detected size:", W, "x", H)

pixels = data[:W * H]

img = Image.frombytes("P", (W, H), pixels)
img.putpalette(pal)

out = os.path.join(OUT, "SPMLANE_clean.png")
img.save(out)

print("Saved:", out)
