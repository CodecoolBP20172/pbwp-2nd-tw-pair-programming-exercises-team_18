import datetime


def years(age):
    old = 100 - int(age) + 2016

    return old


def main():
    name = input('What is your name?')
    age = input("How old are you?")
    print("Hello {} you'll be a hundred yeras in {}".format(name, years(age)))
    return


if __name__ == '__main__':
    main()
