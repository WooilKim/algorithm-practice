# https://programmers.co.kr/learn/courses/30/lessons/43162
from functools import reduce


# TODO: error why??
def solution2(n, computers):
    for i in range(n):
        computers[i] = int(''.join(map(str, computers[i])), 2)

    networks = {computers[0]}
    for c_i, computer in enumerate(computers):
        checks = [network & computer for network in networks]
        if any(checks):
            networks = [networks[i] for i in range(len(networks)) if not checks[i]]
            networks.append(
                computer | reduce(lambda a, b: a | b, [networks[i] for i in range(len(networks)) if checks[i]], 0))
        else:
            networks.append(computer)
    return len(networks)


def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0] * n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1

        while bfs:
            node = bfs.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
    print(solution(5, [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]), 5)
