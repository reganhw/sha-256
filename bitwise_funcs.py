limit = 2**32
MASK = (1 << 32) - 1

def neg(x):
    return x ^MASK                  # bitwise negation while making it 32 bits

def shr(n,x):
    return x>>n

def rotl(n,x):
    result = (x<<n) |(x>>(32-n))     # actual output
    return result & MASK             # keep under 32 bits

def rotr(n,x):
    result = (x>>n)|(x<<(32-n))      # actual output
    return result & MASK             # keep under 32 bits

def Ch(x,y,z):
    return (x & y) ^ (neg(x) & z)  

def Maj(x,y,z):
    return (x & y) ^(x & z) ^(y &z)

def Sig0(x):
    return rotr(2,x)^ rotr(13,x)^rotr(22,x)

def Sig1(x):
    return rotr(6,x)^rotr(11,x)^rotr(25,x)

def sig0(x):
    return rotr(7,x)^rotr(18,x)^shr(3,x)

def sig1(x):
    return rotr(17,x)^rotr(18,x)^shr(10,x)
'''
def xor(x,y):
    result = bin(x^y)[2:]
    l = len(result)    
    for i in range (32-l):
        result = "1"+result
    return int(result, 2)

print("a:", format(a, '032b'), " b: ", format(b,'032b'))
print("c:", format(c, '032b'))
'''
'''
import random
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


'''