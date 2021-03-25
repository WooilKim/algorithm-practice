# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        return Solution().tsum(triangle, 0, 0)

    def tsum(self, triangle, h, i):
        if h == len(triangle) - 1:
            return triangle[h][i]
        # print(h, i, Solution().tsum(triangle, h + 1, i), Solution().tsum(triangle, h + 1, i + 1))
        return triangle[h][i] + min(Solution().tsum(triangle, h + 1, i), Solution().tsum(triangle, h + 1, i + 1))


print(Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
