def getBASIC():
    store = []
    while True:
        line = input()
        store.append(line)
        if line.endswith('END'):
            break
    return store
