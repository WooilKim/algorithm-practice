import numpy as np
import pprint


def solution():
    pass


tetriminos = [
    [[1, 1],
     [1, 1]],
    [[1, 1, 1, 1]],
    [[1, 0],
     [1, 1],
     [0, 1]],
    [[1, 0],
     [1, 0],
     [1, 1]],
    [[1, 0],
     [1, 1],
     [1, 0]],
]


def test():
    tetriminos.append(list(reversed(list(zip(*tetriminos[1])))))
    tetriminos.append(list(reversed(list(zip(*tetriminos[2])))))
    tetriminos.append(list(reversed(list(zip(*tetriminos[3])))))
    tetriminos.append(list(reversed(list(zip(*tetriminos[4])))))
    tmp1 = list(reversed(list(zip(*tetriminos[3]))))
    tmp2 = list(reversed(list(zip(*tetriminos[4]))))
    tetriminos.append(tmp1)
    tetriminos.append(tmp2)
    tmp1 = list(reversed(list(zip(*tmp1))))
    tmp2 = list(reversed(list(zip(*tmp2))))
    tetriminos.append(tmp1)
    tetriminos.append(tmp2)
    pprint.pprint(tetriminos)


if __name__ == '__main__':
    test()
    # n, m = list(map(int, input().split()))
    # board = list()
    # for i in range(n):
    #     board.append(list(map(int, input().split())))
