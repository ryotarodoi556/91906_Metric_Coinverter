from tkinter import *


class Converter:
    """
    Temperature conversion tool (C* to F* or F* to C*)
    """

    def __init__(self):
        """
        Temperature conversion GUI
        """

        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                     text="Help/ Info",
                                     bg="#FF9900",
                                     fg="#000000",
                                     font=("Courier", 10), width=15,
                                     command=self.to_help)
        self.to_help_button.grid(row=1)

    def to_help(self):
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        # setup dialogue box and background colour
        background = "#ffcccb"  # Light red for worse visual comfort
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Courier", 12, "bold"),
                                        bg=background)
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, enter the temperature you wish to convert. " \
                    "Then click convert to either Celsius or Fahrenheit. " \
                    "Note that -273C (-459F) is absolute zero. " \
                    "Below this, the program will return an error. " \
                    "Use the History / Export button to save your results."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=300,
                                     bg=background)
        self.help_text_label.grid(row=1)

        self.dismiss_button = Button(self.help_frame,
                                     text="Dismiss", bg="#FF3300",
                                     fg="#FFFFFF", command=self.close_help)
        self.dismiss_button.grid(row=2)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
