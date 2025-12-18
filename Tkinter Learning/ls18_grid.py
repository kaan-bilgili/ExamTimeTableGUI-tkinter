from tkinter import *

window = Tk()

titleLabel = Label(window,text="User Information",font=("Arial",16)).grid(row=0,column=0,columnspan=2)

fnLabel = Label(window,text="First Name",width=15,background="brown").grid(row=1,column=0)
fnEntry = Entry(window).grid(row=1,column=1)

lnLabel = Label(window,text="Last Name",width=25,background="pink").grid(row=2,column=0)
lnEntry = Entry(window).grid(row=2,column=1)
mailLabel = Label(window,text="Email",width=30,background="red").grid(row=3,column=0)
mailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit",width=20,background="lightblue").grid(row=4,column=0,columnspan=2)



window.mainloop()