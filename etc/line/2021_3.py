import json


def solution(enter, leave):
    ans = list()
    for _ in enter:
        ans.append(0)
    for l in leave:
        for i in range(enter[:enter.index(l)]):
            ans[i] += 1

    for i in enter:
        for j in enter:
            if i == j:
                continue
            if (enter.index(i) - enter.index(j)) * (leave.index(i) - leave.index(j)) < 0:
                ans[i - 1].add(j)
    return ans


if __name__ == '__main__':
    enter = json.loads(input())
    leave = json.loads(input())
    print(solution(enter, leave))
    pass
