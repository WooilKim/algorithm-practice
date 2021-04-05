# https://leetcode.com/problems/next-greater-element-ii/

# Runtime: 8068 ms, faster than 5.04% of Python3 online submissions for Next Greater Element II.
# Memory Usage: 15.7 MB, less than 83.91% of Python3 online submissions for Next Greater Element II.
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        ans = [-1 for _ in nums]
        for i in range(len(nums)):
            for j in range(len(nums)):
                jdx = (i + j + 1) % len(nums)
                if nums[jdx] > nums[i]:
                    ans[i] = nums[jdx]
                    break
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElements(nums=[1, 2, 1]))
    print(Solution().nextGreaterElements(nums=[1, 2, 3, 4, 3]))
    print(Solution().nextGreaterElements(nums=[1, 2, 3, 4, 5]))
    print(Solution().nextGreaterElements(nums=[5, 4, 3, 2, 1]))
