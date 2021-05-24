from collections import deque
from collections import defaultdict
import random


def solution(N, edges):
    G = defaultdict(dict)
    for edge in edges:
        G[edge[0]][edge[1]] = edge[2]
        G[edge[1]][edge[0]] = edge[2]
    print(G)
    queue = deque()
    visited = set()
    dist_table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for k, v in G[1].items():
        queue.append((1, k, v))
    print(queue)
    while queue:
        start, target, dist = queue.popleft()
        if (min(start, target), max(start, target)) in visited:
            continue
        # if dist_table[min(start, target)][max(start, target)] != 0:
        #     continue
        visited.add((min(start, target), max(start, target)))
        dist_table[min(start, target)][max(start, target)] = dist
        for next_node, next_dist in G[start].items():
            if next_node != target:
                queue.append((next_node, target, dist + next_dist))
                queue.append((next_node, start, next_dist))
        for next_node, next_dist in G[target].items():
            if next_node != start:
                queue.append((next_node, start, dist + next_dist))
                queue.append((next_node, target, next_dist))
    answer = 0
    for i in range(N + 1):
        answer += sum(dist_table[i])
    return answer


def printTreeEdges(prufer, m):
    vertices = m + 2

    # Initialize the array of vertices
    vertex_set = [0] * vertices

    # Number of occurrences of vertex in code
    for i in range(vertices - 2):
        vertex_set[prufer[i] - 1] += 1

    print("The edge set E(G) is :")

    # Find the smallest label not present in
    # prufer.
    edges = list()
    j = 0
    for i in range(vertices - 2):
        for j in range(vertices):

            # If j+1 is not present in prufer set
            if (vertex_set[j] == 0):
                # Remove from Prufer set and print
                # pair.
                vertex_set[j] = -1
                print("(", (j + 1), ", ", prufer[i], ") ", sep="", end="")
                edges.append([j + 1, prufer[i], 1])
                vertex_set[prufer[i] - 1] -= 1
                break

    j = 0
    edges.append([0, 0, 1])
    # For the last element
    for i in range(vertices):
        if (vertex_set[i] == 0 and j == 0):
            print("(", (i + 1), ", ", sep="", end="")
            edges[-1][0] = i + 1
            j += 1
        elif (vertex_set[i] == 0 and j == 1):
            print((i + 1), ")")
            edges[-1][1] = i + 1

    return edges


# Driver code

if __name__ == '__main__':
    prufer = list(range(1, 1000))
    random.shuffle(prufer)
    n = len(prufer)
    edges = printTreeEdges(prufer, n)
    print(edges)

    # N = int(input())
    # edges = [list(map(int, input().split())) for _ in range(N - 1)]
    # print(solution(N, edges))

    print(solution(n + 2, edges))
"""
3
3 2 100
2 1 100
"""
