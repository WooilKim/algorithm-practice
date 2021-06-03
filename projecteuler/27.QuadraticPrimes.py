# https://projecteuler.net/problem=27
# 27. Quadratic Primes

import math

primes = set()


def is_prime(num):
    if num in primes:
        return True
    if num < 2:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    primes.add(num)
    return True


def testEquation(a, b):
    n = 0
    while True:
        eq = n ** 2 + a * n + b
        if is_prime(eq):
            n += 1
        else:
            break
    return n


if __name__ == '__main__':
    best = 0
    besta = 0
    bestb = 0
    primes.add(2)
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            c = testEquation(a, b)
            if c > best:
                best, besta, bestb = c, a, b
    print(besta * bestb)

"""
-1000<=a,b<=1000
"""
