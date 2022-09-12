from z3 import *
def XxX(leaked, off, orecal):
    leaked = BitVecVal(leaked, 48)
    orecal = BitVecVal(orecal, 48)
    off  = BitVecVal(off,48)

    res  = BitVec('res', 48)
    sss  = BitVec('sss', 48)

    s = Solver()

    s.add((sss>>12)^res==leaked)
    s.add((sss>>12)-(res>>12)==off)
    s.add(((res<<36)>>36)==orecal)



    if str(s.check()) == 'sat':
        m = s.model()
        # print(m)
        return  m.evaluate(res).as_long()
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
    for x in range(0x1000):
        p = process("./main")
        
        leaked = recv_num()
        off = recv_num()
        orecal = recv_num()
        res = XxX(leaked,off,orecal)
        print(hex(res))

        p.send(p64(res))
        res = p.read()
        if b'Success\n' != res:
            print("???")
            exit(1)
        p.close()
    print("ALL DONE")
