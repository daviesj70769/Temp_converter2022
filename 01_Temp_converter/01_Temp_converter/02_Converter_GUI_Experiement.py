from tkinter import *
from functools import partial  # To prevent unwanted windows 
import random


class Converter:
    def __init__(self):

        # Formatting variables 
        background_color = "light blue"

        # Converter Frame 
        self.converter_frame = Frame(width=300, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()                             
       
        # Temperature Converter Heading (row 0)
        self.temp_converter_label=Label(self.converter_frame,text="Temperature Converter",
                                        font=("Arial 16 bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                                  "converted and then push"
                                                  "one of the buttons below...",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)                                     

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
        
        # Conversion buttons frame (row 3)

        # Answer label (row 4)

        # History / Help button frame (row 5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
