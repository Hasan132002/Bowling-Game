import subprocess
import os

VLC_PATH = "vlc"  # agar VLC installed hai
VIDEO_DIR = "videos"

def play_animation(event):
    video = os.path.join(VIDEO_DIR, f"{event}.mp4")

    if not os.path.exists(video):
        print("Video not found:", video)
        return

    subprocess.Popen([
        VLC_PATH,
        "--fullscreen",
        "--play-and-exit",
        video
    ])
