# https://programmers.co.kr/learn/courses/30/lessons/42897
from collections import deque


def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):  # 마지막 집을 안 터는 경우
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):  # 첫 집을 안 터는 경우
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(max(dp1), max(dp2))  # 두 경우 중 최대


if __name__ == '__main__':
    print(solution([1, 2, 3, 1]), 4)
    print(solution([1, 1, 4, 1, 4]), 8)
    print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]), 3000)
    print(solution([1000, 1, 0, 1, 2, 1000, 0]), 2001)
    print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]), 2000)
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
    print(solution([11, 0, 2, 5, 100, 100, 85, 1]), 198)
    print(solution([1, 2, 3]), 3)
    print(solution([91, 90, 5, 7, 5, 7]), 104)
    print(solution([90, 0, 0, 95, 1, 1]), 185)

"""
dp[i] = max(dp[i-2] + money[i], dp[i-1])

"""
