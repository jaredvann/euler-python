'''

Project Euler Problem 20:

n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

def main():
    x = 100

    r = [0]*200
    r[0] = 1

    for i in range(1, x+1):
        carry = 0

        for j in range(0, 200):
            r[j] = r[j] * i + carry
            carry = 0

            while r[j] > 9:
                r[j] -= 10
                carry += 1

    print(sum(r))


if __name__ == '__main__':
    main()
