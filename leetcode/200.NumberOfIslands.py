# https://leetcode.com/problems/number-of-islands/
from collections import deque
from typing import List

# Runtime: 144 ms, faster than 51.65% of Python3 online submissions for Number of Islands.
# Memory Usage: 19.2 MB, less than 14.38% of Python3 online submissions for Number of Islands.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_island = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) in visited:
                    continue
                queue = deque()
                if grid[y][x] == '1':
                    num_island += 1
                    queue.append((y, x))
                    while queue:
                        j, i = queue.popleft()
                        if (j, i) in visited:
                            continue
                        visited.add((j, i))
                        if j > 0 and grid[j - 1][i] == "1":
                            queue.append((j - 1, i))
                        if i > 0 and grid[j][i - 1] == "1":
                            queue.append((j, i - 1))
                        if j < len(grid) - 1 and grid[j + 1][i] == "1":
                            queue.append((j + 1, i))
                        if i < len(grid[0]) - 1 and grid[j][i + 1] == "1":
                            queue.append((j, i + 1))
        return num_island


if __name__ == '__main__':
    print(Solution().numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
    print(Solution().numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
