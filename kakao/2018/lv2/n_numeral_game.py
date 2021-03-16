# https://programmers.co.kr/learn/courses/30/lessons/17687

import math


def solution(n, t, m, p):
    # 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = list()
    x = 0
    while len(answer) < t:
        total_turn = m * x + p
        order = int(math.log(total_turn, n))
        this_turn = total_turn - (n ** order + 1)  # +1 to count 0
        num = total_turn - (n ** order + 1) / (order + 1)
        r = total_turn - (n ** order + 1)) % (order + 1)  # +1 to count 0, +1 for ceiling

        2 ** k
        x += 1
        pass
    return answer


if __name__ == '__main__':
    n, t, m, p = input(), input(), input(), input()
    print(n, t, m, p)
    pass
