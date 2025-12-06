from tkinter import *
window = Tk()      #instantiate an instance of a windows
window.title("Labels in Tkinter")  #set the title of the window
window.geometry("500x500")  #set the size of the window

photo = PhotoImage(file= "C:\\Users\\Kaan\\Desktop\\tk\\icon.png")

label=Label(window,text="Hello World",
            font= ("Arial",40,"italic"), 
            fg="pink" , 
            bg = "black",
            border= 40,
            relief='sunken',
            padx=20,
            pady=20,
            image=photo, 
            compound=BOTTOM 
            
            )
label.pack()

label2= Label(window , text="Hello Earth" , font=("calibri",12,"bold"))
label2.place(x=0, y=0)

window.config(background="lightblue")
window.mainloop()