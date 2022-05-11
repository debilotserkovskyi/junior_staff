from tkinter import *
import base64

window = Tk()
window.geometry('500x300')
window.title('Message Encode and Decode')


def encode_b64(key, message):
    return base64.b64encode(message.encode(key)).decode(key)


def decode_b64(key, message):
    return base64.b64decode(message.encode(key)).decode(key)


print(decode_b64('ascii', 'cHl0aG9uIGlzIGZ1bg=='))
# window.mainloop()
