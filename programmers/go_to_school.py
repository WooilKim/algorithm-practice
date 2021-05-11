# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    board = [[1] * m for _ in range(n)]
    for j, i in puddles:
        board[i - 1][j - 1] = 0
        if j == 1:
            for y in range(i, n):
                board[y][j - 1] = 0
        if i == 1:
            for x in range(j, m):
                board[i - 1][x] = 0
    for j in range(1, n):
        for i in range(1, m):
            if board[j][i] == 0:
                continue
            board[j][i] = board[j - 1][i] + board[j][i - 1]
    return board[n - 1][m - 1] % 1000000007


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))  # return 4
    print(solution(2, 2, []), 2)
    print(solution(3, 3, []), 6)
    print(solution(3, 3, [[2, 2]]), 2)
    print(solution(3, 3, [[2, 3]]), 3)
    print(solution(3, 3, [[1, 3]]), 5)
    print(solution(3, 3, [[1, 3], [3, 1]]), 4)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
    print(solution(4, 4, [[3, 2], [2, 4]]), 7)
    print(solution(100, 100, []), 690285631)
