# https://leetcode.com/problems/valid-parentheses/

# Runtime: 32 ms, faster than 58.05% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.1 MB, less than 96.72% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        q = list()
        d = {']': '[', ')': '(', '}': '{'}
        for c in s:
            if q and c in d:
                if q.pop() != d[c]:
                    return False
            else:
                q.append(c)
        return True if not q else False


if __name__ == '__main__':
    print(Solution().isValid(s="()"))
    print(Solution().isValid(s="()[]{}"))
    print(Solution().isValid(s="(]"))
    print(Solution().isValid(s="([)]"))
    print(Solution().isValid(s="{[]}"))
