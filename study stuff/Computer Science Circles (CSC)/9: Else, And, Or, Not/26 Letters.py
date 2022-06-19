letter = input()

# if 65 < ord(letter) < 90:
#     print('letter', letter, 'in the alphabet:', ord(letter)-64)
# else:
#     print('invalid input', letter)

if 65 < ord(letter) < 90:
    print(ord(letter)-64)
else:
    print('invalid')
    