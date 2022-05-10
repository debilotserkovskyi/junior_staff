from tkinter import *
import random

score_u = 0
score_c = 0
yellow = "#f7f5dd"


def game():
    global user_choise, score_u, score_c
    comp_choise = random.choice([1, 2, 3])
    if comp_choise == 1:
        comp_choise = 'paper'
        emo_c = '✋'
    elif comp_choise == 2:
        comp_choise = 'rock'
        emo_c = '🤜'
    else:
        comp_choise = 'scissors'
        emo_c = '✌️'
        
    if user_choise == comp_choise:
        # same.config(text='you droped the same', bg=yellow)
        pass
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
    print(score_c, score_u)
    score_comp.config(text=f'comp: {score_c}')
    score_user.config(text=f'user: {score_u}')
    emo = ''
    if user_choise == 'paper':
        emo = '✋'
    elif user_choise == 'rock':
        emo = '🤜'
    elif user_choise == 'scissors':
        emo = '✌️'
    drop.config(text=f'u drop {emo}\ncomp drop {emo_c}')
    
    
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

Label(text='chose what you want to drop', bg=yellow).grid(columnspan=3, row=0)

rock_b = Button(text='rock', command=rock)
rock_b.grid(column=0, row=1)

paper_b = Button(text='paper', command=paper)
paper_b.grid(column=1, row=1)

scissors_b = Button(text='scissors', command=scissors)
scissors_b.grid(column=2, row=1)

Label(text='SCORE:', bg=yellow).grid(columnspan=3, row=3)
score_user = Label(text=f'user: {score_u}', bg=yellow)
score_user.grid(column=0, row=4)
score_comp = Label(text=f'comp: {score_c}', bg=yellow)
score_comp.grid(column=2, row=4)

drop = Label(bg=yellow)
drop.grid(columnspan=3, row=5)

same = Label(bg=yellow)
same.grid(columnspan=3, row=6)

window.mainloop()
