# https://projecteuler.net/problem=29
# Distinct Powers

def distinct_powers(a, b) -> set:
    res_set = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            res_set.add(i ** j)
    return res_set


if __name__ == '__main__':
    print(len(distinct_powers(5, 5)))
    print(len(distinct_powers(100, 100)))
