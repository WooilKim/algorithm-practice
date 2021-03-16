# https://programmers.co.kr/learn/courses/30/lessons/17677

import re
import math
from collections import Counter


def solution(str1: str, str2: str):
    str1, str2 = str1.lower(), str2.lower()
    str1, str2 = re.sub(r'[^a-z]', ' ', str1), re.sub(r'[^a-z]', ' ', str2)
    l1 = [str1[i:i + 2] if ' ' not in str1[i:i + 2] else None for i in range(len(str1) - 1)]
    l2 = [str2[i:i + 2] if ' ' not in str2[i:i + 2] else None for i in range(len(str2) - 1)]
    l1, l2 = list(filter(lambda a: a is not None, l1)), list(filter(lambda a: a is not None, l2))
    intersection = list((Counter(l1) & Counter(l2)).elements())
    union = list((Counter(l1) | Counter(l2)).elements())
    if len(union) == 0:
        return 65536
    answer = int(len(intersection) / len(union) * 65536)
    return answer


# 모범답안
def solution2(str1, str2):
    str1 = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
    str2 = [str2[i:i + 2].lower() for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum / hap_sum) * 65536)


def test():
    print(solution('FRANCE', 'french'))
    print(solution('handshake', 'shake hands'))
    print(solution('aa1+aa2', 'AAAA12'))
    print(solution('E=M*C^2', 'e=m*c^2'))


if __name__ == '__main__':
    test()
    # str1, str2 = input(), input()
    # print(solution(str1, str2))
