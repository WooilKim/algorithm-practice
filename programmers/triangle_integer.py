# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    answer = 0
    for row in triangle[-2::-1]:
        print(row)
        for i in range(len(row)):
            triangle[-1][i] = row[i] + max(triangle[-1][i], triangle[-1][i + 1])
    return triangle[-1][0]


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
