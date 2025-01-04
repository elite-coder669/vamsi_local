from tkinter import *

def pressed():
    print('button press')

# Create main application window
calculatorApp = Tk()
calculatorApp.geometry("350x450")
calculatorApp.title("Calculator")
calculatorApp.config(bg="White")

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
entry = Entry(calculatorApp, font=("Arial", 30), bg="white", bd=0, highlightthickness=0, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

# Calculator buttons
cancel_button = Button(calculatorApp, text="C", fg='red', font=("Arial", 22), command=pressed)
cancel_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

back_space = Button(calculatorApp, text="back", fg='lightgreen', font=("Arial", 22), command=pressed)
back_space.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

percentage = Button(calculatorApp, text="%", fg='lightgreen', font=("Arial", 22), command=pressed)
percentage.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

divide = Button(calculatorApp, text="/", fg='lightgreen', font=("Arial", 22), command=pressed)
divide.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

seven = Button(calculatorApp, text="7", fg='lightgreen', font=("Arial", 22), command=pressed)
seven.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

eight = Button(calculatorApp, text="8", fg='lightgreen', font=("Arial", 22), command=pressed)
eight.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

nine = Button(calculatorApp, text="9", fg='lightgreen', font=("Arial", 22), command=pressed)
nine.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

multiply = Button(calculatorApp, text="*", fg='lightgreen', font=("Arial", 22), command=pressed)
multiply.grid(row=2, column=3, sticky="ew", padx=5, pady=5)

four = Button(calculatorApp, text="4", fg='lightgreen', font=("Arial", 22), command=pressed)
four.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

five = Button(calculatorApp, text="5", fg='lightgreen', font=("Arial", 22), command=pressed)
five.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

six = Button(calculatorApp, text="6", fg='lightgreen', font=("Arial", 22), command=pressed)
six.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

subtract = Button(calculatorApp, text="-", fg='lightgreen', font=("Arial", 22), command=pressed)
subtract.grid(row=3, column=3, sticky="ew", padx=5, pady=5)

one = Button(calculatorApp, text="1", fg='lightgreen', font=("Arial", 22), command=pressed)
one.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

two = Button(calculatorApp, text="2", fg='lightgreen', font=("Arial", 22), command=pressed)
two.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

three = Button(calculatorApp, text="3", fg='lightgreen', font=("Arial", 22), command=pressed)
three.grid(row=4, column=2, sticky="ew", padx=5, pady=5)

add = Button(calculatorApp, text="+", fg='lightgreen', font=("Arial", 22), command=pressed)
add.grid(row=4, column=3, sticky="ew", padx=5, pady=5)

sqrt = Button(calculatorApp, text="√", fg='lightgreen', font=("Arial", 22), command=pressed)
sqrt.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

zero = Button(calculatorApp, text="0", fg='lightgreen', font=("Arial", 22), command=pressed)
zero.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

dot = Button(calculatorApp, text=".", fg='lightgreen', font=("Arial", 22), command=pressed)
dot.grid(row=5, column=2, sticky="ew", padx=5, pady=5)

equal = Button(calculatorApp, text="=", fg='lightgreen', font=("Arial", 22), command=pressed)
equal.grid(row=5, column=3, sticky="ew", padx=5, pady=5)

# Start the Tkinter event loop
calculatorApp.mainloop()
