from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

# LOGIN BUTTON FUNCTIONALITY
def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Ayoushri' and passwordEntry.get()=='1234':
        messagebox.showinfo('Succesful login','Welcome')
        root.destroy()
        import sms
    else:
        messagebox.showerror('Error','Enter the correct credentials')

root = Tk() #object of Tk class

root.title('Login System of Student Management System')
root.geometry('1280x700+0+0')  # +0+0 is the distance from the x axis and the y axis of the window
root.resizable(False,False)  # to disable the maximise button so that window size cannot be changed

# ADDING BACKGROUND IMAGE
bgImg=ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(root,image=bgImg)
bgLabel.place(x=0,y=0)

# CREATING FRAME
loginFrame = Frame(root,bg='white')
loginFrame.place(x=400,y=150)

# ADDING LOGO IMAGE
logoImg = ImageTk.PhotoImage(file='student.jpg')
logoLabel = Label(loginFrame,image=logoImg)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)  #logolabel will now take 2 column spaces - column 0 and 1
   #pady=10 means 10px vertical spacing is provided to see gap b/w logo & username

# ADDING USERNAME
userImg = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame,image=userImg,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white') #compound = LEFT is used to see the image on the left side of the text
usernameLabel.grid(row=1,column=0)

usernameEntry = Entry(loginFrame,font=('times new roman',18,'bold'),bd=5,fg='brown') #bd=border
usernameEntry.grid(row=1,column=1,padx=20) #padx provides horizontal spacing

# ADDING PASSWORD
passwordImg = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame,image=passwordImg,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white') #compound = LEFT is used to see the image on the left side of the text
passwordLabel.grid(row=2,column=0,pady=10)

passwordEntry = Entry(loginFrame,font=('times new roman',18,'bold'),bd=5,fg='brown') #bd=border
passwordEntry.grid(row=2,column=1,padx=20,pady=10) #padx provides horizontal spacing

# CREATE LOGIN BUTTON
loginButton=Button(loginFrame,text="LogIn",font=('times new roman',18,'bold'),bd=3,bg='lightblue',width=10,activebackground='red',activeforeground='green',cursor='hand2',
                   command=login)
loginButton.grid(row=3,column=1,pady=10)




root.mainloop()
