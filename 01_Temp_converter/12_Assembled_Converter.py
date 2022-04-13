from tkinter import *
from functools import partial  # To prevent unwanted windows 


class Converter:
    def __init__(self):

        # Formatting variables 
        background_color = "teal"

        # In actual program this is blank and is populated with user calculation

        '''self.all_calc_list = ['5 degrees C is -17.2 degrees F',
                              '6 degrees C is -16.7 degrees F',
                              '7 degrees c is -16.1 degrees F',
                              '8 degrees c is -15.8 degrees F',
                              '9 degrees c is -15.1 degrees F',
                                ]'''

        # Initialise list to hold calculation history 
        self.all_calc_list = []

        # Converter Frame 
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()                             
       
        # Temperature Converter Heading (row 0)
        self.temp_converter_label=Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font=("Arial 16 bold"), bg=background_color,
                                        padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                                  "converted and then push one"
                                                  "of the buttons below...",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)                                     

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
        
        # Conversion buttons frame (row 3) , slategray3 
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="slategray3", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)      

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="to Fahrenheit", font="Arial 10 bold",
                                  bg="slategray3", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)                   

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="midnightblue", bg=background_color, 
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # history / history button frame (row 5)
        self.hist_history_frame = Frame(self.converter_frame, bg=background_color)
        self.hist_history_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_history_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15,
                                    command=lambda: self.history(self.all_calc_list))
        self.calc_hist_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.calc_hist_button.config(state=DISABLED)
        
        self.help_button = Button(self.hist_history_frame, text="help", 
                                  font=("Arial 12 bold"),
                                   command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self,low):
        print (low)

        error = "#ffafaf"  # Pale pink background when entry box has errors

        # Retrieve amount entered into Entry Field
        to_convert = self.to_convert_entry.get() 

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to Farenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
            # Input is invalid (too cold)!!
                answer = "Too Cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)
           
            # Add Answer to list for history
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.calc_hist_button.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        
        return rounded
          
    def history(self, calc_history):
        History(self, calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box"
                                          "and then ")

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


      
class Help:
    def __init__(self, partner):
        
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)
        
        #sets up child window (ie: help box)
        self.help_box = Toplevel()        
       
        # If user press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
       
        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
       
        # Set up Help Heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)                        
        
        # Help text (Label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)   
        self.help_text.grid(row=1)                        
       
        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", 
                                  width=10,  bg="orange", font="arial 10 bold",
                           command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, padx=10, pady=10)                   
        
    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
