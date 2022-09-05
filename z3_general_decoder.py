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


if __name__ == "__main__":
  print(hex(XxX(0x000055500000c7f9,0,0x2a0)))
