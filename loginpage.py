from tkinter import *

database = { #this is a sample dictionary that contains sample user data
    'user1' : 'pass1',
    'user2' : 'pass2',
    'user3' : 'pass3',
    'user4' : 'pass4',
    'user5' : 'pass5'
} 
def Login_event():
    global global_val
    username = Username.get()
    password = Password.get()
    if database.get(username) == password:
        greeting.configure(text=f"hi {username}. glad to see you here!")
        
    else:
        greeting.configure(text="check back you maybe entering wrong details!")
        
def set_background(root, image_path):
    bg_image = PhotoImage(file=image_path)
    bg_label = Label(root, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)



root = Tk()
root.title('Login Form')
root.geometry('1024x600')
root.configure(bg='#3B3B3B')
set_background(root, 'C:\\Users\\VAMSIKETAN\\new_cpp\\image.png')
header = Label(root,text='Login',)
username_head = Label(root, text='Username')
password_head = Label(root,text='Password')
Username = Entry(root)
Password = Entry(root)
login_button = Button(root,text='Login',command=Login_event)

header.grid(row=0)
username_head.grid(row=1)
Username.grid(row= 1, column=1)
password_head.grid(row=2)
Password.grid(row=2,column=1)
login_button.grid(row=3)

greeting = Label(root, text="",bg='#3B3B3B',fg='white')
greeting.grid(row=4, column=1, pady=10)

root.mainloop()