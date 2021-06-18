# https://leetcode.com/problems/coin-change/
# 322. Coin Change

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1 for _ in range(amount + 1)]
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            cand = []
            if i in coins:
                continue
            for c in coins:
                if i - c > 0 and dp[i - c] > 0:
                    cand.append(dp[i - c])
            if cand:
                dp[i] = min(cand) + 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().coinChange(coins=[1, 2, 5], amount=11))
    print(Solution().coinChange(coins=[2], amount=3))
