# https://www.acmicpc.net/problem/11054
# 11054. 가장 긴 바이토닉 부분 수열

def solution(N):
    dp_increasing = [0 for _ in range(len(N) + 1)]
    dp_decreasing = [0 for _ in range(len(N) + 1)]
    dp_increasing[0] = 1
    dp_decreasing[-1] = 1

    


if __name__ == '__main__':
    input()
    print(solution(list(map(int, input().split()))))
