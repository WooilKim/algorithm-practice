"""
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
"""


def counting_sundays(start_year, end_year):
    months = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
              [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    n = 1 + sum(months[1]) % 7  # 3 -> 1901-01-01 : Wednesday
    ans = 0
    for y in range(start_year, end_year + 1):
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            opt = 1
        else:
            opt = 0
        for m in months[opt]:
            n += m
            if n % 7 == 0:
                ans += 1
    return ans


if __name__ == '__main__':
    print(counting_sundays(1901, 2000))
