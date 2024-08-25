import random
from bitwise_funcs import*

def neg_test():
    for i in range (20):
        x = random.randint(0,2**32-1)   # For a random integer x,
        negx = neg(x)
        assert(x^negx == 2**32-1)       # x ^ neg(x) should equal a 32bit string of 1s.

def rot_test():
    for i in range (20):
        x = random.randint(0,2**32-1)
        n = random.randint(0,31)
        assert(rotl(n,x)==rotr(32-n,x))
        

def Ch_test():
    for i in range (20):
        # Get random integers and calculate Ch(x,y,z)
        x = random.randint(0,2**32-1)
        y = random.randint(0,2**32-1)
        z = random.randint(0,2**32-1)
        ch = Ch(x,y,z)

        # Convert to 32bit string
        xb = format(x, '032b')
        yb = format(y, '032b')
        zb = format(z, '032b')
        chb = format(ch, '032b')
        
        # Check condition holds for all 32bits
        for j in range(32):
            if(xb[j]=='1'):
                assert(chb[j]==yb[j])
            else:
                assert(chb[j]==zb[j])
    return None

