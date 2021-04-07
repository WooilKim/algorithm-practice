# https://leetcode.com/problems/reorganize-string/
#
# Runtime: 32 ms, faster than 70.30% of Python3 online submissions for Reorganize String.
# Memory Usage: 14.3 MB, less than 33.45% of Python3 online submissions for Reorganize String.

class Solution:
    def reorganizeString(self, S: str) -> str:
        S = list(S)
        d = dict()
        for s in S:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        queue = sorted(list(d.keys()), key=lambda x: -d[x])
        if 2 * d[queue[0]] - 1 > len(S):
            return ''

        i, idx = 0, 0
        ans = [' '] * len(S)
        while i < len(queue):
            if d[queue[i]] > 0:
                # first loop : 1 char and 1 blank
                if idx // len(S) == 0:
                    ans[idx] = queue[i]
                    d[queue[i]] -= 1
                    if idx + 1 < len(S):
                        ans[idx + 1] = ' '
                    idx += 2
                # next loop : 1 char in every blank
                else:
                    while ans[idx % len(S)] != ' ':
                        idx += 1
                    ans[idx % len(S)] = queue[i]
                    d[queue[i]] -= 1
            else:
                i += 1
        return ''.join(ans)


if __name__ == '__main__':
    print(Solution().reorganizeString("aab"))
    print(Solution().reorganizeString("aaab"))
