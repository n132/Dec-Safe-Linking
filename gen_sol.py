def XxX(leaked,page_off, orecal):
    if(page_off<0):
        neg=1
        page_off=-page_off
    else:
        neg=-1
    x1 = (page_off >> 24)
    x2 = ((page_off >> 12) & 0xfff)
    x3 = (page_off & 0xfff)
    A = leaked >> 36
    D = orecal
    G = (leaked & 0xfff) ^ D
    if(x3>G):
        JW1 = 1
    else:
        JW1 = 0 
    
    C = G + 0x1000 * JW1 + x3*neg
    F = ((leaked>>12)&0xfff) ^ C

    if( x2 > F-JW1 ):
        JW2 = 1
    else:
        JW2 = 0 
    B = F-JW1 + 0x1000 * JW2 + x2*neg
    # print(hex(leaked),hex(page_off),hex(JW2),hex(F))
    res = (A<<36) | (B <<24) | (C<<12) | D
    return res
if __name__ == "__main__":
  print(hex(XxX(0x000055500000c7f9,0,0x2a0)))
