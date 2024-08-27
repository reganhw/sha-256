from bitwise_funcs import *
from preprocessing import *
import constants

limit = 2**32

def sha256(M):
    '''
    Input: Message string M of any length.
    Output: The sha256 hash for M.
    '''
    M_padded = padding(M)                                    # pad M.
    M_blocks = split_512bit(M_padded)                        # split into 512 bit blocks.
    H = constants.H.copy()                                   # initialise hash values.

    for block in M_blocks:                                   # for each message block...
        W = get_message_schedule(block)                      # obtain word schedule.
        working_variables = update_variables(W,H)            # obtain working variables.
        for j in range (8):                                  
            H[j] = (H[j]+ working_variables[j])%limit        # update hash values.

    return H_to_hex(H)                                       # convert final hash values into hex string.

def update_variables(W,H):
    '''
    Input - W: Word schedule W of a message. Array of 64 integers.
    Input - H: Hash values at the current stage. Array of 8 integers.
    Output - Array of integers [a,b,c,d,e,f,g,h] as in the NIST specification.
    '''
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
    Input: Array of integers H.
    Output: String where each integer in H is converted to 8-digit hex and then concatenated.
    '''
    output = ""
    for num in H:
        output = output + format(num, '08x')
    return output

# Take input from command line.
if __name__ == '__main__':
    message = input("Input: ")
    hash = sha256(message)
    print("Hash: ",hash)