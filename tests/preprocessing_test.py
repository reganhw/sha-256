import random
from preprocessing import*

def test_get_k():
    for i in range (20):                 # For 20 random integers l,
        l = random.randint(0,10000)
        k = get_k(l)                     # get k and check:
        assert(0<=k)                     # k is non-negative
        assert(k<512)                    # k is the smallest non-negative integer satisfying this
        assert(((k+1+l)%512)==448)       # k+1+l :=448 mod 512

def test_padding():
    M = '1'
    M_padded = padding(M)
    assert(len(M_padded)%512==0)
    assert(M_padded[8]=="1")
    assert(M_padded[-4:-1]+M_padded[-1]=="1000")