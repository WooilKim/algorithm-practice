# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    res = [0, 0, 0]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, a in enumerate(answers):
        if a == i % 5 + 1:
            res[0] += 1
        if a == p2[i % 8]:
            res[1] += 1
        if a == p3[i % 10]:
            res[2] += 1

    m = max(res)
    answer = list()
    while m in res:
        idx = res.index(m)
        answer.append(idx + 1)
        res[idx] = 0
    return answer


if __name__ == '__main__':
    # print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))
