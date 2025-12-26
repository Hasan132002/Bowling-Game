import struct

ANI = r"E:\Bowling Game\TENPIN\STILLS\STRIKE1.ANI"
data = open(ANI, "rb").read()

print("File size:", len(data))
print("Magic:", data[:4])

# WORDs
for i in range(0, 32, 2):
    w = struct.unpack("<H", data[i:i+2])[0]
    print(f"{i:02X}: {w}")
