# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/

# Your runtime beats 79.76 % of python3 submissions.
class Solution:
    def myAtoi(self, s: str) -> int:
        m, M = -2 ** 31, 2 ** 31 - 1
        signs = ['-', '+']
        nums = [a for a in '0123456789']
        sign = '+'
        ans = 0
        i = 0
        if not s:
            return 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in signs:
            sign = s[i]
            i += 1
        num = ''
        while i < len(s) and s[i] in nums:
            num += s[i]
            i += 1
        if not num:
            return ans
        else:
            ans = int(num)
            if sign == '-':
                ans = max(m, -ans)
            else:
                ans = min(M, ans)
            return ans


if __name__ == '__main__':
    print(Solution().myAtoi("42"))
    print(Solution().myAtoi(s="   -42"))
    print(Solution().myAtoi(s="4193 with words"))
    print(Solution().myAtoi(s="words and 987"))
    print(Solution().myAtoi(s="-91283472332"))
    print(Solution().myAtoi(s=""))
