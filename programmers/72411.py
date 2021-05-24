# https://programmers.co.kr/learn/courses/30/lessons/72411
# title : 메뉴 리뉴얼

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        tmp = list()
        for order in orders:
            cb = list(combinations(sorted(order), c))
            tmp += cb
        counter = Counter(tmp)
        if counter and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


#
# def solution(orders, course):
#     answer = []
#     d = [["0"] * 26 for _ in orders]
#     for i in range(len(orders)):
#         for c in orders[i]:
#             d[i][ord(c) - ord('A')] = "1"
#     answers = dict()
#     for i in range(len(d)):
#         tmp = defaultdict(int)
#         for j in range(len(d)):
#             if i != j:
#                 a, b = int(''.join(d[i]), 2), int(''.join(d[j]), 2)
#                 s = format(a & b, '026b')
#                 tmp[s] += 1
#         print(tmp)
#
#
#     for c in course:
#         for ans in answers[c]:
#             tmp = ''
#             for i in range(len(ans)):
#                 if ans[i] == '1':
#                     tmp += chr(ord('A') + i)
#             answer.append(tmp)
#
#     # for item in l:
#     #     print(item.count('1'))
#     return sorted(answer)


if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]),
          ["AC", "ACDE", "BCFG", "CDE"])

"""
ORDER : A-Z
len(order) of each customer >= 2
2<=len(orders)<=20
2<=len(orders[i])<=10
orders[i] != orders[j]
0<=len(course)<=10
course[i]<course[j] (i<j)

return:
ascending order (dictionary)
len(answer) >= 1

["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]

111000000000000000000000 
10111000000000000000000000 
111000000000000000000000
"""
