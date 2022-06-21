letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402,
                  0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015,
                  0.0197, 0.0007]
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


def decoder(txt: str, s: int):
    new_txt = ''
    for index, char in enumerate(txt):
        if char == ' ':
            new_txt += ' '
        else:
            position = letters.find(char)
            new_char = letters[(position + s) % 26]
            new_txt += new_char
    return new_txt


def try_to_decode(message):
    shift = 0
    chance_store = [store[i] for i in message]
    while shift != 18:
        word_chance_sum = 0
        message = decoder(message, shift)
        shift += 1
        for index, char in enumerate(message):
            word_chance_sum += store[char]
            chance_store.append(store[char])
    print(word_chance_sum, sum(chance_store))
    print(message, shift)


# run the program
if __name__ == '__main__':
    print(try_to_decode('JRRG'))
    