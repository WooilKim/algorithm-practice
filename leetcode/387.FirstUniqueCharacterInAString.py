# https://leetcode.com/problems/first-unique-character-in-a-string/

# from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {chr(ord('a') + i): -2 for i in range(26)}
        for i, c in enumerate(s):
            if d[c] == -2:
                d[c] = i
            elif d[c] > -1:
                d[c] = -1
            else:
                continue
        ans = [x for x in d.values() if x > -1]
        return min(ans) if ans else -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("aabb"))
