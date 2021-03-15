# https://programmers.co.kr/learn/courses/30/lessons/17681

import json


def solution(n, arr1, arr2):
    answer = ''
    str1, str2 = '', ''
    for i in range(len(arr1)):
        str1 += format(arr1[i], f"0{n}b")
        str2 += format(arr2[i], f"0{n}b")

    for i in range(len(str1)):
        if str1[i] == '0' and str2[i] == '0':
            answer += ' '
        else:
            answer += '#'
    # print(str1, str2)
    return [answer[i:i + n] for i in range(0, len(answer), n)]


def test():
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    print('test1')
    print(solution(n, arr1, arr2))
    # answer ['#####', '# # #', '### #', '#  ##', '#####']

    print('test2')
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
    # answer ["######", "### #", "## ##", " #### ", " #####", "### # "]


if __name__ == '__main__':
    test()
    n = input()
    arr1 = json.loads(input())
    arr2 = json.loads(input())

    answer = solution(n, arr1, arr2)
    print(answer)
