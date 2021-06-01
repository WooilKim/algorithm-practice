# https://py.checkio.org/en/mission/the-highest-building/
# The Highest Building

def highest_building(buildings):
    answer = [[i + 1, 0] for i in range(len(buildings[0]))]
    for j in range(len(buildings))[::-1]:
        for i in range(len(buildings[0])):
            if buildings[j][i] == 1 and answer[i][1] == len(buildings) - (j + 1):
                answer[i][1] += 1
    return sorted(answer, key=lambda x: -abs(x[1]))[0]


if __name__ == '__main__':
    print("Example:")
    print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == [3, 4], "Common"
    assert highest_building([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]) == [4, 1], "Cabin in the wood"
    assert highest_building([
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]) == [1, 5], "Triangle"
    assert highest_building([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]) == [4, 6], "Pyramid"
    print("Coding complete? Click 'Check' to earn cool rewards!")
