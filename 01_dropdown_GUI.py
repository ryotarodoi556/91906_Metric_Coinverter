from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Dropdown Example")

main_frame = Frame(root, padx=10, pady=10)
main_frame.grid()

conversion_var = StringVar()
conversion_dropdown = ttk.Combobox(
    main_frame,
    textvariable=conversion_var,
    values=["Centimeters to Inches", "Meters to Feet", "Kilometers to Miles"],
    state="readonly",
    font=("Arial", 12)
)
conversion_dropdown.grid(row=0, pady=10)
conversion_dropdown.current(0)  # Default selection

root.mainloop()
