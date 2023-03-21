import datetime
from tkinter import *
from docx import Document
    
# Create the main window
root = Tk()

# Set the window title
root.title("JustJot")

# Set the window size
root.geometry("500x700")

# Create a label for the title
title_label = Label(root, text="JustJot", font=("Helvetica", 20))
title_label.pack(pady=20)

# Create a label for the journal entry
entry_label = Label(root, text="Title (optional):", font=("Helvetica", 12), anchor='w')
entry_label.pack(padx=20, pady=10)

# Create a text box for the title
title_text = Entry(root, width=60, font=("Helvetica", 14))
title_text.pack(padx=20, pady=10)

# Create a text box for the journal entry
entry_text = Text(root, width=60, height=25, font=("Helvetica", 14), wrap=WORD)
entry_text.pack(padx=20, pady=10)

# Add a scrollbar to the text box
scrollbar = Scrollbar(root, command=entry_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
entry_text.config(yscrollcommand=scrollbar.set)

# Set the scrollbar to fill the y-axis of the window
scrollbar.pack(side=RIGHT, fill=Y)

#documents
journal = Document()
file_name = str(datetime.date.today().year) + 'Jots.docx'
file_path = 'E:\\' + file_name

def on_key_press(event):
    if event.keysym == 'Return':
        if event.state == 12:
            value=entry_text.get("1.0",END)
            if title_text.get() != '':
                print(title_text.get())
            else:
                print('no title')
            entry_text.delete('1.0', END)
            print(value)

root.bind("<Control-KeyPress>", on_key_press)
title_text.focus_set()

journal.save(file_path)

# Run the main event loop
root.mainloop()

