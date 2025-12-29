from tkinter import *
import time
from Ball import *

window= Tk()
WIDTH=500
HEIGHT=500

canvas = Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()

volley_ball = Ball(canvas,0,0,80,1,1,"white")
tennis_ball = Ball(canvas,100,100,40,2,3,"yellow")
football_ball = Ball(canvas,200,200,60,3,2,"brown")




while True:
    volley_ball.move()
    tennis_ball.move()
    football_ball.move()
    window.update()
    time.sleep(0.01)
window.mainloop()