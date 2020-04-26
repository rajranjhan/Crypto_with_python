from Crypto.Hash import SHA256


def hash(plaintext):
    '''
    Returns 64 Hexadecimal characters (256 bit)
    '''
    sha2 = SHA256.new()
    # convert to bytes
    sha2.update(plaintext.encode())
    return sha2.hexdigest()


if if __name__ == "__main__":
    plaintext = input("Enter your text to be hashed : ")
    print(hash(plaintext))
