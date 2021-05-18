from collections import deque

import heapq


def solution(arr):
    visited = set()
    arr.sort()
    queue = list()
    queue.append((-sum(arr), arr))
    heapq.heapify(queue)

    # queue = deque([arr])

    def check(ar):
        s = sum(ar)
        numq = deque()
        numq.append((1, 0))
        numq.append((1, ar[0]))
        while numq:
            i, a = numq.popleft()
            if a == s // 2:
                return True
            if i < len(numq) - 1 and a < s // 2:
                numq.append((i + 1, a))
                numq.append((i + 1, a + ar[i]))
        return False

    while queue:
        curr_sum, curr = heapq.heappop(queue)
        curr_sum *= -1
        if tuple(curr) in visited:
            continue
        visited.add(tuple(curr))
        if sum(curr) % 2 == 0:
            if check(curr):
                return sum(curr) // 2
        else:
            for i in range(len(curr)):
                queue.append(curr[:i] + curr[i + 1:])
    return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    print(solution(arr))
