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
