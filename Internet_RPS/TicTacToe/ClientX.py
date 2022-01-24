import os
import requests
import time
import phpfetch
srvip = "10.240.93.104:8080"
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=0'")
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
        
        if win == 1:
            phpfetch.setval(srvip, "setinfo.php?win=1")
            
        if win == 2:
            phpfetch.setval(srvip, "setinfo.php?win=2")
            
        if win == 3:
            phpfetch.setval(srvip, "setinfo.php?win=3")
            
        if win == 0:
            phpfetch.setval(srvip, "setinfo.php?win=0")
        return win
os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=1'")
cl2con = "0"
while cl2con == "0":
    time.sleep(.3)
    res = requests.get("http://" + srvip + "/connect/p2")
    if res.status_code == 200:
        p2 = int(res.text)
        if p2 == 1:
            cl2con = "1"
game = 1
turn = 2
phpfetch.setval(srvip, "setinfo.php?val=_&pos=a1")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=b1")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=c1")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=a2")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=b2")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=c2")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=a3")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=b3")
phpfetch.setval(srvip, "setinfo.php?val=_&pos=c3")

while game == 1:
    os.system("curl 'http://" + srvip + "/setinfo.php?turn=1'")
    time.sleep(.3)
    print("Clients connected!")
    while turn == 2:

        time.sleep(2)
        res = requests.get("http://" + srvip + "/info/turn")
        if res.status_code == 200:
            turn = int(res.text)
            if turn == 1:
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
        if a1 != "O":
            if a1 != "X":
                print("Place an X on A1")
        if a2 != "O":
            if a2 != "X":
                print("Place an X on A2")
        if a3 != "O":
            if a3 != "X":
                print("Place an X on A3")
        if b1 != "O":
            if b1 != "X":
                print("Place an X on B1")
        if b2 != "O":
            if b2 != "X":
                print("Place an X on B2")
        if b3 != "O":
            if b3 != "X":
                print("Place an X on B3")
        if c1 != "O":
            if c1 != "X":
                print("Place an X on C1")
        if c2 != "O":
            if c2 != "X":
                print("Place an X on C2")
        if c3 != "O":
            if c3 != "X":
                print("Place an X on C3")
        amv = str(input("?"))
        xmv = amv.upper()
        if xmv == "A1":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=a1")
        if xmv == "A2":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=a2")
        if xmv == "A3":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=a3")
        if xmv == "B1":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=b1")
        if xmv == "B2":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=b2")
        if xmv == "B3":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=b3")
        if xmv == "C1":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=c1")
        if xmv == "C1":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=c2")
        if xmv == "C3":
            phpfetch.setval(srvip, "setinfo.php?val=X&pos=c3")
    
    
    os.system("curl 'http://" + srvip + "/setinfo.php?turn=2'")
    os.system("curl 'http://" + srvip + "/setinfo.php?trdy1=1'")
    #rdy2 = 0
    #while trdy2 == 0:
    #
    #    time.sleep(3)
    #    res = requests.get("http://" + srvip + "/info/trdy2")
    #    if res.status_code == 200:
    #        trdy2 = int(res.text)
    #        if trdy2 == 1:
    #            trdy2 = 1
    
    #algorithm
    
    #algor()
    trdy2 = 0
    while trdy2 == 0:

        time.sleep(.3)
        res = requests.get("http://" + srvip + "/info/trdy2")
        if res.status_code == 200:
            trdy2 = int(res.text)
            if trdy2 == 1:
                trdy2 = 1
    iswin = 0
    while iswin == 0:

        time.sleep(.3)
        res = requests.get("http://" + srvip + "/info/win")
        if res.status_code == 200:
            winck = int(res.text)
            print("winck", winck)
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
        time.sleep(3)
        os.system("curl 'http://" + srvip + "/index.php?clean=1'")
        game = 0
    if win == 2:
        print("Player O wins!")
        time.sleep(3)
        os.system("curl 'http://" + srvip + "/index.php?clean=1'")
        game = 0
    if win == 0:
        print("Tie!")
        time.sleep(3)
        os.system("curl 'http://" + srvip + "/index.php?clean=1'")
        game = 0
    if win == 3:
        print("Continue")
        os.system("curl 'http://" + srvip + "/setinfo.php?trdy1=0'")
    time.sleep(3)
    turn = 2

