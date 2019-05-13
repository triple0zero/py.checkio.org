def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    array = text.split(" ")
    array[0] = array[0].capitalize()
    result = ""
    for a in array:
        result += a + " "
    result = result.rstrip()
    if result.endswith("."):
        pass
    else:
        result += "."
    return result


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("welcome to New York"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
