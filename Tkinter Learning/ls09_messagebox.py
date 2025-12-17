from tkinter import *
from tkinter import messagebox

def click():

    #messagebox.showinfo
    #messagebox.showerror
    #messagebox.showwarning
    
    
    messagebox.showinfo(title="U got scammed",
                        message="Ur dumb",
                    )
    
    if messagebox.askokcancel(title="You sure??",message="Do you still want free money?"):
        print("Here you go")
    else:
        print("Ur loss")
    

    answer = messagebox.askquestion(title="Question",message="Do you still want money")
    print(answer)
    if answer == "yes":
        messagebox.showinfo(title="Congrats",message="Yo yo ur rich now")
    else:
        messagebox.showinfo(title="So sad",message=":(")

        
    answer = messagebox.askyesnocancel(title="Last Question",message="Do you want to try again?",icon="warning")
    if answer == True:
        print("User wants to try again")
    elif answer == False:
        print("User does not want to try again")
    else:
        print("User cancelled")
             
window = Tk()
window.geometry("300x300")
button= Button(window,command=click,text="Free Money",font=("calibri",30,"bold"))
button.pack()



window.mainloop()