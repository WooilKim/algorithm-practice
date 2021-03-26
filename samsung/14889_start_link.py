# https://www.acmicpc.net/problem/14889
from itertools import combinations


class Solution:
    def min_diff(self, n, S: list[list[int]]) -> int:
        global m
        m = 9999
        cs = list(x for x in combinations(range(n), n // 2) if 0 in x)
        for c in cs:
            partsumA = 0
            partsumB = 0
            for a, b in combinations(c, 2):
                partsumA += S[a][b] + S[b][a]
            for a, b in combinations([x for x in range(n) if x not in c], 2):
                partsumB += S[a][b] + S[b][a]

            m = min(m, abs(partsumB - partsumA))

        return m


if __name__ == '__main__':
    n = int(input())
    S = [list(map(int, input().split())) for i in range(n)]
    print(Solution().min_diff(n, S))
