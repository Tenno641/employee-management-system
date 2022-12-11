from tkinter import *
from tkinter import ttk

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

