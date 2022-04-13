from ast import Lambda
from tkinter import *
from functools import partial  # To prevent unwanted windows 

class Converter:
    def __init__(self):

        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F']

        # Formatting variables...
        background_color= "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)
        
    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):
        
        background = "#a9ef99"  # Pale Green 

        # disable history button
        partner.history_button.config(state=DISABLED)
        
        #sets up child window (ie: history box)
        self.history_box = Toplevel()        
       
        # If user press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))
       
        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()
       
        # Set up history Heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (Label, row 1)
        self.history_text = Label(self.history_frame,
                                          text="Here are your most recent"
                                               "calculations. Please use the"
                                               "export button to create a text"
                                               "file of all your calculations for"
                                               "this session", wrap=250,
                                        font="arial 10 italic",
                                        justify=LEFT, bg=background, fg="maroon",
                                        padx=10, pady=10)      
        self.history_text.grid(row=1) 

        # history Output goes here.. (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)
                - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation"
                                              "history. you can use the"
                                              "export button to save this"
                                              "data to a text file if"
                                              "desired.")
                
                
        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background,font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame) 
        self.export_dismiss_frame.grid(row=3, pady=10)                
        
        # Export Button 
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0,column=1)


        # Dismiss Button 
        self.dismiss_button= Button(self.export_dismiss_frame, text="Dismiss",
                                    font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)
      
    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()
        
class Convertor:
    def __init__(self, parent, calc_history):

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
                            justify=LEFT, bg=background_color, fg="teal",
                              font="Arial 10 italic", wrap=225, padx=10,
                              pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_text = Entry(self.converter_frame)
        self.filename_text.grid(row = 3)

        # Export Button (row 1)
        self.export_button = Button(self.export_dismiss_frame, text="Export", font="Arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0,column=1)
       
    def export(self):
        print("you asked for export")
        get_export = Export(self)
        get_export.export_text.configure(text="Export text goes here")

    def export(self, calc_history):
        Export(self, calc_history)
       
       
class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)
        
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
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
