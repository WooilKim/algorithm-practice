# https://py.checkio.org/en/mission/reverse-every-ascending/

def reverse_ascending(items):
    i, j = 0, 1
    while j < len(items):
        if items[j] > items[i]:
            j += 1
        else:
            items = items[:i] + sorted(items[i:j], reverse=True) + items[j:]
            i = j
            j += 1
    return items


if __name__ == '__main__':
    print("Example:")
    test = [1, 2, 3, 4, 5]
    test[0:3].sort(reverse=True)
    print(test)
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
