from tkinter import *

def getVal():
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),addEntry.get())
    addEntry.delete(0,END)
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())




window = Tk()
window.geometry("200x200")

subbutton =  Button(window,text=("GET VALUE"),
                 font=("calibri",15),
                 command=getVal)
subbutton.pack()







listbox = Listbox(window,fg="lightblue",
                  width=22)
listbox.insert(0,"kaan")
listbox.insert(1,"karya")
listbox.insert(2,"beyza")
listbox.insert(3,"evren")

listbox.config(height=listbox.size())

listbox.pack()

addEntry = Entry(window)
addEntry.pack()

addButton = Button(window,text="ADD",command=add)
addButton.pack()

deleteButton = Button(window,text="DELETE", command=delete)
deleteButton.pack()

window.mainloop()