# https://programmers.co.kr/learn/courses/30/lessons/72412
# title : 순위 검색
from collections import defaultdict


def solution(info, query):
    for i in range(len(info)):
        info[i] = info[i].split()
    for i in range(len(query)):
        query[i] = [x for x in query[i].split() if x != 'and']
    mem = defaultdict(list)
    for i in info:
        for k in range(16):
            tmp = list()
            for j in range(4):
                if k & 2 ** j:
                    tmp.append('-')
                else:
                    tmp.append(i[j])
            mem[tuple(tmp)].append(int(i[-1]))
    answer = list()
    for v in mem.values():
        v.sort()

    for q in query:
        tmp = mem[tuple(q[:-1])]
        if tmp:
            i, j, k = 0, len(tmp), int(q[-1])
            t = 0
            while i < j:
                t = (i + j) // 2
                if tmp[t] >= k:
                    j = t
                elif tmp[t] < k:
                    i = t + 1
                else:
                    break
            answer.append(len(tmp) - i)
        else:
            answer.append(0)
    return answer


if __name__ == '__main__':
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]), [1, 1, 1, 1, 2, 4])

"""
language : [cpp, java, python]
job : [backend, frontend]
career : [junior, senior]
soulfood : [chicken, pizza]

3* 2* 2* 2
1 <= len(info) <= 50000
1 <= score <= 100000
1 <= len(query) <= 100000
- : skip


"""
