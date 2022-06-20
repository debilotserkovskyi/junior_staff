def check(s: str):
    if_sum = 0
    s = s.replace(' ', '')
    if len(s) == 16 and s[:3] != s[4:7]:
        for i in s:
            if i.isalpha():
                return False
            if_sum += int(i)
        if if_sum % 10 == 0 and if_sum != 0:
            return True
        else:
            return False
    else:
        return False

