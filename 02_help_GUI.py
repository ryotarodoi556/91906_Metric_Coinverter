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
        self.temp_frame.grid(padx=10, pady=10)

        self.to_help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#FF9900",
                                     fg="#000000",
                                     font=("Courier", 10),
                                     width=15,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, pady=10)

    def to_help(self):
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        # Setup help window
        background = "#fce5cd"  # Softer peach tone for better comfort
        self.help_box = Toplevel()
        self.help_box.title("Help / Information")

        # Center window on screen
        self.help_box.geometry("+{}+{}".format(
            self.help_box.winfo_screenwidth() // 2 - 150,
            self.help_box.winfo_screenheight() // 2 - 100))

        self.help_frame = Frame(self.help_box, bg=background, padx=20, pady=20)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Courier", 14, "bold"),
                                        bg=background)
        self.help_heading_label.grid(row=0, pady=(0, 10))

        help_text = (
            "To use the program:\n"
            "- Enter the temperature you want to convert.\n"
            "- Click the button to convert to Celsius or Fahrenheit.\n\n"
            "Note: -273°C (-459°F) is absolute zero. "
            "The program will return an error below this value.\n\n"
            "Use the 'History / Export' button to save your results."
        )

        self.help_text_label = Label(self.help_frame,
                                     text=help_text,
                                     wraplength=300,
                                     justify=LEFT,
                                     bg=background)
        self.help_text_label.grid(row=1, pady=10)

        self.dismiss_button = Button(self.help_frame,
                                     text="Dismiss",
                                     bg="#FF3300",
                                     fg="#FFFFFF",
                                     command=self.close_help)
        self.dismiss_button.grid(row=2, pady=(10, 0))

    def close_help(self):
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
