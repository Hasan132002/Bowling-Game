import os
import subprocess

BASE_DIR = r"E:\Bowling Game\TENPIN\extracted_PIL"
OUT_VIDEO = r"E:\Bowling Game\TENPIN\ALL_ANIMATIONS_DEMO.mp4"

# create file list for ffmpeg
list_file = "videos.txt"

with open(list_file, "w") as f:
    for folder in sorted(os.listdir(BASE_DIR)):
        mp4 = os.path.join(BASE_DIR, folder, f"{folder}.mp4")
        if os.path.exists(mp4):
            f.write(f"file '{mp4}'\n")

# ffmpeg concat
subprocess.run([
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", list_file,
    "-c", "copy",
    OUT_VIDEO
])

print("🎬 ALL animations merged into:", OUT_VIDEO)
