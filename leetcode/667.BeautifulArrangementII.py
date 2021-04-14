# https://leetcode.com/problems/beautiful-arrangement-ii/
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n + 1))
        i = 0
        k -= 1
        while k >= 2:
            ans = ans[:2 * i + 1] + [ans[-1]] + ans[2 * i + 1:-1]
            k -= 2
            i += 1
        if k == 1:
            ans[-2], ans[-1] = ans[-1], ans[-2]
        return ans


if __name__ == '__main__':
    print(Solution().constructArray(n=3, k=2))
    print(Solution().constructArray(n=5, k=4))
    print(Solution().constructArray(n=3, k=1))

# 1 2 3 4 5  1
# 1 2 3 5 4  2
#
# 1 5 2 3 4  3
# 1 2 5 3 4  1,2,3
