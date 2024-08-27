from bitwise_funcs import *
from preprocessing import *
from constants import*

limit = 2**32


def the(M):
    H = [0x6a09e667, 0xbb67ae85,0x3c6ef372,0xa54ff53a, 0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    W = get_message_schedule(M)
    a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]

    for t in range (64):
        T1 = (h + Sig1(e) + Ch(e,f,g) + K[t] + W[t])%limit
        T2 = (Sig0(a) + Maj(a,b,c))%limit
        h = g
        g = f
        f = e
        e = (d + T1)%limit
        d = c
        c=b
        b=a
        a = (T1 + T2)%limit

    
    values = [a,b,c,d,e,f,g,h]
    for j in range (8):
        H[j] = (H[j]+ values[j])%limit
    

    return H_to_hash(H)

def H_to_hash(H):
    output = ""
    for hash in H:
        output = output + format(hash, '08x')
    return output

o = the(a_padded)
print(o)