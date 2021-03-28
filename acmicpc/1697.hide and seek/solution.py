# https://www.acmicpc.net/problem/1697
# 1697. 숨바꼭질

# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def shortest_time(self, n: int, k: int) -> int:
        if n > k:
            return n - k
        global memo
        memo = dict()
        t = 0
        for i in range(n // 2, n):
            memo[i] = n - i
        # t += 1
        for i in range(n, k):
            if i % 2 == 0:
                memo[i] = min(memo[i - 1] + 1, memo[])
        print(min(self.move(n - 1, t + 1, k), self.move(n + 1, t + 1, k), self.move(2 * n, t + 1, k)))

    def distance(self, start, end):
        if start == end:
            return 0
        elif n < 0:
            return 99999999
        if n in memo:
            memo[n] = min(memo[n], t)
            return memo[n]
        else:
            memo[n] = t
            return min(self.distance(n - 1, end) + 1,
                       self.distance(start + 1, end) + 1,
                       self.distance(2 * start, end) + 1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(Solution().shortest_time(n, k))
