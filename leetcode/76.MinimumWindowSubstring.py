# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/902/
# Amazon

from collections import Counter, defaultdict
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        t_len = len(t)
        left, right = 0, 0
        res = (0, math.inf)
        for right, c in enumerate(s):
            if t_map[c] > 0:
                t_len -= 1
            t_map[c] -= 1
            if t_len == 0:
                while t_map[s[left]] != 0:
                    t_map[s[left]] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                t_map[s[left]] += 1
                left += 1
                t_len += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]


# Runtime: 2044 ms, faster than 5.00% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 15.3 MB, less than 8.95% of Python3 online submissions for Minimum Window Substring.
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        ct = Counter(t)
        d = defaultdict(list)
        q = list()
        w = [0, len(s)]
        for i in range(len(s)):
            c = s[i]
            if c in ct:
                q.append(c)
                d[c].append(i)
                if len(d.keys()) >= len(ct.keys()) and all([True if len(d[c]) >= ct[c] else False for c in ct.keys()]):
                    while len(d[q[0]]) > ct[q[0]]:
                        tmp = q.pop(0)
                        d[tmp].remove(min(d[tmp]))
                    if w[1] - w[0] > max(d[q[-1]]) - min(d[q[0]]):
                        w = (min(d[q[0]]), max(d[q[-1]]))
                        ans = s[w[0]:w[1] + 1]
        return ans


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
    print(Solution().minWindow(s="a", t="a"))
    print(Solution().minWindow(s="a", t="aa"))
