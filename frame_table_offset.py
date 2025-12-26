import struct

ANI = r"E:\Bowling Game\TENPIN\ANIMATE\STRIKE1.ANI"
data = open(ANI, "rb").read()

print("Magic:", data[0:4])

version = struct.unpack("<H", data[4:6])[0]
flags = struct.unpack("<I", data[6:10])[0]
header_size = struct.unpack("<I", data[10:14])[0]
table_offset = struct.unpack("<I", data[14:18])[0]

print("Version:", version)
print("Flags:", flags)
print("Header size:", header_size)
print("Frame table offset:", hex(table_offset))
