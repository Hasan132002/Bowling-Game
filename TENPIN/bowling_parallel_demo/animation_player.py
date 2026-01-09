import subprocess
import os

VLC = "vlc"   # agar VLC path issue kare to full path likhna
VIDEO_DIR = "videos"

def play(event):
    video = os.path.join(VIDEO_DIR, f"{event}.mp4")

    if not os.path.exists(video):
        print("❌ Missing video:", video)
        return

    subprocess.Popen([
        VLC,
        "--fullscreen",
        "--play-and-exit",
        "--no-video-title-show",
        video
    ])
