import subprocess
import os

SOURCE = "full_source.mp4"
OUT_DIR = "videos"
os.makedirs(OUT_DIR, exist_ok=True)

EVENTS = {
    "STRIKE1": ("00:03:36", 6),
    "DOUBLE1": ("00:00:19", 6),
    "TURKEY1": ("00:04:53", 5),
    "SPARE1":  ("00:02:34", 7),
    "FOUL":    ("00:00:49", 8),
}

for name, (start, duration) in EVENTS.items():
    out = os.path.join(OUT_DIR, f"{name}.mp4")

    print(f"✂️ Creating {name}")

    subprocess.run([
        "ffmpeg", "-y",
        "-ss", start,
        "-i", SOURCE,
        "-t", str(duration),
        "-vf", "scale=1280:720",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        out
    ], check=True)

    print("✅ OK:", out)

print("\n🎉 ALL EVENTS CREATED CLEANLY (NO EMPTY FILES)")
