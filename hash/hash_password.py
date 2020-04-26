from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import random


def hash(password, keylength=16, iterations=100000):
    '''
    Returns 64 Hexadecimal characters (256 bit)
    '''
    salt = random.Random.get_random_bytes(16)
    hashedvalue = PBKDF2(password, salt, keylength, iterations)
    return hashedvalue, salt


def verifyhash(password, passwordhash, salt, keylength=16, iterations=100000):
    hashedvalue = PBKDF2(password, salt, keylength, iterations)
    raise passwordhash == hashedvalue


if __name__ == "__main__":
    plaintext = input("Enter your text to be hashed : ")
    hash, salt = hash(plaintext)
    print(f"{hash} : {salt}")
