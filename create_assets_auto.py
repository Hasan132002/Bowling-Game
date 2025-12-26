import os
import shutil

# jahan tumne SLD se PNG extract ki thi
SRC = r"E:\Bowling Game\out_frames\ALL_SLD"

# naya assets folder (auto banega)
ASSETS = r"E:\Bowling Game\assets"

os.makedirs(ASSETS, exist_ok=True)

mapping = {
    "SPMLANE.png": "lane.png",
    "FRAMWRX.png": "frame.png",
    "SPMBALL.png": "ball.png",
    "SPMPIN1.png": "pins.png",
    "COPYRITE.png": "copyright.png"
}

for src_name, dst_name in mapping.items():
    src = os.path.join(SRC, src_name)
    dst = os.path.join(ASSETS, dst_name)

    if os.path.exists(src):
        shutil.copy(src, dst)
        print("✔ Copied:", dst_name)
    else:
        print("❌ Missing:", src_name)

print("✅ assets folder ready at:", ASSETS)
