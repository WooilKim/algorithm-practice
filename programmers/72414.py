# https://programmers.co.kr/learn/courses/30/lessons/72414

def parse_time(s):
    s = list(map(int, s.split(':')))
    return s[0] * 60 * 60 + s[1] * 60 + s[2]


def restore_time(n):
    return f'{n // 3600:02d}:{(n % 3600) // 60:02d}:{n % 60:02d}'


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return restore_time(0)
    arr = [0] * parse_time('100:00:00')
    for log in logs:
        log = log.split('-')
        s, e = parse_time(log[0]), parse_time(log[1])
        arr[s] += 1
        arr[e] -= 1
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]

    pt, at = parse_time(play_time), parse_time(adv_time)
    ts = arr[at]
    for st in range(pt):
        end = arr[st + at + 1] - arr[st] if st + at < pt else pt
        ts = max(ts, arr[end] - arr[st])
    # window_sum = [arr[i + at] - arr[i] for i in range(pt - at)]
    # ts = window_sum.index(max(window_sum))

    return restore_time(ts)


if __name__ == '__main__':
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]), "01:30:59")
    print(solution("99:59:59", "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
    print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")
