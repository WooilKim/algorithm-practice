"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome_product(digit):
    ans = 0
    for a in range(10 ** (digit - 1), 10 ** digit)[::-1]:
        for b in range(10 ** (digit - 1), 10 ** digit)[::-1]:
            if f'{a * b}' == f'{a * b}'[::-1]:
                ans = max(ans, a * b)
    return ans


if __name__ == '__main__':
    print(largest_palindrome_product(2))  # 9009 = 91 * 99
    print(largest_palindrome_product(3))
