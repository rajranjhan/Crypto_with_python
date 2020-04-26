import hash_passwords


def login(user_name, password):
    with open("account.txt") as file:
        account_info = file.read()
        s = account_info.split(':')
        user_name = s[0]
        password = s[1]
        salt = s[2]

        hash_passwords.hash(password,)


if __name__ == "__main__":
    input = raw_input("Enter: \n 1] to Register\n 2) to Login\nChoice>  ")
     
    if input == '1'
        user_name = raw_input("Enter a username: ")
        password = raw_input("Enter a password ")
        register(user_name, password)
    elif input = '2':
        user_name = raw_input("Enter a username: ")
        password = raw_input("Enter a password ")
        login(user_name, password)