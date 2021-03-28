# https://www.acmicpc.net/problem/13458
import math


def solution(applicants, b, c):
    answer = 0
    for a in applicants:
        if a - b > 0:
            n = 1 + math.ceil((a - b) / c)
            answer += n
        else:
            answer += 1
    return answer


if __name__ == '__main__':
    n = int(input())
    aplicants = list(map(int, input().split()))
    b, c = list(map(int, input().split()))
    print(solution(aplicants, b, c))
