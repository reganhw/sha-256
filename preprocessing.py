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
    Input: integer
    '''
    Mb = bin(M)[2:]
    l = len(Mb)
    output = Mb + "1"
    k = get_k(l)
    for i in range (k):
        output = output +"0"
    
    output = output+ format(l, '064b')
    return output

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

'''
nums = []
for i in range (16):
    n = random.randint(0, 2**32-1)
    nums.append(n)

msg = ""
for n in nums:
    msg = msg+format(n, '032b')

M = split_32bit(msg)

assert (nums==M)
'''