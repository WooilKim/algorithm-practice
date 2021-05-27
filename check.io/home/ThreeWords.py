# https://py.checkio.org/en/mission/three-words/

def checkio(words: str) -> bool:
    cnt = 0
    for word in words.split():
        cnt = cnt + 1 if word.isalpha() else 0
        if cnt == 3:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    print(checkio("one two 3 four five 6 seven eight 9 ten eleven 12"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
