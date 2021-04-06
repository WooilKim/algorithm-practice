# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2964/
# 3999 / 3999 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 14.2 MB
# Your runtime beats 84.60 % of python3 submissions.
# Your memory usage beats 83.13 % of python3 submissions.

class Solution:
    # 1 <= num <= 3999
    def intToRoman(self, num: int) -> str:
        if not 1 <= num <= 3999:
            return "range error"
        kv = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
              (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
              (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        ans = ""
        for n, roman in kv:
            d = num // n
            ans += roman * d
            num -= d * n
        return ans


if __name__ == '__main__':
    print(Solution().intToRoman(num=3))
    print(Solution().intToRoman(num=4))
    print(Solution().intToRoman(num=9))
    print(Solution().intToRoman(num=58))
    print(Solution().intToRoman(num=1994))
