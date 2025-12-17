from tkinter import *

def printer():
    if var1.get() == 0:
        print("urnot super")
    else:
        print("ur super")

def printer2():
    if var2.get() == 0:
        print("ur nice")
    else:
        print("ur nicest")



window = Tk()
window.geometry("500x500")

label = Label(window,text="Hello",font=("arial",30,"italic"))
label2 =Label(window,text="Checkboxes",
              font=("arial",12,"bold"),justify="left",compound="left")
label.pack()
label2.place(x=0,y=100)



icon = PhotoImage(file="C:\\Users\\Kaan\\Desktop\\tk\\GUI\\icon.png")
icon=icon.subsample(6,6)

var1 = IntVar()
var2= IntVar()
checkbox = Checkbutton(window,text="Is your name karya?",variable=var1,onvalue=1 , offvalue= 0,command=printer)
checkbox.config(image=icon,
                compound="right" 
                )
checkbox.place(x=0,y=120)


checkbox2 = Checkbutton(window,text="Is your name kaan?",variable=var2,command=printer2)
checkbox2.config(image=icon,
                compound="right" 
                )
checkbox2.place(x=0,y=200)


window.mainloop()