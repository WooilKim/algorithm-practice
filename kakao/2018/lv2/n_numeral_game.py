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


# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def solution(n: int, t: int, m: int, p: int):
    answer = list()
    x = 0
    base = 0
    order = 1
    while x < t:
        # print('x', x)
        total_turn = m * x + p - 1
        if total_turn == 0:
            answer.append('0')
            x += 1
            continue

        next = int(order * (n ** order - n ** (order - 1)))

        while total_turn >= base + next:
            base += next
            order += 1
            next = order * (n ** order - n ** (order - 1))
        current_turn = total_turn - base
        num = base + current_turn // order + 1
        print(next, total_turn, current_turn, base)
        # print(current_turn, total_turn, order)
        # d, r = divmod(current_turn, order)
        print('c', num, convert(num, n), 'base', base, current_turn // order, int(current_turn % order),
              convert(num, n)[int(current_turn % order) - 1])
        print(answer)
        answer.append(convert(num, n)[int(current_turn % order)])
        # print(answer)
        x += 1
    print(answer)
    return ''.join(answer)


def test():
    # ans1 = solution(2, 4, 2, 1)
    # ans1 = solution(2, 4, 2, 2)
    ans2 = solution(16, 16, 2, 1)
    ans3 = solution(16, 16, 2, 2)


if __name__ == '__main__':
    test()
    # n, t, m, p = input(), input(), input(), input()
    # print(n, t, m, p)
    pass

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.3MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.16ms, 10.3MB)
# 테스트 6 〉	실패 (0.15ms, 10.2MB)
# 테스트 7 〉	실패 (0.15ms, 10.3MB)
# 테스트 8 〉	통과 (0.10ms, 10.2MB)
# 테스트 9 〉	실패 (0.10ms, 10.3MB)
# 테스트 10 〉	실패 (0.10ms, 10.2MB)
# 테스트 11 〉	통과 (0.10ms, 10.2MB)
# 테스트 12 〉	실패 (0.09ms, 10.2MB)
# 테스트 13 〉	실패 (0.09ms, 10.2MB)
# 테스트 14 〉	통과 (3.08ms, 10.2MB)
# 테스트 15 〉	실패 (3.11ms, 10.2MB)
# 테스트 16 〉	실패 (3.71ms, 10.2MB)
# 테스트 17 〉	실패 (0.62ms, 10.2MB)
# 테스트 18 〉	실패 (0.76ms, 10.1MB)
# 테스트 19 〉	실패 (0.53ms, 10.2MB)
# 테스트 20 〉	실패 (0.24ms, 10.3MB)
# 테스트 21 〉	실패 (1.24ms, 10.1MB)
# 테스트 22 〉	실패 (2.14ms, 10.2MB)
# 테스트 23 〉	실패 (3.57ms, 10.2MB)
# 테스트 24 〉	실패 (3.95ms, 10.5MB)
# 테스트 25 〉	실패 (3.58ms, 10.2MB)
# 테스트 26 〉	실패 (1.68ms, 10.2MB)
