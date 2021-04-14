"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def even_fibonacci_numbers(limit):
    a = 1
    b = 2
    ans = [b]
    while b < limit:
        a, b = b, b + a
        if b % 2 == 0:
            ans.append(b)
    print(ans)
    return sum(ans)


if __name__ == '__main__':
    print(even_fibonacci_numbers(4 * 1000000))
