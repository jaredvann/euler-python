'''

Project Euler Problem 17:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''

def main():
    _1 = 3;
    _2 = 3;
    _3 = 5;
    _4 = 4;
    _5 = 4;
    _6 = 3;
    _7 = 5;
    _8 = 5;
    _9 = 4;
    _10 = 3;
    _11 = 6;
    _12 = 6;
    _13 = 8;
    _14 = 8;
    _15 = 7;
    _16 = 7;
    _17 = 9;
    _18 = 8;
    _19 = 8;
    _20 = 6;
    _30 = 6;
    _40 = 5;
    _50 = 5;
    _60 = 5;
    _70 = 7;
    _80 = 6;
    _90 = 6;
    _x00 = 7;
    _x000 = 8;
    _and = 3;

    _1_9 = _1 + _2 + _3 + _4 + _5 + _6 + _7 + _8 + _9;

    _10_19 = _10 + _11 + _12 + _13 + _14 + _15 + _16 + _17 + _18 + _19;

    _1_99 = _1_9*9 + _10_19 + (_20 + _30 + _40 + _50 + _60 + _70 + _80 + _90)*10;

    _x00_x99 = _x00*100 + _and*99 + _1_99;

    _1_1000 = _1_99 + _1_9*100 + _x00_x99*9 + _1 + _x000;

    print(_1_1000)


if __name__ == '__main__':
    main()
