from tkinter import *

window = Tk()      #instantiate an instance of a windows
window.geometry("500x300")  #set the size of the window
window.title("Introduction to Tkinter")  #set the title of the window

icon = PhotoImage(file="C:\\Users\\Kaan\\Desktop\\tk\\GUI\\icon.png")  #load an icon image
window.iconphoto(True, icon) #set the icon of the window

window.config(background="lightblue")  #set the background color of the window
window.mainloop()   #place window on a computer screen , listen 

