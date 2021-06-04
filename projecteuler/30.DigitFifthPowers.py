# https://projecteuler.net/problem=30

def nth_powers(n):
    res = []
    for num in range(2, 10 ** (n+2)):
        s = 0
        i = num
        while i > 0:
            i, m = divmod(i, 10)
            s += m ** n
        if s == num:
            res.append(s)
    return sum(res)


if __name__ == '__main__':
    print(nth_powers(4))
    print(nth_powers(5))
