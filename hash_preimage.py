import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'
    INT_BYTE_LEN = 4
    while(True):
        nonce = get_random_bytes(INT_BYTE_LEN)
        if get_last_k_bits(len(target_string), nonce) == int(target_string, 2):
            return nonce
    return( nonce )

def get_random_bytes(byte):
    return os.urandom(byte)

def get_last_k_bits(k, bytes):
    kMask = 2 ** k - 1
    bytes = hashlib.sha256(bytes)
    bits = int(bytes.hexdigest(), 16)
    res = bits & kMask
    return res