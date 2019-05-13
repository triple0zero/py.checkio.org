def checkio(data: str) -> bool:
    import re

    numbers = re.findall(r'\d', data)
    letters_low = re.findall(r'[a-z]', data)
    letters_big = re.findall(r'[A-Z]', data)
    # print(numbers)
    # print(letters_low)
    # print(letters_big)

    return True if len(data) >= 10 and len(numbers) > 0 and len(letters_big) > 0 and len(letters_low) > 0 else False

# Some hints
# Just check all conditions

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
