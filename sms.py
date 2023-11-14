from tkinter import *
import time
from tkinter.ttk import Button
import pandas
import ttkthemes
from tkinter import ttk,messagebox,filedialog #  ttk helps to apply themes on button ; native library in tkinter which is used to stle the widgets
import pymysql


#Functionality Part

def exit_student():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        window.destroy()
    else:
        pass


def export_student():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()  #to get all the indexes of the rows
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table = pandas.DataFrame(newlist,columns=['Enrollment Number','Name','Section','Year','Department','Mobile Number','Email','Address','Gender','Date of Birth','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')

def update_student():

    def update_data():
        en = enval.get()
        name = nameval.get()
        sec = secval.get()
        year = yearval.get()
        department = departmentval.get()
        mn = mnval.get()
        em = emval.get()
        ad = adval.get()
        gen = genval.get()
        dob = dobval.get()
        currentdate = time.strftime('%Y-%m-%d')
        currenttime = time.strftime('%H:%M:%S')
        query = 'update student set EnrollmentNumber=%s,Name=%s,Section=%s,Year=%s,Department=%s,MobileNo=%s,email=%s,address=%s,Gender=%s,dob=%s,addeddate=%s,addedtime=%s where EnrollmentNumber=%s'
        mycursor.execute(query,(en,name,sec,year,department,mn,em,ad,gen,dob,currentdate,currenttime,en))
        con.commit()
        messagebox.showinfo('Success',f'Enrollment Number {en} is updated successfully',parent=update_window)
        update_window.destroy()
        query = 'select *from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    update_window = Toplevel()
    update_window.grab_set()  # not allow me to click on some other button when the toplevel window is opened
    update_window.geometry('600x550+350+20')
    update_window.title('Update Student')
    update_window.resizable(0, 0)

    enLabel = Label(update_window, text='Enrollment Number', font=('times new roman', 20, 'bold'), fg='dodger blue')
    enLabel.grid(row=0, column=0, padx=5, pady=5,
                 sticky=W)  # sticky is used to stick and align all the labels on the left hand side
    enval = StringVar()
    enEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=enval)
    enEntry.grid(row=0, column=1, pady=5, padx=5)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'), fg='dodger blue')
    nameLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    nameval = StringVar()
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=nameval)
    nameEntry.grid(row=1, column=1, pady=5, padx=5)

    secLabel = Label(update_window, text='Section', font=('times new roman', 20, 'bold'), fg='dodger blue')
    secLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    secval = StringVar()
    secEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=secval)
    secEntry.grid(row=2, column=1, pady=5, padx=5)

    yearLabel = Label(update_window, text='Year Of Study', font=('times new roman', 20, 'bold'), fg='dodger blue')
    yearLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    yearval = StringVar()
    yearEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=yearval)
    yearEntry.grid(row=3, column=1, pady=5, padx=5)

    departmentLabel = Label(update_window, text='Department', font=('times new roman', 20, 'bold'), fg='dodger blue')
    departmentLabel.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    departmentval = StringVar()
    departmentEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=departmentval)
    departmentEntry.grid(row=4, column=1, pady=5, padx=5)

    mnLabel = Label(update_window, text='Mobile Number', font=('times new roman', 20, 'bold'), fg='dodger blue')
    mnLabel.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    mnval = StringVar()
    mnEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=mnval)
    mnEntry.grid(row=5, column=1, pady=5, padx=5)

    emLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'), fg='dodger blue')
    emLabel.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    emval = StringVar()
    emEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=emval)
    emEntry.grid(row=6, column=1, pady=5, padx=5)

    adLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'), fg='dodger blue')
    adLabel.grid(row=7, column=0, padx=5, pady=5, sticky=W)
    adval = StringVar()
    adEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=adval)
    adEntry.grid(row=7, column=1, pady=5, padx=5)

    genLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'), fg='dodger blue')
    genLabel.grid(row=8, column=0, padx=5, pady=5, sticky=W)
    genval = StringVar()
    genEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=genval)
    genEntry.grid(row=8, column=1, pady=5, padx=5)

    dobLabel = Label(update_window, text='Date Of Birth', font=('times new roman', 20, 'bold'), fg='dodger blue', )
    dobLabel.grid(row=9, column=0, padx=5, pady=5, sticky=W)
    dobval = StringVar()
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'), width=25, textvariable=dobval)
    dobEntry.grid(row=9, column=1, pady=5, padx=5)

    update_student_button = ttk.Button(update_window, text='UPDATE STUDENT', style='aB.TButton',command=update_data)
    update_student_button.grid(row=10, columnspan=10, pady=5)
    aB = ttk.Style()
    aB.configure('aB.TButton', font=(None, 15, 'bold'), foreground='magenta4', width=20)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']
    enEntry.insert(0,listdata[0])
    nameEntry.insert(0, listdata[1])
    secEntry.insert(0, listdata[2])
    yearEntry.insert(0, listdata[3])
    departmentEntry.insert(0, listdata[4])
    mnEntry.insert(0, listdata[5])
    emEntry.insert(0, listdata[6])
    adEntry.insert(0, listdata[7])
    genEntry.insert(0, listdata[8])
    dobEntry.insert(0, listdata[9])




def show_student():
    query = 'select *from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def delete_student():
    indexing=studentTable.focus()  #to find the index of the row which will be deleted
    #print(indexing)
    content=studentTable.item(indexing) #content is the row that is to be deleted ; it is a dictionary
    #print(content)
    contentid=content['values'][0]  #contentid is the value based on which the row will be deleted
    #print(contentid)
    query = 'delete from student where EnrollmentNumber=%s'
    mycursor.execute(query,contentid)
    con.commit()
    messagebox.showinfo('Deleted',f'Enrollment Number {contentid} is deleted successfully')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def search_student():
    def search_data():
        en = enval.get()
        sec = secval.get()
        year = yearval.get()
        department = departmentval.get()
        query = "select *from student where EnrollmentNumber=%s or Section=%s or Year=%s or Department=%s"
        mycursor.execute(query,(en,sec,year,department))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)


    search_window = Toplevel()
    search_window.grab_set()  # not allow me to click on some other button when the toplevel window is opened
    search_window.geometry('550x250+350+150')
    search_window.title('Search Student')
    search_window.resizable(0, 0)

    enLabel = Label(search_window, text='Enrollment Number', font=('times new roman', 20, 'bold'), fg='dodger blue')
    enLabel.grid(row=0, column=0, padx=5, pady=5,
                 sticky=W)  # sticky is used to stick and align all the labels on the left hand side
    enval = StringVar()
    enEntry = Entry(search_window, font=('roman', 15, 'bold'), width=25, textvariable=enval)
    enEntry.grid(row=0, column=1, pady=5, padx=5)

    secLabel = Label(search_window, text='Section', font=('times new roman', 20, 'bold'), fg='dodger blue')
    secLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    secval = StringVar()
    secEntry = Entry(search_window, font=('roman', 15, 'bold'), width=25, textvariable=secval)
    secEntry.grid(row=2, column=1, pady=5, padx=5)

    yearLabel = Label(search_window, text='Year Of Study', font=('times new roman', 20, 'bold'), fg='dodger blue')
    yearLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    yearval = StringVar()
    yearEntry = Entry(search_window, font=('roman', 15, 'bold'), width=25, textvariable=yearval)
    yearEntry.grid(row=3, column=1, pady=5, padx=5)

    departmentLabel = Label(search_window, text='Department', font=('times new roman', 20, 'bold'), fg='dodger blue')
    departmentLabel.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    departmentval = StringVar()
    departmentEntry = Entry(search_window, font=('roman', 15, 'bold'), width=25, textvariable=departmentval)
    departmentEntry.grid(row=4, column=1, pady=5, padx=5)

    search_student_button = ttk.Button(search_window, text='SEARCH', style='aB.TButton',command=search_data)
    search_student_button.grid(row=10, columnspan=10, pady=5)
    aB = ttk.Style()
    aB.configure('aB.TButton', font=(None, 15, 'bold'), foreground='magenta4', width=20)


def add_student():

    def add_data():
        en = enval.get()
        name = nameval.get()
        sec = secval.get()
        year = yearval.get()
        department = departmentval.get()
        mn = mnval.get()
        em = emval.get()
        ad = adval.get()
        gen = genval.get()
        dob = dobval.get()
        if en=='' or name=='' or sec=='' or year=='' or department=='' or mn=='' or em=='' or ad=='' or gen=='' or dob=='' :
            messagebox.showerror('Error','All fields are required',parent=add_window)
        else:
            currentdate = time.strftime('%Y-%m-%d')
            currenttime = time.strftime('%H:%M:%S')
            query='insert into Student (EnrollmentNumber,Name,Section,Year,Department,MobileNo,email,address,Gender,dob,addeddate,addedtime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            val =(en,name,sec,year,department,mn,em,ad,gen,dob,currentdate,currenttime)
            mycursor.execute(query,val)
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent = add_window)
            if result==True:
                enval.set('')
                nameval.set('')
                secval.set('')
                yearval.set('')
                departmentval.set('')
                mnval.set('')
                emval.set('')
                adval.set('')
                genval.set('')
                dobval.set('')
            else:
                pass

            query = 'select *from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children()) #used to delete all the previous data so that no previous data is repeated
            for data in fetched_data:
                datalist=list(data)
                studentTable.insert('',END,values=datalist)  #''-empty string represents root node; index - END - To added at bottom 'end' and 0 if at top



    add_window=Toplevel()
    add_window.grab_set()  #not allow me to click on some other button when the toplevel window is opened
    add_window.geometry('600x550+350+20')
    add_window.title('Add Student')
    add_window.resizable(0,0)

    enLabel=Label(add_window,text='Enrollment Number',font=('times new roman',20,'bold'),fg='dodger blue')
    enLabel.grid(row=0,column=0,padx=5,pady=5,sticky=W)  #sticky is used to stick and align all the labels on the left hand side
    enval = StringVar()
    enEntry=Entry(add_window,font=('roman',15,'bold'),width=25,textvariable=enval)
    enEntry.grid(row=0,column=1,pady=5,padx=5)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'),fg='dodger blue')
    nameLabel.grid(row=1, column=0, padx=5, pady=5,sticky=W)
    nameval = StringVar()
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=nameval)
    nameEntry.grid(row=1, column=1, pady=5, padx=5)

    secLabel = Label(add_window, text='Section', font=('times new roman', 20, 'bold'),fg='dodger blue')
    secLabel.grid(row=2, column=0, padx=5, pady=5,sticky=W)
    secval = StringVar()
    secEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=secval)
    secEntry.grid(row=2, column=1, pady=5, padx=5)

    yearLabel = Label(add_window, text='Year Of Study', font=('times new roman', 20, 'bold'),fg='dodger blue')
    yearLabel.grid(row=3, column=0, padx=5, pady=5,sticky=W)
    yearval = StringVar()
    yearEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=yearval)
    yearEntry.grid(row=3, column=1, pady=5, padx=5)

    departmentLabel = Label(add_window, text='Department', font=('times new roman', 20, 'bold'),fg='dodger blue')
    departmentLabel.grid(row=4, column=0, padx=5, pady=5,sticky=W)
    departmentval = StringVar()
    departmentEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=departmentval)
    departmentEntry.grid(row=4, column=1, pady=5, padx=5)

    mnLabel = Label(add_window, text='Mobile Number', font=('times new roman', 20, 'bold'),fg='dodger blue')
    mnLabel.grid(row=5, column=0, padx=5, pady=5,sticky=W)
    mnval = StringVar()
    mnEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=mnval)
    mnEntry.grid(row=5, column=1, pady=5, padx=5)

    emLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'),fg='dodger blue')
    emLabel.grid(row=6, column=0, padx=5, pady=5,sticky=W)
    emval = StringVar()
    emEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=emval)
    emEntry.grid(row=6, column=1, pady=5, padx=5)

    adLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'),fg='dodger blue')
    adLabel.grid(row=7, column=0, padx=5, pady=5,sticky=W)
    adval = StringVar()
    adEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=adval)
    adEntry.grid(row=7, column=1, pady=5, padx=5)

    genLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'),fg='dodger blue')
    genLabel.grid(row=8, column=0, padx=5, pady=5,sticky=W)
    genval = StringVar()
    genEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=genval)
    genEntry.grid(row=8, column=1, pady=5, padx=5)

    dobLabel = Label(add_window, text='Date Of Birth', font=('times new roman', 20, 'bold'),fg='dodger blue',)
    dobLabel.grid(row=9, column=0, padx=5, pady=5,sticky=W)
    dobval = StringVar()
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=25,textvariable=dobval)
    dobEntry.grid(row=9, column=1, pady=5, padx=5)

    add_student_button = ttk.Button(add_window,text='SUBMIT',style='aB.TButton',command=add_data)
    add_student_button.grid(row=10,columnspan=10,pady=5)
    aB = ttk.Style()
    aB.configure('aB.TButton', font=(None, 15, 'bold'), foreground='magenta4',width=20)

def connect_database():
    def connect():
        global mycursor
        global con
        try:
            con=pymysql.connect(host='localhost',user='root',password='dataAnalyst@29')
            mycursor=con.cursor()  #helps in executing the commands
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query = 'create database sms'
            mycursor.execute(query)
            query = 'use sms'
            mycursor.execute(query)
            query = 'create table Student(EnrollmentNumber varchar(100) primary key,Name varchar(100),Section char,Year int,Department varchar(10),MobileNo varchar(100),email varchar(50),address varchar(100),Gender char,dob Date,addeddate date,addedtime time)';
            mycursor.execute(query)
        except:
            query = 'use sms'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection Successful',parent=connectWindow) #parent is written to show the messageinfo over that toplevel window connectWindow only
        connectWindow.destroy()

        addStudent.config(state=NORMAL)
        searchStudent.config(state=NORMAL)
        deleteStudent.config(state=NORMAL)
        updateStudent.config(state=NORMAL)
        showStudent.config(state=NORMAL)
        exportStudent.config(state=NORMAL)


    connectWindow=Toplevel()  #Toplevel() is used to create a GUI window on the top of main window
    connectWindow.geometry('470x250+450+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text="Host Name",font=('arial',20,'bold'),fg='maroon')
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=20,pady=20)

    usernameLabel = Label(connectWindow, text="User Name", font=('arial', 20, 'bold'),fg='maroon')
    usernameLabel.grid(row=1, column=0, padx=20)
    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=20, pady=20)

    passwordLabel = Label(connectWindow, text="Password", font=('arial', 20, 'bold'),fg='maroon')
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=20, pady=20)

    connectButton = ttk.Button(connectWindow,text="CONNECT",width=15,style='cB.TButton',command=connect)
    connectButton.grid(row=3,columnspan=2)
    cB = ttk.Style()
    cB.configure('cB.TButton',font=(None,15,'bold'),foreground='magenta4')


def clock():
    currentDate = time.strftime('%d/%m/%Y')  # Y for displaying 2023 ; y for displaying only 23
    currentTime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'    Date:{currentDate}\nTime:{currentTime}') #config method is used to update something ; f string is used to concatenate the string with the variable
    datetimeLabel.after(1000,clock)  # after method is used to update something after some time, here some time means 1second=1000millisecond

count = 0
text = ""
def slider():
    global text,count
    if  count == len(s):
        count = 0
        text = ""
    text = text + s[count]  # s[count]=S when count = 0
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(200,slider)

#GUI Part
window = ttkthemes.ThemedTk() # similar to Tk class only

window.get_themes()
window.set_theme('arc')

window.geometry('1174x680+50+0')
window.resizable(0,0)
window.title('Student Management System')

# DISPLAY DATE-TIME
datetimeLabel = Label(window,font=('times new roman',20,'bold'),fg='orchid')
datetimeLabel.place(x=5,y=5)
clock()

# CREATING SLIDER TEXT
s = "Student Management System"
sliderLabel = Label(window,text=s,font=('arial',30,'italic bold'),fg='red',width=30)
sliderLabel.place(x=200,y=8)
slider()

# CREATING DATABASE BUTTON
connectButton = ttk.Button(window,text="Connect to Database",command=connect_database)
connectButton.place(x=980,y=25)

# CREATING LEFT FRAME
leftFrame = Frame(window)
leftFrame.place(x=50,y=80)

# ADDING LOGO IMAGE
logo_image = PhotoImage(file='logo_image.png')
logoLabel = Label(leftFrame,image=logo_image)
logoLabel.grid(row=0,column=0,pady=5)

# ADDING BUTTONS
addStudent = ttk.Button(leftFrame,text='Add Student',width=20,style='Y.TButton',state=DISABLED,command=add_student)
addStudent.grid(row=1,column=0,pady=12)
sty = ttk.Style() #Creating an instance of Style Object
sty.configure('Y.TButton',font=(None,15)) #Configuring the properties of button ; TButton is used for ttk.Button

searchStudent = ttk.Button(leftFrame,text='Search Student',width=20,style='Y.TButton',state=DISABLED,command=search_student)
searchStudent.grid(row=2,column=0,pady=12)
#sty = ttk.Style()
#sty.configure('big.TButton',font=(None,10))

deleteStudent = ttk.Button(leftFrame,text='Delete Student',width=20,style='Y.TButton',state=DISABLED,command=delete_student)
deleteStudent.grid(row=3,column=0,pady=12)
#sty = ttk.Style()
#sty.configure('big.TButton',font=(None,10))

updateStudent = ttk.Button(leftFrame,text='Update Student',width=20,style='Y.TButton',state=DISABLED,command=update_student)
updateStudent.grid(row=4,column=0,pady=12)
#sty = ttk.Style()
#sty.configure('big.TButton',font=(None,10))

showStudent = ttk.Button(leftFrame,text='Show Student',width=20,style='Y.TButton',state=DISABLED,command=show_student)
showStudent.grid(row=5,column=0,pady=12)
#sty = ttk.Style()
#sty.configure('big.TButton',font=(None,10))

exportStudent = ttk.Button(leftFrame,text='Export Student',width=20,style='Y.TButton',state=DISABLED,command=export_student)
exportStudent.grid(row=6,column=0,pady=12)
#sty = ttk.Style()
#sty.configure('big.TButton',font=(None,10))

exit = ttk.Button(leftFrame,text='Exit',width=20,style='Y.TButton',command=exit_student)
exit.grid(row=7,column=0,pady=12)
#sty = ttk.Style()
#sty.configure("big.TButton", font=(None, 15))

# CREATING RIGHT FRAME
rightFrame = Frame(window)
rightFrame.place(x=350,y=80,width=820,height=550)

# CREATING TREE VIEW

# CREATING SCROLLBAR
scrollbarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY = Scrollbar(rightFrame,orient=VERTICAL)


studentTable=ttk.Treeview(rightFrame,columns=('Enrollment Number','Name','Section','Year','Department','Mobile No','Email','Address','Gender','Date Of Birth','Added Date','Added Time'),
                          xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)  #set method is used to coonect the scrollbar to the other widget studentTable here. The other widget method for this connection is xscrollcommand or yscrollcommand.
# i.e set method of scrollbar connects with studentTable treeview with the help of xscrollcommand or yscrollcommand method

scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)  #fills both x & y axis

b = ttk.Style()  # tells tkinter that we are creating a style and we are storing it inside the variable b
b.configure("Treeview.Heading",font=(None,15,'bold'))  #Treeview.Heading is the name of the element for the column headings

studentTable.heading('Enrollment Number',text='Enrollment Number')
studentTable.heading('Name',text='Name')
studentTable.heading('Section',text='Section')
studentTable.heading('Year',text='Year')
studentTable.heading('Department',text='Department')
studentTable.heading('Mobile No',text='Mobile Number')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('Date Of Birth',text='Date Of Birth')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.config(show='headings')

studentTable.column('Enrollment Number',width=250,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Section',width=150,anchor=CENTER)
studentTable.column('Year',width=150,anchor=CENTER)
studentTable.column('Department',width=150,anchor=CENTER)
studentTable.column('Mobile No',width=250,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=250,anchor=CENTER)
studentTable.column('Gender',width=150,anchor=CENTER)
studentTable.column('Date Of Birth',width=250,anchor=CENTER)
studentTable.column('Added Date',width=250,anchor=CENTER)
studentTable.column('Added Time',width=250,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=35,font=('arial',12,'bold'),foreground='VioletRed4')

window.mainloop()