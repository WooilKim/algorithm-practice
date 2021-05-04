# https://www.acmicpc.net/problem/16236


def baby_shark(n, board):
    baby = [0, 0, 0, 2]  # y,x, eaten, size
    smaller = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 9:
                baby[0], baby[1] = y, x
            if board[y][x] < 2:
                smaller += 1
    t = 0
    dirs = [[-1, 0],  # up
            [0, -1],  # left
            [0, 1],  # right
            [1, 0]]  # down
    while smaller > 0:
        mem = set()
        q = list()
        q.append((0, baby[0], baby[1]))  # d, y, x
        candidates = list()
        while q:
            dist, y, x = q.pop(0)
            if 9 > board[y][x] > baby[3] or (y, x) in mem:
                continue
            if 0 < board[y][x] < baby[3]:
                mem.add((y, x))
                candidates.append((dist, y, x))
            else:
                mem.add((y, x))
                for dir in dirs:
                    next_y, next_x = y + dir[0], x + dir[1]
                    if 0 <= next_y < n and 0 <= next_x < n:
                        q.append((dist + 1, next_y, next_x))
        if candidates:
            dist, y, x = sorted(candidates)[0]
            board[baby[0]][baby[1]] = 0
            board[y][x] = 9
            baby[0], baby[1] = y, x
            t += dist
            # eat fish
            baby[2] += 1
            smaller -= 1
            if baby[3] == baby[2]:
                baby[3] += 1
                baby[2] = 0
                smaller += len([0 for y in range(n) for x in range(n) if board[y][x] == baby[3] - 1])
        else:
            break
    return t


if __name__ == '__main__':
    n = int(input())
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    print(baby_shark(n, board))

# https://www.acmicpc.net/board/view/49232
"""
반례

10
2 0 2 0 1 1 1 0 1 0 
0 4 4 0 4 0 0 0 3 0 
4 3 5 0 1 0 2 6 0 0 
0 0 5 5 3 1 3 1 3 4 
6 0 5 1 4 2 4 0 5 0 
0 0 5 0 2 1 1 2 1 0 
2 0 5 2 4 0 9 1 6 2 
4 1 2 0 3 0 3 2 4 6 
3 0 1 0 4 0 0 5 0 1 
0 4 1 1 6 6 1 6 0 0 

answer : 87
Process finished with exit code 0

"""