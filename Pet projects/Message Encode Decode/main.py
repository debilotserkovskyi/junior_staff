from tkinter import *
import base64


# f2
def encode_b64():
    message = message_entry.get()
    key = 'ascii'
    out_en = Label(text=base64.b64encode(message.encode(key)).decode(key))
    out_en.grid(columnspan=3, row=3)
    root.clipboard_clear()
    root.clipboard_append(str(base64.b64encode(message.encode(key)).decode(key)))


def decode_b64():
    message = message_entry.get()
    key = 'ascii'
    out_de = Label(text=base64.b64decode(message.encode(key)).decode(key))
    out_de.grid(columnspan=3, row=5)
    root.clipboard_clear()
    root.clipboard_append(str(base64.b64decode(message.encode(key)).decode(key)))


# f3
def roman_shift():
    new_list = []
    code = ''
    shift: int = int(shift_number.get())
    txt = roman_txt.get()
    if shift == str:
        Label(f3, text='it must be a number').grid(column=5, row=6)
        raise_frame(f3)
    for i in txt:
        if i == ' ':
            new_list.append(' ')
        else:
            new_list.append(chr(ord(i) + shift))
    out = Label(text=''.join(new_list))
    out.grid(columnspan=4, row=7)
    root.clipboard_clear()
    root.clipboard_append(''.join(new_list))
    
        
# main
root = Tk()
# root.geometry('500x300')
root.title('Message Encode and Decode')

# main frame
f1 = Frame(root)
# b64 frame
f2 = Frame(root)
# roman shift frame
f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')


def raise_frame(frame):
    frame.tkraise()


# start screen
Label(f1, text='to decode or encode txt based on ascii').grid(columnspan=4, row=0)
Button(f1, text='go', command=lambda: raise_frame(f2)).grid(columnspan=3, row=1)

Label(f1, text='to decode/encode based on roman shift').grid(columnspan=5, row=2)
Button(f1, text='go', command=lambda: raise_frame(f3)).grid(columnspan=3, row=3)

# f2, based on ascii b45
Label(f2, text='Print your message:').grid(columnspan=3, row=0)

message_entry = Entry(f2)
message_entry.grid(columnspan=3, row=1)

Button(f2, text='decode', command=decode_b64).grid(column=0, row=2)
Button(f2, text='encode', command=encode_b64).grid(column=2, row=2)

Button(f2, text='back', command=lambda: raise_frame(f1)).grid(column=2, row=3)

# f3, based on shift (roman decode)
Label(f3, text='put txt here:').grid(columnspan=3, row=0)
roman_txt = Entry(f3)
roman_txt.grid(columnspan=3, row=1)

Label(f3, text='type the shift number').grid(columnspan=3, row=2)

shift_number = Entry(f3)
shift_number.grid(columnspan=3, row=3)
Button(f3, text='get txt', command=roman_shift).grid(column=2, row=4)

Button(f3, text='back', command=lambda: raise_frame(f1)).grid(column=2, row=5)


raise_frame(f1)
root.mainloop()
