import string
import random


if __name__ == "__main__":
    upper = list(string.ascii_lowercase)
    lower = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_char = list(string.punctuation)
    characters = []

    characters.extend(upper)
    characters.extend(lower)
    characters.extend(digits)
    characters.extend(special_char)

    password_len = input("Enter the password length : ")

    if password_len.isnumeric() and int(password_len) < len(characters):
        if  int(password_len) < 8:
            print("Password length must be greater than 7 !!!")
        else:
            password_len = int(password_len)
            print("".join(random.sample(characters, password_len)))
    else:
        print("Password length is invalid!!!")
