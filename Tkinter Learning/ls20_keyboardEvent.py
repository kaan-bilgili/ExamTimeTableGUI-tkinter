from tkinter import *

def funcUp(event):      #There must be a parameter 
    print("You pressed the ↑ ")
    print("You pressed :" + event.keysym)
    label.config(text=event.keysym)
    

window = Tk()

window.bind("<Key>",funcUp)  #<Key>  is for every single key
 

label = Label(window,font=("calibri",50),width="30")
label.pack()


window.mainloop()