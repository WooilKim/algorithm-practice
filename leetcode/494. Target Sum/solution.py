# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# 378. Kth Smallest Element in a Sorted Matrix


from itertools import combinations
PLUS, MINUS = 1, -1



class Solution:
    def findTargetSumWays(self, nums: list[int], S: int) -> int:
        # global memo
        # memo = dict()
        comb = combinations([PLUS for _ in nums]+[MINUS for _ in nums], len(nums))
        print(set(comb))
        answer = self.dfs(nums, 0, 0, PLUS, S) + self.dfs(nums, 0, 0, MINUS, S)
        return answer

    def dfs(self, nums, a, i, opt, S):
        if i <= len(nums) - 1:
            s = a + opt * nums[i]
            # if (i+1,s)
            if i == len(nums) - 1:
                if s == S:
                    return 1
                return 0
            return self.dfs(nums, s, i + 1, PLUS, S) + self.dfs(nums, s, i + 1, MINUS, S)
        else:
            return 0


if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))
    # print(Solution().findTargetSumWays(nums=[8, 48, 11, 47, 26, 12, 16, 39, 38, 50, 21, 12, 34, 1, 28, 1, 3, 9, 17, 50],
    #                                    S=3))
