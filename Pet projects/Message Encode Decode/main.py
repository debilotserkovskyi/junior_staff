from tkinter import *
import base64

window = Tk()
window.geometry('500x300')
window.title('Message Encode and Decode')


def encode(key, message):
    enc = []
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i] + ord(key_c))) % 256))
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode()


def decode(key, message):
    dec = []
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((ord(message[i] - ord(key_c))) % 256))
    return ''.join(dec)



window.mainloop()
