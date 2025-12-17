from tkinter import *

window=Tk()
frame = Frame(window)

Button(frame,text="W",font=("calibri",20,'bold'),width=3).pack(side="top")
Button(frame,text="A",font=("calibri",20,'bold'),width=3).pack(side="left")
Button(frame,text="S",font=("calibri",20,'bold'),width=3).pack(side="left")
Button(frame,text="D",font=("calibri",20,'bold'),width=3).pack(side="left")
frame.config(border=12,bg="gray",relief="sunken")
frame.place(x=10,y=10)

window.mainloop()