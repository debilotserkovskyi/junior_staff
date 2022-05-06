from pprint import pprint

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key, value)
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    #Access row.student or row.score
    pass


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_nato = pandas.read_csv('nato_phonetic_alphabet.csv')

true_list = {raw.letter: raw.code for index, raw in data_nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_name = [true_list[i] for i in input(' ').upper()]
print(nato_name)
