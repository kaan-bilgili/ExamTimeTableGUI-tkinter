from tkinter import *


count = 0
def click():
    global count
    count +=1
    label.config(text=count)



window = Tk()
icon = PhotoImage(file="C:\\Users\\Kaan\\Desktop\\tk\\GUI\\icon.png")

button = Button(window, text="zikirmatik ")
button.config(command=click,
              font=("arial",25,'bold'),
                fg="blue",
                bg="lightblue",
                activebackground="red",
                activeforeground="pink",
                image=icon,
                compound="bottom"
              )
button.pack()

label = Label(window, text=count)
label.config(font=("arial",25))
label.pack()

window.mainloop()



