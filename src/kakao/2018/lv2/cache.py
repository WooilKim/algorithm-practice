# https://programmers.co.kr/learn/courses/30/lessons/17680

import json


def solution(cacheSize, cities):
    cache = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in [''.join(city.strip().split()).lower() for city in cities]:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
    return answer


def test():
    inputs = [[3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]], \
              [3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]], \
              [2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]], \
              [5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]], [2, ["Jeju", "Pangyo", "NewYork", "newyork"]], [0,
                                                                          ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]]
    for inp in inputs:
        print(solution(inp[0], inp[1]))


if __name__ == '__main__':
    test()
    # cachesize = input()
    # cities = json.loads(input())
    #
    # answer = solution(cachesize, cities)
