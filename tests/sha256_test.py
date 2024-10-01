import hashlib

from sha256 import *
from bitwise_funcs import*

def test_single_block():
    text_vectors = ("", "a", "!£$%^&", "Hello world")
    for v in text_vectors:
        compare_against = hashlib.sha256(v.encode()).hexdigest()
        hash_bin = sha256(v, "bin")
        assert(sha256(v)==compare_against)
        assert(format(int(hash_bin,2), '064x')==compare_against)

def test_many_blocks():

    long_str1 = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq" # 448 bits
    long_str2=("I\'m the golden baby born into the center. Mother was a gun and I fed nature to the beggars. "
    +"Always talking but the kids never listen, they die in the evening, become demons for the weekend.")
    long_str3=("Somebody hooted and they hollered: Can I buy a vowel? "
    +"Don\'t let her catch you in the act of throwing in the towel! "
    +"And when it\'s not as it appears to be the flagrant foul, "
    +"can I put my fingers in your mouth before you start to growl?")
    
    for v in (long_str1, long_str2, long_str3):
        compare_against = hashlib.sha256(v.encode()).hexdigest()
        hash_bin = sha256(v, "bin")
        assert(sha256(v)==compare_against)
        assert(format(int(hash_bin,2), '064x')==compare_against)
  