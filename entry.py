import tkinter as tk
def clickevent():
    label = tk.Label(text=(entry.get()))
    label.pack()

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="enter" , padx=10, pady=10, command=clickevent)
button.pack()

root.mainloop()