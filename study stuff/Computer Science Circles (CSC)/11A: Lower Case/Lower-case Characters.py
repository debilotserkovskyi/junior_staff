def lowerChar(char: str):
    if ord('A') <= ord(char) <= ord('Z'):
        return chr(ord(char) + 32)
    else:
        return char
