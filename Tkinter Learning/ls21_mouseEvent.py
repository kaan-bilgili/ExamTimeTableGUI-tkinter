from tkinter import *

def func(event):
    print("You clicked at : "+ str(event.x) + ", " + str(event.y)) 


window = Tk()


#window.bind("<Button-1>",func)
#button-1 is left click
#button-2 is middle click
#button-3 is right click
#window.bind("<ButtonRelease-1>",func)  #this one is for releasing the left click
#window.bind("<Double-1>",func)        #this one is for double left click
#window.bind("<Enter>",func)          #this one is for entering the window
#window.bind("<Leave>",func)          #this one is for leaving the window
window.bind("<Motion>",func)         #this one is for moving, goood  for games and paint apps

window.mainloop()