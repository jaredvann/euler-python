'''

Project Euler Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''

def main():
    largest = 0

    for i in range(1, 1000):
        for j in range(1, 1000):
            z = i*j

            if z > largest and z.__str__() == z.__str__()[::-1]:
                largest = z

    print(largest)


if __name__ == '__main__':
    main()
