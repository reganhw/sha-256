from bitwise_funcs import*
from constants import *

def str_to_bin(M):
    '''
    Takes in a string and converts to a binary string where each character is 8 bits.
    '''
    output = ""    
    for char in M:
        if(ord(char)>126):
            raise Exception(f"The following character is not supported: {char}")
        output = output+format(ord(char), '08b')
    
    
    return output

def get_k(l):
    '''
    Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 448 mod 512.
    '''
    n = (l+1)%512
    return (448-n)%512

def padding(M):
    '''
    Takes in a message string of length l and appends:
      - One "1"
      - k zeros such that 1+l+k := 448 mod 512
      - l in 64 bits
    '''
    Mb = str_to_bin(M)                 # convert to binary string
    l = len(Mb)                        # l = message length
    k = get_k(l)                       # calculate k
    zeros = ""                         # k zeros
    for i in range (k):
        zeros = zeros+"0"
    lb = format(l, '064b')             # l in 64bits
    return Mb + "1"+zeros+lb

def split_512bit(M):
    '''
    Input: string of length 512n for some n.
    Output: M split into 512bit blocks.
    '''
    total_blocks = int(len(M)/512)
    message_blocks = []
    for i in range (total_blocks):
        block = M[512*i:512*(i+1)]
        message_blocks.append(block)
    return message_blocks

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
    '''
    Input: string of length 512
    Output: array of 64 integers
    '''
    W = split_32bit(M).copy()
    for t in range(16,64):
        Wt = (sig1(W[t-2]) + W[t-7] + sig0(W[t-15])+W[t-16])%(2**32)
        W.append(Wt)
    return W
