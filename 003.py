'''

Project Euler Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''

import math

def isPrime(num):
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
    num = 600851475143

    for x in range(int(math.sqrt(num)), 0, -1):
        if num % x == 0 and isPrime(x):
            print(x)
            return


if __name__ == '__main__':
    main()
