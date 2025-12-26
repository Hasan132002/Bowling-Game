from PIL import Image

ANI = r"E:\Bowling Game\TENPIN\STILLS\STRIKE1.ANI"
PAL = r"E:\Bowling Game\SCORER\NSP_DEF.PAL"

data = open(ANI,"rb").read()
pal = open(PAL,"rb").read()[:768]

W = 320

# try dynamic height
for off in [0x200, 0x300, 0x380, 0x400, 0x500]:
    pixels = data[off:]
    if len(pixels) < 20000:
        continue

    H = len(pixels) // W
    pixels = pixels[:W*H]

    img = Image.frombytes("P",(W,H),pixels)
    img.putpalette(pal)
    img.save(f"test_{hex(off)}.png")
    print("Saved", off)
