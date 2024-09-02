import random
from bitwise_funcs import*
from preprocessing import*
from sha256 import*

def sha256_single_block_test():
    # Reference: https://coding.tools/sha256
    assert(sha256("")=="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    assert(sha256("a")=="ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb")
    assert(sha256("!$%^&")=="eb012954744da04f90257fab2b276062e7f9f21bc7c6d43ca610a9c328d692a0")
    assert(sha256("Hello world")=="64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c")

def sha256_many_block_test():
    # Reference: https://coding.tools/sha256

    long_str1 = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
    long_str2=("I\'m the golden baby born into the center. Mother was a gun and I fed nature to the beggars. "
    +"Always talking but the kids never listen, they die in the evening, become demons for the weekend.")
    long_str3=("Somebody hooted and they hollered: Can I buy a vowel? "
    +"Don\'t let her catch you in the act of throwing in the towel! "
    +"And when it\'s not as it appears to be the flagrant foul, "
    +"can I put my fingers in your mouth before you start to growl?")

    assert(sha256(long_str1)=="248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1")
    assert(sha256(long_str2)=="78a7fab979239554f368f42b7c6cffacd52cc9823bd920b1bd40f869713845cc")
    assert(sha256(long_str3)=="80f48d65f3de367836fecac2fd98c034d3bfcc9d280b374881c0b6bf88e18825")


#-----------------------------------------------------------------------------------------------------------

def neg_test():
    for i in range (20):
        x = random.randint(0,2**32-1)   # For a random integer x,
        negx = neg(x)
        assert(x^negx == 2**32-1)       # x ^ neg(x) should equal a 32bit string of 1s.

def rot_test():
    for i in range (20):
        x = random.randint(0,2**32-1)   # For a random integer x,
        n = random.randint(0,31)        # and random n,
        assert(rotl(n,x)==rotr(32-n,x)) # rotl(n,x) = rotr((32-n,x)).
        

def Ch_test():
    for i in range (20):
        # Get random integers and calculate Ch(x,y,z)
        x = random.randint(0,2**32-1)
        y = random.randint(0,2**32-1)
        z = random.randint(0,2**32-1)
        ch = Ch(x,y,z)

        # Convert to 32bit string
        xb = format(x, '032b')
        yb = format(y, '032b')
        zb = format(z, '032b')
        chb = format(ch, '032b')
        
        # Check condition holds for all 32bits
        for j in range(32):
            if(xb[j]=='1'):
                assert(chb[j]==yb[j])
            else:
                assert(chb[j]==zb[j])
    return None

def Maj_test():
    for i in range (20):
        # Get random integers and calculate Ch(x,y,z).
        x = random.randint(0,2**32-1)
        y = random.randint(0,2**32-1)
        z = random.randint(0,2**32-1)
        maj = Maj(x,y,z)

        # Convert to 32bit string.
        xb = format(x, '032b')
        yb = format(y, '032b')
        zb = format(z, '032b')
        majb = format(maj, '032b')
        
        # Check condition holds for all 32bits.
        for j in range(32):
            if((int(xb[j])+ int(yb[j])+ int(zb[j]))>1):
                assert(majb[j]=="1")
            else:
                assert(majb[j]=="0")
    return None

def get_k_test():
    for i in range (20):                 # For 20 random integers l,
        l = random.randint(0,10000)
        k = get_k(l)                     # get k and check:
        assert(0<=k)                     # k is non-negative
        assert(k<512)                    # k is the smallest non-negative integer satisfying this
        assert(((k+1+l)%512)==448)       # k+1+l :=448 mod 512


if __name__ == '__main__':
    sha256_single_block_test()
    sha256_many_block_test()
  