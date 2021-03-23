# https://www.acmicpc.net/problem/14503
N, E, S, W = 0, 1, 2, 3


def solution(r, c, d, board):
    pass


if __name__ == '__main__':
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = list()
    for i in range(n):
        board.append(list(map(int, input().split())))
    solution(r, c, d, board)
