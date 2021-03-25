# https://www.acmicpc.net/problem/14889
from itertools import combinations


class Solution:
    def min_diff(self, n, S: list[list[int]]) -> int:
        global m
        m = 9999
        # for i in range(n):
        #     for j in range(i, n):
        #         S[i][j], S[j][i] = S[i][j] + S[j][i], S[i][j] + S[j][i]
        # print(list(combinations(n,2)))
        scores = [S[a][b] + S[b][a] for a, b in combinations(range(n), 2)]
        cs = list(x for x in combinations(range(n), n // 2) if 0 in x)
        print(cs)

        # a 가 포함된것만 하면 반이됨
        size = len(scores)
        m = min([sum(c) for c in combinations(scores, size // 2)])
        print(m)
        print(scores)
        cs = combinations(range(n), n // 2)
        print(list(cs))
        for c in cs:
            pass


if __name__ == '__main__':
    n = int(input())
    S = [list(map(int, input().split())) for i in range(n)]
    # print(S)
    print(Solution().min_diff(n, S))
