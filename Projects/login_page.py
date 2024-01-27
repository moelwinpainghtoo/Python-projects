from tkinter import *
from tkinter import messagebox

main = Tk()
main.title('Login Page')
main.geometry('925x500+290+150')
main.config(bg='white')
main.resizable(False, False)

def signin():
    username = user.get()
    password = pwd.get()

    if username != 'admin' and password != 'admin123':
        messagebox.showinfo('Invalid Error', 'Username and Password are incorrect')
    elif username != 'admin':
        messagebox.showinfo('Invalid Error', 'Username is incorrect.')
    elif password != 'admin123':
        messagebox.showinfo('Invalid Error', 'Password is incorrect.')
    elif username == 'admin' and password == 'admin123':
        screen =
        
img = PhotoImage(file= r'C:\Users\Lenovo\Pictures\login4.png')
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
sign_up.place(x=230,y=268)
main.mainloop()