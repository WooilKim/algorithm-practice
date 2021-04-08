# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3692/

from typing import List
from collections import Counter

# Runtime: 48 ms, faster than 53.26% of Python3 online submissions for Largest Unique Number.
# Memory Usage: 14.4 MB, less than 63.39% of Python3 online submissions for Largest Unique Number.
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A.sort()
        i = len(A) - 1
        while i > -1:
            if i == 0 or A[i - 1] != A[i]:
                return A[i]
            while i > 0 and A[i - 1] == A[i]:
                i -= 1
            i -= 1
        return -1

# Runtime: 52 ms, faster than 10.96% of Python3 online submissions for Largest Unique Number.
# Memory Usage: 14.4 MB, less than 86.22% of Python3 online submissions for Largest Unique Number.
class Solution2:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = Counter(A).most_common()[::-1]
        ans = -1
        for k, v in c:
            if v > 1:
                break
            ans = max(ans, k)
        return ans


if __name__ == '__main__':
    print(Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
