# https://leetcode.com/problems/triangle/

# memo = dict()

# Runtime: 72 ms, faster than 21.25% of Python3 online submissions for Triangle.
# Memory Usage: 17.3 MB, less than 7.42% of Python3 online submissions for Triangle.
class Solution:
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
print(memo)
print(Solution().minimumTotal(triangle=[[1], [2, 3]]))
print(memo)
