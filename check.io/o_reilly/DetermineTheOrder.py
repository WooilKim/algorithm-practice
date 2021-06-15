# https://py.checkio.org/en/mission/determine-the-order/
# O'reilly
# Determine the Order

import functools


def checkio(data):
    def compare(a, b):
        for d in data:
            if a in d and b in d:
                print(d.index(a), d.index(b))
                return d.index(a) - d.index(b)
        return 0

    res = ''
    for s in data:
        if not res:
            res += s
            continue
        idx = 0
        for c in s:
            if c in res:
                idx = res.index(c)
                continue
            list(res).insert(idx, c)

    answer = set()
    for s in data:
        for c in s:
            answer.add(c)
    answer = list(answer)
    print(answer)
    answer.sort(key=functools.cmp_to_key(compare))
    answer.sort(key=functools.cmp_to_key(compare))
    print(answer)
    return ''.join(answer)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"

"""
a-c
a-b
c-b
a-c-b
b-d
z-w-a
k-l-m
k-a-d-l
l-s-m
d-f-g
f-r-t
t-y-g

d-f-g
d-f-r-t-y-g


0 1 2 dfg
0 1 2 frt
0 1 2 tyg

z w a c b d
k a d l m
kadlsm

a<c<b
b<d
z<w<a

klmads

03 1 2
zwacbda
dfrtyg
0 d 
1 f
1 r
dfrtyg
acbd
kadlsm
2 t
1 y
4 g

"""
