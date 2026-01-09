import os
from PIL import Image

BASE = r"E:\Bowling Game\TENPIN\extracted"

for folder in os.listdir(BASE):
    path = os.path.join(BASE, folder)
    if not os.path.isdir(path):
        continue

    for f in os.listdir(path):
        if not f.lower().endswith(".png"):
            continue
        if "_" not in f:
            continue

        fp = os.path.join(path, f)
        try:
            img = Image.open(fp)
            img = img.convert("RGB")  # strip palette + filters
            img.save(fp, format="PNG", optimize=False)
        except Exception as e:
            print("❌ Could not fix:", fp, e)

print("✅ PNG normalization complete")
