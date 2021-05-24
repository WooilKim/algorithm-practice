# https://leetcode.com/problems/word-break/

from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort()
        queue = deque([s])
        while queue:
            curr = queue.popleft()
            for w in wordDict:
                if curr == w:
                    return True
                if len(curr) > len(w):
                    if curr[:len(w)] == w:
                        queue.append(curr[len(w):])
        return False


if __name__ == '__main__':
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
