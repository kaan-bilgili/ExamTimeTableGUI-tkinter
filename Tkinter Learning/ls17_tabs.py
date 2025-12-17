from tkinter import *
from tkinter import ttk

window = Tk()


notebook = ttk.Notebook(window) # Create a notebook widget 

tab1 = Frame(notebook) # new frame for tab1
tab2 = Frame(notebook) 
notebook.add(tab1,text="Tab1",)
notebook.add(tab2,text="Tab2")
notebook.pack( expand=True, fill="both" )

Label(tab1,text="t1",width=25,height=25).pack(side="bottom")
Label(tab2,text="t2",width=25,height=25).pack(side="bottom")
window.mainloop()
