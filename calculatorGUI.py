from tkinter import *
import math
import time
import re
# default check event for binding
# def pressed():
    # print('button press')



def evaluator():
    expression = entry.get() #this will return entry content as a string.
    try:
        result = eval(expression)
        entry.delete(0,END)
        entry.insert(0,str(result))
    except Exception as e:
        entry.delete(0,END)
        entry.insert(0,"Invalid")
        # time.sleep(3)
        entry.insert(0,f"{e}")

def restrict_keys(event):
    # Define the allowed keys for the calculator
    allowed_keys = "0123456789+-*/.s"  # Include "s" for sqrt
    if event.char in allowed_keys:
        return True  # Allow the key press
    else:
        return "break"  # Ignore the key press



# Function to bind keys for specific buttons
def bind_keys():
    calculatorApp.bind("<s>", lambda event: entry.insert(INSERT, "√"))  # Bind 's' for sqrt button
    calculatorApp.bind("<Return>", lambda event: evaluator())  # Bind 'Return' key for equal (=) button



# Create main application window
calculatorApp = Tk()
calculatorApp.geometry("350x450")
calculatorApp.title("Calculator")
calculatorApp.config(bg="White")
calculatorApp.resizable(False,False)
# Configure the grid to make sure rows and columns behave properly
calculatorApp.grid_rowconfigure(0, weight=0)  # Row 0 for entry widget, no stretching
calculatorApp.grid_rowconfigure(1, weight=1)  # Row 1 for buttons, stretchable
calculatorApp.grid_rowconfigure(2, weight=1)  # Row 2 for buttons, stretchable
calculatorApp.grid_rowconfigure(3, weight=1)  # Row 3 for buttons, stretchable
calculatorApp.grid_rowconfigure(4, weight=1)  # Row 4 for buttons, stretchable
calculatorApp.grid_rowconfigure(5, weight=1)  # Row 5 for buttons, stretchable

calculatorApp.grid_columnconfigure(0, weight=1)  # Columns stretchable
calculatorApp.grid_columnconfigure(1, weight=1)
calculatorApp.grid_columnconfigure(2, weight=1)
calculatorApp.grid_columnconfigure(3, weight=1)

# Entry widget at the top (row 0)
entry = Entry(calculatorApp, font=("Arial", 30), bg="white", bd=0, highlightthickness=0, relief="flat", justify="right")
entry.grid(row=0, column=0,columnspan=4, sticky="ew", padx=10, pady=10)

# entry = Text(calculatorApp, font=("Arial", 30), bg="white", bd=0, highlightthickness=0, relief="flat", , wrap=NONE, height=1, width=20)
# entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)


# Calculator buttons
cancel_button = Button(calculatorApp, text="C", fg='red',font=("Arial", 22),command= lambda: entry.delete(0, END))
cancel_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

back_space = Button(calculatorApp, text="🔙", height=2,command= lambda: entry.delete(len(entry.get())-1, END))
back_space.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

percentage = Button(calculatorApp, text="%", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"%"))
percentage.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

by = Button(calculatorApp, text="/", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT, "/"))
by.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

seven = Button(calculatorApp, text="7", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"7"))
seven.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

eight = Button(calculatorApp, text="8", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"8"))
eight.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

nine = Button(calculatorApp, text="9", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"9"))
nine.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

cross = Button(calculatorApp, text="*", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"*"))
cross.grid(row=2, column=3, sticky="ew", padx=5, pady=5)

four = Button(calculatorApp, text="4", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"4"))
four.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

five = Button(calculatorApp, text="5", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"5"))
five.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

six = Button(calculatorApp, text="6", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"6"))
six.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

minus = Button(calculatorApp, text="-", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"-"))
minus.grid(row=3, column=3, sticky="ew", padx=5, pady=5)

one = Button(calculatorApp, text="1", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"1"))
one.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

two = Button(calculatorApp, text="2", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"2"))
two.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

three = Button(calculatorApp, text="3", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"3"))
three.grid(row=4, column=2, sticky="ew", padx=5, pady=5)

plus = Button(calculatorApp, text="+", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"+"))
plus.grid(row=4, column=3, sticky="ew", padx=5, pady=5)

# sqrt = Button(calculatorApp, text="√", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"√"))
# sqrt.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

zero = Button(calculatorApp, text="0", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"0"))
zero.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

dot = Button(calculatorApp, text=".", fg='green', font=("Arial", 22), command= lambda: entry.insert(INSERT,"."))
dot.grid(row=5, column=2, sticky="ew", padx=5, pady=5)

equal = Button(calculatorApp, text="=", fg='green', font=("Arial", 22), command= evaluator)
equal.grid(row=5, column=3, sticky="ew", padx=5, pady=5)

bind_keys()
entry.bind("<Key>", restrict_keys)
# Start the Tkinter event loop
calculatorApp.mainloop()
