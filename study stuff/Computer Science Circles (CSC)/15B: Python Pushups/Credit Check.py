def check(s: str):
    if_sum = 0
    for i in s:
        if i.isalpha():
            return False
        if i != ' ':
            if_sum += int(i)
    if if_sum % 10 == 0 and if_sum != 0:
        return True
    else:
        return False
        
