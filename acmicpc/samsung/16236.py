# https://www.acmicpc.net/problem/16236

from collections import defaultdict


def min_dist(start, end, board):
    pass


def baby_shark(n, board):
    baby = [2, [0, 0]]  # size, (y, x)
    d = defaultdict(list)
    for y in range(n):
        for x in range(n):
            d[board[y][x]].append((y, x))
    baby[1] = list(d[9][0])

    # no smaller fish to eat
    if len(d[1]) == 0:
        return 0
    print(d, baby)
    print(board)


if __name__ == '__main__':
    n = int(input())
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    print(baby_shark(n, board))
