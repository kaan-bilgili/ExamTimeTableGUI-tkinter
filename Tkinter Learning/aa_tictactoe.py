from tkinter import *
import random
from tkinter import messagebox



def endGame(winner=None):
    global player1,player2;round
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')
    button4.config(state='disabled')
    button5.config(state='disabled')
    button6.config(state='disabled')
    button7.config(state='disabled')
    button8.config(state='disabled')
    button9.config(state='disabled')
    if round==9 and winner==None:
        messagebox.showinfo(title="It's a tie",
                        message="No one wins!",
                        )
    else:
        messagebox.showinfo(
                        "We have a winner",
                        f"{symbolToName[winner]} wins!"
)



def winner():
    global player1,player2
    buttons=[0,button1,button2,button3,button4,button5,button6,button7,button8,button9]
    
    if (buttons[1]["text"] == buttons[2]["text"] ==
        buttons[3]["text"] != ""): 
        endGame(button1["text"])
        return
    elif (buttons[4].cget("text") == buttons[5].cget("text") ==
        buttons[6].cget("text") != ""):
        endGame(button4.cget("text"))
        return
    elif (buttons[7].cget("text") == buttons[8].cget("text") ==
        buttons[9].cget("text") != ""):
        endGame(button7.cget("text"))
        return
    elif (buttons[1].cget("text") == buttons[4].cget("text") ==
        buttons[7].cget("text") != ""):
        endGame(button1.cget("text"))
        return
    elif (buttons[2].cget("text") == buttons[5].cget("text") ==
        buttons[8].cget("text") != ""):
        endGame(button2.cget("text"))
        return
    elif (buttons[3].cget("text") == buttons[6].cget("text") ==
        buttons[9].cget("text") != ""):
        endGame(button3.cget("text"))
        return
    elif (buttons[1].cget("text") == buttons[5].cget("text") ==
        buttons[9].cget("text") != ""):
        endGame(button1.cget("text"))
        return
    elif (buttons[3].cget("text") == buttons[5].cget("text") ==
        buttons[7].cget("text") != ""):
        endGame(button3.cget("text"))
        return
    if round == 9:
        endGame()
    
        
    


def newGame():
    global player1,player2,round
    round=0
    
    button1.config(text="",state='active')
    button2.config(text="",state='active')
    button3.config(text="",state='active')
    button4.config(text="",state='active')
    button5.config(text="",state='active')
    button6.config(text="",state='active')
    button7.config(text="",state='active')
    button8.config(text="",state='active')
    button9.config(text="",state='active')
    chooseStarter()

def click(button):
    global player1,player2,round
    if button.cget("text") == '':
        round+=1
        if player1Label.cget("bg") == "green":
            button.config(text=player1)
            player2Label.config(bg="green")
            player1Label.config(bg="white")

        else:
            button.config(text=player2)
            player1Label.config(bg="green")
            player2Label.config(bg="white")
    winner()




def chooseStarter():
    global player1,player2
    whoStarts = random.randint(0,1)

    if whoStarts == 0:
        player1Label.config(bg="green")
        player2Label.config(bg="white")
        player1="X"
        player2="O"
        player1Label.config(text="Kaan (X)")
        player2Label.config(text="Banu (O)")
    else:
        player2Label.config(bg="green")
        player1Label.config(bg="white")
        player1="O"
        player2="X"
        player1Label.config(text="Kaan (O)")
        player2Label.config(text="Banu (X)")



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


symbolToName = {
    "X": "Kaan",
    "O": "Banu"
}


player1=""
player2=""
round=0



chooseStarter()

window.mainloop()







    
    







