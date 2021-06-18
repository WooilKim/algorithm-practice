# https://py.checkio.org/en/mission/end-of-other/

def checkio(words_set):
    return any([True for a in words_set for b in words_set if len(a) < len(b) and b[-len(a):] == a])