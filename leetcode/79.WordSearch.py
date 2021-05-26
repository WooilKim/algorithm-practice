# https://leetcode.com/problems/word-search/
from typing import List

# Runtime: 7972 ms, faster than 5.01% of Python3 online submissions for Word Search.
# Memory Usage: 14.4 MB, less than 12.73% of Python3 online submissions for Word Search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        arr = [(y, x) for y in range(len(board)) for x in range(len(board[0])) if board[y][x] == word[0]]

        def dfs(path):
            if len(path) == len(word):
                return True
            py, px = path[-1]
            tmp = list()
            for i in range(4):
                ny, nx = py + dy[i], px + dx[i]
                if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                    if (ny, nx) in path:
                        continue
                    if board[ny][nx] == word[len(path)]:
                        tmp.append((ny, nx))
            return any([dfs(path + [(y, x)]) for (y, x) in tmp])

        return any([dfs([(y, x)]) for (y, x) in arr])


if __name__ == '__main__':
    print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
    print(Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
