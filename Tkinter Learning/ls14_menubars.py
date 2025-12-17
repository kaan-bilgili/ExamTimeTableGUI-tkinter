from tkinter import *
from tkinter import filedialog

def openFile():
    #filedialog returns string
    #initialdir sets the initial directory
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Kaan\\Desktop\\tk\\GUI",
                                          title="Open the file calmly",
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*"))) 
    if  not filepath :
        return
    else:
        myfile = open(filepath,"r")
        print(myfile.read())
        myfile.close()

def saveFile():
    print("File has been saved")

window = Tk()

menubar= Menu(window)
window.config(menu=menubar)

fileMenu= Menu(menubar,tearoff=0)  #tearoff gets rid off the unwanted dotted line
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Edit x")
editMenu.add_command(label="Edit y")
editMenu.add_separator()
editMenu.add_command(label="Exit",command=quit)



window.mainloop()