class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i != j:
            if sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                return [index for index, x in enumerate(nums) if x == sorted_nums[i] or x == sorted_nums[j]]


if __name__ == '__main__':
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(nums=[3, 2, 4], target=6))
    print(Solution().twoSum(nums=[3, 3], target=6))
