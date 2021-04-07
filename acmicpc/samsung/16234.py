# https://www.acmicpc.net/problem/16234
# 16234 인구이동

import copy


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def count_migration(self, n, l, r, population) -> int:
        # print(n, l, r, population)

        global memo, groups
        groups = list(set())
        memo = [i for i in range(n * n)]
        flag = True
        cnt = 0
        while flag:
            flag = False
            for j in range(n):
                for i in range(n):
                    if i < n - 1 and l <= abs(population[j][i] - population[j][i + 1]) <= r \
                            and memo[j * n + i + 1] != memo[j * n + i]:
                        memo[j * n + i + 1] = memo[j * n + i]
                        flag = True
                    if j < n - 1 and l <= abs(population[j][i] - population[j + 1][i]) <= r \
                            and memo[(j + 1) * n + i] != memo[j * n + i]:
                        memo[(j + 1) * n + i] = memo[j * n + i]
                        flag = True
            cp = copy.deepcopy(population)
            if not flag:
                for v in set(memo):
                    coords = [c for c in range(len(memo)) if memo[c] == v]
                    s = sum([population[c // n][c % n] for c in coords])
                    for c in coords:
                        cp[c // n][c % n] = s // len(coords)
                if cp == population:
                    break
                else:
                    population = cp
                    cnt += 1

        return cnt
        # return sorted([j for sub in matrix for j in sub])[k - 1]


if __name__ == '__main__':
    n, l, r = map(int, input().split())
    population = [list(map(int, input().split())) for _ in range(n)]
    print(Solution().count_migration(n, l, r, population))
