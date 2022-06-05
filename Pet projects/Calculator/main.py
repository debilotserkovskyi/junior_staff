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
    if key == "AC":
        display.delete(0, END)
    elif key == "=":
        for i in display.get().split('+'):
            display.delete(0, END)
            i = int(i)
            num.append(i)
        print(sum(num))
    else:
        display.insert(0, key)
    

root.mainloop()
