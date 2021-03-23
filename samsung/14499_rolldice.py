# https://www.acmicpc.net/problem/14499

E, W, N, S, B = 1, 2, 3, 4, 5
dice = list()


def solution(x, y, board, cmds):
    key = 1
    dice = dict()
    for i in range(6):
        dice[i + 1] = 0
    for cmd in cmds:
        x_next, y_next, key = move(x, y, key, cmd)
        if -1 < x_next < len(board[0]) and -1 < y_next < len(board):
            if board[y_next][x_next] != 0:
                dice[roll_dice(key, B)] = board[y_next][x_next]
                board[y_next][x_next] = 0
            else:
                board[y_next][x_next] = dice[roll_dice(key, B)]
            print(dice[key])
            x, y = x_next, y_next


def move(x, y, key, cmd):
    x_next = x
    y_next = y

    if cmd == E:
        x_next += 1
        key = roll_dice(key, W)
    elif cmd == W:
        x_next -= 1
        key = roll_dice(key, E)
    elif cmd == N:
        y_next -= 1
        key = roll_dice(key, S)
    elif cmd == S:
        y_next += 1
        key = roll_dice(key, N)
    else:
        print('move()/print cmd error')
    return x_next, y_next, key


def update_dice(dice, key, value):
    dice[key] = value


def roll_dice(key, d):
    if key == 1:
        if d == E:
            return 3
        elif d == S:
            return 5
        elif d == W:
            return 4
        elif d == N:
            return 2
        else:
            return 6
    elif key == 2:
        if d == E:
            return 3
        elif d == S:
            return 1
        elif d == W:
            return 4
        elif d == N:
            return 6
        else:
            return 5
    elif key == 3:
        if d == E:
            return 6
        elif d == S:
            return 5
        elif d == W:
            return 1
        elif d == N:
            return 2
        else:
            return 4
    elif key == 4:
        if d == E:
            return 1
        elif d == S:
            return 5
        elif d == W:
            return 6
        elif d == N:
            return 2
        else:
            return 3
    elif key == 5:
        if d == E:
            return 3
        elif d == S:
            return 6
        elif d == W:
            return 4
        elif d == N:
            return 1
        else:
            return 2
    elif key == 6:
        if d == E:
            return 3
        elif d == S:
            return 2
        elif d == W:
            return 4
        elif d == N:
            return 5
        else:
            return 1


if __name__ == '__main__':
    n, m, y, x, k = list(map(int, input().split()))
    board = list()
    cmds = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    cmds = list(map(int, input().split()))
    solution(x, y, board, cmds)
    pass
