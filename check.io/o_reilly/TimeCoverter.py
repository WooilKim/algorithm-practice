# https://py.checkio.org/en/mission/time-converter-12h-to-24h/
# O'REILLY
# Time Converter (12h to 24h)

def time_converter(time):
    if time[-4] == 'p':
        time = time.split()[0]
        if int(time.split(':')[0]) < 12:
            time = f"{12 + int(time.split(':')[0]):02d}:{time.split(':')[1]}"
        return time
    else:
        time = time.split()[0].split(':')
        return f'{int(time[0]):02d}:{time[1]}'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
