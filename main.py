from bitwise_funcs import *
from preprocessing import *
import constants

limit = 2**32


def sha256(M):
    M_padded = padding(M)
    M_blocks = split_512bit(M_padded)
    H = constants.H.copy()
    for block in M_blocks:
        W = get_message_schedule(block)
        working_variables = update_variables(W,H)
        for j in range (8):
            H[j] = (H[j]+ working_variables[j])%limit
    return H_to_hex(H)

def update_variables(W,H):
    a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
    for t in range (64):
        T1 = (h + Sig1(e) + Ch(e,f,g) + constants.K[t] + W[t])%limit
        T2 = (Sig0(a) + Maj(a,b,c))%limit
        h = g
        g = f
        f = e
        e = (d + T1)%limit
        d = c
        c=b
        b=a
        a = (T1 + T2)%limit
    return a,b,c,d,e,f,g,h


def H_to_hex(H):
    '''
    Input: array of integers H
    Output: each integer in H converted to 8-digit hex and concatenated as a string.
    '''
    output = ""
    for num in H:
        output = output + format(num, '08x')
    return output

