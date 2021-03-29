# https://www.acmicpc.net/problem/2206
# 2206. 벽 부수고 이동하기

class Solution:
    def shortest_path(self, n, m, board) -> int:
        visited = set()
        q = list()
        q.append((0, 0, 1, 1))  # y, x, drill, i
        visited.add((0, 0, 1))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        answer = -1
        while q:
            y, x, drill, i = q.pop(0)
            if y == n - 1 and x == m - 1:
                answer = i
                break
            for dir in directions:
                next_y, next_x = y + dir[0], x + dir[1]
                if -1 < next_x < m and -1 < next_y < n:
                    if board[next_y][next_x] == '0' and (next_y, next_x, drill) not in visited:
                        visited.add((next_y, next_x, drill))
                        q.append((next_y, next_x, drill, i + 1))
                    elif board[next_y][next_x] == '1' and drill == 1 and (next_y, next_x, drill) not in visited:
                        visited.add((next_y, next_x, drill))
                        q.append((next_y, next_x, 0, i + 1))
        return answer


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [input() for i in range(n)]
    print(Solution().shortest_path(n, m, board))
