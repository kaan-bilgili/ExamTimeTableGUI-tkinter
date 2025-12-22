from tkinter import *
def moveUp(event):
    widget = label1
    xpos = widget.winfo_x()
    ypos= widget.winfo_y()
    widget.place(x=xpos,y=ypos-20)

def moveDown(event):
    widget = label1
    xpos = widget.winfo_x()
    ypos= widget.winfo_y()
    widget.place(x=xpos,y=ypos+20)

def moveRight(event):
    widget = label1
    xpos = widget.winfo_x()
    ypos= widget.winfo_y()
    widget.place(x=xpos+20,y=ypos)

def moveLeft(event):
    widget = label1
    xpos = widget.winfo_x()
    ypos= widget.winfo_y()
    widget.place(x=xpos-20,y=ypos)

def moveUp(event):
    widget = label1
    xpos = widget.winfo_x()
    ypos= widget.winfo_y()
    widget.place(x=xpos,y=ypos-20)



window = Tk()
window.geometry("500x500")

photo = PhotoImage(file= "C:\\Users\\Kaan\\Desktop\\tk\\GUI\\Tkinter Learning\\icon2.png")
photo = photo.subsample(10,10)

label1 = Label(window,image=photo)
label1.pack()

window.bind("<w>",moveUp)
window.bind("<a>",moveLeft)
window.bind("<s>",moveDown)
window.bind("<d>",moveRight)

window.bind("<Up>",moveUp)
window.bind("<Left>",moveLeft)
window.bind("<Down>",moveDown)
window.bind("<Right>",moveRight)


window.mainloop()