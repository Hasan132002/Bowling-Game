import os
import imageio.v2 as imageio
from PIL import Image
import numpy as np

BASE_DIR = r"E:\Bowling Game\TENPIN\extracted_PIL"
OUT_VIDEO = r"E:\Bowling Game\TENPIN\ALL_ANIMATIONS_DEMO.mp4"
FPS = 15

writer = imageio.get_writer(OUT_VIDEO, fps=FPS, codec="libx264")

total = 0

for folder in sorted(os.listdir(BASE_DIR)):
    mp4 = os.path.join(BASE_DIR, folder, f"{folder}.mp4")
    if not os.path.exists(mp4):
        continue

    reader = imageio.get_reader(mp4)
    for frame in reader:
        writer.append_data(frame)
        total += 1

    reader.close()

writer.close()
print("🎬 Merged video created:", OUT_VIDEO, "Frames:", total)
