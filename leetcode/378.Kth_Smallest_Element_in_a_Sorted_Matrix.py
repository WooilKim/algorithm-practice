# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# 378. Kth Smallest Element in a Sorted Matrix

from heapq import *


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution2:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted([j for sub in matrix for j in sub])[k - 1]


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        minHeap = []
        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
        print(minHeap)
        # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
        # if the row of the top element has more elements, add the next element to the heap
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            print(number, i, row)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i + 1:
                heappush(minHeap, (row[i + 1], i + 1, row))
        return number


if __name__ == '__main__':
    print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
