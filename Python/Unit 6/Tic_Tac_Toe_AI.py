import os
from random import randint
import nn
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
def restart():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global plr_win_ct
    global bot_win_ct
    a1 = "_"
    a2 = "_"
    a3 = "_"
    b1 = "_"
    b2 = "_"
    b3 = "_"
    c1 = "_"
    c2 = "_"
    c3 = "_"
    plr_win_ct = 0
    bot_win_ct = 0
def choice(client):
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global plr_win_ct
    global bot_win_ct
    cho = 20
    while int(cho) != 7 and int(cho) != 8 and int(cho) != 9 and int(cho) != 4 and int(cho) !=5 and int(cho) != 6 and int(cho) != 1 and int(cho) != 2 and int(cho) != 3 and int(cho) != 0:
        if a1 == "_":
            print("(7) Place a " + client + " on a1")
        if a2 == "_":
            print("(4) Place a " + client + " on a2")
        if a3 == "_":
            print("(1) Place a " + client + " on a3")
        if b1 == "_":
            print("(8) Place a " + client + " on b1")
        if b2 == "_":
            print("(5) Place a " + client + " on b2")
        if b3 == "_":
            print("(2) Place a " + client + " on b3")
        if c1 == "_":
            print("(9) Place a " + client + " on c1")
        if c2 == "_":
            print("(6) Place a " + client + " on c2")
        if c3 == "_":
            print("(3) Place a " + client + " on c3")
        print("(0) Quit")
        cho = input("? ")
        if int(cho) == 7:
            if a1 == "X" or a1 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                a1 = client
        elif int(cho) == 4:
            if a2 == "X" or a2 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))   
                cho = 20
            else:
                a2 = client
        elif int(cho) == 1:
            if a3 == "X" or a3 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                a3 = client
        elif int(cho) == 8:
            if b1 == "X" or b1 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                b1 = client
        elif int(cho) == 5:
            if b2 == "X" or b2 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                b2 = client
        elif int(cho) == 2:
            if b3 == "X" or b3 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                b3 = client
        elif int(cho) == 9:
            if c1 == "X" or c1 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                c1 = client
        elif int(cho) == 6:
            if c2 == "X" or c2 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                c2 = client
        elif int(cho) == 3:
            if c3 == "X" or c3 == "O":
                os.system("clear")
                print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
                print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
                cho = 20
            else:
                c3 = client
        elif int(cho) == 0:
            exit()
        else:
            os.system("clear")
            print("Invalid choice!\nDONT YOU EVEN TRY TO CHEAT!!")
            print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
            cho = 20
 
def win_decode(gtfo):
    global player
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    win = nn.algor(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    if win == 1:
        os.system("clear")
        print("Player X wins!")
        print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
        again = input("Play again?\n(1) Yes\n(2) No\n? ")
        if again == "1":
            restart()
        else:
            exit()
        player = randint(0,1)
    if win == 2:
        os.system("clear")
        print("Player O wins!")
        print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
        again = input("Play again?\n(1) Yes\n(2) No\n? ")
        if again == "1":
            restart()
        else:
            exit()
        player = randint(0,1)
    if win == 3:
        pass
    if win == 0:
        os.system("clear")
        print("Tie!")
        print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
        again = input("Play again?\n(1) Yes\n(2) No\n? ")
        if again == "1":
            restart()
        else:
            exit()
        player = randint(0,1)
    if gtfo == 0:
        os.system("clear")
        print("You have screwed over the bot! the bot now despises you!")
        print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
        again = input("Play again?\n(1) Yes\n(2) No\n? ")
        if again == "1":
            restart()
        else:
            exit()
        player = randint(0,1)
restart()
game = 1
player = randint(0,1)
os.system("clear")
mode = int(input("What mode would you like?\n(1) Normal\n(2) Debug/explination\n? "))
while game == 1:
    if player == 0:
        win_decode(1)
        os.system("clear")
        win_decode(1)
        print(getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3))
        win_decode(1)
        choice("O")
        win_decode(1)
        player = 1
    if player == 1:
        win_decode(1)
        if mode == 1:
            orig_board_list = nn.ai(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        else:
            orig_board_list = nn.ai_DEMO(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        win_decode(orig_board_list)
        a1 = orig_board_list[0]
        a2 = orig_board_list[1]
        a3 = orig_board_list[2]
        b1 = orig_board_list[3]
        b2 = orig_board_list[4]
        b3 = orig_board_list[5]
        c1 = orig_board_list[6]
        c2 = orig_board_list[7]
        c3 = orig_board_list[8]
        player = 0
        win_decode(1)
