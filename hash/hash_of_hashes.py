from Crypto.Hash import SHA256

def hash_with_pepper(value, pepper):
    
    sha256 = SHA256.new()
    # convert to bytes
    sha256.update(value.encode())
    hashofValue = sha256.hexdigest()
    sha256.update(pepper.encode() + hashofValue.encode())
    ValueHashSeed = sha256.hexdigest()
    sha256.update(ValueHashSeed.encode() + hashofValue.encode())
    ValueHash = sha256.hexdigest()
    return ValueHash


if __name__ == "__main__":
    results = set()
    for i in range(1,10):
      results.add(hash_with_pepper('389023334339480', '298e1d96ef827bcc47a142934854d415b0f193920ff2f56c2d06f34365429659'))
      
    print(results)