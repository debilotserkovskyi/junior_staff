import random
from data import data, stages

chosen_word = random.choice(data)

display = []
game = True
lives = 6

for i in range(len(chosen_word)):
    display.append('_')

while game:
    print(display)
    guess = input('guess the letter\n').lower()
    if guess in display:
        print('you already wrote this letter!')
    if guess in chosen_word:
        print('Right')
    else:
        lives -= 1
        print('letter {} not in the word'.format(guess))
        print(stages[lives])
    
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            
    if "_" not in display:
        print('GREAT, you won')
        game = False
    
    if lives == 0:
        print('you lose')
        game = False

