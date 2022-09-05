def dec(addr):
    x1 = addr >>36
    x2 = (addr >> 24) & 0xfff
    x3 = (addr >> 12) & 0xfff
    x4 = addr & 0xfff
    r1 = x1
    r2 = x2^r1
    r3 = x3^r2
    r4 = x4^r3
    print(hex(x1),hex(x2),hex(x3),hex(x4),hex(addr))
    return  r1<<36 | r2<<24  | r3<<12 | r4
if __name__ == "__main__":
    print(hex(dec(0x000055500000c7f9)))
