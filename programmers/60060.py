# https://programmers.co.kr/learn/courses/30/lessons/60060
# 가사 검색
# 2020 KAKAO BLIND RECRUITMENT

from collections import defaultdict


class Node:
    def __init__(self, key):
        self.key = key
        self.len_dict = defaultdict(int)
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str):
        cur = self.root
        for i, w in enumerate(list(word)):
            if w not in cur.child:
                cur.child[w] = Node(w)
            cur.len_dict[len(word) - i] += 1
            cur = cur.child[w]
        cur.child['*'] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        if '*' in cur.child:
            return True

    # def search_wildcard(self, word: str) -> set[str]:
    #     res= list()
    #     cur = self.root
    #     for w in word:
    #         if w == '?':
    #     return {}

    def query(self, word: str) -> int:
        cur = self.root
        for w in word:
            if w == '?':
                return sum(cur.len_dict.values())
            if w not in cur.child:
                return 0
            cur = cur.child[w]
        return 0


def solution(words: list[int], queries: list[int]) -> list[int]:
    answer = []
    trie = Trie()
    for word in words:
        trie.insert(word)

    return answer


if __name__ == '__main__':
    words = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    print(solution(words, words))
