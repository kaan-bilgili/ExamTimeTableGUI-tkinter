from tkinter import* 
def getValue():
    print(scale.get())


window = Tk()
icon = PhotoImage(file="C:\\Users\\Kaan\\Desktop\\tk\\GUI\\icon.png")
icon = icon.subsample(5,5)
smileLabel = Label(window,image=icon)
smileLabel.pack()

scale = Scale(window,from_=0,
              to=100,
              length=200,
              orient=VERTICAL,
              font=("consolas",8),
              tickinterval= 30, # adds numeric indicator
              showvalue= 1,  
              resolution=0.3,
              troughcolor="red",
              fg="red",
              bg= "black",
              width=100

              )
scale.set((scale["to"]-scale["from"])/2) # makes a default value
scale.pack()


button = Button(window,command=getValue,text="Get Value")
button.pack(anchor="center")




window.mainloop()