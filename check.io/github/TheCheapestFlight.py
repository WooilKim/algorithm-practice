# https://py.checkio.org/en/mission/the-cheapest-flight/
# Github
# The Cheapest Flight

from typing import List
from collections import defaultdict


def cheapest_flight(costs: List, a: str, b: str) -> int:
    graph = defaultdict(dict)
    for start, target, price in costs:
        graph[start][target] = price
        graph[target][start] = price
    res = list()

    def dfs(path, p):
        if path[-1] == b:
            res.append(p)
        else:
            for key in graph[path[-1]].keys():
                if key not in path:
                    dfs(path + key, p + graph[path[-1]][key])

    dfs(a, 0)
    return min(res) if res else 0
