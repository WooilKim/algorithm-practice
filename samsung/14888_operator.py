# https://www.acmicpc.net/problem/14888
from itertools import permutations

PLUS, MINUS, MULTIPLY, DEVIDE = 0, 1, 2, 3


def solution(A, O):
    m, M = 999999999, -999999999
    # for a in A:
    perm = list()
    for o, n in enumerate(O):
        for i in range(n):
            perm.append(o)
    # print(len(set(permutations(perm, 5))))
    for operators in set(permutations(perm)):
        val = A[0]
        for i in range(len(A) - 1):
            if operators[i] == PLUS:
                val += A[i + 1]
            elif operators[i] == MINUS:
                val -= A[i + 1]
            elif operators[i] == MULTIPLY:
                val *= A[i + 1]
            elif operators[i] == DEVIDE:
                if val < 0:
                    val *= -1
                    val //= A[i + 1]
                    val *= -1
                else:
                    val //= A[i + 1]
            else:
                print('operators error')
        m = min(m, val)
        M = max(M, val)

    print(M)
    print(m)


if __name__ == '__main__':
    n = input()
    A = list(map(int, input().split()))
    O = list(map(int, input().split()))
    solution(A, O)

    pass
