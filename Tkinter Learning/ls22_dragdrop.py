from tkinter import *

def invert_hex(hex_color):
    hex_color = hex_color.lstrip('#')
    
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    r_inv = 255 - r
    g_inv = 255 - g
    b_inv = 255 - b

    return "#{:02X}{:02X}{:02X}".format(r_inv, g_inv, b_inv)


def tk_color_to_hex(color, widget):
    r, g, b = widget.winfo_rgb(color)
    return "#{:02x}{:02x}{:02x}".format(r//256, g//256, b//256)


window = Tk()
window.geometry("600x600")

label1 = Label(window, height=5, width=10, bg="#000000")
label1.pack(pady=100)

original_color = tk_color_to_hex(label1.cget("bg"), window)


invertedColor = invert_hex(original_color)


label2 = Label(window, height=5, width=10, bg=invertedColor)
label2.place(x=400, y=100)


#---------Drag Drop starts here---------
def drag1(event):
    widget = event.widget
    widget.startx = event.x
    widget.starty = event.y

def drag_motion1(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x
    y = widget.winfo_y() - widget.starty + event.y
    widget.place(x=x, y=y)

    

label1.bind("<Button-1>",drag1)
label1.bind("<B1-Motion>",drag_motion1)


label2.bind("<Button-1>",drag1)
label2.bind("<B1-Motion>",drag_motion1)


window.mainloop()
