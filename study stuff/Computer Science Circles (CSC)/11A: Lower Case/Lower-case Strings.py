def lowerChar(char: str):
    if ord('A') <= ord(char) <= ord('Z'):
        return chr(ord(char) + 32)
    else:
        return char


def lowerString(string: str):
    lower_str = ''
    for i in string:
        lower_str += lowerChar(i)
    return lower_str
        