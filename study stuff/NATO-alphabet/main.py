import pandas



# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_nato = pandas.read_csv('nato_phonetic_alphabet.csv')

true_list = {raw.letter: raw.code for index, raw in data_nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_name = [true_list[i] for i in input(' ').upper()]
print(nato_name)
