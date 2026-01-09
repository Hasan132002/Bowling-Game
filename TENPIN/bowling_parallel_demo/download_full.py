import subprocess

URL = "https://www.youtube.com/watch?v=70p3S7MS2U0"
OUT = "full_source.mp4"

print("⬇️ Downloading FULL source video")

subprocess.run([
    "yt-dlp",
    "-f", "bv*[vcodec=h264]+ba[acodec=aac]/b",
    "--merge-output-format", "mp4",
    "-o", OUT,
    URL
], check=True)

print("✅ Full video downloaded:", OUT)
