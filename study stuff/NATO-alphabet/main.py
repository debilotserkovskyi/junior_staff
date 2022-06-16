import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

list_names = {raw.letter: raw.code for index, raw in data.iterrows()}

done = []
in_put = input().upper()
for i in in_put:
    if i == ' ':
        done.append('\n')
    elif i == '.':
        done.append('dot')
    elif i == '@':
        done.append('at')
    else:
        done.append(list_names[i])

print(' '.join(done))
