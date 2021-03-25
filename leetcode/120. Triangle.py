# https://leetcode.com/problems/triangle/

# Runtime: 52 ms, faster than 95.68% of Python3 online submissions for Triangle.
# Memory Usage: 15 MB, less than 86.86% of Python3 online submissions for Triangle.
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        h = len(triangle)
        minlen = triangle[-1]
        for layer in range(h - 1)[::-1]:
            for i in range(layer + 1):
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]
        print(triangle)
        return minlen[0]


# Runtime: 72 ms, faster than 21.25% of Python3 online submissions for Triangle.
# Memory Usage: 17.3 MB, less than 7.42% of Python3 online submissions for Triangle.
class Solution2:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        global memo
        memo = dict()
        return Solution().tsum(triangle, 0, 0)

    def tsum(self, triangle, h, i):
        if h == len(triangle) - 1:
            return triangle[h][i]
        # print(h, i, Solution().tsum(triangle, h + 1, i), Solution().tsum(triangle, h + 1, i + 1))
        if (h + 1, i) not in memo:
            memo[(h + 1, i)] = Solution().tsum(triangle, h + 1, i)
        if (h + 1, i + 1) not in memo:
            memo[(h + 1, i + 1)] = Solution().tsum(triangle, h + 1, i + 1)

        return triangle[h][i] + min(memo[(h + 1, i)], memo[(h + 1, i + 1)])


print(Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minimumTotal(triangle=[[1], [2, 3]]))
