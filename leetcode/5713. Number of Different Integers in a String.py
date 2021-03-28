# https://leetcode.com/contest/weekly-contest-234/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in range(len(word)):
            if ord('a') <= ord(word[i]) <= ord('z'):
                word = ' '.join((word[:i], word[i + 1:]))

        return len(set(map(int, word.split())))


if __name__ == '__main__':
    print(Solution().numDifferentIntegers(word="a123bc34d8ef34"))
    print(Solution().numDifferentIntegers(word="leet1234code234"))
    print(Solution().numDifferentIntegers(word="a1b01c001"))
