## Asymmetric
Used in:
    * TLS
    * SSH
    * SFTP
    

Public-Private key pair
Public key to encrypt the cleartext so only the party with the private key can decrypt it

Slow compared to symmetric
RSA recommened with 2048 or 4096 bits
ECC  -  heavily used on  slower machines

### Digital Signatures
    Provide Authenticity
    Non repudiation

    Hashing provide integrity checks

    Reverse of above.  Cleartext is signed with private key and hashed.