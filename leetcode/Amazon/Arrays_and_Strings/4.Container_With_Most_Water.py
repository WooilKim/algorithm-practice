# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2963/

# Your runtime beats 16.83 % of python3 submissions.
# Your memory usage beats 24.67 % of python3 submissions.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        M, i, j = 0, 0, len(height) - 1
        while i != j:
            M = max(M, abs(i - j) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return M


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([1, 1]))
    print(Solution().maxArea([4, 3, 2, 1, 4]))
    print(Solution().maxArea([1, 2, 1]))
