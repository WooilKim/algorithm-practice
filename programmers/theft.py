# https://programmers.co.kr/learn/courses/30/lessons/42897
from collections import deque


def solution(money):
    # if len(money) % 2 == 1:
    #     return max(sum([money[i] for i in range(len(money) - 1) if i % 2 == 0]),
    #                sum([money[i] for i in range(1, len(money)) if i % 2 == 0]),
    #                sum([money[i] for i in range(len(money)) if i % 2 == 1]))
    # else:
    #     return max(sum([money[i] for i in range(len(money)) if i % 2 == 0]),
    #                sum([money[i] for i in range(len(money)) if i % 2 == 1]))
    # visited = set()
    queue = deque()
    queue.append((1, len(money) - 2, 0))
    queue.append((2, len(money) - 2, money[1]))
    queue.append((1, len(money) - 3, money[-1]))
    answer = 0
    while queue:
        i, j, m = queue.popleft()
        answer = max(answer, m)
        if i < j:
            queue.append((i + 1, j - 1, m))
            queue.append((i + 2, j - 1, m + money[i]))
            queue.append((i + 1, j - 2, m + money[j]))
        if i + 1 < j:
            queue.append((i + 2, j - 2, m + money[i] + money[j]))
    return answer


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
