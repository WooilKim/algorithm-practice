"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""


def nth_prime(n) -> int:
    p = 0
    num = 2
    while p < n:
        flag = True
        for j in range(2, num):
            if num % j == 0:
                flag = False
                break
        if flag:
            p += 1
        num += 1
    return num - 1


if __name__ == '__main__':
    print(nth_prime(6))
    print(nth_prime(10001))
