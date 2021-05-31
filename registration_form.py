from tkinter import *
from tkinter import ttk

window=Tk()

window.title("Registration Form")
window.geometry('600x600')
window.configure(background= "Yellow");

a = Label(window,width = 8,height = 2,font=("bold",10),text="First Name").grid(row = 0,column = 0)
b = Label(window,width = 8,height = 2,font=("bold",10),text="Last Name").grid(row = 1,column = 0)
c = Label(window,width = 8,height = 2,font=("bold",10),text="Course").grid(row = 2,column = 0)
d = Label(window,width = 8,height = 2,font=("bold",10),text="Semester").grid(row = 3,column = 0)
e = Label(window,width = 8,height = 2,font=("bold",10),text="Branch").grid(row = 4,column = 0)
f = Label(window,width = 8,height = 2,font=("bold",10),text="Email-id").grid(row = 5,column = 0)
g = Label(window,width = 8,height = 2,font=("bold",10),text="Contact-No").grid(row = 6,column = 0)
h = Label(window,width = 8,height = 2,font=("bold",10),text="Address").grid(row = 7,column = 0)
i = Label(window,text="Gender",font=("bold",10),width = 8).grid(row =8,column = 0)
var = IntVar()
Radiobutton(window,text="Male",variable=var,value=1).grid(row = 8,column = 1)
Radiobutton(window,text="Female",variable=var,value=2).grid(row = 8,column = 2)


a1 = Entry(window,).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
f1 = Entry(window).grid(row = 5,column = 1)
g1 = Entry(window).grid(row = 6,column = 1)
h1 = Entry(window).grid(row = 7,column = 1)


def clicked():
    res ="welcome to " +txt.get()
    lbl.configure(text=res)

btn = ttk.Button(window,width=20,text="submit").place(x=240,y=380) 


window.mainloop()


