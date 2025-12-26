from PIL import Image
import imageio
import os

ASSETS = r"E:\Bowling Game\assets_fixed"
OUT = r"E:\Bowling Game\out_animate\STRIKE_PERFECT.gif"

lane  = Image.open(os.path.join(ASSETS, "lane.png"))
frame = Image.open(os.path.join(ASSETS, "frame.png"))
ball  = Image.open(os.path.join(ASSETS, "ball.png"))
pins  = Image.open(os.path.join(ASSETS, "pins.png"))

W, H = lane.size
frames = []

ball = ball.resize((ball.width // 2, ball.height // 2), Image.NEAREST)

ball_x = W//2 - ball.width//2
pin_x  = W//2 - pins.width//2
pin_y  = H - pins.height - 20

# ball roll
for y in range(20, pin_y, 6):
    canvas = lane.copy()
    canvas.paste(ball, (ball_x, y))
    canvas.paste(frame, (0,0))
    frames.append(canvas)

# pins appear
for _ in range(10):
    canvas = lane.copy()
    canvas.paste(pins, (pin_x, pin_y))
    canvas.paste(frame, (0,0))
    frames.append(canvas)

imageio.mimsave(OUT, frames, fps=15)
print("🎳 STRIKE PERFECT:", OUT)
