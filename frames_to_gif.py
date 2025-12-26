import imageio
import os

BASE = r"E:\Bowling Game\out_animate"

for folder in os.listdir(BASE):
    path = os.path.join(BASE, folder)
    if not os.path.isdir(path):
        continue

    frames = sorted([
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.endswith(".png")
    ])

    if len(frames) < 2:
        continue

    out_gif = os.path.join(path, f"{folder}.gif")
    images = [imageio.imread(f) for f in frames]

    imageio.mimsave(out_gif, images, fps=15)
    print("🎬 Created:", out_gif)

print("✅ ALL GIFS CREATED")
