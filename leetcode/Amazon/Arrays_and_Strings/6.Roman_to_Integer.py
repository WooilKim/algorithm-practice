# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2965/

class Solution:
    def romanToInt(self, s: str) -> int:
        # Better to go in reverse
        # Use a dictionary to encode the values of each letter
        # Add or substract based on previous value
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        val = 0
        for c in s[::-1]:
            cur = d[c]
            if (prev > cur):
                val -= cur
            else:
                val += cur
            prev = cur

        return val


class Solution2:
    def romanToInt(self, s: str) -> int:
        if not 1 <= len(s) <= 15:
            return -1
        kv = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
              (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
              (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        ans = 0
        i = 0
        j = 0
        while i < len(s):
            n, roman = kv[j][0], kv[j][1]
            if s[i:i + len(roman)] == roman:
                ans += n
                i += len(roman)
            else:
                j += 1

        return ans


# 1 <= num <= 3999
# 1 <= s.length <= 15
if __name__ == '__main__':
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("IX"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))
