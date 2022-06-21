def coder(txt: str, s: int):
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
                    code_txt += chr(ord('A') + j - 1)
                else:
                    code_txt += chr(ord(i) + s)
    
    return code_txt


letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402,
                  0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015,
                  0.0197, 0.0007]
enc = 'LQKP OG CV GKIJV DA VJG BQQ'.split()
decrypt = []

# generating alphabet
k = ord('a') - 1
letters = ''
while k < ord('z'):
    k += 1
    letters += chr(k).upper()
    
# save relates between letter and frequency
store = {}
for i, j in enumerate(letterGoodness):
    store[letters[i]] = j

# run the program
if __name__ == '__main__':
    print(decrypt)
