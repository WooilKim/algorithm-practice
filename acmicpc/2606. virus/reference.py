def solution():
    computer = int(input())
    line = [[] for _ in range(computer + 1)]

    for i in range(int(input())):
        a, b = map(int, input().strip().split())
        line[a].append(b)

    virus = [0] * (computer + 1)
    virus[1] = 1

    q = []
    q.append(1)
    cnt = 0
    while q:
        v = q.pop(0)
        if len(line) >= 0:
            for i in line[v]:
                if virus[i] == 0:
                    virus[i] = 1
                    q.append(i)
                    cnt += 1

    print(cnt)


if __name__ == '__main__':
    solution()
