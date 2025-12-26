import os

ANI = r"E:\Bowling Game\TENPIN\STILLS\STRIKE1.ANI"

data = open(ANI, "rb").read()

# SLD files usually don't have magic, but raw VGA blocks
# we scan for long blocks of non-zero bytes (image-like)

candidates = []

for i in range(0, len(data) - 20000, 256):
    chunk = data[i:i+20000]
    if chunk.count(b'\x00') < len(chunk) * 0.2:
        candidates.append(i)

print("Possible image blocks at offsets:")
for c in candidates[:10]:
    print(hex(c))
