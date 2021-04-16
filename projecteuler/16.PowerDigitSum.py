"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""
from functools import reduce


def power_digit_sum(n):
    return reduce(lambda a, b: a + b, map(int, str(2 ** n)))


if __name__ == '__main__':
    print(power_digit_sum(15))  # 32768
    print(power_digit_sum(1000))
