# https://www.acmicpc.net/problem/2668
# BOJ 2668 숫자고르기 (1996 KOI 초등부)


def solution(n, numbers):
    while True:
        flag = True
        for i in range(n):
            if numbers[i] != 0 and i + 1 not in numbers:
                tmp = numbers[i]
                numbers[i] = 0
                while numbers[tmp] > 0:
                    numbers[tmp] = 0
                    tmp = numbers[tmp]
                flag = False
        if flag:
            break
    answer = [i for i in numbers if i != 0]
    print(len(answer))
    print('\n'.join(map(str, sorted(answer))))


if __name__ == '__main__':
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    solution(n, numbers)

"""
7
2
6
5
4
3
2
7

2 4 6 7 8
6 8 4 2 7

9
5 
6 
2 
8 
3 
4 
2 
7 
6

10 
2 
4 
1 
7 
7 
4 
4 
8 
2 
1
"""
