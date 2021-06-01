# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray
from typing import List

# Runtime: 68 ms, faster than 45.11% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 15.2 MB, less than 11.25% of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        M = dp[0] = nums[0]
        for i, n in enumerate(nums):
            if i > 0:
                dp[i] = n + max(dp[i - 1], 0)
                M = max(M, dp[i])
        return M


if __name__ == '__main__':
    print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray(nums=[1]))
    print(Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))
