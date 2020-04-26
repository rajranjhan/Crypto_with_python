import hash_password

def register(user_name, password):
    with open("account.txt", "w") as file:
        hashedpassword, salt = hash_password.hash(password)
        file.write(f'{user_name}:{hashedpassword}:{salt}')

def login(user_name, password):
    with open("account.txt") as file:
        account_info = file.read()
        s = account_info.split(':')
        user_name = s[0]
        passwordhash = s[1]
        salt = s[2]

        hash_password.verifyhash(password, passwordhash, salt)


if __name__ == "__main__":
    choice = input("Enter: \n 1] to Register\n 2) to Login\nChoice>  ")
     
    if choice == '1':
        user_name = input("Enter a username: ")
        password = input("Enter a password ")
        register(user_name, password)
    elif input == '2':
        user_name = input("Enter a username: ")
        password = input("Enter a password ")
        login(user_name, password)
    else:
        print('Invalid choice')