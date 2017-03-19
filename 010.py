'''

Project Euler Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

'''


def isPrime(num):
    # Taken from problem 3

    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i, w = 5, 2

    while i*i <= num:
        if num % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def main():
    sum_ = 0

    for i in range(2, 2000000):
        if isPrime(i):
            sum_ += i

    print(sum_)


if __name__ == '__main__':
    main()
