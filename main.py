def get_k(l):
    '''
    Given 'l', 'k' is the smallest non-negative integer satisfying l+1+k = 448 mod 512.
    '''
    n = (l+1)%512
    return (448-n)%512

'''
import random
for i in range (10):
    l = random.randint(1,10000)
    k = get_k(l)
    assert(k>=0)
    assert((l+1+k)%512 == 448)
'''