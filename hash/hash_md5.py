from Crypto.Hash import MD5


def hash(plaintext):
    '''
    Good integrity checker
    Not meant for protecting passwords
    Returns 32 Hexadecimal characters (128 bit)
    '''
    md5 = MD5.new()
    # convert to bytes
    md5.update(plaintext.encode())
    return md5.hexdigest()


if if __name__ == "__main__":
    plaintext = input("Enter your text to be hashed : ")
    print(hash(plaintext))
