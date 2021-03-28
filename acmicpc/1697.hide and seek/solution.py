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
        # t = 0
        memo[n] = 0
        # t += 1
        while k not in memo:
            for t in list(memo.keys()):
                if t > 0:
                    if t - 1 in memo:
                        memo[t - 1] = min(memo[t - 1], memo[t] + 1)
                    else:
                        memo[t - 1] = memo[t] + 1
                if t + 1 in memo:
                    memo[t + 1] = min(memo[t + 1], memo[t] + 1)
                else:
                    memo[t + 1] = memo[t] + 1
                if 2 * t in memo:
                    memo[2 * t] = min(memo[2 * t], memo[t] + 1)
                else:
                    memo[2 * t] = memo[t] + 1
        return memo[k]
    #     for i in range(n, k):
    #         if i % 2 == 0:
    #             memo[i] = min(memo[i - 1] + 1, memo[])
    #     print(min(self.move(n - 1, t + 1, k), self.move(n + 1, t + 1, k), self.move(2 * n, t + 1, k)))
    #
    #     print(self.distance(k))
    #
    # def distance(self, destination):
    #     if destination in memo:
    #         return memo[destination]
    #
    #     if destination > 0:
    #         if destination % 2 == 0:
    #             return min(self.distance(destination - 1) + 1,
    #                        self.distance(destination + 1) + 1,
    #                        self.distance(destination // 2) + 1)
    #         else:
    #             return min(self.distance(destination - 1) + 1,
    #                        self.distance(destination + 1) + 1)
    #     else:
    #         if destination % 2 == 0:
    #             return min(self.distance(destination + 1) + 1,
    #                        self.distance(destination // 2) + 1)
    #         else:
    #             return self.distance(destination + 1) + 1


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(Solution().shortest_time(n, k))
