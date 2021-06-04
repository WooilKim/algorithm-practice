# https://projecteuler.net/problem=28
# 28. Number spiral diagonals

def spiral_diagonals(n):
    res = 1
    for i in range(1, n // 2 + 1):
        spiral_sum = 2 * (2 * (i * 2 + 1) ** 2 - (i * 2) * 3)
        res += spiral_sum
    return res


"""
i = 0, > 1
i = 1, 3,5,7,9 => 9-3 = 6 = 3*2, (9-3)*2 
i = 2, 13, 17, 21, 25 => 38*2 2* (i*2+1)**2 25-13 = 12 = 3*4 
i = 3, 31, 37, 43 ,49 => 80*2 (i*2+1)**2 18 49-31 = 18 = 3*6
for 
i = k, last : (k*2+1)**2, first : (k*2+1)**2 - 3*2*k
answer = sum(last,fist)*2
"""


if __name__ == '__main__':
    print(spiral_diagonals(5))
    print(spiral_diagonals(1001))
