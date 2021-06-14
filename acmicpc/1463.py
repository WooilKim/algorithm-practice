# https://www.acmicpc.net/problem/1463
# 1로 만들기

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
def solution(n):
    dp = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        cand = list([dp[i - 1]])
        if i % 3 == 0:
            cand.append(dp[i // 3])
        if i % 2 == 0:
            cand.append(dp[i // 2])
        dp[i] = min(cand) + 1
    return dp[n]


if __name__ == '__main__':
    print(solution(int(input())))
