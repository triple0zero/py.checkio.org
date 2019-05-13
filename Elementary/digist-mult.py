def checkio(number: int) -> int:

    num = list(str(number))
    result = 1
    for n in num:
        if int(n) != 0:
            result *= int(n)
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    print(checkio(999))
    print(checkio(1000))
    print(checkio(1111))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
