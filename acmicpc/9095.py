# https://www.acmicpc.net/problem/9095
# 9095. 1, 2, 3 더하기

if __name__ == '__main__':
    dp = [0, 1, 2, 4] + [0 for _ in range(4, 12)]
    for i in range(4, 12):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    t = int(input())
    for _ in range(t):
        print(dp[int(input())])