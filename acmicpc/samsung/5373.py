# https://www.acmicpc.net/problem/5373
# 5373 큐빙


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted([j for sub in matrix for j in sub])[k - 1]


if __name__ == '__main__':
    n = int(input())
    for _ in n:
        k = int(input())


    print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
