# https://www.acmicpc.net/problem/5430
# 분류 : 구현 자료구조 문자열 덱

import json


def solution(T):
    for t in T:
        is_error = False
        direction = 1
        for cmd in t[0]:
            if cmd == 'R':
                direction *= -1
                # t[1] = list(reversed(t[1]))
            else:
                if len(t[1]) == 0:
                    is_error = True
                    break
                if direction == 1:
                    t[1].pop(0)
                else:
                    del (t[1][-1])
        if is_error:
            print('error')
        else:
            if direction == 1:
                print(t[1])
            else:
                print(list(reversed(t[1])))


if __name__ == '__main__':
    t = int(input())  # T<=100
    T = list()
    for i in range(t):
        p = input()
        n = int(input())
        arr = json.loads(input())
        T.append([p, arr])

    solution(T)
