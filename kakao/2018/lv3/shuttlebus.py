import json


# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable
def solution(n, t, m, timetable):
    answer = -1
    crews = list()
    for time in timetable:
        crews.append(int(time.split(":")[0]) * 60 + int(time.split(":")[1]))
    crews = sorted(crews)
    print(crews)
    first = crews[0] - 1
    buses = [540 + i * t for i in range(n)]
    rides = list()

    for bus in buses:

        i = 0
        for crew in crews:
            if crew > bus:
                break
            i += 1
            if i == m:
                break

        if i == m:
            answer = crews[i-1] - 1
        else:
            answer = bus
        crews = crews[i:]

    #
    # if rides[-1] < m:
    #     try:
    #         answer = buses[-1]
    #     except TypeError as e:
    #         print(e)
    # elif rides[-1] == m:
    #     answer = first - 1
    # else:
    #     pass
    # # print(buses)
    # # print(crews)
    # #
    # # print(buses)
    # # print(rides)
    # # answer = -1
    # # for i_reversed, ride in enumerate(rides[::-1]):
    # #     if ride < m:
    # #         answer = f'{buses[::-1][i_reversed] // 60:02d}:{buses[::-1][i_reversed] % 60:02d}'
    # #         break
    # # if answer == -1:
    # #     answer = f'{(first - 1) // 60:02d}:{(first - 1) % 60:02d}'
    return f'{answer // 60:02d}:{answer % 60:02d}'


def test():
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60, 45,
                   ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                    "23:59", "23:59", "23:59", "23:59", "23:59"]))


if __name__ == '__main__':
    test()
    solution(input(), input(), input(), json.loads(input()))
    pass
