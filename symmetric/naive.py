"""
    Encryption based on substituin cipher
"""
def calculate_key(key):

    results = reduce(lambda acc, item: ord(acc) + ord(item), key)

    return int (results/len(key))

def decrypt(file_path, key):
    pass

def encrypt(file_path, key):
    substitution_key = calculate_key(key)
    with open(file_path, 'r') as file:
        file_contents = file.read()
    ciphertext = ''
    for line in file_contents:
        for word in line:
            for char in word:
                int_char =  ord(char) + substitution_key
                ciphertext += int_char
       
    with open(file_path, "w") as file:
        file.write(ciphertext)

    print('done encryption')


def main():
    print('Please Choose One of the following:\n 1]Encrypt\n 2]Decrypt')
    choice =  input('>')
    if choice != '1' or choice != '2':
        print('Invalid Option')
        return 
    print('Enter the Secret Key')
    key= input('>')
    #Encrypt
    if choice == '1':
        encrypt(file_path, key)
    #Decrypt
    elif choice == '2':
        decrypt(file_path, key)
  

if __name__ == "__main__":
    main()