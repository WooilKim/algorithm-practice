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
        i = 0
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node(w)
            cur.len_dict[len(word) - i] += 1
            cur = cur.child[w]
            i += 1

    def query(self, word: str) -> int:
        cur = self.root
        i = 0
        for w in word:
            if w == '?':
                return cur.len_dict.get(len(word) - i, 0)
            if w not in cur.child:
                return 0
            cur = cur.child[w]
            i += 1
        return 0


def solution(words, queries):
    answer = []
    trie_left, trie_right = Trie(), Trie()
    for word in words:
        trie_left.insert(word)
        trie_right.insert(word[::-1])

    for query in queries:
        if query[0] == '?':
            answer.append(trie_right.query(query[::-1]))
        else:
            answer.append(trie_left.query(query))
    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["?????"]
    print(solution(words, queries))
