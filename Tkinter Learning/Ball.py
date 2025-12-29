class Ball:
    def __init__(self,window,x,y,diameter,xVel,yVel,color):
        self.window=window
        self.image = window.create_oval(x,y,diameter,diameter,fill=color)
        self.xVel = xVel
        self.yVel = yVel
    
    def move(self):
        self.window.move(self.image,self.xVel,self.yVel)

        coords = self.window.coords(self.image)

        if coords[0] <= 0 or coords[2] >= self.window.winfo_width():
            self.xVel *= -1

        if coords[1] <= 0 or coords[3] >= self.window.winfo_height():
            self.yVel *= -1

        

