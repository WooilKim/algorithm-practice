# https://www.acmicpc.net/problem/12100

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

"""
solution(n,arr):
    tree
    breadth first
    
    if direction == 0
        start position  
    if direction == 1
    
    if direction == 2
    
    if direction == 3
"""


def solution(n, arr):
    print(arr)
    print(move(LEFT, arr))
    # print(arr)


def move(d, arr):
    arr_copy = [row[:] for row in arr]
    if d == LEFT:
        # sum and trim
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr_copy[i][j] == arr_copy[i][j + 1]:
                    arr_copy[i][j] *= 2
                    arr_copy[i][j + 1] = 0
                    for k in range(j + 1, len(arr) - 1):
                        arr_copy[i][k] = arr_copy[i][k + 1]
                    arr_copy[i][len(arr) - 1] = 0
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr_copy[i][j] == 0:
                    for k in range(j, len(arr) - 1):
                        arr_copy[i][k] = arr_copy[i][k + 1]
                    arr_copy[i][len(arr) - 1] = 0

    elif d == RIGHT:
        pass
    elif d == UP:
        pass
    elif d == DOWN:
        pass
    else:
        print('move()/direction error')
        return None
    return arr_copy


if __name__ == '__main__':
    n = int(input())
    arr = list()
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(n, arr)

"""
반례
4
2 2 2 2
0 0 4 4
0 0 8 16
2 0 0 2
"""