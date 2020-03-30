
import binascii

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(message, key):
    m = toHex(message)
    k = toHex(key)
    code = m^k
    return code

print
