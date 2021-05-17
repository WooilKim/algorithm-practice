# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
from copy import deepcopy

# Runtime: 2012 ms, faster than 5.04% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.9 MB, less than 5.12% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mArr, MArr = deepcopy(prices), deepcopy(prices)
        for i in range(1, len(prices)):
            mArr[i] = min(mArr[i - 1], mArr[i])
        for i in range(0, len(prices) - 1)[::-1]:
            MArr[i] = max(MArr[i], MArr[i + 1])
        return max([MArr[i] - mArr[i] for i in range(len(prices))])


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
