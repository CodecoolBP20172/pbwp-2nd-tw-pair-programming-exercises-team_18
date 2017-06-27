def fizzbuzz(number):
    for i in range(1, 101):
        if number%15 == 0:
            return 'FizzBuzz'
            
        elif number%3 == 0:
            return 'Fizz'

        elif number%5 == 0:
            return 'Buzz'

        else:
            return number


def main():
    number = 0
    fizzbuzz(number)

if __name__ == '__main__':
    main()
