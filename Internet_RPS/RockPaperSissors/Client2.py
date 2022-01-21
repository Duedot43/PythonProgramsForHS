import os
import requests
import time
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=0'")
srvip = "127.0.0.1:8080"
os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=1'")
cl2con = "0"
while cl2con == "0":
    time.sleep(1)
    res = requests.get("http://" + srvip + "/connect/p1")
    if res.status_code == 200:
        p2 = int(res.text)
        if p2 == 1:
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
    move = str(input("Now Player 2 take your choice \n (1) rock \n (2) paper \n (3) sissors \n"))
    os.system("curl 'http://" + srvip + "/setinfo.php?client=2&move=" + move + "'")
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
    res = requests.get("http://" + srvip + "/info/p1mv")
    p1mv = int(res.text)
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
            if winck == 0:
                win = 0
                iswin = 1
    if win == 1:
        print("Player 1 wins!")
    if win == 2:
        print("Player 2 wins!")
    if win == 0:
        print("Tie!")
    os.system("curl 'http://" + srvip + "/index.php?clean=2'")
    turn = 1