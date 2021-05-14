# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    res = [0]
    for n in numbers:
        res = [r + n for r in res] + [r - n for r in res]
    return len([r for r in res if r == target])


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3), 5)
