def time_converter(time):
    # replace this for solution
    import time as t

    pref = 'AM' if time.split()[1] == 'a.m.' else 'PM'

    # print(pref)
    # print(f'{time.split()[0]} {pref}')
    st_time = t.strptime(f'{time.split()[0]} {pref}', "%I:%M %p")
    # print(st_time)

    py_time = t.strftime("%R", st_time)
    # print(py_time)

    return py_time


if __name__ == '__main__':
    print("Example:")
    # print(time_converter('12:30 p.m.'))
    # print(time_converter('9:00 a.m.'))
    # print(time_converter('11:15 p.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")