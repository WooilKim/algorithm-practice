# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    queue = []
    dic = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    for m in msg:
        queue.append(m)
        if ''.join(queue) in dic:
            continue
        else:
            dic.append(''.join(queue))
            answer.append((dic.index(''.join(queue[:-1]))) + 1)
            queue = queue[-1:]
    answer.append((dic.index(''.join(queue))) + 1)
    return answer


def test():
    print(solution('KAKAO'))
    print(solution('TOBEORNOTTOBEORTOBEORNOT'))
    print(solution('ABABABABABABABAB'))


if __name__ == '__main__':
    # msg = input()
    # print(solution(msg))
    msg = input()
    print(solution(msg))
