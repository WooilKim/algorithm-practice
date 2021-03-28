# https://programmers.co.kr/learn/courses/30/lessons/17676
import json
from datetime import datetime as dt
import time
from collections import Counter


def solution(lines):
    base = (dt.strptime('2016-09-15 00:00:00.000', '%Y-%m-%d %H:%M:%S.%f').timestamp())

    # print('base', base)
    lines = [
        (int((dt.strptime(' '.join(line.split()[0:2]), '%Y-%m-%d %H:%M:%S.%f').timestamp()) * 1000),
         int(float(line.split()[2][:-1]) * 1000)) for line in
        lines]
    # print('lines', lines)
    m = max(min([line[0] - line[1] + 1 for line in lines]), int(base * 1000))
    M = max([line[0] for line in lines])
    print(m, M)
    answer = 0
    # for t in range(m, M + 1 - 1000):

    for i, line in enumerate(lines):
        st = line[0] - line[1] + 1
        et = line[0]
        cnt = [0, 0, 0, 0]
        # for curline in lines[:i] + lines[i + 1:]:
        for curline in lines:
            cst = curline[0] - curline[1] + 1
            cet = curline[0]

            if cet >= st - 1000 + 1 and st >= cst:
                cnt[0] += 1
            if cet >= st and st + 999 >= cst:
                cnt[1] += 1
            if cet >= et - 1000 + 1 and et >= cst:
                cnt[2] += 1
            if cet >= et and et + 999 >= cst:
                cnt[3] += 1

        answer = max(max(cnt), answer)
    return answer

# 모범답안
def solution2(lines):
    # get input
    S, E = [], []
    totalLines = 0
    for line in lines:
        totalLines += 1
        type(line)
        (d, s, t) = line.split(" ")

        ##time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)

    # count the maxTraffic
    S.sort()

    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while ((countE < totalLines) & (countS < totalLines)):
        if (S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else:  ## it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic


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

    # print(solution(["2016-09-15 20:59:57.421 0.351s",
    #                 "2016-09-15 20:59:58.233 1.181s",
    #                 "2016-09-15 20:59:58.299 0.8s",
    #                 "2016-09-15 20:59:58.688 1.041s",
    #                 "2016-09-15 20:59:59.591 1.412s",
    #                 "2016-09-15 21:00:00.464 1.466s",
    #                 "2016-09-15 21:00:00.741 1.581s",
    #                 "2016-09-15 21:00:00.748 2.31s",
    #                 "2016-09-15 21:00:00.966 0.381s",
    #                 "2016-09-15 21:00:02.066 2.62s"]))
    # print(solution(["2016-09-15 00:00:00.000 3s"]))
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))


if __name__ == '__main__':
    test()
    # lines = json.loads(input())
    # solution(lines)
    pass
