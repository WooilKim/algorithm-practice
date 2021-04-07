# https://www.acmicpc.net/problem/15685
# 15685 드래곤 커브


E, N, W, S = 0, 1, 2, 3
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


class Solution:
    def count_squares(self, n, curves) -> int:
        points = set()
        for x, y, d, g in curves:
            c = self.dragon_curve(x, y, d, g)
            # print(c)
            for p in c:
                points.add(p)
        cnt = 0
        # print(points)
        for j in range(100):
            for i in range(100):
                if (j, i) in points and (j + 1, i) in points and (j, i + 1) in points and (j + 1, i + 1) in points:
                    cnt += 1
        return cnt

    def dragon_curve(self, x, y, d, g):
        if g == 0:
            return [(y, x), (y + directions[d][0], x + directions[d][1])]
        else:
            base = self.dragon_curve(x, y, d, g - 1)
            focus = base[-1]
            base += [(focus[0] - focus[1] + b[1], focus[1] + focus[0] - b[0]) for b in base[:-1]][::-1]
            return base


if __name__ == '__main__':
    n = int(input())
    curves = [list(map(int, input().split())) for _ in range(n)]
    print(Solution().count_squares(n, curves))
