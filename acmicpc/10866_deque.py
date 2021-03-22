# https://www.acmicpc.net/problem/10866

def solution(cmds):
    deque = list()
    for cmd in cmds:
        if cmd[0] == "push_front":
            deque.insert(0, int(cmd[1]))
        elif cmd[0] == "push_back":
            deque.append(int(cmd[1]))
        elif cmd[0] == "pop_front":
            if len(deque):
                print('{}'.format(deque.pop(0)))
            else:
                print('{}'.format(-1))
        elif cmd[0] == "pop_back":
            if len(deque):
                print('{}'.format(deque.pop(len(deque) - 1)))
            else:
                print('{}'.format(-1))
        elif cmd[0] == "size":
            print(len(deque))
        elif cmd[0] == "empty":
            if len(deque):
                print('{}'.format(0))
            else:
                print('{}'.format(1))
        elif cmd[0] == "front":
            if len(deque):
                print('{}'.format(deque[0]))
            else:
                print('{}'.format(-1))
        elif cmd[0] == "back":
            if len(deque):
                print(deque[len(deque) - 1])
            else:
                print('{}'.format(-1))


if __name__ == '__main__':
    n = int(input())
    cmds = list()
    for line in range(n):
        cmds.append(input().split(' '))
