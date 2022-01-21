import os
import requests
import time
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=0'")
srvip = "127.0.0.1:8080"
os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=1'")
cl2con = "0"
while cl2con == "0":
    time.sleep(1)
    res = requests.get("http://" + srvip + "/connect/p2")
    if res.status_code == 200:
        p2 = int(res.text)
        if p2 == 1:
            cl2con = "1"
game = 1
turn = 2
while game == 1:
    os.system("curl 'http://" + srvip + "/setinfo.php?turn=1'")
    time.sleep(2)
    print("Clients connected!")
    while turn == 2:

        time.sleep(1)
        res = requests.get("http://" + srvip + "/info/turn")
        if res.status_code == 200:
            turn = int(res.text)
            if turn == 1:
                print("Your turn!")
    p1mv = str(input("Now Player 1 take your choice \n (1) rock \n (2) paper \n (3) sissors \n"))
    os.system("curl 'http://" + srvip + "/setinfo.php?client=1&move=" + p1mv + "'")
    os.system("curl 'http://" + srvip + "/setinfo.php?turn=2'")
    os.system("curl 'http://" + srvip + "/setinfo.php?trdy1=1'")
    trdy2 = 0
    while trdy2 == 0:

        time.sleep(1)
        res = requests.get("http://" + srvip + "/info/trdy2")
        if res.status_code == 200:
            trdy2 = int(res.text)
            if trdy2 == 1:
                trdy2 = 1
    res = requests.get("http://" + srvip + "/info/p2mv")
    p2mv = int(res.text)
    p1mv = int(p1mv)
    if p1mv == p2mv:
        print("Tie!");
    if p1mv == 1:
        if p2mv == 2:
            os.system("curl http://" + srvip + "/setinfo.php?win=2")
        if p2mv == 3:
            os.system("curl http://" + srvip + "/setinfo.php?win=1")
    if p1mv == 2:
        if p2mv == 1:
            os.system("curl http://" + srvip + "/setinfo.php?win=1")
        if p2mv == 3:
            os.system("curl http://" + srvip + "/setinfo.php?win=2")
    if p1mv == 3:
        if p2mv == 1:
            os.system("curl http://" + srvip + "/setinfo.php?win=2")
        if p2mv == 2:
            os.system("curl http://" + srvip + "/setinfo.php?win=1")
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
    if win == 1:
        print("Player 1 wins!")
    if win == 2:
        print("Player 2 wins!")
    time.sleep(3)
    os.system("curl 'http://" + srvip + "/index.php?clean=2'")
    turn = 2