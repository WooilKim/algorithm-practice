# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, cnt in Counter(nums).most_common()[:k]]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
