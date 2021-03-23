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
