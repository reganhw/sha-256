from bitwise_funcs import*

def str_to_bin(M):
    '''
    Takes in a string and converts to a binary string.
    Each character in the string is converted to an 8 bit string.
    '''
    output = ""    
    for char in M:
        if(ord(char)>126):
            raise Exception(f"The following character is not supported: {char}")
        output = output+format(ord(char), '08b')
    
    
    return output

# ---------------------------------NIST document page 13, section 5.1.1.---------------------------------
def get_k(l):
    '''
    Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 448 mod 512.
    '''
    n = (l+1)%512
    return (448-n)%512

def padding(M):
    '''
    Takes in a string M of length l and appends:
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

# ---------------------------------Page 14, section 5.2.1.---------------------------------

def split_512bit(M):
    '''
    Input: String of length 512n for some n.
    Output: String array, M split into 512bit blocks.
    '''
    total_blocks = int(len(M)/512)    # number of total blocks
    message_blocks = []               # array to store values
    for i in range (total_blocks):
        block = M[512*i:512*(i+1)]
        message_blocks.append(block)
    return message_blocks

def split_32bit(M):
    '''
    Input: String M of length 512
    Output: Integer array, M split into 16 blocks of 32 bits, each block then converted to an integer.
    '''
    output = []
    for i in range (16):
        block = M[32*i:32*(i+1)]
        output.append(int(block,2))
    return output

# ---------------------------------Page 22, section 6.2.2.-1---------------------------------

def get_message_schedule(M):
    '''
    Input: String M of length 512
    Output: Array of 64 integers, message schedule as described in the NIST document
    '''
    W = split_32bit(M).copy()
    for t in range(16,64):
        Wt = (sig1(W[t-2]) + W[t-7] + sig0(W[t-15])+W[t-16])%(2**32)
        W.append(Wt)
    return W
