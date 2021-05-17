# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import deque


# def solution(tickets):
#     answer = []
#     q = deque([[('ICN', 'ICN')]])
#     while q:
#         cur = q.popleft()
#         flag = True
#         for ticket in tickets:
#             if ticket[0] == cur[-1][1] and tuple(ticket) not in cur:
#                 q.append(cur + [tuple(ticket)])
#                 flag = False
#         if flag:
#             answer.append(cur)
#     # answer = [b for (a, b) in answer]
#     for i in range(len(answer)):
#         answer[i] = [b for a, b in answer[i]]
#     answer.sort(key=lambda a: (-len(a), a))
#     # print(answer)
#     return answer[0]


def solution(tickets):
    # 1. 그래프 생성
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

        # 2. 시작점 - [끝점] 역순으로 정렬
    for r in routes.keys():
        routes[r].sort(reverse=True)

    # 3. DFS 알고리즘으로 path를 만들어줌.
    st = ["ICN"]
    path = []

    while st:
        top = st[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    # 4. 만든 path를 거꾸로 돌림.
    answer = path[::-1]
    return answer


if __name__ == '__main__':
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]), ["ICN", "JFK", "HND", "IAD"])
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ICN"], ["ATL", "SFO"], ["SFO", "ATL"]]),
          ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]),
          ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
    print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'], ['AAA', 'ICN']]))
