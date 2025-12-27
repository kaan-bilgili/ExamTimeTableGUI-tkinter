from tkinter import *
import random


def newGame():
    global player1,player2
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")
    chooseStarter()

def click(button):
    global player1,player2
    if button.cget("text") == '':
        if player1Label.cget("bg") == "green":
            button.config(text=player1)
            player2Label.config(bg="green")
            player1Label.config(bg="white")

        else:
            button.config(text=player2)
            player1Label.config(bg="green")
            player2Label.config(bg="white")





def chooseStarter():
    global player1,player2
    whoStarts = random.randint(0,1)

    if whoStarts == 0:
        player1Label.config(bg="green")
        player2Label.config(bg="white")
        player1="X"
        player2="O"
    else:
        player2Label.config(bg="green")
        player1Label.config(bg="white")
        player1="O"
        player2="X"



window = Tk()

mainlabel=Label(text="TIC TAC TOE",font=("Calibri",48))
mainlabel.grid(row=0,column=0,columnspan=3)
mainlabel.config(padx=4)
newGameButton = Button(window,text="New Game",font=("Calibri",12,"bold"),command=newGame)
newGameButton.grid(row=1,column=1,columnspan=1,pady=10)
player1Label=Label(text="Kaan",font=("free ink",12))
player1Label.grid(row=1,column=0)
player2Label=Label(text="Banu",font=("free ink",12,))
player2Label.grid(row=1,column=2)


button1=Button(text="",width=6,height=3,command=lambda: click(button1))
button1.grid(row=2,column=0,sticky="nsew")

button2=Button(text="",width=6,height=3,command=lambda: click(button2))
button2.grid(row=2,column=1,sticky="nsew")

button3=Button(text="",width=6,height=3,command=lambda: click(button3))
button3.grid(row=2,column=2,sticky="nsew")

button4=Button(text="",width=6,height=3,command=lambda: click(button4))
button4.grid(row=3,column=0,sticky="nsew")

button5=Button(text="",width=6,height=3,command=lambda: click(button5))
button5.grid(row=3,column=1,sticky="nsew")

button6=Button(text="",width=6,height=3,command=lambda: click(button6))
button6.grid(row=3,column=2,sticky="nsew")

button7=Button(text="",width=6,height=3,command=lambda: click(button7))
button7.grid(row=4,column=0,sticky="nsew")

button8=Button(text="",width=6,height=3,command=lambda: click(button8))
button8.grid(row=4,column=1,sticky="nsew")

button9=Button(text="",width=6,height=3,command=lambda: click(button9) )
button9.grid(row=4,column=2,sticky="nsew")

for i in range(3):
    window.grid_columnconfigure(i, weight=1)

for i in range(2, 5):
    window.grid_rowconfigure(i, weight=1)


player1=""
player2=""


chooseStarter()








window.mainloop()







    
    







