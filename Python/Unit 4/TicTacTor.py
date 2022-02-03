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
        return win
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


a1 = "_"
a2 = "_"
a3 = "_"
b1 = "_"
b2 = "_"
b3 = "_"
c1 = "_"
c2 = "_"
c3 = "_"


game = 1
while game == 1:
    if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 3:
        print("The current board")
        board = getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        print(board)
        a1val = 0
        a2val = 0
        a3val = 0
        b1val = 0
        b2val = 0
        b3val = 0
        c1val = 0
        c2val = 0
        c3val = 0
        yes = 0
        if a1 != "O":
            if a1 != "X":
                print("Place an X on A1")
                a1val = 1
                
        if a2 != "O":
            if a2 != "X":
                print("Place an X on A2")
                a2val = 1
                
        if a3 != "O":
            if a3 != "X":
                print("Place an X on A3")
                a3val = 1
                
        if b1 != "O":
            if b1 != "X":
                print("Place an X on B1")
                b1val = 1
                
        if b2 != "O":
            if b2 != "X":
                print("Place an X on B2")
                b2val = 1
                
        if b3 != "O":
            if b3 != "X":
                print("Place an X on B3")
                b3val = 1
                
        if c1 != "O":
            if c1 != "X":
                print("Place an X on C1")
                c1val = 1
                
        if c2 != "O":
            if c2 != "X":
                print("Place an X on C2")
                c2val = 1
                
        if c3 != "O":
            if c3 != "X":
                print("Place an X on C3")
                c3val = 1
                
        amv = str(input("?"))
        xmv = amv.upper()
        if a1val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            a1val = 1
        if a2val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            a2val = 1
        if a3val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            a3val = 1
        if b1val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            b1val = 1
        if b2val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            b2val = 1
        if b3val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            b3val = 1
        if c1val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            c1val = 1
        if c2val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            c2val = 1
        if c3val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            c3val = 1
        if xmv == "A1":
            if a1val == 1:
                a1 = "X"
                yes = 1
            if a1val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "A2":
            if a2val == 1:
                a2 = "X"
                yes = 1
            if a2val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "A3":
            if a3val == 1:
                a3 = "X"
                yes = 1
            if a3val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "B1":
            if b1val == 1:
                b1 = "X"
                yes = 1
            if b1val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "B2":
            if b2val == 1:
                b2 = "X"
                yes = 1
            if b2val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "B3":
            if b3val == 1:
                b3 = "X"
                yes = 1
            if b3val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "C1":
            if c1val == 1:
                c1 = "X"
                yes = 1
            if c1val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "C2":
            if c2val == 1:
                c2 = "X"
                yes = 1
            if c2val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "C3":
            if c3val == 1:
                c3 = "X"
                yes = 1
            if c3val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if yes != 1:
            print("What?")
            exit()
    else:
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 1:
            print("Player X wins!")
            playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
            if playag != 1:
                if playag != 2:
                    thing = 1
                    while thing == 1:
                        playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
                        if playag != 1:
                            if playag != 2:
                                print("Invalid!")
                        if playag == 1:
                            thing = 0
                        if playag == 2:
                            thing = 0
            if playag == 1:
                a1 = "_"
                a2 = "_"
                a3 = "_"
                b1 = "_"
                b2 = "_"
                b3 = "_"
                c1 = "_"
                c2 = "_"
                c3 = "_"
            if playag == 2:
                exit()
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 2:
            print("Player O wins!")
            playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
            if playag != 1:
                if playag != 2:
                    thing = 1
                    while thing == 1:
                        playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
                        if playag != 1:
                            if playag != 2:
                                print("Invalid!")
                        if playag == 1:
                            thing = 0
                        if playag == 2:
                            thing = 0
            if playag == 1:
                a1 = "_"
                a2 = "_"
                a3 = "_"
                b1 = "_"
                b2 = "_"
                b3 = "_"
                c1 = "_"
                c2 = "_"
                c3 = "_"
            if playag == 2:
                exit()
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 0:
            print("Tie!")
            playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
            if playag != 1:
                if playag != 2:
                    thing = 1
                    while thing == 1:
                        playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
                        if playag != 1:
                            if playag != 2:
                                print("Invalid!")
                        if playag == 1:
                            thing = 0
                        if playag == 2:
                            thing = 0
            if playag == 1:
                a1 = "_"
                a2 = "_"
                a3 = "_"
                b1 = "_"
                b2 = "_"
                b3 = "_"
                c1 = "_"
                c2 = "_"
                c3 = "_"
            if playag == 2:
                exit()
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 3:
            print("Continue")


    os.system("clear")

######PLAYER 2######



    if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 3:
        print("The current board")
        board = getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        print(board)
        a1val = 0
        a2val = 0
        a3val = 0
        b1val = 0
        b2val = 0
        b3val = 0
        c1val = 0
        c2val = 0
        c3val = 0
        yes = 0
        if a1 != "O":
            if a1 != "X":
                print("Place an O on A1")
                a1val = 1
                
        if a2 != "O":
            if a2 != "X":
                print("Place an O on A2")
                a2val = 1
                
        if a3 != "O":
            if a3 != "X":
                print("Place an O on A3")
                a3val = 1
                
        if b1 != "O":
            if b1 != "X":
                print("Place an O on B1")
                b1val = 1
                
        if b2 != "O":
            if b2 != "X":
                print("Place an O on B2")
                b2val = 1
                
        if b3 != "O":
            if b3 != "X":
                print("Place an O on B3")
                b3val = 1
                
        if c1 != "O":
            if c1 != "X":
                print("Place an O on C1")
                c1val = 1
                
        if c2 != "O":
            if c2 != "X":
                print("Place an O on C2")
                c2val = 1
                
        if c3 != "O":
            if c3 != "X":
                print("Place an O on C3")
                c3val = 1
                
        amv = str(input("?"))
        xmv = amv.upper()
        if a1val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            a1val = 1
        if a2val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            a2val = 1
        if a3val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            a3val = 1
        if b1val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            b1val = 1
        if b2val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            b2val = 1
        if b3val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            b3val = 1
        if c1val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            c1val = 1
        if c2val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            c2val = 1
        if c3val != 1:
            amv = str(input("?"))
            xmv = amv.upper()
            c3val = 1
        if xmv == "A1":
            if a1val == 1:
                a1 = "O"
                yes = 1
            if a1val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "A2":
            if a2val == 1:
                a2 = "O"
                yes = 1
            if a2val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "A3":
            if a3val == 1:
                a3 = "O"
                yes = 1
            if a3val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "B1":
            if b1val == 1:
                b1 = "O"
                yes = 1
            if b1val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "B2":
            if b2val == 1:
                b2 = "O"
                yes = 1
            if b2val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "B3":
            if b3val == 1:
                b3 = "O"
                yes = 1
            if b3val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "C1":
            if c1val == 1:
                c1 = "O"
                yes = 1
            if c1val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "C2":
            if c2val == 1:
                c2 = "O"
                yes = 1
            if c2val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if xmv == "C3":
            if c3val == 1:
                c3 = "O"
                yes = 1
            if c3val != 1:
                print("You have done a great wrong fire monkey is not pleased you will die now")
                exit()
        if yes != 1:
            print("What?")
            exit()
    else:
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 1:
            print("Player X wins!")
            playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
            if playag != 1:
                if playag != 2:
                    thing = 1
                    while thing == 1:
                        playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
                        if playag != 1:
                            if playag != 2:
                                print("Invalid!")
                        if playag == 1:
                            thing = 0
                        if playag == 2:
                            thing = 0
            if playag == 1:
                a1 = "_"
                a2 = "_"
                a3 = "_"
                b1 = "_"
                b2 = "_"
                b3 = "_"
                c1 = "_"
                c2 = "_"
                c3 = "_"
            if playag == 2:
                exit()
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 2:
            print("Player O wins!")
            playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
            if playag != 1:
                if playag != 2:
                    thing = 1
                    while thing == 1:
                        playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
                        if playag != 1:
                            if playag != 2:
                                print("Invalid!")
                        if playag == 1:
                            thing = 0
                        if playag == 2:
                            thing = 0
            if playag == 1:
                a1 = "_"
                a2 = "_"
                a3 = "_"
                b1 = "_"
                b2 = "_"
                b3 = "_"
                c1 = "_"
                c2 = "_"
                c3 = "_"
            if playag == 2:
                exit()
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 0:
            print("Tie!")
            playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
            if playag != 1:
                if playag != 2:
                    thing = 1
                    while thing == 1:
                        playag = int(input("Play again?\n(1)Yes\n(2)No\n"))
                        if playag != 1:
                            if playag != 2:
                                print("Invalid!")
                        if playag == 1:
                            thing = 0
                        if playag == 2:
                            thing = 0
            if playag == 1:
                a1 = "_"
                a2 = "_"
                a3 = "_"
                b1 = "_"
                b2 = "_"
                b3 = "_"
                c1 = "_"
                c2 = "_"
                c3 = "_"
            if playag == 2:
                exit()
        if algor(a1,a2,a3,b1,b2,b3,c1,c2,c3) == 3:
            print("Continue")
    os.system("clear")