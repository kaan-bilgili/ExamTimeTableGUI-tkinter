from tkinter import *
from tkinter import colorchooser 

def invert_hex(hex_color):
    hex_color = hex_color.lstrip('#')
    
    
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    
    r_inv = 255 - r
    g_inv = 255 - g
    b_inv = 255 - b

    
    return "#{:02X}{:02X}{:02X}".format(r_inv, g_inv, b_inv)



def click():
    color = colorchooser.askcolor()[1]
    if color :
        button.config(bg=color) 
        window.config(bg = invert_hex(color))



window = Tk()
window.geometry("420x420")

button = Button(text="Click to choose a color",command=click)
button.pack()

window.mainloop()