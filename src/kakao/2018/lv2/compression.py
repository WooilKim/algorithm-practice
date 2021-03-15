# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    dic = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    i, j = 0, 0
    while (i < len(msg)):
        if msg[i:j] in dic:
            print(i, j, msg[i:j])

    return answer


if __name__ == '__main__':
    msg = input()
    print(solution(msg))
