# https://www.acmicpc.net/problem/14502
#
from itertools import combinations

WALL, VIRUS = 1, 2


def solution(n, m, board):
    M = 0
    ws = list()
    vs = list()
    rs = list()
    for j in range(n):
        for i in range(m):
            if board[j][i] == WALL:
                ws.append((j, i))
            elif board[j][i] == VIRUS:
                vs.append((j, i))
            else:
                rs.append((j, i))
    cs = list(combinations(rs, 3))

    for c in cs:
        tmp = [[board[j][i] for i in range(m)] for j in range(n)]
        for x in c:
            tmp[x[0]][x[1]] = 1
        is_changed = True
        is_higher = True
        while is_changed and is_higher:
            is_changed = False
            for j in range(n):
                for i in range(m):
                    if tmp[j][i] == VIRUS:
                        nbs = neighbors(n, m, j, i)
                        for nb in nbs:
                            if tmp[nb[0]][nb[1]] == 0:
                                tmp[nb[0]][nb[1]] = 2
                                is_changed = True
            if M > len([1 for j in range(n) for i in range(m) if tmp[j][i] == 0]):
                is_higher = False
        M = max(M, len([1 for j in range(n) for i in range(m) if tmp[j][i] == 0]))

    print(M)


def neighbors(n, m, y, x):
    res = list()
    if -1 < y - 1 < n:
        res.append((y - 1, x))
    if -1 < y + 1 < n:
        res.append((y + 1, x))
    if -1 < x - 1 < m:
        res.append((y, x - 1))
    if -1 < x + 1 < m:
        res.append((y, x + 1))
    return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    solution(n, m, board)


# import copy
# from collections import deque
#
# n,m = map(int, input().split())
# dir_list = [[1, 0], [-1, 0],[0, 1],[0, -1]]
# graph = []
# max_zero_cnt = 0
# for _ in range(n):
#     graph.append(list(map(int, input().strip().split())))
#
# def check_zero_cnt(graph):
#     global n, m
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 cnt += 1
#     return cnt
#
# def make_virus_fill(graph):
#     global n, m
#     dq = deque()
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 2:
#                 dq.append((j, i)) # x, y
#
#     while dq:
#         x, y = dq.popleft()
#         for dir in dir_list:
#             dx = dir[0]
#             dy = dir[1]
#             next_x = x+dx
#             next_y = y+dy
#             if 0 <= next_x < m and 0 <= next_y < n and graph[next_y][next_x] == 0:
#                 graph[next_y][next_x] = 2
#                 dq.append((next_x, next_y))
#     return check_zero_cnt(graph)
#
# def make_map_dfs(graph, cnt):
#     global n, m, max_zero_cnt
#     if cnt == 3:
#         max_zero_cnt = max(max_zero_cnt, make_virus_fill(graph))
#     elif cnt < 3:
#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] == 0:
#                     tmp_graph = copy.deepcopy(graph)
#                     tmp_graph[i][j] = 1
#                     make_map_dfs(tmp_graph, cnt+1)
#
# make_map_dfs(graph, 0)
# print(max_zero_cnt)