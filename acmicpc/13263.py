# https://www.acmicpc.net/problem/13263
mem = dict()


def cut_trees(n, A, B):
    mem[0] = 0

    def dp(i, A, B):
        if i not in mem:
            mem[i] = min([dp(j, A, B) + A[i] * B[j] for j in range(0, i)])
        return mem[i]

    print(mem)
    return dp(n - 1, A, B)


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(cut_trees(n, A, B))
"""
5
1 2 3 4 5
5 4 3 2 0

6
1 2 3 10 20 30
6 5 4 3 2 0

"""

"""
cut first
cost = B[0]
max = A[-1]*B[0] + cost
start = 1
while True:
    arr = [A[i]*cost+B[i]*A[-1] for i in range(start, n-1)]
    m = min(arr)
    if m < max:
        max = m
        start = arr.index(m) + 1
    else:
        break
"""
