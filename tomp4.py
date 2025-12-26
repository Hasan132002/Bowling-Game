from PIL import Image
import imageio
import numpy as np
import os

# ===== PATHS =====
ASSETS = r"E:\Bowling Game\assets_fixed"
OUT    = r"E:\Bowling Game\out_animate\STRIKE_PERFECT.mp4"

os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ===== LOAD ASSETS =====
lane  = Image.open(os.path.join(ASSETS, "lane.png")).convert("RGB")
frame = Image.open(os.path.join(ASSETS, "frame.png")).convert("RGB")
ball  = Image.open(os.path.join(ASSETS, "ball.png")).convert("RGB")
pins  = Image.open(os.path.join(ASSETS, "pins.png")).convert("RGB")

W, H = lane.size
frames = []

# scale ball safely
ball = ball.resize((ball.width // 2, ball.height // 2), Image.NEAREST)

ball_x = W // 2 - ball.width // 2
pin_x  = W // 2 - pins.width // 2
pin_y  = H - pins.height - 20

# ===== BALL ROLL =====
for y in range(20, pin_y, 6):
    canvas = lane.copy()
    canvas.paste(ball, (ball_x, y))
    canvas.paste(frame, (0, 0))
    frames.append(canvas)

# ===== PIN HIT HOLD =====
for _ in range(12):
    canvas = lane.copy()
    canvas.paste(pins, (pin_x, pin_y))
    canvas.paste(frame, (0, 0))
    frames.append(canvas)

# ===== WRITE MP4 =====
writer = imageio.get_writer(
    OUT,
    fps=15,
    codec="libx264",
    quality=8
)

for f in frames:
    writer.append_data(np.array(f))   # ✅ FIX HERE

writer.close()

print("✅ STRIKE MP4 CREATED SUCCESSFULLY:")
print(OUT)
