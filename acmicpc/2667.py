# https://www.acmicpc.net/problem/2667
# BOJ 2667 단지번호 붙이기 (1996 KOI 초등부)
from collections import deque


def solution(n, board):
    answer = list()
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    for j in range(n):
        for i in range(n):
            if board[j][i] > 0:
                queue = deque()
                queue.append((j, i))
                cnt = 0
                while queue:
                    y, x = queue.popleft()
                    if board[y][x] == 0:
                        continue
                    board[y][x] = 0
                    cnt += 1
                    for d in range(4):
                        next_y, next_x = y + dy[d], x + dx[d]
                        if 0 <= next_y < n and 0 <= next_x < n:
                            queue.append((next_y, next_x))
                answer.append(cnt)
    print(len(answer))
    answer.sort()
    print('\n'.join(map(str, answer)))
    # for a in answer:
    #     print(a)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    solution(n, board)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

5
11011
11011
00000
11011
11011

5리
11110
00000
11100
00000
11000

5
10101
01010
10101
10101
01010

5
11000
00000
00000
00000
00001
"""
