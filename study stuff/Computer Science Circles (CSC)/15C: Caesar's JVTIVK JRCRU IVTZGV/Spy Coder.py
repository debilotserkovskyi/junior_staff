def coder(txt: str, s:int):
    code_txt = ''
    if s > 0:
        for i in txt:
            if i == ' ':
                code_txt += i
            elif ord('A') <= ord(i) <= ord('Z'):
                if ord(i) + s >= ord('Z'):
                    k, j = 0, 0
                    while ord(i) + k < ord('Z'):
                        k += 1
                    j = s - k
                    code_txt += chr(ord('A')+j-1)
                else:
                    code_txt += chr(ord(i)+s)
    elif s < 0:
        for i in txt:
            if i == ' ':
                code_txt += i
            elif ord('A') <= ord(i) <= ord('Z'):
                if ord(i) + s <= ord('A'):
                    k, j = 0, 0
                    while ord(i) - k > ord('A'):
                        k += 1
                    j = s + k
                    code_txt += chr(ord('Z') + j + 1)
                else:
                    code_txt += chr(ord(i)+s)
    else:
        return txt
    
    return code_txt


if __name__ == '__main__':
    print(coder('HUD', -6))
    