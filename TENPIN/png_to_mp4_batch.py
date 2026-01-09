import os
import imageio.v2 as imageio
from PIL import Image
import numpy as np

BASE = r"E:\Bowling Game\TENPIN\extracted"
FPS = 15

for folder in os.listdir(BASE):
    path = os.path.join(BASE, folder)
    if not os.path.isdir(path):
        continue

    frames = sorted(
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.lower().endswith(".png") and "_" in f
    )

    if len(frames) < 2:
        continue

    out_mp4 = os.path.join(path, f"{folder}.mp4")
    writer = imageio.get_writer(out_mp4, fps=FPS)

    ok_frames = 0

    for f in frames:
        try:
            img = Image.open(f).convert("RGB")
            writer.append_data(np.array(img))
            ok_frames += 1
        except Exception as e:
            print("⚠️ Skipped bad frame:", f, e)

    writer.close()

    if ok_frames > 0:
        print(f"🎬 MP4 created: {out_mp4} ({ok_frames} frames)")
    else:
        print(f"❌ No valid frames for {folder}")

print("✅ ALL MP4s DONE")
