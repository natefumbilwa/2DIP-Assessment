#Importing Modules
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter
import os
import random
from tkinter.font import BOLD
import json

#Defining function that prints user's information
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

    out_line = "Name: {}".format(name) + "\t" + "Age: {}".format(age) + "\t" + "Gender: {}".format(gender) + "\t" + "Phone Number: {}".format(ph_no) + "\t" + "E-Mail: {}".format(mail)
    print(out_line)
    messagebox.showinfo("Congratulation", 'Record Inserted Successfully')
    quiz()

#Defing the quiz function
def quiz():
    global quiz, frame 
    frame = Frame(root)
    frame.pack(side="top", expand=True, fill="both")

    for widgets in frame.winfo_children():
        widgets.destroy()

    quiz = Quiz()

#Creates window
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

#Placing entry box titles
title.place(x=290, y=17)
name_label.place(x=263, y=59)
age_label.place(x=263, y=96)
gender_label.place(x=263, y=154)
number_label.place(x=263, y=199)
mail_label.place(x=263, y=237)

#Creating entry boxes
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

#Creating submit Button
submit = Button(text='Submit', command=insert_data, width=17, height = 2, relief = "solid")
submit.place(x=341, y=370)

#Beginning Quiz
class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.score = 0

#Defining quiz question
    def question(self, qn):
        t = Label(root, text="Quiz on the New Zealand Road Code", width="50", bg="white", fg="black", font=("futura", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], font=("times", 16, "bold"), anchor="center")
        qn.place(x=70, y=70)
        return qn

#Defining radio buttons
    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 45
        return b

#Displays answer options
    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
              self.opts[val]['text'] = op
              val += 1

#Creates Buttons in quiz
    def buttons(self):
        nbutton = Button(root, text="Next",command=self.nextbtn, border = 4, width=10,bg="green",fg="white",font=("helvitica",16,"bold"))
        nbutton.place(x=340,y=380)

        
#Defining functions
    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
             return True
        
    def nextbtn(self):
        if self.checkans(self.qn):
            self.score += 1
        self.qn += 1
        if self.qn == len(q):
            self.end_quiz()
        else:
            self.display_options(self.qn)       
        
    def end_quiz(self):
        print("You Scored: {}".format(self.score))
        root.destroy()



with open('quiz.json') as f:
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])

root.mainloop()
