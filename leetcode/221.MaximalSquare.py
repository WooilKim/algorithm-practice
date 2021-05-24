# https://leetcode.com/problems/maximal-square/

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        visited = dict()
        res = 0

        def is_square(y, x, size):
            if (y, x, size) in visited:
                return visited[(y, x, size)]
            if y > len(matrix) - size - 1 or x > len(matrix[0]) - size - 1:
                return False
            dy, dx = [0, 1, 0, 1], [0, 0, 1, 1]
            nexts = [[y + dy[i], x + dx[i]] for i in range(4)]

            if size == 1:
                if all([matrix[j][i] for j, i in nexts]):
                    visited[(y, x, size)] = True
                    return True
                else:
                    visited[(y, x, size)] = False
                    return False
            else:
                visited[(y, x, size)] = all([is_square(y + j, x + i, size - 1) for j, i in nexts])
                return visited[(y, x, size)]

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return int(matrix[0][0])
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                s = 1
                while True:
                    if is_square(y, x, s):
                        s += 1
                    else:
                        break
                res = max(res, s - 1)
        return res ** 2


if __name__ == '__main__':
    print(Solution().maximalSquare(
        matrix=[["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]))
    print(Solution().maximalSquare(
        matrix=[["0", "1"], ["1", "0"]]))

    print(Solution().maximalSquare(
        matrix=["0"]))
    print(Solution().maximalSquare(
        matrix=[["1"]]))
