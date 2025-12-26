from PIL import Image, ImageEnhance
import imageio
import os

ASSETS = r"E:\Bowling Game\assets"
OUT = r"E:\Bowling Game\out_animate\STRIKE.gif"

lane = Image.open(os.path.join(ASSETS, "lane.png")).convert("RGBA")
frame = Image.open(os.path.join(ASSETS, "frame.png")).convert("RGBA")
ball = Image.open(os.path.join(ASSETS, "ball.png")).convert("RGBA")
pins = Image.open(os.path.join(ASSETS, "pins.png")).convert("RGBA")

W, H = lane.size
frames = []

# 1️⃣ Ball roll
for y in range(10, H - 90, 6):
    canvas = lane.copy()
    canvas.paste(ball, (W//2 - ball.width//2, y), ball)
    canvas.paste(frame, (0, 0), frame)
    frames.append(canvas)

# 2️⃣ Pins hit
for _ in range(6):
    canvas = lane.copy()
    canvas.paste(pins, (W//2 - pins.width//2, H - pins.height - 15), pins)
    canvas.paste(frame, (0, 0), frame)
    frames.append(canvas)

# 3️⃣ Strike flash
for i in range(6):
    canvas = frames[-1].copy()
    enhancer = ImageEnhance.Brightness(canvas)
    canvas = enhancer.enhance(1.0 + i * 0.15)
    frames.append(canvas)

imageio.mimsave(OUT, frames, fps=15)
print("✅ STRIKE animation created:", OUT)
