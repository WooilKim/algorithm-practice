# https://leetcode.com/problems/decode-ways/
from collections import deque

# time limit : "111111111111111111111111111111111111111111111"
class Solution2:
    def numDecodings(self, s: str) -> int:
        cnt = 0
        queue = deque([s])
        while queue:
            curr = queue.popleft()
            if curr == '':
                cnt += 1
                print(queue)
                continue
            if curr[0] != '0':
                if len(curr) > 1:
                    if 0 < int(curr[:2]) < 27:
                        queue.append(curr[2:])
                queue.append(curr[1:])
        return cnt


# Runtime: 24 ms, faster than 96.43% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.6 MB, less than 11.36% of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:
        visited = dict()

        def dfs(t):
            if t in visited:
                return visited[t]
            if not t:
                return 1
            if t[0] != '0':
                if len(t) > 1:
                    if 0 < int(t[:2]) < 27:
                        visited[t] = dfs(t[2:]) + dfs(t[1:])
                        return visited[t]
                visited[t] = dfs(t[1:])
                return visited[t]
            else:
                return 0

        cnt = dfs(s)
        return cnt


if __name__ == '__main__':
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings("226"))
    print(Solution().numDecodings("0"))
    print(Solution().numDecodings("06"))
    print(Solution().numDecodings("2101"))
    print(Solution().numDecodings("111111111111111111111111111111111111111111111"))
