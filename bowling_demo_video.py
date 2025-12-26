from PIL import Image
import imageio
import os

BASE = r"E:\Bowling Game\out_frames\ALL_SLD"
OUT = r"E:\Bowling Game\bowling_demo.gif"

lane = Image.open(os.path.join(BASE, "SPMLANE.png")).convert("RGBA")
ball = Image.open(os.path.join(BASE, "SPMBALL.png")).convert("RGBA")
pins = Image.open(os.path.join(BASE, "SPMPIN1.png")).convert("RGBA")
frame = Image.open(os.path.join(BASE, "FRAMWRX.png")).convert("RGBA")

W, H = lane.size

frames = []

# ball movement (top → bottom)
for y in range(10, H - 40, 8):
    canvas = lane.copy()

    # paste ball
    canvas.paste(ball, (W//2 - ball.width//2, y), ball)

    # add frame overlay
    canvas.paste(frame, (0, 0), frame)

    frames.append(canvas)

# last frames with pins
for _ in range(10):
    canvas = lane.copy()
    canvas.paste(pins, (W//2 - pins.width//2, H - pins.height - 10), pins)
    canvas.paste(frame, (0, 0), frame)
    frames.append(canvas)

# write video
writer = imageio.get_writer(OUT, fps=15)


for f in frames:
    writer.append_data(f)

writer.close()
print("🎳 Bowling demo video created:", OUT)
