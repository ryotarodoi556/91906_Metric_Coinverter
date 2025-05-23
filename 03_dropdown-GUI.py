from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Length Conversion Selector")


conversion_var = StringVar()


conversion_dropdown = ttk.Combobox(
    textvariable=conversion_var,
    values=["Centimeters to Inches", "Meters to Feet", 100],  # Mixed types
    state="readonly"
)
conversion_dropdown.current("zero")
conversion_dropdown.bind("<<ComboboxSelected>>")

# root.mainloop()