# https://programmers.co.kr/learn/courses/30/lessons/72413
# title : 합승 택시 요금


import math
from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    graph = defaultdict(dict)

    for f in fares:
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]

    dist_table = [[math.inf] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        queue = list()
        heapq.heappush(queue, (0, i))
        dist_table[i][i] = 0
        visited = [False] * (n + 1)
        while queue:
            curr_dist, curr_target = heapq.heappop(queue)
            if not visited[curr_target]:
                if dist_table[i][curr_target] < curr_dist:
                    continue
                for new_target, new_dist in graph[curr_target].items():
                    dist = curr_dist + new_dist
                    if dist < dist_table[i][new_target]:
                        dist_table[i][new_target] = dist
                        heapq.heappush(queue, [dist, new_target])
    answer = math.inf
    for i in range(1, n + 1):
        answer = min(answer, dist_table[s][i] + dist_table[i][a] + dist_table[i][b])
    return answer


if __name__ == '__main__':
    print(solution(6, 4, 6, 2,
                   [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                    [1, 6, 25]]), 82)
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]), 14)
    print(solution(6, 4, 5, 6,
                   [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]), 18)
