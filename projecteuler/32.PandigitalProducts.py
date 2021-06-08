# https://projecteuler.net/problem=32
# Problem 32. Pandigital Products

def pandigital_products():
    def is_pandigital(a, b, c):
        return len(f'{a}{b}{c}') == 9 and all([True if a == b else False for a, b in
                                               zip(sorted(list(map(int, f'{a}{b}{c}'))), [i for i in range(1, 10)])])

    print([i for i in range(1, 10)])
    res = set()
    for i in range(1, 10000):
        for j in range(1, 10000):
            if is_pandigital(i, j, i * j):
                res.add(i * j)
    return res


if __name__ == '__main__':
    print(pandigital_products())
