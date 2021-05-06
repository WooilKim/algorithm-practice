# https://www.acmicpc.net/problem/19236
from copy import deepcopy


def teen_shark(A, B):
    shark = [0, 0, 0]  # y,x,d
    dirs = [[-1, 0],
            [-1, -1],
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1]]

    def dfs(shark, A, B, eaten):

        fish = {A[j][i]: [j, i, B[j][i]] for j in range(4) for i in range(4) if A[j][i] > 0}
        fkeys = sorted(fish.keys())
        # move fish
        for size in fkeys:
            y, x, d = fish[size]
            for i in range(8):
                next_d = (d + i) % 8
                next_y, next_x = y + dirs[next_d][0], x + dirs[next_d][1]
                # if next is in board and not shark
                if 0 <= next_x < 4 and 0 <= next_y < 4 and all([next_y, next_x] != shark[:1]):
                    # change fish 1 and 2 from A, B
                    if A[next_y][next_x] in fish:
                        fish[A[next_y][next_x]][0], fish[A[next_y][next_x]][1] = y, x
                    fish[size][0], fish[size][1] = next_y, next_x
                    A[y][x], A[next_y][next_x] = A[next_y][next_x], A[y][x]
                    # TODO : update B
                    break
        # eat
        i = 0
        cases = list()
        while True:
            next_y, next_x = shark[0] + dirs[shark[2]][0] * i, shark[1] + dirs[shark[2]][1] * i
            if 0 <= next_y < 4 and 0 <= next_x < 4:
                if A[next_y][next_x] != 0:
                    f = A[next_y][next_x]
                    A_copy, B_copy = deepcopy(A), deepcopy(B)
                    A_copy[next_y][next_x] = 0
                    B_copy[next_y][next_x] = -1
                    cases.append([[next_y, next_x, B[next_y][next_x]], A_copy, B_copy, eaten + f])
            else:
                break
        if cases:
            ans = max([dfs(c[0], c[1], c[2], eaten) for c in cases])
        else:
            return eaten
        return ans

    """
    shark = 0,0,0
    eat 0,0,0 fish
    update shark direction
    return dfs()
    def dfs(shark, A, B):
        fish = {A[j][i]:[j, i, B[j][i]] for j in range(4) for i in range(4) if A[j][i] > 0}
        fish.sort()
        fkeys = fish.keys().sort()
        for f in fkeys:
            size, y, x, d
            for i in range(8):
                next_d = (d+i)%8
                next_y, next_x = y + dirs[next_d][0], x+dirs[next_d][1] 
                if 0<= next_x, next_y < 4 and (next_y, next_X != shark)
                    if A[next_y][next_x] in fish:
                        fish[A[next_y][next_x]][0], fish[A[next_y][next_x]][1] = y, x
                        fish[size][0], fish[size][1] = next_y, next_x  
                    A[y][x], A[next_y][next_x] = A[next_y][next_x], A[y][x]
                    break
        
        move fishes
        from smaller fishes
            fish = y,x,d
            for i in range(8):
                next_y, next_x = y + dirs[d][0], x+dirs[d][1] 
                if 0<= next_x, next_y < 4 and (next_y, next_X != shark)
                    A[y][x], A[next_y][next_x] = A[next_y][next_x], A[y][x]
                    break
        eat fishes
        
        def eat(shark.copy, A.copy, B.copy)
            return eat()
        return [teen_shark]    
    dfs
        A,B copy
        n + eat
        return max
        
    """


if __name__ == '__main__':
    A, B = list(), list()
    for i in range(4):
        nums = list(map(int, input().split()))
        A.append([nums[i] for i in range(len(nums)) if i % 2 == 0])
        B.append([nums[i] - 1 for i in range(len(nums)) if i % 2 == 1])  # dir - 1

    print(teen_shark(A, B))
    pass
