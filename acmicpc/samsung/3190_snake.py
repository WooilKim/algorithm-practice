# https://www.acmicpc.net/problem/3190
# 뱀
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def solution(n, apples, turns):
    snake = [[0, 0]]  # tail : head
    going = RIGHT
    time = 0
    next = list()
    i = 0
    while True:
        if i in [x[0] for x in turns]:
            idx = [x[0] for x in turns].index(i)
            if turns[idx][1] == "L":
                if going == UP:
                    going = LEFT
                elif going == DOWN:
                    going = RIGHT
                elif going == LEFT:
                    going = DOWN
                elif going == RIGHT:
                    going = UP
            else:  # D
                if going == UP:
                    going = RIGHT
                elif going == DOWN:
                    going = LEFT
                elif going == LEFT:
                    going = UP
                elif going == RIGHT:
                    going = DOWN
        if going == UP:
            next = [snake[len(snake) - 1][0] - 1, snake[len(snake) - 1][1]]
        if going == DOWN:
            next = [snake[len(snake) - 1][0] + 1, snake[len(snake) - 1][1]]
        if going == LEFT:
            next = [snake[len(snake) - 1][0], snake[len(snake) - 1][1] - 1]
        if going == RIGHT:
            next = [snake[len(snake) - 1][0], snake[len(snake) - 1][1] + 1]
        #     move
        # next case : apples,  board , snake, out of board,
        if next in apples:
            snake.append(next)
            apples.remove(next)
            time += 1
        elif next not in snake and -1 < next[0] < n and -1 < next[1] < n:
            snake.append(next)
            snake.pop(0)
            time += 1
        else:  # die
            time += 1
            break
        i += 1
        # print(i, snake)
    return time


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    apples = list()
    for row in range(k):
        apples.append(list(map(int, (input().split()))))
    for i in range(k):
        apples[i] = [apples[i][0] - 1, apples[i][1] - 1]
    # print(apples)
    l = int(input())
    turns = list()
    for row in range(l):
        turns.append(input().split())
        turns[row][0] = int(turns[row][0])
    print(solution(n, apples, turns))
