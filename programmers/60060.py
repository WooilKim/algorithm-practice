# https://programmers.co.kr/learn/courses/30/lessons/60060
# 가사 검색
# 2020 KAKAO BLIND RECRUITMENT

class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node(w)
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

    def search_wildcard(self, prefix: str) -> bool:
        l = len(prefix)
        cnt = prefix.count('?')
        cur = self.root
        for w in prefix:
            if w not in cur.child:
                return False
            cur = cur.child[w]

        return True


def solution(words: list[int], queries: list[int]) -> list[int]:
    answer = []
    return answer
