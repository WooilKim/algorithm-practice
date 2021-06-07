# https://py.checkio.org/en/mission/words-order/

def words_order(text: str, words: list) -> bool:
    text = text.split()
    tdx = [text.index(words[i]) + 1 if words[i] in text else False for i in range(len(words))]
    return all(tdx[i - 1] < tdx[i] for i in range(1, len(words))) if all(tdx) else False


if __name__ == '__main__':
    print("Example:")
    print(words_order("hi world im here", ["country", "world"]))
    print(words_order("london in the capital of great britain", ["london"]))
    # print(words_order('hi world im here', ['world', 'here']))
    # print(words_order('hi world im here', ['here', 'world']))
    # print(words_order('hi world im here', ['world']))
    # print(words_order('hi world im here', ['world', 'here', 'hi']))
    # print(words_order('hi world im here', ['wo', 'rld']))
    # print(words_order('hi world im here', ['world', 'hi', 'here']))
    # print(words_order('', ['world', 'here']))
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert words_order('hi world im here', ['world', 'here']) == True
    # assert words_order('hi world im here', ['here', 'world']) == False
    # assert words_order('hi world im here', ['world']) == True
    # assert words_order('hi world im here',
    #                    ['world', 'here', 'hi']) == False
    # assert words_order('hi world im here',
    #                    ['world', 'im', 'here']) == True
    # assert words_order('hi world im here',
    #                    ['world', 'hi', 'here']) == False
    # assert words_order('hi world im here', ['world', 'world']) == False
    # assert words_order('hi world im here',
    #                    ['country', 'world']) == False
    # assert words_order('hi world im here', ['wo', 'rld']) == False
    # assert words_order('', ['world', 'here']) == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")
