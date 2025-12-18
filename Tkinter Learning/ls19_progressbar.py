from tkinter import *
from tkinter.ttk import *
import time

def manuel():
    print("nothing")
    # bar.start()       triggers animations in indeterminate mode
    bar["value"]+= 10
    percent.set("%"+str(bar["value"]))
    if bar["value"] > 101:
        time.sleep(1)
        window.quit()

def auto():
    tasks=10
    x=0
    while(x<tasks):
        time.sleep(1)
        bar["value"]+=10
        x+=1
        percent.set("%"+str((x/ tasks)*100))
        window.update_idletasks()
        time.sleep(1)
        window.quit()


window = Tk()

percent = StringVar()
percent.set("%0")

bar= Progressbar(window,
                 orient="horizontal",
                 length=500,
                 mode="determinate"
                 )

bar.pack(pady=10)

percentLabel=Label(window,textvariable=percent,foreground="black").pack()

manuelbutton = Button(window,text="Install",command=manuel)
manuelbutton.pack()

autobutton = Button(window,text="Download",command=auto)
autobutton.pack()




window.mainloop()