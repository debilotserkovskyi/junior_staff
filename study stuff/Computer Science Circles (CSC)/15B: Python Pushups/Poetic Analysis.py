poem = []
count = 0
store = set()
while True:
    line = input().lower().split()
    if '###' in line:
        break
    
    poem += line
    if len(poem) > 1:
        for i, j in enumerate(poem):
            if poem.count(j) > count:
                count = poem.count(j)
                if count > 1:
                    store.add(j)
    else:
        store.add(line[0])
    
print(list(store)[0])
