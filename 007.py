'''

Project Euler Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

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
    n = 0

    for i in range(1, 100000000000):
        if isPrime(i):
            n += 1

            if n == 10001:
                print(i)
                return


if __name__ == '__main__':
    main()
