import os
import numpy as np
from PIL import Image
import imageio.v2 as imageio

BASE_DIR = r"E:\Bowling Game\TENPIN\extracted_PIL"
OUT_VIDEO = r"E:\Bowling Game\TENPIN\ALL_ANIMATIONS_DEMO_PIXEL.mp4"
FPS = 15

# 🔒 FINAL FIXED CANVAS (no scaling, only padding)
CANVAS_W = 320
CANVAS_H = 240

writer = imageio.get_writer(
    OUT_VIDEO,
    fps=FPS,
    codec="libx264",
    macro_block_size=1
)

total = 0

for folder in sorted(os.listdir(BASE_DIR)):
    folder_path = os.path.join(BASE_DIR, folder)
    if not os.path.isdir(folder_path):
        continue

    frames = sorted(
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".png")
    )

    for frame_path in frames:
        img = Image.open(frame_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        # 🧱 BLACK CANVAS (pixel-perfect)
        canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (0, 0, 0))
        canvas.paste(img, (0, 0))  # top-left, no scaling

        writer.append_data(np.array(canvas))
        total += 1

writer.close()

print("🎬 Pixel-perfect merged video created")
print("Resolution:", CANVAS_W, "x", CANVAS_H)
print("Total frames:", total)
