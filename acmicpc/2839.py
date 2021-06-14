# https://www.acmicpc.net/problem/2839
# 2839. 설탕 배달

def solution(n):
    dp = [-1, -1, -1, 1, -1, 1] + [0 for _ in range(6, n + 1)]
    for i in range(6, n + 1):
        if dp[i - 3] < 0 and dp[i - 5] < 0:
            dp[i] = -1
            continue
        if dp[i - 3] < 0:
            dp[i] = dp[i - 5] + 1
            continue
        if dp[i - 5] < 0:
            dp[i] = dp[i - 3] + 1
            continue
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    return dp[n]


if __name__ == '__main__':
    print(solution(int(input())))
