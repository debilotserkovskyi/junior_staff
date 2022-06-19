width = int(input())

while True:
    txt = input()
    if txt == 'END':
        break
    dots = '.' * width
    L = len(txt)
    left = ''
    
    if width % 2 != 0:
        if L % 2 == 0:
            left = '.' * ((width-L)//2 + width % 2) + txt[:len(txt)//2]
        else:
            left = '.' * ((width-L)//2) + txt[:len(txt)//2]
    else:
        if L % 2 == 0:
            left = '.' * ((width - L) // 2 + width % 2) + txt[:len(txt) // 2]
        else:
            left = '.' * ((width-L)//2 + 1) + txt[:len(txt)//2]
    right = txt[len(txt)//2:] + '.' * ((width-L)//2)
    print(left+right)
    