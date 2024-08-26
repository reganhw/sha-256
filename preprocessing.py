import random
from bitwise_funcs import*
def get_k(l):
    '''
    Given 'l', 'k' is the smallest non-negative integer satisfying l+1+k = 448 mod 512.
    '''
    n = (l+1)%512
    return (448-n)%512

def padding(M):
    '''
    Takes in a message of length l and appends:
      - One "1"
      - k zeros such that 1+l+k := 448 mod 512
      - l in 64bits
    '''
    Mb = bin(M)[2:]                    # convert to binary string
    l = len(Mb)                        # l = message length
    k = get_k(l)                       # calculate k
    zeros = ""                         # k zeros
    for i in range (k):
        zeros = zeros+"0"
    lb = format(l, '064b')             # l in 64bits
    return Mb + "1"+zeros+lb

for i in range (20):
    m = random.randint(0, 2**32-1)
    result = padding(m)
    assert(len(result)==512)


def split_32bit(M):
    '''
    Input: string of length 512
    Output: Array of 16 blocks of 32 bits
    '''
    output = []
    for i in range (16):
        block = M[32*i:32*(i+1)]
        output.append(int(block,2))
    return output

def get_message_schedule(M):
    W = split_32bit(M).copy()
    for t in range(16,80):
        mid = W[t-3]^W[t-8]^W[t-14]^W[t-16]
        W.append(rotl(1,mid))
    return W