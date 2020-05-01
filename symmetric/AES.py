from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import base64


class AESCrypto:
    def md5_hash(self, text):
        hash = MD5.new()
        hash.update(text.encode())
        return hash.hexdigest()

    def __init__(self, key):
        # Key size has to be 128 bits
        self.key = self.md5_hash(key)

    def encrypt(self, cleartext):
        # Block size should be equal to 128 bits or 16 bytes
        Block_size = 16
        # pad the value
        def pad(s): return s + (Block_size - len(s) %
                                Block_size) * chr(Block_size - len(s) % Block_size)
        cleartext_blocks = pad(cleartext)

        iv = Random.new().read(Block_size)
        crypto = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + crypto.encrypt(cleartext_blocks))

    def decrypt(self, ciphertext):
        decodedtext = base64.b64decode(ciphertext)
        iv = decodedtext[:16]
        crypto = AES.new(self.key, AES.MODE_CBC, iv)
        unpad = lambda s : s[0:-ord(s[-1])]
        return unpad(crypto.decrypt(decodedtext[16:]))


if __name__ == "__main__":
    aes = AESCrypto("thisisatest")
    encrypted = aes.encrypt('Hello world')
    print(encrypted)
    decrypted = aes.decrypt(encrypted)
    print(decrypted)
