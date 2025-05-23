from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Dropdown")

dropdown = ttk.Combobox(
    root,
    values=["One", "Two", "Three", "Maybe", "Banana", "?", "123", "None"],
    font=("Comic Sans MS", 8),
    state="normal"
)
dropdown.pack(padx=50, pady=50)

# No default value set, and no action bound

root.mainloop()