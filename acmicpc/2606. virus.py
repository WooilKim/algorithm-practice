# https://www.acmicpc.net/problem/2606
# 2060.바이러스


class Solution:
    def get_infected(self, n: int, m: int, graph: list[list[int]]) -> int:
        infected = {1}
        flag = True
        while flag:
            flag = False
            for node in graph:
                if node[0] in infected and node[1] not in infected:
                    infected.add(node[1])
                    flag = True
                elif node[0] not in infected and node[1] in infected:
                    infected.add(node[0])
                    flag = True
        return len(infected) - 1


if __name__ == '__main__':
    n, m = int(input()), int(input())
    graph = [list(map(int, input().split())) for _ in range(m)]
    print(Solution().get_infected(n, m, graph))
