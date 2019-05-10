VOWELS = "aeiouy"


def translate(phrase):
    result = []
    words = phrase.split()

    for word in words:
        ww = list(word)
        for n, letter in enumerate(ww):
            if letter in VOWELS:
                if letter == ww[n+1] and letter == ww[n+2]:
                    result.append(letter)
                    for i in range(2):
                        ww.remove(ww[n + 1])
            else:
                result.append(letter)
                ww.remove(ww[n+1])
        result.append(' ')

    return ''.join(result).rstrip(' ')


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))
    print(translate("aaa bo cy da eee fe"))
    print(translate("sooooso aaaaaaaaa"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
