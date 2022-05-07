import random
import time
from data import data, stages

# print('Welcome!')
# name = input('enter your name:')
# print('good luck, {}'.format(name))
# time.sleep(1)
# print('The game is about to start')

# step 1
# TODO 1 -- randomly choose a word from the world_list and assign it to variable called chosen_word.
chosen_word = random.choice(data)
print(chosen_word)
# TODO 2 -- Ask the user to guess a letter and assign their answer to a var called guess. Make guess lowercase.
guess = input('guess the letter\n').lower()
# TODO 3 - Check if the letter the user guessed is one of the letters in the chosen_word.
if guess in chosen_word:
    print('Right')
else:
    print('Wrong')
# Step 2
# TODO-1: - Create an empty List called display.
#  For each letter in the chosen_word, add a "_" to 'display'.
#  So if the chosen_word was "apple", display should be
#  ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in chosen_word:
    display.append('_')
print(display)
# TODO-2: - Loop through each position in the chosen_word;
#  If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#  e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
if guess in chosen_word:
    display.insert()
        
print(display)
# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other
#  letter replace with "_".
#  Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Step 3
# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all
#  the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# Step 4
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.

# TODO-2: - If guess is not a letter in the chosen_word,
#  Then reduce 'lives' by 1.
#  If lives goes down to 0 then the game should stop and it should print "You lose."

# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives'

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    count = 0
    word = random.choice(words_to_guess)
    length = len(word)
    display = "_" * length
    already_guessed = []
    play_game = []
    
    
def play_loop():
    global play_game
    play_game = input('Do you want to play? y/n \n').lower()
    while play_game not in ['y','n']:
        if play_game == 'y':
            main()
        elif play_game == 'n':
            print('see you then')
            exit()
            
            
def hangman():
    global count, display, word, already_guessed



