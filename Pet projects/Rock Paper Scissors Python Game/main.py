from tkinter import *
import random

def game():
    comp_choise = random.choice([1,2,3])
    if comp_choise == 1:
        comp_choise = 'paper'
    elif comp_choise == 2:
        comp_choise = 'rock'
    else:
        comp_choise = 'scissors'
    user_choise = 'paper'
    if user_choise == comp_choise:
        print('you have chose the same ')
    elif user_choise == 'paper' and comp_choise == 'rock':
        print('user win')
    elif user_choise == 'paper' and comp_choise == 'scissors':
        print('com win')
    elif user_choise == 'scissors' and comp_choise == 'rock':
        print('you lose')
    elif user_choise == 'scissors' and comp_choise == 'paper':
        print('you win')
    elif user_choise == 'rock' and comp_choise == 'paper':
        print('you lose')
    elif user_choise == 'rock' and comp_choise == 'scissors':
        print('you win')


window = Tk()
window.title('R P S')
window.config(padx=20, pady=20, bg="#f7f5dd")

canvas = Canvas(width=500, height=600, bg="#f7f5dd", highlightthickness=0)

Label(text='chose what you want to drop')

rock_b = Button(text='rock', command='rock')
rock_b.grid(column=0, row=1)

paper_b = Button(text='paper', command='paper')
paper_b.grid(column=1, row=1)

scissors_b = Button(text='scissors', command='scissors')
scissors_b.grid(column=2, row=1)

window.mainloop()
