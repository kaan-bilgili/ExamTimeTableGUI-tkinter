from tkinter import *
import time

WIDTH=500
HEIGHT=500

xVelocity = 3
yVelocity=2


window = Tk()
bgphoto = PhotoImage(file= "C:\\Users\\Kaan\\Downloads\\pngwing.com.png")
bgphoto = bgphoto.subsample(2,2)

photo = PhotoImage(file= "C:\\Users\\Kaan\\Desktop\\tk\\GUI\\Tkinter Learning\\icon2.png")
photo = photo.subsample(20,20)

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

bg= canvas.create_image(0,0,image=bgphoto,anchor=NW)
my_ufo= canvas.create_image(0,0,image=photo,anchor=NW)


photo_width = photo.width()
photo_height= photo.height()

while True:
    coordinates = canvas.coords(my_ufo)
    canvas.move(my_ufo,xVelocity,yVelocity)
    if (canvas.coords(my_ufo)[0]) > WIDTH-photo_width:
        xVelocity = xVelocity*-1
    elif(canvas.coords(my_ufo)[0]) < 0:
        xVelocity = xVelocity*-1

    if (canvas.coords(my_ufo)[1]) > HEIGHT-photo_height:
        yVelocity = yVelocity*-1
    elif(canvas.coords(my_ufo)[1]) < 0:
        yVelocity = yVelocity*-1


    window.update()
    time.sleep(0.01)



window.mainloop()