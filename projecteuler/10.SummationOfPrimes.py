"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def sum_primes(n) -> int:
    nums = [i for i in range(n + 1)]
    nums[1] = -1
    for i in range(2, n + 1):
        for j in range(2, (n) // i + 1):
            nums[i * j] = -1
    return sum([nums[i] for i in range(len(nums)) if nums[i] > 0])


if __name__ == '__main__':
    print(sum_primes(10))
    print(sum_primes(2000000))
