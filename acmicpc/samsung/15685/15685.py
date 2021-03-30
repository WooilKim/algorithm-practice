# https://www.acmicpc.net/problem/15685
# 15685 드래곤 커브


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted([j for sub in matrix for j in sub])[k - 1]


if __name__ == '__main__':
    print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
