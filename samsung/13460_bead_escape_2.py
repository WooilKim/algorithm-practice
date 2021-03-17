# https://www.acmicpc.net/problem/13460

import numpy as np


def solution(n, m, board):
    pass


def move_left(board):
    pass


def move_right(board):
    pass


def move_up(board):
    pass


def move_right(board):
    pass


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    board = list()
    for row in range(int(n)):
        board.append(list(input()))
    print(n, m, board)
    board = [[board[i][j] for j in range(1, m - 1)] for i in range(1, n - 1)]
    solution(n - 2, m - 2, board)
    print(board)

    # board = list(np.array(board)[(1, 2, 3), ...][..., (1, 2, 3)])
