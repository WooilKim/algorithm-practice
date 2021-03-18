# https://www.acmicpc.net/problem/3190


def solution(n, k, apples, l, dirs):
    pass


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    apples = list()
    for row in range(k):
        apples.append(list(map(int, (input().split()))))
    l = int(input())
    dirs = list()
    for row in range(l):
        dirs.append(input().split())
        dirs[row][0] = int(dirs[row][0])
    print(solution(n, k, apples, l, dirs))
