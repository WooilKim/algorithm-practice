# https://leetcode.com/problems/trapping-rain-water/


from typing import List

# Runtime: 48 ms, faster than 90.88% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 14.7 MB, less than 96.95% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        w, h = 0, 1
        i, j = 0, len(height) - 1
        while i < j:
            while height[i] < h and i < j:
                w += h - height[i] - 1
                i += 1
            while height[j] < h and i < j:
                w += h - height[j] - 1
                j -= 1
            h += 1
        return w


if __name__ == '__main__':
    print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap(height=[4, 2, 0, 3, 2, 5]))
