from PIL import Image
import imageio
import os

ASSETS = r"E:\Bowling Game\assets"
OUT = r"E:\Bowling Game\out_animate\STRIKE_FINAL.gif"

lane  = Image.open(os.path.join(ASSETS, "lane.png"))
frame = Image.open(os.path.join(ASSETS, "frame.png"))
ball  = Image.open(os.path.join(ASSETS, "ball.png"))
pins  = Image.open(os.path.join(ASSETS, "pins.png"))

W, H = lane.size
frames = []

# resize ball safely
ball = ball.resize((ball.width // 2, ball.height // 2), Image.NEAREST)

ball_x = W // 2 - ball.width // 2
pin_x  = W // 2 - pins.width // 2
pin_y  = H - pins.height - 20

# 1️⃣ Ball roll
for y in range(20, pin_y, 6):
    canvas = lane.copy()
    canvas.paste(ball, (ball_x, y))
    canvas.paste(frame, (0, 0))
    frames.append(canvas.convert("RGB"))  # 🔥 KEY FIX

# 2️⃣ Pins appear
for _ in range(10):
    canvas = lane.copy()
    canvas.paste(pins, (pin_x, pin_y))
    canvas.paste(frame, (0, 0))
    frames.append(canvas.convert("RGB"))  # 🔥 KEY FIX

imageio.mimsave(OUT, frames, fps=15)
print("✅ STRIKE FINAL animation created:", OUT)
