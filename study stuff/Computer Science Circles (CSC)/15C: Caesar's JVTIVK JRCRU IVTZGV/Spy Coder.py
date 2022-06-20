def coder(txt: str, s:int):
    code_txt = ''
    for i in txt:
        if i == ' ':
            code_txt += i
        elif ord(i) == ord('Z'):
            i = 'A'
        elif ord('A') <= ord(i) <= ord('Z'):
            if ord(i) + s >= ord('Z'):
                k = ord(i) + 1 == ord('A')
                code_txt += chr(ord(i)+s)
            else:
                code_txt += chr(ord(i)+s)
        print(code_txt)
    return code_txt


if __name__ == '__main__':
    print(coder('LQKP OG CV GKIJV DA VJG BQQ', -2))
    