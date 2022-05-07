import random
import time

print('Welcome!')
name = input('enter your name:')
print('good luck, {}'.format(name))
time.sleep(1)
print('The game is about to start')


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



