# https://www.acmicpc.net/problem/14891

N, S = '0', '1'


class Solution:
    def sum_score(self, wheels: list[str], k: int, R: list[list[int]]) -> int:
        print(wheels, k, R)
        score = 0

        return score


if __name__ == '__main__':
    wheels = [input() for i in range(4)]
    k = int(input())
    R = [list(map(int, input().split())) for i in range(k)]

    print(Solution().sum_score(wheels, k, R))
