import datetime
from tkinter import *
from docx import Document

def on_key_press(event):
    if event.keysym == 'Return':
        if event.state == 0x4:
            print("Ctrl+Enter pressed")
            get_entry()
        else:
            print(f"Key '{event.char}' ({event.keycode}) pressed")

def get_entry():
    print('hello')

root = Tk()
root.mainloop

# ...

root.bind("<Control-KeyPress>", on_key_press)
root.focus_set()