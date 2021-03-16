import math


# problem
# 16.5
# 계승(factorial)의 0
# n!의 계산 결과에서 마지막에 붙은 연속된 0의 개수를 계산하는 알고리즘을 작성하라

# 1. factorial을 계산하고 0의 개수를 세는 방법 : int 범위 넘어가면 불가능

# factorial을 구하는 방법
# 단순 반복문
def factorial_for(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


# 재귀함수 사용
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)


# 재귀가 너무 많이 발생해 메모이제이션을 사용
mem = {}


def factorial_recur_mem(n):
    global mem
    if n in mem:
        return mem[n]
    elif n <= 1:
        return 1
    else:
        mem[n] = n * factorial_recur_mem(n - 1)
        return mem[n]


# 전역 메모이제이션을 없애기 위해
# 데코레이터를 사용
def decorator(func):
    mem2 = {}

    def wrapper(n):
        if n in mem2:
            return mem2[n]
        else:
            mem2[n] = func(n)
            return mem2[n]

    return wrapper


@decorator
def factorial_recur_mem2(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recur_mem2(n - 1)


# n을 d로 몇번 나눌 수 있는지 리턴하는 함수
def divider(n, d):
    cnt = 0
    while n % d == 0:
        n //= d
        cnt += 1
    return cnt


# 2-1. 2와 5의 개수 (5가 더 적으므로 5를 센다)
def factorial_cnt5(n):
    cnt = 0
    for i in range(1, n + 1):
        cnt += divider(i, 5)
    return cnt


# 2-2. 2와 5의 개수 (5가 더 적으므로 5를 센다) 5의 배수로 루프를 돈다 (루프 수가 적어짐)
def factorial_cnt5_reduced(n):
    cnt = 0
    for i in range(1, int(math.log(n, 5)) + 1):
        cnt += n // 5
    return cnt


if __name__ == '__main__':
    num = factorial_recur_mem2(20)
    print(num)
    print(divider(num, 20))
    print(factorial_cnt5(20))
    print(factorial_cnt5_reduced(20))
