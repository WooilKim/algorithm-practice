# https://www.acmicpc.net/problem/16235
# 16235 나무재테크

import copy


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def count_tree_alive(self, n, m, k, A, trees) -> int:
        # print(n, m, k, A, trees)
        for i in range(m):
            trees[i] = [trees[i][0] - 1, trees[i][1] - 1, trees[i][2]]
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        B = copy.deepcopy(A)
        for year in range(k):
            #     spring
            for tree in sorted(trees, key=lambda t: t[2]):
                if A[tree[0]][tree[1]] < tree[2]:
                    tree[2] *= -1
                else:
                    A[tree[0]][tree[1]] -= tree[2]
                    tree[2] += 1

            # summer
            for tree in [t for t in trees if t[2] < 0]:
                A[tree[0]][tree[1]] += (tree[2] * -1) // 2
            trees = [t for t in trees if t[2] > 0]

            # fall
            for tree in [t for t in trees if t[2] % 5 == 0]:
                for dir in directions:
                    next = (tree[0] + dir[0], tree[1] + dir[1], 1)
                    if -1 < next[0] < n and -1 < next[1] < n:
                        trees.append(next)

            # winter
            for j in range(n):
                for i in range(n):
                    A[j][i] += B[j][i]

        return len(trees)


if __name__ == '__main__':
    n, m, k = map(int, (input().split()))
    A = [list(map(int, input().split())) for i in range(n)]
    trees = [list(map(int, input().split())) for i in range(m)]
    print(Solution().count_tree_alive(n, m, k, A, trees))
