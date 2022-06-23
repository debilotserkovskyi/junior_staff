# given values
letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402,
                  0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015,
                  0.0197, 0.0007]

# generating alphabet
k = ord('a') - 1
letters = ''
while k < ord('z'):
    k += 1
    letters += chr(k).upper()

# relations between letter and letter goodness
store = {}
for i, j in enumerate(letterGoodness):
    store[letters[i]] = j

# set value, good list and shift to 0
value = []
words_list = []
shifts = 0


def decoder(txt: str, s: int):
    """
    decode or encode a string depends on given str and shift
    :param txt: str
    :param s: int
    :return: encoded or decoded str
    """
    new_txt = ''
    for char in txt:
        if char == ' ':
            new_txt += ' '
        else:
            position = letters.find(char)
            new_char = letters[(position + s) % 26]
            new_txt += new_char
    return new_txt


def main(txt: str):
    return words_list[value.index(txt_goodness([x for x in txt]))]
    
    
def txt_goodness(txt_list: list):
    global value, words_list, shifts, store
    goodness_value = 0
    position = 0
    for char in txt_list:
        if position == len(txt_list)-1:
            goodness_value += store[char]
            value.append(goodness_value)
            nex_txt = ''.join(txt_list)
            words_list.append(nex_txt)
            shifts += 1
            if shifts == 27:
                comp_values()
            else:
                shift_by_one(nex_txt)
        elif char == ' ':
            position += 1
            continue
        else:
            goodness_value += store[char]
            position += 1
    
    
def shift_by_one(new_txt: str):
    shift = 1
    while True:
        position = 0
        next_word = []
        for char in new_txt:
            if char == len(new_txt)-1:
                next_word.append(decoder(char, shift))
                return txt_goodness(next_word)
            elif char == ' ':
                next_word.append(' ')
                position += 1
            else:
                next_word.append(decoder(char, shift))
                position += 1


def comp_values():
    summarize = 0
    position = 0
    while position < len(value):
        for val in value:
            if val > summarize:
                summarize = val
                position += 1
        return summarize

if __name__ == '__main__':
    main('LQKP OG')
    