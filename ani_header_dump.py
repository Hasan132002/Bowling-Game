import struct

ANI = r"E:\Bowling Game\TENPIN\ANIMATE\STRIKE1.ANI"
data = open(ANI, "rb").read()

print("First 64 bytes (hex):")
for i in range(0, 64, 16):
    chunk = data[i:i+16]
    hexs = " ".join(f"{b:02X}" for b in chunk)
    print(f"{i:04X}: {hexs}")

print("\nAs WORDs (16-bit):")
for i in range(0, 32, 2):
    w = struct.unpack("<H", data[i:i+2])[0]
    print(f"{i:02X}: {w}")

print("\nAs DWORDs (32-bit):")
for i in range(0, 32, 4):
    d = struct.unpack("<I", data[i:i+4])[0]
    print(f"{i:02X}: {d}")
