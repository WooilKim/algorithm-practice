# https://www.acmicpc.net/problem/12100

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3


def solution(n, arr):
    print(arr)


def move(d):
    pass


if __name__ == '__main__':
    n = int(input())
    arr = list()
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(n, arr)
