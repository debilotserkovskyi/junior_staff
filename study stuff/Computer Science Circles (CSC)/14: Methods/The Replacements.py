def replace(l: list, x, y):
    for i, j in enumerate(l):
        if j == x:
            l.remove(x)
            l.insert(i, y)
    print(l)
