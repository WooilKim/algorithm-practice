# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2967/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums)-2):

            continue
        pass


# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
if __name__ == '__main__':
    print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
