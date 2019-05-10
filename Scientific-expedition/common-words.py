def checkio(first, second):
    first_list = first.split(',')
    second_list = second.split(',')
    result = []

    for fl in first_list:
        if second_list.count(fl) > 0:
            result.append(fl)
    print(result)
    result.sort()
    print(result)
    print(','.join(result))

    return ','.join(result)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
