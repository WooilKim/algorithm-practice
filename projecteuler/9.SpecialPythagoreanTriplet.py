"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def special_pythagorean_triplet(n) -> int:
    for a in range(1, n):
        for b in range(a + 1, n):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


if __name__ == '__main__':
    print(special_pythagorean_triplet(1000))
