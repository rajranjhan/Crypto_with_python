from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"

    def __init__(self):
       pass
    
    def __save_file(self, contents, file_name):
        with open(file_name, "w") as file:
            file.write(contents)
    
    def __read_file(self, file_name):
        with open(file_name) as file:
            contents = file.read() 
        return contents

    def __generate_random(self):
        return Random.new().read()

    def generate_keys(self):
        keys =  RSA.generate(4096)
        private_key = keys.exportkey("PEM")
        public_key =  keys.publickey().exportkey("PEM")
        self.__save_file(private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(public_key, self.PUBLIC_KEY_FILE)
        print("Much success in generating keys")

    def encrypt(self, cleartext, public_keypath = None):
        if public_keypath == None:
            public_keypath = self.PUBLIC_KEY_FILE

        public_key =  RSA.importKey(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext)
        return base64.b64encode(encrypted_data)

    def decrypt(self,ciphertext, private_keypath =None):
        if private_keypath == None:
            private_keypath = self.PRIVATE_KEY_FILE

        ciphertext = base64.b64decode(ciphertext)
        private_key =  RSA.importKey(self.__read_file(private_keypath))
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(ciphertext)


if __name__ == "__main__":
    CryptoRSA().generate_keys()
    encrypted_data = CryptoRSA().encrypt("Hello World")
    print(encrypted_data)
    decrypted_data =  CryptoRSA().decrypt(encrypted_data)
    print(decrypted_data)
