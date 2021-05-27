from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    for x in files:
        if len(x) - x.rindex('.') == 4:
            print(x[x.rindex('.'):], x[:x.rindex('.')])
        else:
            print('.aaa', x)

    # print([x[x.rindex('.'):], x[:x.rindex('.')] if len(x) - x.rindex('.') == 4 else tuple(('0', x)) for x in files])

    return sorted(files,
                  key=lambda x: (
                      (x[x.rindex('.'):], x[:x.rindex('.')]) if x.rindex('.') > 0 else tuple(
                          ('.', x))))


if __name__ == '__main__':
    print(len('as.asd') - 'as.asd'.rindex('.'))
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))
    print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
