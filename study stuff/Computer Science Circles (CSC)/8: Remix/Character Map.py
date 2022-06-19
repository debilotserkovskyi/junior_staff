x = ord(' ')
for j in range(6):
    print('chr:  ', end='')
    for i in range(x, x+16):
        print(chr(i), end='   ')
    print()
    print('asc: ', end='')
    for i in range(x, x+16):
        if i >= 100:
            print(ord((chr(i))), end=' ')
        else:
            print(str(i) + ' ', end=' ')
    print()
    x += 16
    