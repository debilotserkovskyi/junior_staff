# given value
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

# initialization value, good list and shift to 0, we will store everything here
values = []
words_list = []
shifts = 0


def decoder(txt: str, s: int = 1):
    """
    decode or encode a string depends on given str and shift
    s = 1 because of the task
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
    return main(new_txt)


def main(coded_text: str) -> float:
    """
    do all the work that need in this task
    :param coded_text: given coded text - str
    :return: biggest number - float
    """

    global shifts, words_list
    goodness_value, position = 0, 0
    list_ = [p for p in coded_text]
    for char in list_:
        if position == len(list_)-1:
            goodness_value += store[char]
            values.append(goodness_value)
            words_list.append(''.join(list_))
            shifts += 1
            if shifts == 27:
                return words_list[values.index(final_calc(words_list))]
            else:
                return decoder(''.join(list_))
        elif char == ' ':
            position += 1
            continue
        else:
            goodness_value += store[char]
            position += 1


def final_calc(words: list) -> float:
    """
    I can't understand why not .max() :(
    :param words: list of all possible combination of letters
    :return: biggest number
    """
    biggest_value, position = 0.0, 0
    while position < len(words):
        for value in values:
            if float(value) > float(biggest_value):
                biggest_value = float(value)
                position += 1
        return biggest_value


if __name__ == '__main__':
    print(main(input()))
