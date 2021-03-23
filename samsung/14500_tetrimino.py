import numpy as np


def solution():
    pass


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


def test():
    for t in tetriminos[1:]:
        # t = np.array(t)
        print(t)
        rotated = list(reversed(list(zip(*t))))
        print(rotated)


if __name__ == '__main__':
    test()
    # n, m = list(map(int, input().split()))
    # board = list()
    # for i in range(n):
    #     board.append(list(map(int, input().split())))
