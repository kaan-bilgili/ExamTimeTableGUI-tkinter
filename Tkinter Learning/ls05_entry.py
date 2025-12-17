from tkinter import *

def submit():
    username = entry.get()
    print(f"Hello {username} ")
    return username

def delete():
    username=""
    print(f"{username} ")
    entry.delete(0,END)
   
def backspace():
    entry.delete(len(entry.get())-1 , END)

window= Tk()
window.title("ENTRY")

submit_button=Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button=Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button=Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=RIGHT)

entry = Entry()
entry.config(font=("arial",30),
            bg="black",
            fg="white",
            
            )

#entry.insert(0,"KaaN")   # def value
#entry.config(state=DISABLED) 
entry.config(width=10)
#entry.config(show="*")  # works for passwords!!
entry.pack()


window.mainloop()