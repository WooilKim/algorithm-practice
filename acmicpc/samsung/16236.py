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
    """
    t = 0
    while smaller fish than baby shark exists:
        time = dist to nearest fish
        t += time
        move babyshark to nearest fish
        baby.left -= 1
        if baby.left == 0:
            baby.size+=1
            baby.left = baby.size
        
    
    """
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
