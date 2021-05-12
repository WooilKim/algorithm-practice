# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import deque


def solution(tickets):
    answer = []
    q = deque([[('ICN', 'ICN')]])
    while q:
        cur = q.popleft()
        flag = True
        for ticket in tickets:
            if ticket[0] == cur[-1][1] and tuple(ticket) not in cur:
                q.append(cur + [tuple(ticket)])
                flag = False
        if flag:
            answer.append(cur)
    # answer = [b for (a, b) in answer]
    for i in range(len(answer)):
        answer[i] = [b for a, b in answer[i]]
    answer.sort(key=lambda a: (-len(a), a))
    # print(answer)
    return answer[0]


if __name__ == '__main__':
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]), ["ICN", "JFK", "HND", "IAD"])
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]),
          ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
    print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'], ['AAA', 'ICN']]))
