# https://www.acmicpc.net/problem/1697
# 1697. 숨바꼭질

import heapq


class Solution:
    def shortest_time(self, n: int, k: int) -> int:
        if n > k:
            return n - k
        memo = dict()
        memo[n] = 0
        t = 1
        q = list()
        heapq.heappush(q, n)
        while q:
            key = heapq.heappop(q)
            if k in memo:
                break
            if key - 1 not in memo and key > 0:
                memo[key - 1] = memo[key] + 1
                heapq.heappush(q, key - 1)
            if key + 1 not in memo and key > k:
                memo[key + 1] = memo[key] + 1
                heapq.heappush(q, key + 1)
            if 2 * key not in memo and 2 * key < 3 * k / 2:
                memo[2 * key] = memo[key] + 1
                heapq.heappush(q, 2 * key)
        return memo[k]


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(Solution().shortest_time(n, k))
