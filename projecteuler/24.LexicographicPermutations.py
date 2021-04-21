"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations
import math


def lexicographic_permutations():
    nums = list(range(10))
    p = permutations(nums, 10)
    l = [''.join(map(str, x)) for x in p]
    l.sort()
    return l[1000000 - 1]


def lexicographic_permutations2(nth):
    nums = list(range(10))
    ans = list()
    for i in range(10):
        j = 0
        fact = math.factorial(10 - i - 1)
        while nth > fact:
            nth -= fact
            j += 1
        ans.append(nums[j])
        del nums[j]
    return ''.join(map(str, ans))


if __name__ == '__main__':
    # print(lexicographic_permutations())
    print(lexicographic_permutations2(1000000))
    # 2783915460
