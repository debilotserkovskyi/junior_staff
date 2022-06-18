txt = input()

txt_exchanged = txt[-1] + txt[1:len(txt)-1] + txt[0]
print(txt_exchanged)
