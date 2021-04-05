# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/


# Your runtime beats 79.76 % of python3 submissions.
class Solution:
    def myAtoi(self, s: str) -> int:
        m, M = -2 ** 31, 2 ** 31 - 1
        # 10 ** 22
        signs = ['-', '+']
        nums = [a for a in '0123456789']
        sign = 1
        ans = 0
        i = 0
        if not s:
            return 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in signs:
            if s[i] == '-':
                sign *= -1
            i += 1
        while i < len(s) and s[i] in nums:
            ans = ans * 10 + int(s[i])
            i += 1
            if ans > -m:
                break
        ans *= sign

        if sign < 0:
            return max(m, ans)
        else:
            return min(M, ans)


if __name__ == '__main__':
    print(Solution().myAtoi("42"))
    print(Solution().myAtoi(s="   -42"))
    print(Solution().myAtoi(s="4193 with words"))
    print(Solution().myAtoi(s="words and 987"))
    print(Solution().myAtoi(s="-91283472332"))
    print(Solution().myAtoi(s=""))
