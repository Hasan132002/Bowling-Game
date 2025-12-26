from PIL import Image
import imageio
import os

ASSETS = r"E:\Bowling Game\assets"
OUT = r"E:\Bowling Game\out_animate\STRIKE_FIXED.gif"

lane  = Image.open(os.path.join(ASSETS, "lane.png"))   # P mode
frame = Image.open(os.path.join(ASSETS, "frame.png"))
ball  = Image.open(os.path.join(ASSETS, "ball.png"))
pins  = Image.open(os.path.join(ASSETS, "pins.png"))

W, H = lane.size
frames = []

# resize ball (nearest keeps pixel art clean)
ball = ball.resize((ball.width // 2, ball.height // 2), Image.NEAREST)

ball_x = W // 2 - ball.width // 2
pin_x  = W // 2 - pins.width // 2
pin_y  = H - pins.height - 20

# 1️⃣ Ball roll
for y in range(20, pin_y, 6):
    canvas = lane.copy()
    canvas.paste(ball, (ball_x, y))
    canvas.paste(frame, (0, 0))
    frames.append(canvas)

# 2️⃣ Pins hit
for _ in range(8):
    canvas = lane.copy()
    canvas.paste(pins, (pin_x, pin_y))
    canvas.paste(frame, (0, 0))
    frames.append(canvas)

# 3️⃣ Flash effect (WHITE OVERLAY, SAFE FOR P MODE)
for i in range(4):
    canvas = frames[-1].copy()

    flash = Image.new("P", (W, H), color=255)  # white index
    canvas = Image.blend(canvas.convert("RGB"), flash.convert("RGB"), 0.15)
    canvas = canvas.convert("P")

    frames.append(canvas)

imageio.mimsave(OUT, frames, fps=15)
print("✅ STRIKE animation FIXED & CLEAN:", OUT)
