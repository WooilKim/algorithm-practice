"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from itertools import combinations
import time


def non_abundant_sums():
    a = time.process_time()
    abundant_nums2 = [i for i in range(1, 28123 + 1) if d(i) > i]
    b = time.process_time()
    i = 1
    abundant_nums = set()
    while i < 28123 + 1:
        if i not in abundant_nums:
            if d(i) > i:
                j = 1
                while True:
                    if j * i < 28123:
                        abundant_nums.add(i * j)
                        j += 1
                    else:
                        break
        i += 1
    c = time.process_time()
    print(len(abundant_nums), c - b)
    print(len(abundant_nums2), b - a)

    # d(n) 의 회수를 줄이는데 시간이 더 걸리는 이유는 뭐지???

    c = combinations(abundant_nums, 2)
    ans = set(sum(ci) for ci in c)
    for n in abundant_nums:
        ans.add(2 * n)

    return sum([i for i in range(1, 28123 + 1) if i not in ans])


# print(abundant_nums)


def d(n):
    divs = list()
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
    return sum(divs)


if __name__ == '__main__':
    print(non_abundant_sums())
