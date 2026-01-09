import os
import numpy as np
from PIL import Image
import imageio.v2 as imageio

# ================== CONFIG ==================
BASE_DIR = r"E:\Bowling Game\TENPIN\extracted_PIL"
FPS = 15
CODEC = "libx264"
# ============================================


def pad_to_macroblock(img, block=16):
    """
    Pads image height to nearest multiple of macro block size (default 16)
    to avoid ffmpeg resizing warnings.
    """
    w, h = img.size
    new_h = ((h + block - 1) // block) * block
    if new_h == h:
        return img

    padded = Image.new("RGB", (w, new_h), (0, 0, 0))
    padded.paste(img, (0, 0))
    return padded


for folder in os.listdir(BASE_DIR):
    folder_path = os.path.join(BASE_DIR, folder)

    if not os.path.isdir(folder_path):
        continue

    # Collect PNG frames
    frames = sorted(
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".png")
    )

    if len(frames) < 2:
        print(f"⚠️ Skipping {folder}: not enough frames")
        continue

    out_mp4 = os.path.join(folder_path, f"{folder}.mp4")

    writer = imageio.get_writer(
        out_mp4,
        fps=FPS,
        codec=CODEC
    )

    used_frames = 0

    for frame_path in frames:
        try:
            img = Image.open(frame_path).convert("RGB")
            img = pad_to_macroblock(img)  # safe padding
            writer.append_data(np.array(img))
            used_frames += 1
        except Exception as e:
            print(f"⚠️ Skipped frame: {frame_path} → {e}")

    writer.close()

    if used_frames > 0:
        print(f"🎬 MP4 created: {out_mp4} ({used_frames} frames)")
    else:
        print(f"❌ No valid frames for {folder}")

print("✅ ALL MP4 CONVERSIONS COMPLETE")
