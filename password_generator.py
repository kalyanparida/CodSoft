#Task : Python program for Password Generator

import random
import string

def password_generate(length):
    
    char = string.ascii_letters + string.digits + string.punctuation   

    password = ''.join(random.choice(char) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))

    password = password_generate(length)

    print("Generated Password: ",password)

if __name__ == "__main__":
    main()

    