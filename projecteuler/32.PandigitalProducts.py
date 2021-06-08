# https://projecteuler.net/problem=32
# Problem 32. Pandigital Products

def pandigital_products():
    res = set()
    for i in range(1, 100):
        for j in range(1, 10000):
            if ''.join(sorted(f'{i}{j}{i * j}')) == '123456789':
                res.add(i * j)
    return res


if __name__ == '__main__':
    print(pandigital_products())
