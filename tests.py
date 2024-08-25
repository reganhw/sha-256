import random
from bitwise_funcs import*
for i in range (20):
    x = random.randint(0,2**32-1)
    y = random.randint(0,2**32-1)
    z = random.randint(0,2**32-1)
    ch = Ch(x,y,z)
    xb = format(x, '032b')
    yb = format(y, '032b')
    zb = format(z, '032b')
    chb = format(ch, '032b')
    
    
    for j in range(32):
        if(xb[j]=='1'):
            if(chb[j]!=yb[j]):
                print(f"Error1 at index {j} where x:{x}({xb}), y:{y}({yb}), z:{z}({zb}), ch:{ch}({chb}). chb[j] is {chb[j]} and yb[j] is {yb[j]}")
                break;
        else:
            if(chb[j]!=zb[j]):
                print(f"Error2 at index {j} where x:{x}({xb}), y:{y}({yb}), z:{z}({zb}), ch:{ch}({chb}). chb[j] is {chb[j]} and zb[j] is {zb[j]}")


for i in range (20):
    x = random.randint(0,2**32-1)
    n = random.randint(0,31)
    assert(rotl(n,x)==rotr(32-n,x))