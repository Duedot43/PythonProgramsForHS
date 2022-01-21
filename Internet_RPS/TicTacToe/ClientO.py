import os
import requests
import time
import phpfetch
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=0'")
srvip = "127.0.0.1:8080"
os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=1'")
cl2con = "0"
while cl2con == "0":
    time.sleep(1)
    res = requests.get("http://" + srvip + "/connect/p1")
    if res.status_code == 200:
        p1 = int(res.text)
        if p1 == 1:
            cl2con = "1"
game = 1
turn = 1

while game == 1:
    time.sleep(2)
    print("Clients connected!")
    while turn == 1:

        time.sleep(1)
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

        time.sleep(1)
        res = requests.get("http://" + srvip + "/info/trdy1")
        if res.status_code == 200:
            trdy1 = int(res.text)
            if trdy1 == 1:
                trdy1 = 1
    iswin = 0
    while iswin == 0:

        time.sleep(1)
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
        time.sleep(3)
        os.system("curl 'http://" + srvip + "/index.php?clean=2'")
        game = 0
    if win == 2:
        print("Player O wins!")
        time.sleep(3)
        os.system("curl 'http://" + srvip + "/index.php?clean=2'")
        game = 0
    if win == 0:
        print("Tie!")
        time.sleep(3)
        os.system("curl 'http://" + srvip + "/index.php?clean=2'")
        game = 0
    if win == 3:
        print("Continue")
        os.system("curl 'http://" + srvip + "/setinfo.php?trdy2=0'")
    time.sleep(3)
    turn = 1
