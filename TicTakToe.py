from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import array

def checkwinner():
        if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
           button4["text"]=="X " and button5["text"]=="X" and button6["text"]=="X" or
           button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
           button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
           button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
           button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
           button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
           button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
                messagebox._show("WINNER OF GAME", " PLAYER 1 IS WINNER")
                os.execl(sys.executable, sys.executable, *sys.argv)
                
        elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
           button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
           button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
           button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
           button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
           button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
           button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
           button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
                messagebox._show("WINNER OF GAME", " PLAYER 2 IS WINNER")
                os.execl(sys.executable, sys.executable, *sys.argv)
player = 1
bc= array.array('i',[0,0,0,0,0,0,0,0,0])
def buttonpressed(bn):
        global player
        if (bn==1 and player==1 and bc[0]==0):
                button1.config(text = "X")
                player=2
                bc[0]=1
        elif (bn==1 and player==2 and bc[0]==0):
                button1.config(text="O")
                player=1
                bc[0]=1
        elif(bn==2 and player==1 and bc[1]==0):
                button2.config(text = "X")
                player=2
                bc[1]=1
        elif(bn==2 and player==2 and bc[1]==0):
                button2.config(text = "O")
                player=1
                bc[1]=1
        elif(bn==3 and player==1 and bc[2]==0):
                button3.config(text = "X")
                player=2
                bc[2]=1
        elif(bn==3 and player==2 and bc[2]==0):
                button3.config(text = "O")
                player=1
                bc[2]=1
        elif(bn==4 and player==1 and bc[3]==0):
                button4.config(text = "X")
                player=2
                bc[3]=1
        elif(bn==4 and player==2 and bc[3]==0):
                button4.config(text = "O")
                player=1
                bc[3]=1
        elif(bn==5 and player==1 and bc[4]==0):
                button5.config(text = "X")
                player=2
                bc[4]=1
        elif(bn==5 and player==2 and bc[4]==0):
                button5.config(text = "O")
                player=1
                bc[4]=1
        elif(bn==6 and player==1 and bc[5]==0):
                button6.config(text = "X")
                player=2
                bc[5]=1
        elif(bn==6 and player==2 and bc[5]==0):
                button6.config(text = "O")
                player=1
                bc[5]=1
        elif(bn==7 and player==1 and bc[6]==0):
                button7.config(text = "X")
                player=2
                bc[6]=1
        elif(bn==7 and player==2 and bc[6]==0):
                button7.config(text = "O")
                player=1
                bc[6]=1
        elif(bn==8 and player==1 and bc[7]==0):
                button8.config(text = "X")
                player=2
                bc[7]=1
        elif(bn==8 and player==2 and bc[7]==0):
                button8.config(text = "O")
                player=1
                bc[7]=1
        elif(bn==9 and player==1 and bc[8]==0):
                button9.config(text = "X")
                player=2
                bc[8]=1
        elif(bn==9 and player==2 and bc[8]==0):
                button9.config(text = "O")
                player=1
                bc[8]=1
        checkwinner()
                

root = Tk()
root.geometry('800x680')
style = ttk.Style()

button1 = ttk.Button(root, text = " ", command = lambda:buttonpressed(1),style="TButton")
button1.grid(row = 0 , column =0 ,ipadx=100,ipady=100)

button2 = ttk.Button(root , text = " " , command = lambda:buttonpressed(2))
button2.grid(row=0, column = 1, ipadx= 100, ipady = 100)

button3 = ttk.Button(root , text = " " , command = lambda:buttonpressed(3))
button3.grid(row=0, column = 2, ipadx= 100, ipady = 100)

button4 = ttk.Button(root , text = " " , command = lambda:buttonpressed(4))
button4.grid(row=1, column = 0, ipadx= 100, ipady = 100)

button5 = ttk.Button(root , text = " " , command = lambda:buttonpressed(5))
button5.grid(row=1, column = 1, ipadx= 100, ipady = 100)

button6 = ttk.Button(root , text = " " , command = lambda:buttonpressed(6))
button6.grid(row=1, column = 2, ipadx= 100, ipady = 100)

button7 = ttk.Button(root , text = " " , command = lambda:buttonpressed(7))
button7.grid(row=2, column = 0, ipadx= 100, ipady = 100)

button8 = ttk.Button(root , text = " " , command = lambda:buttonpressed(8))
button8.grid(row=2, column = 1, ipadx= 100, ipady = 100)

button9 = ttk.Button(root , text = " " , command = lambda:buttonpressed(9))
button9.grid(row=2, column = 2, ipadx= 100, ipady = 100)

root.mainloop()
