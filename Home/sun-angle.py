def sun_angle(time):
    import time as t

    py_tup_time = t.strptime(time, "%H:%M")
    ct_minute = py_tup_time[3]*60 + py_tup_time[4]
    angle = ct_minute*0.25 - 90

    return angle if 0 <= angle <= 180 else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("12:00"))
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
