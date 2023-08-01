import string
import random

letters = string.ascii_letters
numbers = string.digits

def password_generator():
    printable = f'{letters}{numbers}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k = 8)
    random_password = ''.join(random_password)
    return random_password

def main():
    password = password_generator()
    print(password)

if __name__ == "__main__":
    main()