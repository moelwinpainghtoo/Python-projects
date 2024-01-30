from tkinter import *
from tkinter import messagebox
from pathlib import Path
from tkinter import ttk

main = Tk()
main.title('Login Page')
main.geometry('925x500+290+150')
main.config(bg='white')
main.resizable(False, False)

img = PhotoImage(file="login4.png")
img1 = PhotoImage(file="login5.png")

####################################################  Sign_up (SUB window)  ######################################################
def createwindow():
    main.iconify() # to hide main window
    sub = Toplevel(main)
    sub.title('Signup Page')
    sub.geometry('925x500+290+150')
    sub.config(bg='white')
    sub.resizable(False, False)

    #### SUB Function #####

    def signin_sub():
        sub.destroy() # to close the sub window(Toplevel window)
        main.deiconify() # to make main window reappear
    def signup():
        a = signup_user.get()
        b = signup_pwd.get()
        c = confirm_pwd.get()
        
        file_path = 'database.txt'
        with open(file_path, 'r') as file:
            lines = file.readlines()
            data = {}
            for line in lines:
                t, v = line.strip().split(':')
                data[t] = v
        if b != c:
            messagebox.showinfo('Invalid Error', 'Password should match with confirm Password!')
        elif a in data:
            messagebox.showinfo('Invalid Error', 'Username already exists.')
        else:
            a = str(a)
            b = str(b)
            file = open('database.txt', 'a')
            file.write(f'{a}:{b}\n')
            signup_user.delete(0, 'end')
            signup_user.insert(0, 'Username')
            signup_pwd.delete(0, 'end')
            signup_pwd.insert(0, 'Password')
            confirm_pwd.delete(0, 'end')
            confirm_pwd.insert(0, 'Confirm your Password')
            messagebox.showinfo('Successful Signup', 'Signup Successfully!')
            file.close()

            
    #### SUB Function #####
    
    Label(sub, image=img1, bg='white').place(x=100,y=125)

    frame1 = Frame(sub, width=350, height=350, bg='white')
    frame1.place(x=490,y=70)

    sign_head = Label(frame1, text='Sign up', fg='#57a1f8', bg='white', font=('Miscrosoft YaHei UI Light',23))
    sign_head.place(x=135,y=25)
    #####--------------------------------------

    def cursor_in(e):
        signup_user.delete(0, 'end')

    def cursor_out(e):
        name = signup_user.get()
        if name == '':
            signup_user.insert(0, 'Username')

    signup_user = Entry(frame1, width=25, fg='black', bd=0, bg='white', font=('Miscrosoft YaHei UI Light',11))
    signup_user.place(x=60,y=100)
    signup_user.insert(0, 'Username')
    signup_user.bind('<FocusIn>', cursor_in)
    signup_user.bind('<FocusOut>', cursor_out)

    Frame(frame1, width=250, height=2, bg='black').place(x=60,y=120)

    #####---------------------------------------------------

    def cursor_in(e):
        signup_pwd.delete(0, 'end')

    def cursor_out(e):
        passwd = signup_pwd.get()
        if passwd == '':
            signup_pwd.insert(0, 'Password')

    signup_pwd = Entry(frame1, width=25, fg='black', bd=0, bg='white', font=('Miscrosoft YaHei UI Light',11))
    signup_pwd.place(x=60,y=150)
    signup_pwd.insert(0, 'Password')
    signup_pwd.bind('<FocusIn>', cursor_in)
    signup_pwd.bind('<FocusOut>', cursor_out)

    Frame(frame1, width=250, height=2, bg='black').place(x=60,y=170)

    def cursor_in(e):
        confirm_pwd.delete(0, 'end')

    def cursor_out(e):
        passwd = confirm_pwd.get()
        if passwd == '':
            confirm_pwd.insert(0, 'Confirm your Password')

    confirm_pwd = Entry(frame1, width=25, fg='black', bd=0, bg='white', font=('Miscrosoft YaHei UI Light',11))
    confirm_pwd.place(x=60,y=200)
    confirm_pwd.insert(0, 'Confirm your Password')
    confirm_pwd.bind('<FocusIn>', cursor_in)
    confirm_pwd.bind('<FocusOut>', cursor_out)

    Frame(frame1, width=250, height=2, bg='black').place(x=60,y=220)

    #####---------------------------------------------------

    confirm_button = Button(frame1, text='Confirm', width=25, bg='#57a1f8', fg='white', font=('Miscrosoft YaHei UI Light',10,'bold'))
    confirm_button.config(bd=0)
    confirm_button.config(command=signup)
    confirm_button.place(x=85,y=260)

    Label(frame1, text="Do you have an account?", bd=0, fg='black', bg='white',font=('Miscrosoft YaHei UI Light',9)).place(x=90,y=330)

    sign_in = Button(frame1, text='Signin', bd=0, bg='white', fg='#57a1f8', width=5, cursor='hand2')
    sign_in.config(command=signin_sub)
    sign_in.place(x=230,y=328)

####################################################  SUB  ######################################################

####################################################  MAIN  ######################################################      

#### MAIN Function #####
##### Open database and identify valid username and password #####
def signin():
    file_path = 'database.txt'
    
    # If the database file doesn't exist, create it
    if not Path(file_path).exists():
        with open(file_path, 'w'):
            pass

    # Open the database file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = {}
        for line in lines:
            a, b = line.strip().split(':')
            data[a] = b

    username = user.get()
    password = pwd.get()

    if username == 'admin' and password == 'admin123':
            screen = Toplevel(main)
            screen.title('Root account')
            screen.geometry('925x500+290+150')
            screen.resizable(False, False)
            
            label = Label(screen, text='Welcome to root account!', fg='black', bg='white', font=('Miscrosoft YaHei UI Light', 15))
            label.place(x=1, y=1)
            # Dropdown box to display usernames and passwords in root account
            current_data = ttk.Combobox(screen, values=list(data.keys()), width=30)
            current_data.place(x=100, y=90)
            label1 = Label(screen, text='Usernames', fg='black', bg='white', font=('Miscrosoft YaHei UI Light', 9))
            label1.place(x=110, y=65)

            def give_value(): # to give user's password, using username to find the value or password of the user
                selected_key = current_data.get()
                selected_value = data.get(selected_key, "Key not found")
                Label(screen, text=selected_value, bg='white', fg='red', font=('Miscrosoft YaHei UI Light', 9)).place(x=330,y=120)
            label1 = Label(screen, text='Password', fg='black', bg='white', font=('Miscrosoft YaHei UI Light', 9))
            label1.place(x=330, y=65)
            button_value = Button(screen, text='Click here to generate the user password.', bg='white', fg='black', font=('Miscrosoft YaHei UI Light', 9))
            button_value.config(bd=2, command=give_value)
            button_value.place(x=330,y=85)
            screen.grab_set()
            screen.wait_window()

    elif username in data:
        if password == data[username]:
            screen1 = Toplevel(main)
            screen1.title('User account')
            screen1.geometry('925x500+290+150')
            screen1.resizable(False, False)
            
            label1 = Label(screen1, text=f"Welcome to {username}'s account!", fg='black', bg='white', font=('Miscrosoft YaHei UI Light', 23))
            label1.place(x=100, y=50)
            screen1.grab_set()
            screen1.wait_window()
        else:
            messagebox.showinfo('Invalid Error', 'Password incorrect!')
    else:
        messagebox.showinfo('Invalid Error', "Username doesn't exist.")
#### MAIN Function #####

Label(main, image=img, bg='white').place(x=100,y=125)

frame = Frame(main, width=350, height=350, bg='white')
frame.place(x=490,y=70)

sign_head = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Miscrosoft YaHei UI Light',23))
sign_head.place(x=135,y=25)

#####---------------------------------------------------

def cursor_in(e):
    user.delete(0, 'end')

def cursor_out(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', bd=0, bg='white', font=('Miscrosoft YaHei UI Light',11))
user.place(x=60,y=100)
user.insert(0, 'Username')
user.bind('<FocusIn>', cursor_in)
user.bind('<FocusOut>', cursor_out)

Frame(frame, width=250, height=2, bg='black').place(x=60,y=120)

#####---------------------------------------------------

def cursor_in(e):
    pwd.delete(0, 'end')

def cursor_out(e):
    passwd = pwd.get()
    if passwd == '':
        pwd.insert(0, 'Password')

pwd = Entry(frame, width=25, fg='black', bd=0, bg='white', font=('Miscrosoft YaHei UI Light',11))
pwd.place(x=60,y=150)
pwd.insert(0, 'Password')
pwd.bind('<FocusIn>', cursor_in)
pwd.bind('<FocusOut>', cursor_out)

Frame(frame, width=250, height=2, bg='black').place(x=60,y=170)

#####---------------------------------------------------

sign_in_button = Button(frame, text='Login', width=25, bg='#57a1f8', fg='white', font=('Miscrosoft YaHei UI Light',10,'bold'))
sign_in_button.config(bd=0)
sign_in_button.config(command=signin)
sign_in_button.place(x=85,y=210)

Label(frame, text="Don't have an account?", bd=0, fg='black', bg='white',font=('Miscrosoft YaHei UI Light',9)).place(x=90,y=270)

sign_up = Button(frame, text='Signup', bd=0, bg='white', fg='#57a1f8', width=5, cursor='hand2')
sign_up.config(command=createwindow)
sign_up.place(x=230,y=268)
main.mainloop()
####################################################  MAIN  ######################################################