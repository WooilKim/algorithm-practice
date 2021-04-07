# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2966/
from typing import List


# Runtime: 848 ms, faster than 73.33% of Python3 online submissions for 3Sum.
# Memory Usage: 17.3 MB, less than 91.87% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans


# time limit exceed
# 0 <= nums.length <= 3000
# -10**5 <= nums[i] <= 10**5
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mem = set()
        mem2 = set()
        ans = set()
        for i, v1 in enumerate(nums):
            if v1 not in mem2:
                mem2.add(v1)
                for j, v2 in enumerate(nums[i + 1:]):
                    if (v1, v2) not in mem:
                        mem.add((v1, v2))
                        v3 = -v1 - v2
                        for k in range(i + j + 2, len(nums)):
                            if nums[k] == v3:
                                ans.add((v1, v2, v3))
                                break
                            if nums[k] > v3:
                                break
        return list(list(a) for a in ans)


if __name__ == '__main__':
    print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum(nums=[]))
    print(Solution().threeSum(nums=[0]))
    print(Solution().threeSum(nums=[0, 0, 0]))
