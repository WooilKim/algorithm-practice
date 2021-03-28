# https://www.acmicpc.net/problem/14500

import numpy as np
import pprint
from itertools import permutations

tetriminos = [
    [1, 1, 1, 1],
    [[1, 1],
     [1, 1]],
    [[1, 0],
     [1, 0],
     [1, 1]],
    [[1, 0],
     [1, 1],
     [0, 1]],
    [[1, 0],
     [1, 1],
     [1, 0]],
]


def solution(n, m, board):
    l = [1, 2, 3, 4, 5, 2]  # 1 right 2 down
    blocks = set(permutations(l, 3))
    print(len(blocks))
    board = np.squeeze(np.asarray(board))
    M = 0
    for block in blocks:
        cnt1 = len([i for i in block if i == 1])
        cnt2 = len([i for i in block if i == 2])
        blk = [[0 for _ in range(cnt1 + 1)] for _ in range(cnt2 + 1)]
        bi, bj = 0, 0
        blk[bj][bi] = 1
        for b in block:
            if b == 1:  # right
                bi += 1
                blk[bj][bi] = 1
            else:  # down
                bj += 1
                blk[bj][bi] = 1
        print(blk)
        for y in range(n - len(blk) + 1):
            for x in range(m - len(blk[0]) + 1):
                # print(y, y + len(blk), x, x + len(blk[0]))
                # print(board[y:y + len(blk), x:x + len(blk[0])])
                # print(blk.shape, board[y:y + len(blk), x:x + len(blk[0])].shape)
                # # print(blk.shape, )
                # print(np.dot(blk, board[y:y + len(blk), x:x + len(blk[0])]))
                # for j in range(len(blk)):
                #     for i in range(len(blk[0])):
                #         sum +=
                # s = np.dot(blk, board[y:y + len(blk)][x:x + len(blk[0])])
                print(y, x, y + len(blk), x + len(blk[0]), blk)
                print(board[y:y + len(blk), x:x + len(blk[0])])
                s = 0
                for j in range(len(blk)):
                    for i in range(len(blk[0])):
                        s += blk[j][i] * board[y:y + len(blk), x:x + len(blk[0])][j][i]
                print(s)
                # print([blk[i][j] for i in range(len(blk[0])) for j in range(len(blk))])
                # print([blk[j][i] * board[y:y + len(blk), x:x + len(blk[0])][j][i] for i in range(len(blk[0])) for j in
                #        range(len(blk))])
                # s = sum([blk[j][i] * board[y:y + len(blk), x:x + len(blk[0])][j][i] for i in range(len(blk[0])) for j in
                #          range(len(blk))])

                if s > M:
                    M = s

    print(M)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    solution(n, m, board)
