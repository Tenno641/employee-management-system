from tkinter import *
from tkinter import ttk
import database

#initializing the project's window
window = Tk()
window.title('Students Management System')
window.geometry('1200x600+50+50')
window.resizable(False, False)
window.configure(bg='#36393e')

#initializing student form
infoForm = Frame(window, bg='#1e2124')
infoForm.place(x=10, y=10, width=300, height=580)

#initializing the student form title
titleForm = Label(infoForm, text='Students Informations', font=('', 13, 'bold'), fg='#ffffff', bg='#1e2124')
titleForm.place(x=10, y=10, height=50)

#initializing student details
#Name
nameBox = Label(infoForm, text='Name', font=(13), fg='#ffffff', bg='#1e2124')
nameBox.place(x=10, y=70)
stuName = Entry(infoForm, width=20, font=(12))
stuName.place(x=80, y=70)

#ID
idBox = Label(infoForm, text='ID', font=(13), fg='#ffffff', bg='#1e2124')
idBox.place(x=10, y=120)
stuId = Entry(infoForm, width=20, font=(12))
stuId.place(x=80, y=120)

#Gender
genderBox = Label(infoForm, text='Gender', font=(13), fg='#ffffff', bg='#1e2124')
genderBox.place(x=10, y=170)
stuGender = ttk.Combobox(infoForm, width=18, font=(12), state='readonly')
stuGender['values'] = ("Male", "Female")
stuGender.place(x=80, y=170)

#Phone 
phoneBox = Label(infoForm, text='Phone', font=(13), fg='#ffffff', bg='#1e2124')
phoneBox.place(x=10, y=220)
stuPhone = Entry(infoForm, width=20, font=(12))
stuPhone.place(x=80, y=220)

#E-mail
emailBox = Label(infoForm, text='E-mail', font=(13), fg='#ffffff', bg='#1e2124')
emailBox.place(x=10, y=270)
stuEmail = Entry(infoForm, width=20, font=(12))
stuEmail.place(x=80, y=270)

#City
cityBox = Label(infoForm, text='City', font=(13), fg='#ffffff', bg='#1e2124')
cityBox.place(x=10, y=320)
stuCity = Entry(infoForm, width=20, font=(12))
stuCity.place(x=80, y=320)

