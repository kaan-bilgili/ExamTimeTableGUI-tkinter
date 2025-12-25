from tkinter import * 



def clickbutton(value):
    global equation
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(value))
    equation = (str(current)+str(value))


def clear():
    entry.delete(0,END)



def equal():
    global equation
    equation=entry.get()
    result=eval(equation)
    entry.delete(0,END)
    entry.insert(0,result)

def backspace():
    entry.delete(len(entry.get())-1 , END)

    
equation=""

window = Tk()
window.title("Calculator") 


entry=Entry(width=22,borderwidth=1,font=("Calibri",15))
entry.grid(row=0,column=1,columnspan=3)

buttonbackspace=Button(text="<-",width=4,height=2,command=backspace)
buttonbackspace.grid(row=0,column=4)

buttondelete=Button(text="DEL",width=9,height=4,command=clear)

button1=Button(text="1",width=9,height=4,command=lambda:clickbutton(1))
button2=Button(text="2",width=9,height=4,command=lambda:clickbutton(2))
button3=Button(text="3",width=9,height=4,command=lambda:clickbutton(3))
button4=Button(text="4",width=9,height=4,command=lambda:clickbutton(4))
button5=Button(text="5",width=9,height=4,command=lambda:clickbutton(5))
button6=Button(text="6",width=9,height=4,command=lambda:clickbutton(6))
button7=Button(text="7",width=9,height=4,command=lambda:clickbutton(7))
button8=Button(text="8",width=9,height=4,command=lambda:clickbutton(8))
button9=Button(text="9",width=9,height=4,command=lambda:clickbutton(9))
button0=Button(text="0",width=9,height=4,command=lambda:clickbutton(0))
buttonsum=Button(text="+",width=9,height=4,command=lambda:clickbutton("+"))
buttonminus=Button(text="-",width=9,height=4,command=lambda:clickbutton("-"))
buttonmultiply=Button(text="*",width=9,height=4,command=lambda:clickbutton("*"))
buttondivide=Button(text="/",width=9,height=4,command=lambda:clickbutton("/"))
buttonequal=Button(text="=",width=9,height=4,command=equal)







button1.grid(row=2,column=1)
button2.grid(row=2,column=2)
button3.grid(row=2,column=3)
button4.grid(row=3,column=1)
button5.grid(row=3,column=2)
button6.grid(row=3,column=3)
button7.grid(row=4,column=1)
button8.grid(row=4,column=2)
button9.grid(row=4,column=3)
button0.grid(row=5,column=2)
buttonsum.grid(row=2,column=4)
buttonminus.grid(row=3,column=4)
buttonmultiply.grid(row=4,column=4)
buttondivide.grid(row=5,column=4)
buttonequal.grid(row=5,column=3)
buttondelete.grid(row=5,column=1)








window.mainloop()