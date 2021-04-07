# https://www.acmicpc.net/problem/15686
# 15686 치킨배달

from itertools import combinations


class Solution:
    def min_chicken_distance(self, n, m, city) -> int:
        chickens = [(j, i) for j in range(n) for i in range(n) if city[j][i] == 2]
        homes = [(j, i) for j in range(n) for i in range(n) if city[j][i] == 1]
        min_sum_distance = 99999
        for case in combinations(chickens, m):
            sum_distance = 0
            for home in homes:
                m = 99999
                for chicken in case:
                    m = min(m, abs(chicken[0] - home[0]) + abs(chicken[1] - home[1]))
                sum_distance += m
            min_sum_distance = min(min_sum_distance, sum_distance)
        return min_sum_distance


if __name__ == '__main__':
    n, m = map(int, (input().split()))
    city = [list(map(int, input().split())) for i in range(n)]
    print(Solution().min_chicken_distance(n, m, city))
