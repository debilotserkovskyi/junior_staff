def findLine(prog: list, target:str):
    for i in prog:
        if target == i.split()[0]:
            return prog.index(i)
