"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def longest_collatz_sequence(limit):
    mem = dict()
    q = list()
    q.append((1, 1))
    mem[1] = 1

    def collatz(n):
        if n in mem:
            return mem[n]
        if n % 2 == 0:
            mem[n] = collatz(n // 2) + 1
            return mem[n]
        else:
            mem[n] = collatz(n * 3 + 1) + 1
            return mem[n]

    for i in range(2, limit):
        collatz(i)

    # for m in sorted([m for m in mem.keys()], key=lambda x: mem[x]):
    #     if mem[m] == check(m):
    #         print('same', m, mem[m], check(m))
    #     else:
    #         print('diff', m, mem[m], check(m))
    return sorted([m for m in mem.keys()], key=lambda x: -mem[x])[0]


def check(n):
    i = 1
    while n > 1:
        print(n, end=' ')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        i += 1
    print(n)
    return i


if __name__ == '__main__':
    """
    424 212 106 53 160 80 40 20 10 5 16 8 4 2 1
    """
    print(check(837799))
    print(longest_collatz_sequence(1000000))
