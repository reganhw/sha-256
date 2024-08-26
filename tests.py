import random
from bitwise_funcs import*
from preprocessing import*

def neg_test():
    for i in range (20):
        x = random.randint(0,2**32-1)   # For a random integer x,
        negx = neg(x)
        assert(x^negx == 2**32-1)       # x ^ neg(x) should equal a 32bit string of 1s.

def rot_test():
    for i in range (20):
        x = random.randint(0,2**32-1)   # For a random integer x,
        n = random.randint(0,31)        # and random n,
        assert(rotl(n,x)==rotr(32-n,x)) # rotl(n,x) = rotr((32-n,x))
        

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

def Maj_test():
    for i in range (20):
        # Get random integers and calculate Ch(x,y,z)
        x = random.randint(0,2**32-1)
        y = random.randint(0,2**32-1)
        z = random.randint(0,2**32-1)
        maj = Maj(x,y,z)

        # Convert to 32bit string
        xb = format(x, '032b')
        yb = format(y, '032b')
        zb = format(z, '032b')
        majb = format(maj, '032b')
        
        # Check condition holds for all 32bits
        for j in range(32):
            if((int(xb[j])+ int(yb[j])+ int(zb[j]))>1):
                assert(majb[j]=="1")
            else:
                assert(majb[j]=="0")
    return None

def get_k_test():
    for i in range (20):                 # For 20 random integers l,
        l = random.randint(0,10000)
        k = get_k(l)                     # get k and check:
        assert(0<=k)                     # k is non-negative
        assert(k<512)                    # k is the smallest non-negative integer satisfying this
        assert(((k+1+l)%512)==448)       # k+1+l :=448 mod 512

def padding_test():
    a_output="011000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    +"000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    +"000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    + "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    +"000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    +"00000000000000000000000000001000"

print(len(str_to_bin("abcde")))
