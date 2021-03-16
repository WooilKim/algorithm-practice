# https://programmers.co.kr/learn/courses/30/lessons/17687

import math
from collections import deque


def convert(num, base):
    q = deque([])
    o = ''
    while num:
        num, m = divmod(num, base)
        o = (str(m) if m < 10 else 'ABCDEF'[m - 10]) + o
        q.appendleft(str(m) if m < 10 else 'ABCDEF'[m - 10])

    return ''.join(q)


def solution(n: int, t: int, m: int, p: int):
    # 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = list()
    x = 0
    base = 0
    order = 0
    while x < t:
        total_turn = m * x + p - 1
        if total_turn == 0:
            answer.append('0')
            x += 1
        next = order * (n ** order - n ** (order - 1))
        while total_turn >= base + next:
            base += next
            order += 1
            next = order * (n ** order - n ** (order - 1))
        current_turn = total_turn - base
        num = n ** (order - 1) + (current_turn) // order
        answer.append(convert(num + 1, n)[current_turn % order])
        x += 1
    return answer


def test():
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
    print(solution(16, 16, 2, 2))


if __name__ == '__main__':
    test()
    # n, t, m, p = input(), input(), input(), input()
    # print(n, t, m, p)
    pass
