val = 0xCAFE
print((val & 0xF) >= 0x7)
print(hex(((val >> 8) | (val << 8)) & 0xFFFF))
print(hex(((val << 4) | (val >> 12)) & 0xFFFF))