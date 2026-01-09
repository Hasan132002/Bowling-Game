import subprocess
import os

OUT_DIR = "videos"
os.makedirs(OUT_DIR, exist_ok=True)

EVENT_SOURCES = {
    "STRIKE1": (
        "https://www.youtube.com/watch?v=70p3S7MS2U0",
        "00:03:36-00:03:42"
    ),
    "DOUBLE1": (
        "https://www.youtube.com/watch?v=70p3S7MS2U0",
        "00:00:19-00:00:25"
    ),
    "TURKEY1": (
        "https://www.youtube.com/watch?v=70p3S7MS2U0",
        "00:04:53-00:04:58"
    ),
    "SPARE1": (
        "https://www.youtube.com/watch?v=70p3S7MS2U0",
        "00:02:34-00:02:41"
    ),
    "FOUL": (
        "https://www.youtube.com/watch?v=70p3S7MS2U0",
        "00:00:49-00:00:57"
    ),
}

for event, (url, section) in EVENT_SOURCES.items():
    out_file = os.path.join(OUT_DIR, f"{event}.mp4")
    print(f"⬇️ Downloading {event}")

    subprocess.run([
        "yt-dlp",
        "--download-sections", f"*{section}",
        "-f", "mp4",
        "-o", out_file,
        url
    ], check=True)

    print(f"✅ Ready: {out_file}")

print("\n🎉 ALL EVENTS DOWNLOADED WITHOUT FFMPEG")
