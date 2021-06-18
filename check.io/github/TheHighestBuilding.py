# https://py.checkio.org/en/mission/the-highest-building/
# Github
# The Highest Building

def highest_building(buildings):
    answer = [[i + 1, 0] for i in range(len(buildings[0]))]
    for j in range(len(buildings))[::-1]:
        for i in range(len(buildings[0])):
            if buildings[j][i] == 1 and answer[i][1] == len(buildings) - (j + 1):
                answer[i][1] += 1
    return sorted(answer, key=lambda x: -abs(x[1]))[0]
