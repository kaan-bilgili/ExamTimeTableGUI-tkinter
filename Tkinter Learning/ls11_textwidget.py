from tkinter import *
def submit():
    input = text.get("1.0",END)
    print(input)
window = Tk()
window.geometry("300x300")
text = Text(window,
            bg ="light yellow",
            font = ("Ink Free",25),
            height = 20,
            width =20,
            padx =20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window,text="submit", command=submit)
button.pack()
window.mainloop()