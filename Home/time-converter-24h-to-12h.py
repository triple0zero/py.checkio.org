def time_converter(time):
    #replace this for solution
    import time as t

    py_tup_time = t.strptime(time, "%H:%M")

    pref = 'a.m.' if py_tup_time[3] < 12 else 'p.m.'
    if py_tup_time[3] == 0 and py_tup_time[4] == 0:
        return '12:00 a.m.'
    hours = py_tup_time[3] if int(py_tup_time[3]) < 13 else int(py_tup_time[3]) - 12
    # minutes = '00' if py_tup_time[4] == 0 else py_tup_time[4]

    if py_tup_time[4] == 0:
        minutes = '00'
    elif py_tup_time[4] < 10:
        minutes = f'0{py_tup_time[4]}'
    else:
        minutes = py_tup_time[4]

    return f'{hours}:{minutes} {pref}'


if __name__ == '__main__':
    print("Example:")
    # print(time_converter('12:30'))
    # print(time_converter('09:00'))
    # print(time_converter('23:15'))
    # print(time_converter('07:07'))
    print(time_converter('00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
