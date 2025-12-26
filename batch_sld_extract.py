from PIL import Image
import os

SLD_DIR = r"E:\Bowling Game\TENPIN\STILLS"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"
OUT = r"E:\Bowling Game\out_frames\ALL_SLD"

os.makedirs(OUT, exist_ok=True)

pal = open(PAL, "rb").read()[:768]

W = 320  # fixed width for bowling assets

for file in os.listdir(SLD_DIR):
    if not file.lower().endswith(".sld"):
        continue

    path = os.path.join(SLD_DIR, file)
    data = open(path, "rb").read()

    H = len(data) // W
    if H <= 0:
        continue

    pixels = data[:W * H]

    try:
        img = Image.frombytes("P", (W, H), pixels)
        img.putpalette(pal)

        out = os.path.join(OUT, file.replace(".SLD", ".png"))
        img.save(out)
        print("Extracted:", out)
    except Exception as e:
        print("Skipped:", file, e)

print("DONE: All possible SLD extracted")
