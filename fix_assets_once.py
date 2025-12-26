from PIL import Image, ImageEnhance
import os

ASSETS = r"E:\Bowling Game\assets"
FIXED  = r"E:\Bowling Game\assets_fixed"

os.makedirs(FIXED, exist_ok=True)

for f in os.listdir(ASSETS):
    if not f.lower().endswith(".png"):
        continue

    img = Image.open(os.path.join(ASSETS, f)).convert("RGB")

    # gentle brightness & contrast fix
    img = ImageEnhance.Brightness(img).enhance(1.4)
    img = ImageEnhance.Contrast(img).enhance(1.2)

    img.save(os.path.join(FIXED, f))
    print("✔ fixed:", f)

print("✅ assets normalized")
