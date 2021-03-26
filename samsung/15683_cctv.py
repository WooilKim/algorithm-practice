# https://www.acmicpc.net/problem/15683

E, S, W, N = 0, 1, 2, 3

rotations = [[0, 1, 2, 3], [0, 1], [0, 1, 2, 3], [0, 1, 2, 3], [0]]
dirs = [[0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]


class Solution:
    def min_blind(self, n: int, m: int, office: list[list[int]]) -> int:
        cctvs = list()
        blinds = list()
        for y in range(n):
            for x in range(m):
                if office[y][x] == 0:
                    blinds.append((y, x))
                elif 0 < office[y][x] < 6:
                    cctvs.append((y, x, office[y][x] - 1))
                else:
                    continue
        cases = list()
        if len(cctvs) == 0:  # if no cctv
            return len(blinds)
        for cctv in cctvs:
            cases = [f'{case}{r}' for case in cases for r in rotations[cctv[-1]]]
            if not cases:
                cases = [f'{r}' for r in rotations[cctv[-1]]]
        memo = dict()
        for case in cases:
            for i, cctv in enumerate(cctvs):
                if i > 0:
                    watches = {x for x in memo[case[:i]]}
                else:
                    watches = set()
                r = int(case[i])
                for d in dirs[cctv[2]]:
                    v = 0
                    if (d + r) % 4 == E:
                        while cctv[1] + v < m and office[cctv[0]][cctv[1] + v] != 6:
                            if office[cctv[0]][cctv[1] + v] == 0:
                                watches.add((cctv[0], cctv[1] + v))
                            v += 1
                    elif (d + r) % 4 == S:
                        while cctv[0] + v < n and office[cctv[0] + v][cctv[1]] != 6:
                            if office[cctv[0] + v][cctv[1]] == 0:
                                watches.add((cctv[0] + v, cctv[1]))
                            v += 1
                    elif (d + r) % 4 == W:
                        while cctv[1] - v > -1 and office[cctv[0]][cctv[1] - v] != 6:
                            if office[cctv[0]][cctv[1] - v] == 0:
                                watches.add((cctv[0], cctv[1] - v))
                            v += 1
                    elif (d + r) % 4 == N:
                        while cctv[0] - v > -1 and office[cctv[0] - v][cctv[1]] != 6:
                            if office[cctv[0] - v][cctv[1]] == 0:
                                watches.add((cctv[0] - v, cctv[1]))
                            v += 1
                    else:
                        print('error')
                    memo[case[:i + 1]] = watches

        return len(blinds) - max([len(memo[c]) for c in cases])


if __name__ == '__main__':
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for i in range(n)]

    print(Solution().min_blind(n, m, office))
