from tkinter import *
from time import *

def update():
    time_str = strftime("%I:%M:%S")
    time_label.config(text=time_str)

    day_str = strftime("%A")
    day_label.config(text=day_str)

    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)
                   

    window.after(1000,update)
window = Tk()

WIDTH = 15
time_label = Label(window,font=("Arial",50),fg="white",bg="black",
                   width=WIDTH)
time_label.pack()

day_label = Label(window,font=("Calibri",25),fg="black",bg="white",
                  width=time_label.cget("width"))
day_label.pack()


date_label = Label(window,font=("Calibri",25),fg="black",bg="white",
                   width=time_label.cget("width"))
date_label.pack()



update()


window.mainloop()