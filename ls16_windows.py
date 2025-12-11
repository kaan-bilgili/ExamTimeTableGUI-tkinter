from tkinter import * 

def newWindow():
    # top level and Tk difference
    # when we use Tk it creates a main window but when we use Toplevel it creates a child window
    new_window = Toplevel()
    newest_window = Tk()

    newest_window.title("This is a newest window")
    newest_window.geometry("200x100")  

    new_window.title("This is a new window")
    new_window.geometry("200x100")  
    window.destroy() # new window dies since they re connected
    

window= Tk()



button =Button(window,text="New window",command=newWindow).pack()

window.mainloop()