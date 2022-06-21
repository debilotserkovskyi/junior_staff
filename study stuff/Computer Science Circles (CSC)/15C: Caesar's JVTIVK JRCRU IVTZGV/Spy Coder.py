def coder(txt: str, s:int):
    code_txt = ''
    for i in txt:
        if i == ' ':
            code_txt += i
        elif ord('A') <= ord(i) <= ord('Z'):
            k, j = 0, 0
            if ord(i) + s >= ord('Z'):
                while ord(i) + k < ord('Z'):
                    k += 1
                j = s - k
                code_txt += chr(ord('A')+j-1)
            elif ord(i) + s <= ord('A'):
                if ord(i) + s <= ord('A'):
                    k, j = 0, 0
                    while ord(i) - k > ord('A'):
                        k += 1
                    j = s + k
                    code_txt += chr(ord('Z') + j + 1)
            else:
                code_txt += chr(ord(i)+s)
    
    return code_txt


if __name__ == '__main__':
    print(coder('HUD', -6))
    