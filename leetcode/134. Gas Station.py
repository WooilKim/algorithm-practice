# https://leetcode.com/problems/gas-station/

from typing import List


# Runtime: 52 ms, faster than 74.04% of Python3 online submissions for Gas Station.
# Memory Usage: 15.4 MB, less than 21.32% of Python3 online submissions for Gas Station.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(rest) < 0:
            return -1

        s, i, j = 0, 0, len(gas) - 1
        while gas[i] - cost[i] < 0:
            i += 1
        j = (i + 1) % len(gas)
        s = gas[i] + gas[j] - cost[i] - cost[j]
        i += len(gas)
        while i % len(gas) != j % len(gas):
            if s < 0:
                i -= 1
                s += gas[i % len(gas)] - cost[i % len(gas)]
            else:
                j += 1
                s += gas[j % len(gas)] - cost[j % len(gas)]
        if s >= 0:
            return j % len(gas)
        else:
            return -1


if __name__ == '__main__':
    print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    print(Solution().canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
    print(Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]))
