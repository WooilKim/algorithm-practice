# https://py.checkio.org/en/mission/reverse-every-ascending/

def reverse_ascending(items):
    l, r = 0, 1
    while r <= len(items):
        if r == len(items) or items[r] <= items[r - 1]:
            items = items[:l] + sorted(items[l:r], reverse=True) + items[r:]
            l = r
        r += 1
    return items


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 2, 3]))
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
