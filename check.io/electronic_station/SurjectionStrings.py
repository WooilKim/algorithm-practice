# https://py.checkio.org/en/mission/isometric-strings/
# Electronic Station
# Surjection Strings

from collections import defaultdict


def isometric_strings(str1: str, str2: str) -> bool:
    d = defaultdict(set)
    for a, b in zip(str1, str2):
        d[a].add(b)
        if len(d[a]) > 1:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
