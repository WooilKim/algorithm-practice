# https://py.checkio.org/en/mission/the-cheapest-flight/
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


if __name__ == '__main__':
    print("Example:")
    # print(cheapest_flight([['A', 'C', 100],
    #                        ['A', 'B', 20],
    #                        ['B', 'C', 50]],
    #                       'A',
    #                       'C'))
    print(cheapest_flight([['A', 'C', 40],
                           ['A', 'B', 20],
                           ['A', 'D', 20],
                           ['B', 'C', 50],
                           ['D', 'C', 70]],
                          'D',
                          'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'A',
                           'C') == 70
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'C',
                           'A') == 70
    assert cheapest_flight([['A', 'C', 40],
                            ['A', 'B', 20],
                            ['A', 'D', 20],
                            ['B', 'C', 50],
                            ['D', 'C', 70]],
                           'D',
                           'C') == 60
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['D', 'F', 900]],
                           'A',
                           'F') == 0
    assert cheapest_flight([['A', 'B', 10],
                            ['A', 'C', 15],
                            ['B', 'D', 15],
                            ['C', 'D', 10]],
                           'A',
                           'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
