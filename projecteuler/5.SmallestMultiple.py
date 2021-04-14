"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import defaultdict
from functools import reduce


def smallest_multiple(limit):
    # divs = set()
    divs = defaultdict(int)
    for i in range(2, limit + 1):
        j = 2
        while i >= j:
            k = 0
            while i % j == 0:
                i //= j
                k += 1
            divs[j] = max(divs[j], k)
            j += 1

    return reduce(lambda a, b: a * b, [key ** divs[key] for key in divs.keys()])


if __name__ == '__main__':
    print(smallest_multiple(10))  # 2520
    print(smallest_multiple(20))
    pass
