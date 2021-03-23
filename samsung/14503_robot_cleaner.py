# https://www.acmicpc.net/problem/14503
import pprint

N, E, S, W = 0, 1, 2, 3


def solution(n, m, r, c, d, board):
    cleaned = 0
    # flag = False
    while True:
        flag = False
        if board[r][c] == 0:
            board[r][c] = -1
            cleaned += 1
        for i in range(4):
            next_r, next_c, next_d = turn_left(r, c, d)
            d = next_d
            if board[next_r][next_c] == 0:
                # if -1 < next_r < n and -1 < next_c < m and board[next_r][next_c] == 0:
                r, c = next_r, next_c
                flag = True
                break
        if flag:
            continue
        else:
            next_r, next_c, next_d = go_back(r, c, d)
            if board[next_r][next_c] != 1:
                r, c, d = next_r, next_c, next_d
            else:
                return cleaned


def turn_left(r, c, d):
    next_r, next_c, next_d = r, c, d
    if d == N:
        next_d = W
        next_c -= 1
    elif d == E:
        next_d = N
        next_r -= 1
    elif d == S:
        next_d = E
        next_c += 1
    elif d == W:
        next_d = S
        next_r += 1
    else:
        print('turn_left():direction error')
    return next_r, next_c, next_d


def go_back(r, c, d):
    next_r, next_c, next_d = r, c, d
    if d == N:
        next_r = r + 1
    elif d == E:
        next_c = c - 1
    elif d == S:
        next_r = r - 1
    elif d == W:
        next_c = c + 1
    else:
        print('go_back():direction error')
    return next_r, next_c, next_d


if __name__ == '__main__':
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    print(solution(n, m, r, c, d, board))
    # pprint.pprint(board)
    # print(r, c, d)
