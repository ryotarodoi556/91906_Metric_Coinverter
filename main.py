from tkinter import *
from tkinter import ttk
from functools import partial
from datetime import date

# Conversion constants
CM_TO_INCH = 0.393701
M_TO_FEET = 3.28084
KM_TO_MILES = 0.621371

MAX_CALCS = 5  # Number of calculations to keep in history


def convert_cm_to_inch(value):
    return round(value * CM_TO_INCH, 2)


def convert_m_to_ft(value):
    return round(value * M_TO_FEET, 2)


def convert_km_to_miles(value):
    return round(value * KM_TO_MILES, 2)


class Converter:
    def __init__(self):
        self.all_calculations_list = []

        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        self.heading = Label(self.main_frame, text="Length Converter",
                             font=("Arial", "16", "bold"))
        self.heading.grid(row=0)

        instructions = ("Enter a number, choose a conversion type from the dropdown, "
                        "and click 'Convert'.\n"
                        "• Centimeters to Inches\n"
                        "• Meters to Feet\n"
                        "• Kilometers to Miles")
        self.instructions_label = Label(self.main_frame, text=instructions,
                                        wraplength=300, justify="left")
        self.instructions_label.grid(row=1)

        self.input_entry = Entry(self.main_frame, font=("Arial", "14"))
        self.input_entry.grid(row=2, pady=10)

        self.conversion_var = StringVar()
        self.conversion_dropdown = ttk.Combobox(
            self.main_frame,
            textvariable=self.conversion_var,
            values=["Centimeters to Inches", "Meters to Feet", "Kilometers to Miles"],
            state="readonly",
            font=("Arial", 12)
        )
        self.conversion_dropdown.grid(row=3)
        self.conversion_dropdown.current(0)  # Default selection

        self.convert_button = Button(self.main_frame, text="Convert",
                                     bg="#084C99", fg="white",
                                     font=("Arial", "12", "bold"),
                                     command=self.check_input)
        self.convert_button.grid(row=4, pady=10)

        self.answer_label = Label(self.main_frame, text="",
                                  fg="#084C99", font=("Arial", "14", "bold"))
        self.answer_label.grid(row=5)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=6)

        # Help and History buttons
        self.to_help_button = Button(self.button_frame, text="Help / Info", bg="#cc6600", fg="white",
                                     font=("Arial", "12", "bold"), width=14, command=self.to_help)
        self.to_help_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg="white",
                                        font=("Arial", "12", "bold"), width=14, command=self.to_history, state=DISABLED)
        self.to_history_button.grid(row=0, column=1, padx=5, pady=5)

    def check_input(self):
        user_input = self.input_entry.get()
        conversion_type = self.conversion_var.get()
        self.answer_label.config(fg="#084C99")
        self.input_entry.config(bg="white")

        if len(user_input.replace('.', '', 1)) > 7:
            self.answer_label.config(text="Input too long (max 7 digits)",
                                     fg="#9C0000")
            self.input_entry.config(bg="#F4CCCC")
            return

        try:
            value = float(user_input)
            self.convert(conversion_type, value)
        except ValueError:
            self.answer_label.config(text="Please enter a valid number",
                                     fg="#9C0000")
            self.input_entry.config(bg="#F4CCCC")

    def convert(self, conversion_type, value):
        if conversion_type == "Centimeters to Inches":
            result = convert_cm_to_inch(value)
            text = f"{value} cm = {result} inches"
        elif conversion_type == "Meters to Feet":
            result = convert_m_to_ft(value)
            text = f"{value} m = {result} feet"
        elif conversion_type == "Kilometers to Miles":
            result = convert_km_to_miles(value)
            text = f"{value} km = {result} miles"
        else:
            text = "Invalid conversion type."

        self.answer_label.config(text=text)
        self.all_calculations_list.append(text)
        self.to_history_button.config(state=NORMAL)

    def to_help(self):
        DisplayHelp(self)

    def to_history(self):
        HistoryExport(self, self.all_calculations_list)


class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()
        partner.to_help_button.config(state=DISABLED)
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        Label(self.help_frame, text="Help / Info",
              font=("Arial", "14", "bold"), bg=background).grid(row=0)

        help_text = ("Enter a number, choose the type of length conversion from the dropdown, "
                     "then click 'Convert'. You can view recent conversions or export them as a text file.")
        Label(self.help_frame, text=help_text, wraplength=350,
              justify="left", bg=background).grid(row=1, padx=10)

        Button(self.help_frame, text="Dismiss", bg="#cc6600", fg="white",
               font=("Arial", "12", "bold"),
               command=partial(self.close_help, partner)).grid(row=2, pady=10)

    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


class HistoryExport:
    def __init__(self, partner, calculations):
        self.history_box = Toplevel()
        partner.to_history_button.config(state=DISABLED)
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        calc_back = "#D5E8D4" if len(calculations) <= MAX_CALCS else "#ffe6cc"
        calc_amount = "all your" if len(calculations) <= MAX_CALCS else f"your recent {MAX_CALCS} of {len(calculations)}"

        recent_intro_txt = f"Below are {calc_amount} conversions."

        newest_first = list(reversed(calculations))[:MAX_CALCS]
        calc_text = "\n".join(newest_first)

        export_text = "Click <Export> to save your conversions to a file."

        label_details = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            [calc_text, ("Arial", "14"), calc_back],
            [export_text, ("Arial", "11"), None],
        ]

        self.export_filename_label = None

        for idx, item in enumerate(label_details):
            lbl = Label(self.history_frame, text=item[0], font=item[1],
                        wraplength=300, justify="left", bg=item[2])
            lbl.grid(row=idx, sticky="w", padx=20, pady=5)
            if idx == 3:
                self.export_filename_label = lbl

        self.button_frame = Frame(self.history_box)
        self.button_frame.grid(row=4)

        Button(self.button_frame, text="Export", bg="#004C99", fg="white",
               font=("Arial", "12", "bold"), width=12,
               command=lambda: self.export_data(calculations)).grid(row=0, column=0, padx=10, pady=10)

        Button(self.button_frame, text="Close", bg="#666666", fg="white",
               font=("Arial", "12", "bold"), width=12,
               command=partial(self.close_history, partner)).grid(row=0, column=1, padx=10, pady=10)

    def export_data(self, calculations):
        today = date.today()
        file_name = f"length_conversions_{today.strftime('%Y_%m_%d')}.txt"

        with open(file_name, "w") as file:
            file.write("**** Length Conversions ****\n")
            file.write(f"Date: {today.strftime('%d/%m/%Y')}\n\n")
            file.write("Oldest to newest:\n")
            for item in calculations:
                file.write(item + "\n")

        self.export_filename_label.config(text=f"Exported to {file_name}!",
                                          bg="#009900", fg="white",
                                          font=("Arial", "12", "bold"))

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Length Converter")
    Converter()
    root.mainloop()
