'''

Project Euler Problem 19:

You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

def main():
    t, day, wday, month, year = 0, 1, 2, 1, 1901

    while year < 2001:
        if day == 1 and wday == 7:
            t += 1

        if wday == 7:
            wday = 1
        else:
            wday += 1

        day += 1

        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                day = 1
                month += 1
        elif month == 2:
            if year % 4 != 0 and day > 28:
                day = 1
                month += 1
            elif year % 4 == 0 and day > 29:
                day = 1
                month += 1
        else:
            if day > 31:
                day = 1
                month += 1

        if month > 12:
            month = 1
            year += 1

    print(t)


if __name__ == '__main__':
    main()
