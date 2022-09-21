from tkinter import *
from functools import partial  # To prevent unwanted windows 

import random
from turtle import back


class Convertor:
    def __init__(self, parent):

        # Formatting variables...
        background_color= "light blue"

        # Converter Main Screen Gui...
        self.converter_frame = Frame(width=1000, height=1000, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)
        self.temp_converter_label=Label(self.converter_frame,text="Temperature Converter",
                                        font=("Arial", "16", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Export Instructions (Label, row 1)
        self.export_text = Label (self.converter_frame, text="Enter a filename in the box below and press the save button to save your calculation history to a text file.",
                            justify=LEFT, width=40,
                                bg=background_color, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.converter_frame, text="If the filename you enter below already exists, be replaced with you calculation history",
                            justify=LEFT, bg=background_color, fg="maroon",
                              font="Arial 10 italic", wrap=225, padx=10,
                              pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_text = Entry(self.converter_frame)
        self.filename_text.grid(row = 3)

        # Export Button (row 1)
        self.export_button = Button(self.converter_frame, text="Export", 
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.export)
        self.export_button.grid(row= 4)            

    def export(self):
        print("you asked for export")
        get_export = Export(self)
        get_export.export_text.configure(text="Export text goes here")
       
       
class Export:
    def __init__(self, partner):
        
        background = "Pale Green"

        # disable export button
        partner.export_button.config(state=DISABLED)
        
        #sets up child window (ie: export box)
        self.export_box = Toplevel()        
       
        # If user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))
        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()
       
        # Set up export Heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        
        # Export text (Label, row 1)
        self.export_text = Label(self.export_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)   
        self.export_text.grid(row=1) 

        # Save button (row 2)  


       
        # Cancel button (row 2)
        self.cancel_btn = Button(self.export_frame, text="Cancel", 
                                  width=10, font="arial 10 bold",
                           command=partial(self.close_export, partner))
        self.cancel_btn.grid(row=2, padx=10, pady=10)


        
    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    # main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()