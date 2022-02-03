import os

def algor(a1,a2,a3,b1,b2,b3,c1,c2,c3):
        
        win = "_"
        #branch left
        if a1 == "O":
            if a2 == "O":
                if a3 == "O":
                    win = "O"
            if b2 == "O":
                if c3 == "O":
                    win = "O"
            if b1 == "O":
                if c1 == "O":
                    win = "O"
        #branch right
        if c1 == "O":
            if c2 == "O":
                if c3 == "O":
                    win = "O"
            if b2 == "O":
                if a3 == "O":
                    win = "O"
        #middle up down
        if b1 == "O":
            if b2 == "O":
                if b3 == "O":
                    win = "O"
        #middle left right
        if a2 == "O":
            if b2 == "O":
                if c2 == "O":
                    win = "O"
        #bottom left right
        if a3 == "O":
            if b3 == "O":
                if c3 == "O":
                    win = "O"


        #branch left
        if a1 == "X":
            if a2 == "X":
                if a3 == "X":
                    win = "X"
            if b2 == "X":
                if c3 == "X":
                    win = "X"
            if b1 == "X":
                if c1 == "X":
                    win = "X"
        #branch right
        if c1 == "X":
            if c2 == "X":
                if c3 == "X":
                    win = "X"
            if b2 == "X":
                if a3 == "X":
                    win = "X"
        #middle up down
        if b1 == "X":
            if b2 == "X":
                if b3 == "X":
                    win = "X"
        #middle left right
        if a2 == "X":
            if b2 == "X":
                if c2 == "X":
                    win = "X"
        #bottom left right
        if a3 == "X":
            if b3 == "X":
                if c3 == "X":
                    win = "X"
        wincalc1 = 0
        wincalc2 = 0
        wincalc3 = 0
        wincalc4 = 0
        wincalc5 = 0
        wincalc6 = 0
        wincalc7 = 0
        wincalc8 = 0
        wincalc9 = 0
    
        if a1 != "_":
            wincalc1 = 3
        if a2 != "_":
            wincalc2 = 3
        if a3 != "_":
            wincalc3 = 3
        if b1 != "_":
            wincalc4 = 3
        if b2 != "_":
            wincalc5 = 3
        if b3 != "_":
            wincalc6 = 3
        if c1 != "_":
            wincalc7 = 3
        if c2 != "_":
            wincalc8 = 3
        if c3 != "_":
            wincalc9 = 3
        tieround = wincalc1+wincalc2+wincalc3+wincalc4+wincalc5+wincalc6+wincalc7+wincalc8+wincalc9
        tieround = int(tieround)
        if tieround == 27:
            win = "T"
        if tieround != 27:
            wins = "N"

        #algorithm

        if win == "X":
            win = 1
            win = int(win)
        if win == "O":
            win = 2
            win = int(win)
        if win == "_":
            win = 3
            win = int(win)
        if win == "T":
            win = 0
            win = int(win)
def getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3):
#    A     B     C  
#       |     |     
#1      |     |     
#  _____|_____|_____
#       |     |     
#2      |     |     
#  _____|_____|_____
#       |     |     
#3      |     |     
#       |     |     
 
    #generate board
    test = "x"
    board = (f"    A     B     C  \n       |     |     \n1   {a1}  |  {b1}  |  {c1}  \n  _____|_____|_____\n       |     |     \n2   {a2}  |  {b2}  |  {c2}   \n  _____|_____|_____\n       |     |     \n3   {a3}  |  {b3}  |  {c3}  \n       |     |     ")
    return board


Xa1 = "_"
Xa2 = "_"
Xa3 = "_"
Xb1 = "_"
Xb2 = "_"
Xb3 = "_"
Xc1 = "_"
Xc2 = "_"
Xc3 = "_"

Oa1 = "_"
Oa2 = "_"
Oa3 = "_"
Ob1 = "_"
Ob2 = "_"
Ob3 = "_"
Oc1 = "_"
Oc2 = "_"
Oc3 = "_"
game = 1
while game == 1:

        print("PLaceholder")