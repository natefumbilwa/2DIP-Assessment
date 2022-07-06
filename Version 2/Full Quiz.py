#Import Modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter

#Defining function that displays user's info
def insert_data():
    name = name_entry.get()

    age = age_entry.get()
    if (not (age.isnumeric() and (int(age) in range(15, 100)))):
        messagebox.showerror("Error", 'Please enter a Valid Age')
        raise Exception("Please enter a Valid Age")

    gen_val = v.get()

    gender = ''
    if gen_val == 1:
        gender = 'Male'
    elif gen_val == 2:
        gender = 'Female'
    else:
        gender = 'Non-Binary'

    ph_no = number_entry.get()
    if (not (ph_no.isnumeric() and len(ph_no) == 10)):
        messagebox.showerror("Error", 'Please enter a Valid Phone Number')
        raise Exception("Please enter a Valid Phone Number")

    mail = mail_entry.get()
    if (not ("@" in mail)):
        messagebox.showerror("Error", 'Please enter a Valid Mail Id')
        raise Exception("Please Enter Valid Mail Id")

    out_line = "Name: {}".format(name) + "\t" + "Age: {}".format(age) + "\t" + "Gender: {}".format(gender) + "\t" + "Phone Number: {}".format(ph_no) + "\t" + "E-Mail: {}".format(mail) + "\t" 
    print(out_line)
    messagebox.showinfo("Congratulation", 'Record Inserted Successfully')

#Creates Window
root = tkinter.Tk()
# root.geometry('500x300')
root.geometry('800x500')
root.resizable(0, 0)
root.title('Road Code Quiz')

#Creating Labels
title = ttk.Label(text = 'QUIZ REGISTRATION', font = ('calibri', 18, 'bold')) 
name_label = ttk.Label(text='Name :')
age_label = ttk.Label(text='Age :')
gender_label = ttk.Label(text='Gender :')
number_label = ttk.Label(text='Phone Number :')
mail_label = ttk.Label(text='Email id :')

#Placing  Entry Box titles
title.place(x=290, y=17)
name_label.place(x=263, y=59)
age_label.place(x=263, y=96)
gender_label.place(x=263, y=154)
number_label.place(x=263, y=199)
mail_label.place(x=263, y=237)

#Creating Entry Fields And Radio Button For Form
name_entry = Entry()
age_entry = Entry()

v = IntVar()
gender1 = ttk.Radiobutton(text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(text='Female', value=2, variable=v)

number_entry = Entry()
mail_entry = Entry()

#Placing the Entry boxes
name_entry.place(x=435, y=59)
age_entry.place(x=435, y=96)
gender1.place(x=435, y=139) 
gender2.place(x=435, y=167)
number_entry.place(x=435, y=199)
mail_entry.place(x=435, y=237)

## Create Buttons
submit = Button(text='Submit', command=insert_data, width=17, height = 2, relief = "solid")
submit.place(x=341, y=370)

root.mainloop()
