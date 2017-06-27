def palindrome(string):
    if string.lower().replace(" ", "") == (string[::-1].lower().replace(" ", "")):
        return True

    else:
        return False

def main():
    string = ""
    palindrome(string)
    return


if __name__ == '__main__':
    main()
