# https://www.acmicpc.net/problem/15684
# 15684 사다리조작

from itertools import combinations, permutations


# Runtime: 164 ms, faster than 87.37% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.41% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def min_horizontal_lines(self, n, m, h, K) -> int:
        global memo, keys
        memo = list()
        keys = list()
        cases = list()
        K = sorted([(k[0] - 1, k[1] - 1) for k in K], key=lambda x: x[1])
        outs = [i for i in range(n)]
        exceptions = list()
        for k in K:
            exceptions.append(k)
            if k[1] > 1:
                exceptions.append((k[0], k[1] - 1))
            if k[1] < n - 2:
                exceptions.append((k[0], k[1] + 1))

        for j in range(h):
            for i in range(n - 1):
                if (i, j) not in exceptions:
                    keys.append((i, j))
        print('start')
        for c in range(3):
            print([1] * (c + 1) + [0] * (len(keys) - c - 1))
            cases.append(list(permutations([1] * (c + 1) + [0] * (len(keys) - c - 1), len(keys))))
        print(cases)

        # print(cases)
        comb = list()
        for k in K:
            outs[k[0]], outs[k[1]] = outs[k[1]], outs[k[0]]
        print(outs)

        return
        # print(n, m, h, K)
        # return sorted([j for sub in matrix for j in sub])[k - 1]

    def dfs(self, ss, K):
        if ss in memo:
            return False
        ladders = sorted(K + [keys[s] for s in ss], key=lambda x: x[1])
        memo.append(ss)
        for l in ladders:
            if (l[0], l[1] - 1) in ladders or (l[0], l[1] + 1) in ladders:
                return False
        outs = [i for i in range(n)]
        for k in ladders:
            outs[k[0]], outs[k[1]] = outs[k[1]], outs[k[0]]
        if all([True if outs[i] == i else False for i in range(n)]):
            return True
        if len(ladders) < len(K) + 3:
            self.dfs(ss, K)


if __name__ == '__main__':
    n, m, h = map(int, input().split())
    K = [tuple(map(int, input().split())) for _ in range(m)]
    print(Solution().min_horizontal_lines(n, m, h, K))
