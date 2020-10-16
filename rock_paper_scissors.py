import tkinter
from tkinter import *
import random as r
import time


#Button Press Functions starts here ->
computer = ['ROCK','PAPER','SCISSORS']
cScore = int(0)
pScore = int(0)


def buttonRock_isClicked():
    global cScore
    global pScore

    data3.set('You Chose: ROCK')
    textBox3['image'] = rockImage

    computerChoice = computer[r.randint(0,2)]
    time.sleep(0.1)
    data5.set('Computer Chose: %s'%computerChoice)
    if computerChoice is 'ROCK':
        textBox5['image'] = rockImage
    elif computerChoice is 'PAPER':
        textBox5['image'] = paperImage
    else:
        textBox5['image'] = scissorsImage

    if computerChoice is 'SCISSORS':
        pScore = pScore + 1
        dataWinner.set('You win this round! Congratulations!')
    elif computerChoice is 'PAPER':
        cScore = cScore + 1
        dataWinner.set('Computer wins this round! :(')
    else:
        dataWinner.set('D R A W')
    data1.set('Player Score:%d'%pScore)
    data2.set('Computer Score:%d'%cScore)


def buttonPaper_isClicked():
    global cScore
    global pScore

    data3.set('You Chose: PAPER')
    textBox3['image'] = paperImage

    computerChoice = computer[r.randint(0,2)]
    time.sleep(0.1)
    data5.set('Computer Chose: %s'%computerChoice)
    if computerChoice is 'ROCK':
        textBox5['image'] = rockImage
    elif computerChoice is 'PAPER':
        textBox5['image'] = paperImage
    else:
        textBox5['image'] = scissorsImage

    if computerChoice is 'SCISSORS':
        cScore = cScore + 1
        dataWinner.set('Computer wins this round! :(')
    elif computerChoice is 'ROCK':
        pScore = pScore + 1
        dataWinner.set('You win this round! Congratulations!')
    else:
        dataWinner.set('D R A W')
    data1.set('Player Score:%d'%pScore)
    data2.set('Computer Score:%d'%cScore)

def buttonScissors_isClicked():
    global cScore
    global pScore

    data3.set('You Chose: SCISSORS')
    textBox3['image'] = scissorsImage

    computerChoice = computer[r.randint(0,2)]
    time.sleep(0.1)
    data5.set('Computer Chose: %s'%computerChoice)
    if computerChoice is 'ROCK':
        textBox5['image'] = rockImage
    elif computerChoice is 'PAPER':
        textBox5['image'] = paperImage
    else:
        textBox5['image'] = scissorsImage

    if computerChoice is 'ROCK':
        cScore = cScore + 1
        dataWinner.set('Computer wins this round! :(')
    elif computerChoice is 'PAPER':
        pScore = pScore + 1
        dataWinner.set('You win this round! Congratulations!')
    else:
        dataWinner.set('D R A W')
    data1.set('Player Score:%d'%pScore)
    data2.set('Computer Score:%d'%cScore)

def buttonReset_isClicked():
    global cScore
    global pScore
    cScore = 0
    pScore = 0
    data1.set('')
    data2.set('')
    data3.set('')
    data5.set('')
    dataWinner.set('')
    textBox3['image'] = blank
    textBox5['image'] = blank
#button press functions ends here.


#GUI Starts from here ->
root = tkinter.Tk()
root.geometry("532x600+550+100")
root.resizable(0,0)
root.title("Rock Paper Scissors using Tkinter")

#Mainframe
mainframe = Frame(root,cursor='target',background='#2A363A')
mainframe.pack(expand = True, fill = 'both')

#pictures
blank = PhotoImage(file = "images/empty.png")
rockImage = PhotoImage(file = "images/rock.png")
paperImage = PhotoImage(file = "images/paper.png")
scissorsImage = PhotoImage(file = "images/scissors.png")

#Display Labels

textBox4 = Label(root,text="Welcome!",anchor=N,font=("times new roman",22), background = "#FECEAB",pady = 2, fg = "#000000",width=32,height=12)
textBox4.pack(expand=True,fill="both")
textBox4.place(x=7,y=190)

#current winner
dataWinner = StringVar()
textBox8 = Label(root,anchor=CENTER,font=("times new roman",16,'bold'),textvariable=dataWinner, background = "#FECEAB", fg = "#000000")
textBox8.pack(expand=True,fill="both")
textBox8.place(anchor='center',x=250,y=476)

#player choice
data3 = StringVar()
textBox6 = Label(root,anchor=CENTER,font=("times new roman",16),textvariable=data3, background = "#FECEAB", fg = "#000000")
textBox6.pack(expand=True,fill="both")
textBox6.place(x=7,y=425)

#computer choice
data5 = StringVar()
textBox7 = Label(root,text="Enter your text",anchor=CENTER,font=("times new roman",16),textvariable=data5, background = "#FECEAB", fg = "#000000")
textBox7.pack(expand=True,fill="both")
textBox7.place(x=265,y=425)

#player image
textBox3 = Label(root,anchor=CENTER,font=("times new roman",22), background = "#FECEAB", fg = "#000000")
textBox3.pack(expand=True,fill="both")
textBox3.place(x=8,y=230)

#computer image
textBox5 = Label(root,anchor=CENTER,font=("times new roman",22), background = "#FECEAB", fg = "#000000")
textBox5.pack(expand=True,fill="both")
textBox5.place(x=367,y=230)

#player score
data1 = StringVar() 
textBox1 = Label(root,text="Enter your text",anchor=CENTER,font=("times new roman",22), textvariable = data1, background = "#FECEAB", fg = "#000000",width=30,height=1)
textBox1.pack(expand=True,fill="both")
textBox1.place(x=7,y=497)

#computer score
data2 = StringVar() 
textBox2 = Label(root,text="Enter your text",anchor=CENTER,font=("times new roman",22), textvariable = data2, background = "#FECEAB", fg = "#000000",width=30,height=1)
textBox2.pack(expand=True,fill="both")
textBox2.place(x=7,y=545)


#Buttons
buttonRock = Button(mainframe,text='ROCK',font=('ms serif',16,'bold'),bg='#F0F8FF',fg='#2A363A',border = 2,command=buttonRock_isClicked,width=15)
buttonRock.pack()
buttonRock.place(anchor=CENTER,x=260,y=40)
buttonPaper = Button(mainframe,text='PAPER',font=('ms serif',16,'bold'),bg='#F0F8FF',fg='#2A363A',border = 2,command=buttonPaper_isClicked,width=15)
buttonPaper.pack()
buttonPaper.place(anchor=CENTER,x=260,y=90)
buttonScissors = Button(mainframe,text='SCISSOR',font=('ms serif',16,'bold'),bg='#F0F8FF',fg='#2A363A',border = 2,command=buttonScissors_isClicked,width=15)
buttonScissors.pack()
buttonScissors.place(anchor=CENTER,x=260,y=140)
buttonReset = Button(mainframe,text='Restart',font=('ms serif',16,'bold'),bg='#E84A5F',fg='white',border = 2,width=10,command=buttonReset_isClicked)
buttonReset.pack()
buttonReset.place(x=10,y=140)
#GUI Ends here

root.mainloop()

