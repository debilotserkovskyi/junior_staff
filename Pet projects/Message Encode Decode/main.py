from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.title('Message Encode and Decode')
clip_text = root.clipboard_get()


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


Label(text='Print your message:').grid(columnspan=3, row=0)
message_entry = Entry()
message_entry.grid(columnspan=3, row=1)

Button(text='decode', command=decode_b64).grid(column=0, row=2)
Button(text='encode', command=encode_b64).grid(column=2, row=2)


root.mainloop()
