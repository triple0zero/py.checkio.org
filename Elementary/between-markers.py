def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    start = text.find(begin)
    stop = text.find(end)

    if start == -1 and stop == -1:
        return text

    if stop == -1:
        stop = len(text)

    if start == -1:
        return text[0:stop]

    if start > stop:
        return ''

    return text[start+len(begin):stop]


if __name__ == '__main__':
    # print('Example:')
    # print(between_markers('What is >apple<123', '>', '<'))
    # print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))
    # print(between_markers('No[/b] hi', '[b]', '[/b]'))
    # print(between_markers('No [b]hi', '[b]', '[/b]'))
    # print(between_markers('No hi', '[b]', '[/b]'))
    # print(between_markers('No <hi>', '>', '<'))


    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
