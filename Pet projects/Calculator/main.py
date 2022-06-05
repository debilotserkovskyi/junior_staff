from tkinter import *
from math import factorial

root = Tk()
root.title('Calc')


buttons = [
    'AC', '+/-', '%', '/',
    '7', '8', '9', 'x',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    "0", ",", "=", '(', ')'
]

row = 1
col = 0

display = Entry()
display.grid(row=0, columnspan=5, sticky=N+E+W+S)

for i in buttons:
    action = lambda x = i: click_event(x)
    Button(root, text=i, relief='raised', command=action).grid(row=row, column=col, sticky='nesw', )
    col += 1
    if col == 4:
        col = 0
        row += 1


def click_event(key):
    num = []
    equation = display.get()
    if key == "AC":
        display.delete(0, END)
    elif key == "=":
        for j in equation:
            # TODO need to read all str and check it
            #  if there is a "+" symbol >> do sum and replace it in str and etc
            if '+' in equation:
                print(sum([int(equation[equation.index('+')-1]), int(equation[equation.index('+')+1])]))
    else:
        display.insert(END, key)
    

root.mainloop()
