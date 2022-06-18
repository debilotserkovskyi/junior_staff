char = input()

if char == 'Z':
    char = 'A'
else:
    char = chr(ord(char) + 1)

print(char)
