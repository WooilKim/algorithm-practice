# https://www.acmicpc.net/problem/2669
# BOJ 2669 직사각형 네개의 합집합의 면적 구하기 (1996 KOI 초등부)

def solution(rects):
    board = [[0 for _ in range(100)] for _ in range(100)]
    for rect in rects:
        for y in range(rect[1], rect[3]):
            for x in range(rect[0], rect[2]):
                board[y][x] = 1

    return sum([sum(board[y]) for y in range(100)])


if __name__ == '__main__':
    rects = [list(map(int, input().split())) for _ in range(4)]
    print(solution(rects))

"""
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
"""
