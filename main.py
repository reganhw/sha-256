import random
from bitwise_funcs import*
def get_k(l):
    '''
    Given 'l', 'k' is the smallest non-negative integer satisfying l+1+k = 448 mod 512.
    '''
    n = (l+1)%512
    return (448-n)%512

'''

for i in range (10):
    l = random.randint(1,10000)
    k = get_k(l)
    assert(k>=0)
    assert((l+1+k)%512 == 448)

'''
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

def make_message_schedule(M):
    W = split_32bit(M).copy()
    for t in range(16,80):
        mid = W[t-3]^W[t-8]^W[t-14]^W[t-16]
        W.append(rotl(1,mid))
    return W

'''
nums = []
for i in range (32):
    n = random.randint(0, 2**16-1)
    nums.append(format(n, '016b'))

msg = ""
for n in nums:
    msg = msg+n

M = split_32bit(msg)

for m in M:
    assert(len(m)==32)

msg2  =""

for m in M:
    msg2 = msg2+m

assert(msg2==msg)
'''