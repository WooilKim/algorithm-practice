def solution(txt):
    l = list()
    for t in txt:
        if t == '[' or t == '(':
            l.append(t)
        elif t == ']':
            if not l:
                return 'no'
            if l[-1] == '[':
                del (l[-1])
            else:
                return 'no'
        elif t == ')':
            if not l:
                return 'no'
            if l[-1] == '(':
                del (l[-1])
            else:
                return 'no'
        else:
            continue
    if l:
        return 'no'
    else:
        return 'yes'


if __name__ == '__main__':
    while True:
        txt = input()
        if txt == '.':
            break
        else:
            print(solution(txt))
