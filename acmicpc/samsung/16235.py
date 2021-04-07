# https://www.acmicpc.net/problem/16235
# 16235 나무재테크
import time
import copy

# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
ts = [0, 0, 0, 0]
season_cnt = [0, 0, 0, 0]


class Solution:
    def count_tree_alive(self, n, m, k, A, trees) -> int:
        for i in range(m):
            trees[i] = [trees[i][0] - 1, trees[i][1] - 1, trees[i][2]]
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        B = copy.deepcopy(A)
        trees = sorted(trees, key=lambda x: -x[2])
        for j in range(n):
            for i in range(n):
                A[j][i] = 5
        for year in range(k):
            #     spring
            tic = time.process_time_ns()
            for tree in trees[::-1]:
                season_cnt[0] += 1
                if A[tree[0]][tree[1]] < tree[2]:
                    tree[2] *= -1
                else:
                    A[tree[0]][tree[1]] -= tree[2]
                    tree[2] += 1
            ts[0] += time.process_time_ns() - tic
            tic = time.process_time_ns()
            # summer
            for tree in [t for t in trees if t[2] < 0]:
                season_cnt[1] += 1
                A[tree[0]][tree[1]] += (tree[2] * -1) // 2
            trees = [t for t in trees if t[2] > 0]
            # [3.623154, 3.081989, 3.021685, 0.016321]
            ts[1] += time.process_time_ns() - tic
            tic = time.process_time_ns()
            # fall
            # [3.498371, 2.500074, 2.994142, 0.015903]
            for tree in [t for t in trees if t[2] % 5 == 0]:
                season_cnt[2] += 1
                # nexts = [[tree[0] + dir[0], tree[1] + dir[1], 1] for dir in directions if
                #          -1 < tree[0] + dir[0] < n and -1 < tree[1] + dir[1] < n]
                # trees.extend(nexts)
                for dir in directions:
                    next = [tree[0] + dir[0], tree[1] + dir[1], 1]
                    if -1 < next[0] < n and -1 < next[1] < n:
                        trees.append(next)
            # print('fall', len(trees), trees)
            ts[2] += time.process_time_ns() - tic
            tic = time.process_time_ns()
            # winter
            for j in range(n):
                for i in range(n):
                    A[j][i] += B[j][i]
            ts[3] += time.process_time_ns() - tic
        print([t / 1000000000 for t in ts])
        print(season_cnt)
        return len(trees)


if __name__ == '__main__':
    n, m, k = map(int, (input().split()))
    A = [list(map(int, input().split())) for i in range(n)]
    trees = [list(map(int, input().split())) for i in range(m)]
    print(Solution().count_tree_alive(n, m, k, A, trees))

# 71
# 5 2 7
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3

# 10 1 1000
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 1 1 1
