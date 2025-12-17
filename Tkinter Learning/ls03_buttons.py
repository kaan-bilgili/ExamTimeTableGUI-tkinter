from tkinter import *

def click():
    print("Hello")

window =Tk()
window.geometry("300x300")
icon = PhotoImage(file="C:\\Users\\Kaan\\Desktop\\tk\\GUI\\icon.png")  #load an icon image


button = Button(window, text="Click or DIEEE")
button.config(command=click,
              font=("arial",25,'bold'),
                fg="blue",
                bg="lightblue",
                activebackground="red",
                activeforeground="pink"
              )
button.pack()
# button.config(state=DISABLED)

label= Label(window , text="smile if ur happy",
             image= icon,
             compound='bottom',
             fg="red"
             )
label.pack()









window.mainloop()