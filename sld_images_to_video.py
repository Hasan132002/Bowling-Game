import cv2
import os

IMG_DIR = r"E:\Bowling Game\out_frames\ALL_SLD"
OUT_VIDEO = r"E:\Bowling Game\sld_showcase.mp4"

images = sorted([
    f for f in os.listdir(IMG_DIR)
    if f.lower().endswith(".png")
])

if not images:
    raise RuntimeError("No images found")

first = cv2.imread(os.path.join(IMG_DIR, images[0]))
h, w, _ = first.shape

out = cv2.VideoWriter(
    OUT_VIDEO,
    cv2.VideoWriter_fourcc(*"mp4v"),
    1,          # 1 FPS (har image 1 second)
    (w, h)
)

for img_name in images:
    frame = cv2.imread(os.path.join(IMG_DIR, img_name))
    out.write(frame)
    print("Added:", img_name)

out.release()
print("Video created:", OUT_VIDEO)
