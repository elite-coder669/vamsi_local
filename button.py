import tkinter as tk
def clickme():
    label = tk.Label(text = 'look i just clicked the button!')
    label.pack()
root = tk.Tk()
button = tk.Button(root, text = "Click me!",padx = 50, pady = 50, command = clickme)
button.pack()
root.mainloop()