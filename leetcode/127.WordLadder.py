# https://leetcode.com/problems/word-ladder/

from typing import List

from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        layer = dict()
        layer[beginWord] = 1
        while layer:
            newLayer = defaultdict(int)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordSet:
                            newLayer[new_word] = layer[
                                                      word] + 1  # add new word to all sequences and form new layer element
            wordSet -= set(newLayer.keys())
            layer = newLayer
        return 0


if __name__ == '__main__':
    print(Solution().ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
