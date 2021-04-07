# https://www.acmicpc.net/problem/1012
# 1012. 유기농 배추


class Solution:
    def min_worm(self, m: int, n: int, k: int, cabs: list[(int, int)]) -> int:
        visited = set()
        for j in range(m):
            for i in range(n):
                if (j, i) in cabs:
                    if any(x for x in [(j - 1, i), (j + 1, i), (j, i + 1), (j, i - 1)] if
                           x in cabs and x not in visited):
                        visited.add((j, i))
                        k -= 1
                        print(visited)
        return k


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        m, n, k = map(int, input().split())
        cabs = [tuple(map(int, input().split())) for i in range(k)]
        print(Solution().min_worm(m, n, k, cabs))
