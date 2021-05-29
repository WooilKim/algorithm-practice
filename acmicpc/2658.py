# https://www.acmicpc.net/problem/2658


def solution(board):
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    # print(board)
    points = list()
    for j in range(10):
        for i in range(10):
            if board[j][i] == 1:
                tmp = [board[j + dy[d]][i + dx[d]] for d in range(8) if 0 <= j + dy[d] < 10 and 0 <= i + dx[d] < 10]
                if 4 < tmp.count(0) < 7:
                    points.append((j, i))
    # print(points)
    if len(points) != 3:
        print(0)
        return
    a = (points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2
    b = (points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2
    c = (points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2
    if (a == b and c == a + b) or (b == c and a == b + c) or (a == c and b == a + c):
        for j, i in sorted(points):
            print(j + 1, i + 1)
        return
    print(0)


if __name__ == '__main__':
    board = [list(map(int, list(input()))) for _ in range(10)]
    solution(board)
