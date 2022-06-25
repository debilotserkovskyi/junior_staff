def nestedListContains(NL, target):
    if isinstance(NL, int):
        if NL == target:
            return True
    else:
        counter = 0
        while counter <= len(NL)-1:
            if nestedListContains(NL[counter], target):
                return True
            counter += 1
        return False
