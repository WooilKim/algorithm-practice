# https://www.acmicpc.net/problem/13460

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3


def solution(n, m, board):
    r, b, o = 0, 0, 0
    walls = list()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                r = (i, j)
            elif board[i][j] == 'B':
                b = (i, j)
            elif board[i][j] == 'O':
                o = (i, j)
            elif board[i][j] == '#':
                walls.append((i, j))

    tree = list()
    tree.append([[r, b]])
    for h in range(10):
        for node in tree[h]:
            for d in range(4):
                flag, r_next, b_next = move(node[0], node[1], o, walls, d)
                if flag == 1:
                    return h + 1
                elif flag == 0:
                    if [r_next, b_next] in tree[h]:
                        continue
                    if h >= len(tree) - 1:
                        tree.append(list())
                    tree[h + 1].append([r_next, b_next])
        if h >= len(tree) - 1:
            break
    return -1


# d: direction
def move(r, b, o, walls, d):
    is_moved = True
    flag = 0
    while is_moved:
        is_moved = False
        if d == LEFT:
            r_next = (r[0], r[1] - 1)
            b_next = (b[0], b[1] - 1)
        elif d == RIGHT:
            r_next = (r[0], r[1] + 1)
            b_next = (b[0], b[1] + 1)
        elif d == UP:
            r_next = (r[0] - 1, r[1])
            b_next = (b[0] - 1, b[1])
        elif d == DOWN:
            r_next = (r[0] + 1, r[1])
            b_next = (b[0] + 1, b[1])
        else:
            return

        if flag == 0:
            if r_next == o:
                flag = 1
                r = (-1, -1)  # is out
                is_moved = True
            elif r_next != b and r_next not in walls:
                r = r_next
                is_moved = True
        if b_next == o:
            flag = -1
            break
        elif b_next != r and b_next not in walls:
            b = b_next
            is_moved = True
    return flag, r, b


#
# 반례
# 6 5
#####
###R#
##..#
# OB.#
# .#.#
#####

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    board = list()
    for row in range(int(n)):
        board.append(list(input()))
    print(solution(n, m, board))
