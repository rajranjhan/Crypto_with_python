from Crypto.Hash import SHA256

TRANSLATION_MAP = str.maketrans(
    {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5'})


def format_perserving_hash(plaintext):
    '''
    Naive implementation of format preserving hash. This is for testing collisions only. 
    Not to be used in any real world applications.
    Will return the digest of same size as the plaintext
    '''
    sha256 = SHA256.new()
    # convert to bytes
    sha256.update(plaintext.encode())
    full_hash = sha256.hexdigest()
    truncated_hash = full_hash[:len(plaintext)]

    return truncated_hash.translate(TRANSLATION_MAP)

if if __name__ == "__main__":
    plaintext = input("Enter your text to be hashed  while preseving format: ")
    print(format_perserving_hash(plaintext))
