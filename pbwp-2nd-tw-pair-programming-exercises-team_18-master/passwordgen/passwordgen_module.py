import string
import random

def passwordgen():
    password = ""
    for i in range(8, 16):
        password += random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice("[!@#$%^&*()?]")

    print(password)
    return password


def main():
    passwordgen()
    


if __name__ == '__main__':
    main()
