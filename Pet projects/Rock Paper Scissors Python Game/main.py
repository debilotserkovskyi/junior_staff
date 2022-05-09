from tkinter import *
import random

score_u = 0
score_c = 0


def game():
    global user_choise, score_u, score_c
    comp_choise = random.choice([1, 2, 3])
    if comp_choise == 1:
        comp_choise = 'paper'
    elif comp_choise == 2:
        comp_choise = 'rock'
    else:
        comp_choise = 'scissors'
    if user_choise == comp_choise:
        print('you have chose the same ')
    elif user_choise == 'paper' and comp_choise == 'rock':
        score_u += 1
    elif user_choise == 'paper' and comp_choise == 'scissors':
        score_c += 1
    elif user_choise == 'scissors' and comp_choise == 'rock':
        score_c += 1
    elif user_choise == 'scissors' and comp_choise == 'paper':
        score_u += 1
    elif user_choise == 'rock' and comp_choise == 'paper':
        score_c += 1
    elif user_choise == 'rock' and comp_choise == 'scissors':
        score_u += 1
    print(user_choise, comp_choise)
    score_comp.update()
    score_user.update()
    
    
def rock():
    global user_choise
    user_choise = 'rock'
    game()


def paper():
    global user_choise
    user_choise = 'paper'
    game()


def scissors():
    global user_choise
    user_choise = 'scissors'
    game()


window = Tk()
window.title('R P S')
window.config(padx=20, pady=20, bg="#f7f5dd")

canvas = Canvas(width=500, height=600, bg="#f7f5dd", highlightthickness=0)

Label(text='chose what you want to drop').pack()

rock_b = Button(text='rock', command=rock)
rock_b.pack()

paper_b = Button(text='paper', command=paper)
paper_b.pack(after=rock_b)

scissors_b = Button(text='scissors', command=scissors)
scissors_b.pack()

score_user = Label(text=score_u)
score_user.pack()
score_comp = Label(text=score_c)
score_comp.pack()


window.mainloop()
