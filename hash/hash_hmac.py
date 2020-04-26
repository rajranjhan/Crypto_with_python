from Crypto.Hash import HMAC

def hash(plaintext, secret):
    """[summary]
    Integrity and Authenticity
    Uses MD5 or SHA1 as the hashing algorithm
    Arguments:
        plaintext {[type]} -- [description]
    """
    h = HMAC.new(secret)
    h.update(plaintext)
    return h.hexdigest()



if __name__ == "__main__":
    print(hash("gus", "secret"))