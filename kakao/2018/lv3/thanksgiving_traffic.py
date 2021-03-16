# https://programmers.co.kr/learn/courses/30/lessons/17676
import json
from datetime import datetime as dt


def solution(lines):
    lines = [(dt.strptime(' '.join(line.split()[0:2]), '%Y-%m-%d %H:%M:%S.%f'), float(line.split()[2][:-1])) for line in
             lines]
    print(lines)
    answer = 0
    return answer


def test():
    print(solution([
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]))


if __name__ == '__main__':
    test()
    # lines = json.loads(input())
    # solution(lines)
    pass
