S = '731+2212'

# print(eval(S))

for i, j in enumerate(S):
    if j == '+':
        print(int(S[:i]) + int(S[i:]))