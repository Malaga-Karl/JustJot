from tkinter import *

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

# Define a function to get the journal entry
def get_entry(event):
    # Do something when Ctrl+Enter is pressed
    if event.state == 4 and event.keysym == 'Return':
        print("Ctrl+Enter pressed!")
        
# Bind the Ctrl+Enter key combination to the get_entry function
entry_text.bind("<Control-Return>", get_entry)

# Run the main event loop
root.mainloop()