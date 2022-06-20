def postalValidate(s: str):
    s = s.upper().replace(' ', '')
    if len(s) == 6:
        for i in range(len(s)):
            if i % 2 == 0:
                if not s[i].isalpha():
                    return False
            else:
                if not s[i].isdigit():
                    return False
    else:
        return False
    return s
