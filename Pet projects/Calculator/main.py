from tkinter import *
from math import factorial

root = Tk()
root.title('Calc')


buttons = [
    'AC', '+/-', '%', '/',
    '7', '8', '9', 'x',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    "0", ",", "="
]

row = 1
col = 0

display = Entry()
display.grid(row=0, columnspan=3, sticky=N+E+W+S)

for i in buttons:
    action = lambda x = i: click_event(x)
    Button(root, text=i, relief='raised', command=action).grid(row=row, column=col, sticky='nesw', )
    col += 1
    if col == 4:
        col = 0
        row += 1


def click_event(key):
    pass


root.mainloop()
