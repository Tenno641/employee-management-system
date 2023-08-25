from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Students.db")

#initializing program window
window = Tk()
window.title("Students Management System")
window.geometry("1600x800+0+10")
window.configure(bg='#424549')
window.resizable(False, False)

code = StringVar()
name = StringVar()
email = StringVar()
gender = StringVar()
phone = StringVar()
city = StringVar()


#initializing entries form
entriesForm = Frame(window, bg="#1e2124")
entriesForm.place(x=10, y=10, width=400, height=780)


#Form title 
formTitle = Label(entriesForm, text="Students Management System", font=('', 16, 'bold'), bg="#1e2124", fg="white")
formTitle.place(x=40, y=30)


#Form entries
#Code
codelbl = Label(entriesForm, text="Code", font=('', 16, 'bold'), bg="#1e2124", fg="white")
codelbl.place(x=20, y=100)
stuCode = Entry(entriesForm, textvariable=code, font=('', 16))
stuCode.place(x=120, y=100) 

#Name
namelbl = Label(entriesForm, text="Name", font=('', 16, 'bold'), bg="#1e2124", fg="white")
namelbl.place(x=20, y=160)
stuName = Entry(entriesForm, textvariable=name, font=('', 16))
stuName.place(x=120, y=160)

#Email
emaillbl = Label(entriesForm, text="E-mail", font=('', 16, 'bold'), bg="#1e2124", fg="white")
emaillbl.place(x=20, y=220)
stuEmail = Entry(entriesForm, textvariable=email, font=('', 16))
stuEmail.place(x=120, y=220)

#Gender
genderlbl = Label(entriesForm, text="Gender", font=('', 16, 'bold'), bg="#1e2124", fg="white")
genderlbl.place(x=20, y=280)
stuGender = ttk.Combobox(entriesForm, textvariable=gender, font=('', 16), width=18, state="readonly")
stuGender['values'] = ("Male", "Female")
stuGender.place(x=120, y=280)

#Phone
phonelbl = Label(entriesForm, text="Phone", font=('', 16, 'bold'), bg="#1e2124", fg="white")
phonelbl.place(x=20, y=340)
stuPhone = Entry(entriesForm, textvariable=phone, font=('', 16))
stuPhone.place(x=120, y=340)

#City
citylbl = Label(entriesForm, text="City", font=('', 16, 'bold'), bg="#1e2124", fg="white")
citylbl.place(x=20, y=400)
stuCity = Entry(entriesForm, textvariable=city, font=('', 16))
stuCity.place(x=120, y=400)

#Buttons functions

def getData(event):
    selected_row = tabelView.focus()
    data = tabelView.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    code.set(row[1])
    name.set(row[2])
    email.set(row[3])
    gender.set(row[4])
    phone.set(row[5])
    city.set(row[6])

def dispalyAll():
    tabelView.delete(*tabelView.get_children())
    for row in db.fetch():
        tabelView.insert("", END, values=row)


def add_student():
    if stuCode.get() == "" or stuName.get() == "" or stuEmail.get() == "" or stuGender.get() == "" or stuPhone.get() == "" or stuCity.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(stuCode.get(),stuName.get(), stuEmail.get() , stuGender.get() ,stuPhone.get(), stuCity.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_student():
    if stuCode.get() == "" or stuName.get() == "" or stuEmail.get() == "" or stuGender.get() == "" or stuPhone.get() == "" or stuCity.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0], stuCode.get(),stuName.get(), stuEmail.get() , stuGender.get() ,stuPhone.get(), stuCity.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_student():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    code.set("")
    name.set("")
    email.set("")
    gender.set("")
    phone.set("")
    city.set("")




#Buttons frame
btnFrame = Frame(entriesForm, bg="#1e2124")
btnFrame.place(x=10, y=460, width=380, height=250)

#Add
addBtn = Button(btnFrame, text="Add", font=('', 16, 'bold'), command=add_student, bg="#7289da", fg="white").place(x=35, y=30, width=300)

#Delete
addDelete = Button(btnFrame, text="Delete", font=('', 16, 'bold'), command=delete_student, bg="#7289da", fg="white").place(x=35, y=80, width=300)

#Update
addUpdate = Button(btnFrame, text="Update", font=('', 16, 'bold'), command=update_student, bg="#7289da", fg="white").place(x=35, y=130, width=300)

#Clear
addClear = Button(btnFrame, text="Clear", font=('', 16, 'bold'), command=clearAll, bg="#7289da", fg="white").place(x=35, y=180, width=300)


#Table Form
tabelFrame = Frame(window)
tabelFrame.place(x=420, y=10, width=1170, height=780)

#Table Heading
tabelView = ttk.Treeview(tabelFrame, columns=(1, 2, 3, 4, 5, 6, 7))

tabelView.heading("1", text="No.")
tabelView.column("1", width=20)

tabelView.heading("2", text="Code")

tabelView.heading("3", text="Name")

tabelView.heading("4", text="E-mail")

tabelView.heading("5", text="Gender")
tabelView.column("5", width=50)

tabelView.heading("6", text="Phone")

tabelView.heading("7", text="City")
tabelView.column("7", width=50)

tabelView['show'] = 'headings'
tabelView.bind("<ButtonRelease-1>", getData)
tabelView.pack(fill=X)


dispalyAll()
window.mainloop()
