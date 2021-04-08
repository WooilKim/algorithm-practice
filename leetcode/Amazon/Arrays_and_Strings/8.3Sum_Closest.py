# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2967/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(s - target):
                    ans = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return ans


# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
if __name__ == '__main__':
    print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
    print(Solution().threeSumClosest(nums=[0, 1, 2], target=1))
