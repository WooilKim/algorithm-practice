# https://www.acmicpc.net/problem/10845

queue = list()


def solution(cmd):
    if len(cmd) > 5:  # push
        n = int(cmd.split()[-1])
        queue.append(n)
    elif cmd == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        print('cmd error')


if __name__ == '__main__':
    n = int(input())
    cmds = list()
    for i in range(n):
        cmds.append(input())

    for cmd in cmds:
        solution(cmd)
