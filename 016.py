'''

Project Euler Problem 16:

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

'''

def main():
    vec = [0]*1000
    vec[0] = 2

    for _ in range(1, 1000):
        c = 0

        for i in range(0, 1000):
            vec[i] = vec[i]*2 + c
            c = 0

            while vec[i] > 9:
                vec[i] -= 10
                c += 1

    print(sum(vec))


if __name__ == '__main__':
    main()
