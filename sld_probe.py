from PIL import Image
import os
import math

SLD = r"E:\Bowling Game\TENPIN\STILLS\SPMLANE.SLD"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\SLD_PROBE"

os.makedirs(OUT, exist_ok=True)

data = open(SLD, "rb").read()
pal = open(PAL, "rb").read()[:768]

print("SLD size:", len(data))

# try common widths
widths = [32, 64, 128, 160, 256, 320]

for w in widths:
    h = len(data) // w
    if h < 10:
        continue

    pixels = data[:w*h]

    try:
        img = Image.frombytes("P", (w, h), pixels)
        img.putpalette(pal)
        out = os.path.join(OUT, f"probe_{w}x{h}.png")
        img.save(out)
        print("Saved:", out)
    except:
        pass
