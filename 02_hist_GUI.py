from tkinter import *
from functools import partial
import all_constants as c
from datetime import date

class Converter:
    def __init__(self):
        self.all_calculations_list = ['10.0 °F is -12 °C', '20.0 °F is -7 °C',
                                      '30.0 °F is -1 °C', '40.0 °F is 4 °C',
                                      '50.0 °F is 10 °C', 'This is a test']

        self.temp_frame = Frame(padx=15, pady=15, bg="#f9f9f9")
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Info",
                                        bg="#4a7a8c",
                                        fg="#ffffff",
                                        font=("Arial", 12, "bold"),
                                        width=15,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=10)

    def to_history(self):
        HistoryExport(self, self.all_calculations_list)

class HistoryExport:
    def __init__(self, partner, calculations):
        self.history_box = Toplevel(bg="#f0f0f0")
        partner.to_history_button.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, bg="#f0f0f0", padx=10, pady=10)
        self.history_frame.grid()

        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#e6f0ff"
            calc_amount = "all your"
        else:
            calc_back = "#fff3e0"
            calc_amount = f"your recent calculations - showing {c.MAX_CALCS} / {len(calculations)}"

        recent_intro_txt = f"Below are {calc_amount} calculations (rounded to the nearest degree)."

        newest_first_list = list(reversed(calculations))
        newest_first_string = "\n".join(
            newest_first_list[:c.MAX_CALCS]
            if len(newest_first_list) > c.MAX_CALCS
            else newest_first_list
        )

        export_instruction_txt = ("Click 'Export' to save your calculations to a file. "
                                  "If the filename already exists, it will be overwritten.")

        history_labels_list = [
            ["History / Export", ("Arial", 16, "bold"), "#f0f0f0"],
            [recent_intro_txt, ("Arial", 11), "#f0f0f0"],
            [newest_first_string, ("Arial", 12), calc_back],
            [export_instruction_txt, ("Arial", 10), "#f0f0f0"]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2], wraplength=300,
                               justify="left", anchor="w", padx=10, pady=6)
            make_label.grid(row=count, sticky="w")
            history_label_ref.append(make_label)

        self.export_filename_label = history_label_ref[3]

        self.hist_button_frame = Frame(self.history_box, bg="#f0f0f0")
        self.hist_button_frame.grid(row=4, pady=10)

        button_details_list = [
            ["Export", "#4a7a8c", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#888888", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            button = Button(self.hist_button_frame,
                            font=("Arial", 11),
                            text=btn[0], bg=btn[1], fg="#ffffff",
                            width=12, command=btn[2])
            button.grid(row=btn[3], column=btn[4], padx=8)

    def export_data(self, calculations):
        today = date.today()
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        file_name = f"temperatures_{year}_{month}_{day}"

        success_string = f"Export successful! File: {file_name}.txt"
        self.export_filename_label.config(fg="#2e7d32", text=success_string,
                                          font=("Arial", 10, "italic"))

        with open(f"{file_name}.txt", "w") as text_file:
            text_file.write("***** Temperature Calculations ******\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Calculation history (oldest to newest):\n")
            for item in calculations:
                text_file.write(item + "\n")

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
