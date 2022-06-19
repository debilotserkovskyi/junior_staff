width = int(input())

while True:
    txt = input()
    if txt == 'END':
        break
    if len(txt) % 2 != 0:
        print(('.'*(width//2 - len(txt)//2)) + txt + ('.' * (width//2 - len(txt)//2)))
    elif len(txt) % 2 == 0:
        print(('.' * (width//2 + 1 - len(txt)//2)) + txt + ('.' * (width//2 - len(txt)//2)))

