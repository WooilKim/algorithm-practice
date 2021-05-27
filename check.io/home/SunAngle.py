# https://py.checkio.org/en/mission/sun-angle/

def sun_angle(time):
    h, m = map(int, time.split(':'))
    answer = (h - 6) * 15 + m * 1 / 4
    return answer if 0 <= answer <= 180 else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
