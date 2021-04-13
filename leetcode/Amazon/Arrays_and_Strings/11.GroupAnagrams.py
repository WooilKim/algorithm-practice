# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2970/

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
