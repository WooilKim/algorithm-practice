"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from collections import defaultdict


def amicable_numbers(n):
    nums = defaultdict(list)
    ans = list()
    for i in range(1, n + 1):
        nums[d(i)].append(i)
    for i in range(1, n + 1):
        for nu in nums[i]:
            if nu in nums[i] and nu in nums and i in nums[nu] and i != nu and i not in ans:
                ans.append(nu)
                ans.append(i)
                break
    return sum(ans), ans


def d(n):
    divs = list()
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
    return sum(divs)


if __name__ == '__main__':
    print(amicable_numbers(10000))
