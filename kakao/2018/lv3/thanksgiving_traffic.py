# https://programmers.co.kr/learn/courses/30/lessons/17676
import json
from datetime import datetime as dt
import time
from collections import Counter


def solution(lines):
    # base = (dt.strptime('2016-09-15 20:59:57.421', '%Y-%m-%d %H:%M:%S.%f').timestamp())

    # print('base', base)
    lines = [
        (int((dt.strptime(' '.join(line.split()[0:2]), '%Y-%m-%d %H:%M:%S.%f').timestamp()) * 1000),
         int(float(line.split()[2][:-1]) * 1000)) for line in
        lines]
    d = dict()
    for line in lines:
        st = line[0] - line[1] + 1
        et = line[0]
        print(dt.fromtimestamp(st / 1000), dt.fromtimestamp(et / 1000))
        for t in range(st, et + 1):
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
    answer = max(d.values())

    print(min(d.values()))
    print(Counter(d))
    l = [key if d[key] == 5 else -1 for key in d]
    print(l)

    print(dt.fromtimestamp(1473940799.447))
    print(dt.fromtimestamp(1473940799.591))
    # print(dt.fromtimestamp(1473940797))
    return answer


def test():
    # print(solution([
    #     "2016-09-15 20:59:57.421 0.351s",
    #     "2016-09-15 20:59:58.233 1.181s",
    #     "2016-09-15 20:59:58.299 0.8s",
    #     "2016-09-15 20:59:58.688 1.041s",
    #     "2016-09-15 20:59:59.591 1.412s",
    #     "2016-09-15 21:00:00.464 1.466s",
    #     "2016-09-15 21:00:00.741 1.581s",
    #     "2016-09-15 21:00:00.748 2.31s",
    #     "2016-09-15 21:00:00.966 0.381s",
    #     "2016-09-15 21:00:02.066 2.62s"
    # ]))

    print(solution(["2016-09-15 20:59:57.421 0.351s",
                    "2016-09-15 20:59:58.233 1.181s",
                    "2016-09-15 20:59:58.299 0.8s",
                    "2016-09-15 20:59:58.688 1.041s",
                    "2016-09-15 20:59:59.591 1.412s",
                    "2016-09-15 21:00:00.464 1.466s",
                    "2016-09-15 21:00:00.741 1.581s",
                    "2016-09-15 21:00:00.748 2.31s",
                    "2016-09-15 21:00:00.966 0.381s",
                    "2016-09-15 21:00:02.066 2.62s"]))


if __name__ == '__main__':
    test()
    # lines = json.loads(input())
    # solution(lines)
    pass
