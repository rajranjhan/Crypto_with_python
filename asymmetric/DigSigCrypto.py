from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256


class DigSigCrypto:
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

    def __sha256(self, input):
        sha256 =  SHA256.new()
        sha256.update(input.encode())
        return sha256

    def generate_keys(self):
        keys =  RSA.generate(4096)
        private_key = keys.exportkey("PEM")
        public_key =  keys.publickey().exportkey("PEM")
        self.__save_file(private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(public_key, self.PUBLIC_KEY_FILE)
        print("Much success in generating keys")


    def sign(self, message, private_keypath = None):
        if private_keypath == None:
            private_keypath = self.PRIVATE_KEY_FILE

        private_key =  RSA.importKey(self.__read_file(private_keypath))
        signature = PKCS1_PSS.new(private_key)
        return signature.sign(self, _sha256(message))

    def verify(self, signed_signature, message, public_keypath = None):
        if public_keypath == None:
            public_keypath = self.PUBLIC_KEY_FILE

        public_key =  RSA.importKey(self.__read_file(public_keypath))
        verifier = PKCS1_PSS.new(public_key)
        verification = verifier.verify(self._sha256(message), signed_signature)
        return verification

if __name__ == "__main__":
    DigSigCrypto().generate_keys()
    signature = DigSigCrypto().sign("Hello world")
    DigSigCrypto().verify(signature, "Hello world")