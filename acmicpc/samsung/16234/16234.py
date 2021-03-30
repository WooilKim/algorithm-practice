# https://www.acmicpc.net/problem/16234
# 16234 인구이동


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def count_migration(self, n, l, r, population) -> int:
        # print(n, l, r, population)
        erased = list()
        for j in range(n):
            for i in range(n):
                if i < n - 1 and l <= abs(population[j][i] - population[j][i + 1]) <= r:
                    erased.append((j, i, j, i + 1))
                if j < n - 1 and l <= abs(population[j][i] - population[j + 1][i]) <= r:
                    erased.append((j, i, j + 1, i))

        return erased
        # return sorted([j for sub in matrix for j in sub])[k - 1]


if __name__ == '__main__':
    n, l, r = map(int, input().split())
    population = [list(map(int, input().split())) for _ in range(n)]
    print(Solution().count_migration(n, l, r, population))
