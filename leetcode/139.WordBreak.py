# https://leetcode.com/problems/word-break/

from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False for _ in s]
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i - len(word) + 1:i + 1] and (dp[i - len(word)] or i - len(word) == -1):
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
