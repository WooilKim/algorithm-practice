# problem
# 16.6
# 최소의 차이
# 두개의 정수 배열이 주어져 있다. 각 배열에서 숫자를 하나씩 선택했을 때 두 숫자의 차이(절대값)가 최소인 값을 출력하라.

import math


# 하나씩 비교해서 차를 구하는 방법
def naive(arr1, arr2):
    diff = 99999
    num1, num2 = 0, 0
    for a in arr1:
        for b in arr2:
            if diff > abs(a - b):
                diff = abs(a - b)
                num1 = a
                num2 = b
                # print(a, b, min)
    return num1, num2


# 정렬해서 비교하는 방법
def sort_and_compare(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i1, i2 = 0, 0
    diff = 99999
    num1, num2 = 0, 0
    while i1 < len(arr1) and i2 < len(arr2):
        if abs(arr1[i1] - arr2[i2]) < diff:
            diff = abs(arr1[i1] - arr2[i2])
            num1, num2 = arr1[i1], arr2[i2]
        if arr1[i1] < arr2[i2]:
            i1 += 1
        else:
            i2 += 1
    return num1, num2
    # print(arr1, arr2)


if __name__ == '__main__':
    arr1 = [1, 3, 15, 11, 2]
    arr2 = [23, 127, 235, 19, 8]
    print(naive(arr1, arr2))
    print(sort_and_compare(arr1, arr2))
