# https://www.acmicpc.net/problem/1021

n, m = [int(i) for i in input().split()]

targets = [int(i) for i in input().split()]

circular_queue = [i + 1 for i in range(n)]
current_index = 0
answer = 0
for target in targets:
    for j in range(len(circular_queue)):
        idx = (current_index + j + 1) % len(circular_queue)
        if circular_queue[idx] == target:
            if j + 1 <= len(circular_queue) / 2:
                answer += j + 1
                # print(j+1)
            else:
                answer += len(circular_queue) - j - 1
                # print(len(circular_queue) - j - 1)
            del (circular_queue[idx])
            current_index = idx
            break
        else:
            continue
print(answer)
