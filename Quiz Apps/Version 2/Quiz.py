#Importing Modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter


def Clear():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    number_entry.delete(0, END)
    mail_entry.delete(0, END)
    v.set(0)


def quit_win():
    bl = messagebox.askquestion("Question", "Do you want to quit")
    if (bl == 'yes'):
        root.quit()


def insert_data():
    fw = open("User_Information.txt", 'a')
    name = name_entry.get()

    age = age_entry.get()
    if (not (age.isnumeric() and (int(age) in range(1, 100)))):
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

    out_line = "Name: {}".format(name) + "\t" + "Age: {}".format(age) + "\t" + "Gender: {}".format(gender) + "\t" + "Phone Number: {}".format(ph_no) + "\t" + "E-Mail: {}".format(mail)
    fw.write(out_line)
    messagebox.showinfo("Congratulation", 'Record Inserted Successfully')


def Insert_Data():
    flag = 0

    try:
        fr = open("User_Information.txt", 'r')
        email_set = set()
        for line in fr:
            email_str = line.split("\t")[4]
            email_set.add(email_str.strip())

        if (mail_entry.get() in email_set):
            flag = 1

        fr.close()
    except Exception as e:
        print(e)

    if flag == 1:
        messagebox.showerror("Error", "User Already Exists")
    else:
        insert_data()


root = tkinter.Tk()
# root.geometry('500x300')
root.geometry('800x500')
root.resizable(0, 0)
root.title('Quiz Registration Form')

## Create a Labels


title = ttk.Label(text = 'QUIZ REGISTRATION', font = ('calibri', 18, 'bold')) 
name_label = ttk.Label(text='Name :')
age_label = ttk.Label(text='Age :')
gender_label = ttk.Label(text='Gender :')
number_label = ttk.Label(text='Phone Number :')
mail_label = ttk.Label(text='Email id :')


title.place(x=290, y=17)
name_label.place(x=263, y=59)
age_label.place(x=263, y=96)
gender_label.place(x=263, y=154)
number_label.place(x=263, y=199)
mail_label.place(x=263, y=237)

## Create a Entry Fields And Radio Button For Form

name_entry = Entry()
age_entry = Entry()

v = IntVar()
gender1 = ttk.Radiobutton(text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(text='Female', value=2, variable=v)

number_entry = Entry()
mail_entry = Entry()

name_entry.place(x=435, y=59)
age_entry.place(x=435, y=96)
gender1.place(x=435, y=139) 
gender2.place(x=435, y=167)
number_entry.place(x=435, y=199)
mail_entry.place(x=435, y=237)

## Create Buttons
submit = Button(text='Submit', command=Insert_Data, width=17, height = 2, relief = "solid")
submit.place(x=321, y=370)

clear = Button(text='Clear', command=Clear, width = 16, height = 2, relief = "solid" )
clear.place(x=400, y=310)

exit = Button(text='Exit', command=quit_win, width = 16, height = 2, relief = "solid")
exit.place(x=242, y=310)



        
root.mainloop()
