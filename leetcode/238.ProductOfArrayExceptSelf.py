# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# zero count
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount, prod = 0, 1
        for i in nums:
            if i == 0:
                zeroCount += 1
            else:
                prod *= i
        if zeroCount >= 2:
            return [0 for i in nums]
        elif zeroCount == 1:
            return [0 if i != 0 else prod for i in nums]
        else:
            return [prod//i for i in nums]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = list(1 for _ in nums)
        curr = 1
        for i, n in enumerate(nums[:-1]):
            curr *= n
            ans[i + 1] *= curr
        curr = 1
        for i in range(len(nums)-1):
            print(i)
            curr *= nums[len(nums) - i - 1]
            ans[len(nums) - i - 2] *= curr
        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
