# https://www.acmicpc.net/problem/14500

import numpy as np
import pprint
from itertools import permutations


def solution(n, m, board):
    l = [1, 1, 1, 2, 2, 2]  # 1 right 2 down
    blocks = set(permutations(l, 3))
    print(len(blocks))
    board = np.array(board)
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
                print(y, y + len(blk), x, x + len(blk[0]))
                print(board[0:2])
                print(board[y:y + len(blk)][x:x + len(blk[0])])
                # s = np.dot(blk, board[y:y + len(blk)][x:x + len(blk[0])])
                # s = sum([blk[j][i] * board[y + j][x + i] for j in range(len(blk[0])) for i in range(len(blk))])
                # if s > M:
                #     M = s

    print(M)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    solution(n, m, board)
