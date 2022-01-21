import os
import requests
import time
import phpfetch
srvip = "127.0.0.1:8080"
def algor():
        a1 = str(phpfetch.getval(srvip, "info/a1"))
        a2 = str(phpfetch.getval(srvip, "info/a2"))
        a3 = str(phpfetch.getval(srvip, "info/a3"))
        b1 = str(phpfetch.getval(srvip, "info/b1"))
        b2 = str(phpfetch.getval(srvip, "info/b2"))
        b3 = str(phpfetch.getval(srvip, "info/b3"))
        c1 = str(phpfetch.getval(srvip, "info/c1"))
        c2 = str(phpfetch.getval(srvip, "info/c2"))
        c3 = str(phpfetch.getval(srvip, "info/c3"))
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
                    win == "O"
        #middle left right
        if a2 == "O":
            if b2 == "O":
                if c2 == "O":
                    win == "O"
        #bottom left right
        if a3 == "O":
            if b3 == "O":
                if c3 == "O":
                    win == "O"


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
                    win == "X"
        #middle left right
        if a2 == "X":
            if b2 == "X":
                if c2 == "X":
                    win == "X"
        #bottom left right
        if a3 == "X":
            if b3 == "X":
                if c3 == "X":
                    win == "X"
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
        #print("win=", win)
        if win == 1:
            phpfetch.setval(srvip, "setinfo.php?win=1")
            #print("win1")
        if win == 2:
            phpfetch.setval(srvip, "setinfo.php?win=2")
            #print("win2")
        if win == 3:
            phpfetch.setval(srvip, "setinfo.php?win=3")
            #print("win3")
        if win == 0:
            phpfetch.setval(srvip, "setinfo.php?win=0")
            #print("win0")
        return win
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=0'")
os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=1'")
cl2con = "0"
while cl2con == "0":
    time.sleep(.3)
    res = requests.get("http://" + srvip + "/connect/p1")
    if res.status_code == 200:
        p1 = int(res.text)
        if p1 == 1:
            cl2con = "1"
game = 1
turn = 1

while game == 1:
    time.sleep(.3)
    print("Clients connected!")
    while turn == 1:

        time.sleep(.3)
        res = requests.get("http://" + srvip + "/info/turn")
        if res.status_code == 200:
            turn = int(res.text)
            if turn == 2:
                print("Your turn!")
    a1 = str(phpfetch.getval(srvip, "info/a1"))
    a2 = str(phpfetch.getval(srvip, "info/a2"))
    a3 = str(phpfetch.getval(srvip, "info/a3"))
    b1 = str(phpfetch.getval(srvip, "info/b1"))
    b2 = str(phpfetch.getval(srvip, "info/b2"))
    b3 = str(phpfetch.getval(srvip, "info/b3"))
    c1 = str(phpfetch.getval(srvip, "info/c1"))
    c2 = str(phpfetch.getval(srvip, "info/c2"))
    c3 = str(phpfetch.getval(srvip, "info/c3"))
    if algor() == 3:
        print("The current board")
        board = phpfetch.getboard(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        print(board)
        if a1 != "X":
            if a1 != "O":
                print("(1) Place an O on A1")
        if a2 != "X":
            if a2 != "O":
                print("(2) Place an O on A2")
        if a3 != "X":
            if a3 != "O":
                print("(3) Place an O on A3")
        if b1 != "X":
            if b1 != "O":
                print("(4) Place an O on B1")
        if b2 != "X":
            if b2 != "O":
                print("(5) Place an O on B2")
        if b3 != "X":
            if b3 != "O":
                print("(6) Place an O on B3")
        if c1 != "X":
            if c1 != "O":
                print("(7) Place an O on C1")
        if c2 != "X":
            if c2 != "O":
                print("(8) Place an O on C2")
        if c3 != "X":
            if c3 != "O":
                print("(9) Place an O on C3")
        xmv = int(input("?"))
        if xmv == 1:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=a1")
        if xmv == 2:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=a2")
        if xmv == 3:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=a3")
        if xmv == 4:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=b1")
        if xmv == 5:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=b2")
        if xmv == 6:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=b3")
        if xmv == 7:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=c1")
        if xmv == 8:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=c2")
        if xmv == 9:
            phpfetch.setval(srvip, "setinfo.php?val=O&pos=c3")
    
    
    os.system("curl 'http://" + srvip + "/setinfo.php?turn=1'")
    os.system("curl 'http://" + srvip + "/setinfo.php?trdy2=1'")
    trdy1 = 0
    while trdy1 == 0:

        time.sleep(.3)
        res = requests.get("http://" + srvip + "/info/trdy1")
        if res.status_code == 200:
            trdy1 = int(res.text)
            if trdy1 == 1:
                trdy1 = 1
    iswin = 0
    while iswin == 0:

        time.sleep(.3)
        res = requests.get("http://" + srvip + "/info/win")
        if res.status_code == 200:
            winck = int(res.text)
            if winck == 1:
                win = 1
                iswin = 1
            if winck == 2:
                win = 2
                iswin = 1
            if winck == 3:
                win = 3
                iswin = 1
            if winck == 0:
                win = 0
                iswin = 1
    if win == 1:
        print("Player X wins!")
        time.sleep(.5)
        os.system("curl 'http://" + srvip + "/index.php?clean=1'")
        game = 0
    if win == 2:
        print("Player O wins!")
        time.sleep(.5)
        os.system("curl 'http://" + srvip + "/index.php?clean=1'")
        game = 0
    if win == 0:
        print("Tie!")
        time.sleep(.5)
        os.system("curl 'http://" + srvip + "/index.php?clean=1'")
        game = 0
    if win == 3:
        print("Continue")
        os.system("curl 'http://" + srvip + "/setinfo.php?trdy2=0'")
    time.sleep(.5)
    turn = 1
