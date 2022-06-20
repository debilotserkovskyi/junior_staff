def getBASIC():
    store = []
    while True:
        line = input()
        store.append(line)
        if line.endswith('END'):
            break
    return store


def findLine(prog: list, target: str):
    for i in prog:
        if target == i.split()[0]:
            return prog.index(i)


def execute(prog: list):
    viseted = [False] * len(prog)
    location = 0
    while True:
        if prog[location] == prog[-1]:
            return 'success'
        elif viseted[location]:
            return 'infinite loop'
        viseted[location] = True
        target = prog[location].split()
        location = findLine(prog, target[-1])


print(execute(getBASIC()))
