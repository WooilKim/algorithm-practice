# https://leetcode.com/problems/missing-number/

from typing import List


class Solution2:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


if __name__ == '__main__':
    nums = [3, 0, 1]
