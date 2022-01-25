import os
import requests
import time
import phpfetch
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=0'")
srvip = "127.0.0.1:8080"
os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=1'")
people = int(input("How many people are there:"))
count = 0
peoplelst = []
listgo = 0
while listgo == 0:
    count = count+1
    peoplelst.append(count)
    if count == people:
        listgo = 1
people = str(people)
phpfetch.setval(srvip, "addclient.php?ammountofclients='" + people + "'")
for x in peoplelst:
    xp = x+1
    print(x)
    x = str(x)
    if xp != people:
        cl2con = "0"
        while cl2con == "0":
            time.sleep(1)
            res = requests.get("http://" + srvip + "/connect/p" + x)
            if res.status_code == 200:
                p2 = int(res.text)
                if p2 == 1:
                    cl2con = "1"
phpfetch.setval(srvip, "setinfo.php?all=1")
phpfetch.setval(srvip, "addclient.php?clientdatafoldernumber=1")
clients = phpfetch.getval(srvip, "connect/clients")
clients = int(clients)
waow = 200*clients
print("Hold on while I set ", waow, " variabels in the server this may take a while...")
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=a" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=b" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=c" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=d" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=e" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=f" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=g" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=h" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=i" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=j" + countstr)

##

count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=a" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=b" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=c" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=d" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=e" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=f" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=g" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=h" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=i" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=j" + countstr)

print("Done!")

print("Time to set your ships! Here is the current board. Give me a minute i need to get all those variables again....")

a1 = phpfetch.getval(srvip, "info/pinfo1/a1")
a2 = phpfetch.getval(srvip, "info/pinfo1/a2")
a3 = phpfetch.getval(srvip, "info/pinfo1/a3")
a4 = phpfetch.getval(srvip, "info/pinfo1/a4")
a5 = phpfetch.getval(srvip, "info/pinfo1/a5")
a6 = phpfetch.getval(srvip, "info/pinfo1/a6")
a7 = phpfetch.getval(srvip, "info/pinfo1/a7")
a8 = phpfetch.getval(srvip, "info/pinfo1/a8")
a9 = phpfetch.getval(srvip, "info/pinfo1/a9")
a10 = phpfetch.getval(srvip, "info/pinfo1/a10")

b1 = phpfetch.getval(srvip, "info/pinfo1/b1")
b2 = phpfetch.getval(srvip, "info/pinfo1/b2")
b3 = phpfetch.getval(srvip, "info/pinfo1/b3")
b4 = phpfetch.getval(srvip, "info/pinfo1/b4")
b5 = phpfetch.getval(srvip, "info/pinfo1/b5")
b6 = phpfetch.getval(srvip, "info/pinfo1/b6")
b7 = phpfetch.getval(srvip, "info/pinfo1/b7")
b8 = phpfetch.getval(srvip, "info/pinfo1/b8")
b9 = phpfetch.getval(srvip, "info/pinfo1/b9")
b10 = phpfetch.getval(srvip, "info/pinfo1/b10")

c1 = phpfetch.getval(srvip, "info/pinfo1/c1")
c2 = phpfetch.getval(srvip, "info/pinfo1/c2")
c3 = phpfetch.getval(srvip, "info/pinfo1/c3")
c4 = phpfetch.getval(srvip, "info/pinfo1/c4")
c5 = phpfetch.getval(srvip, "info/pinfo1/c5")
c6 = phpfetch.getval(srvip, "info/pinfo1/c6")
c7 = phpfetch.getval(srvip, "info/pinfo1/c7")
c8 = phpfetch.getval(srvip, "info/pinfo1/c8")
c9 = phpfetch.getval(srvip, "info/pinfo1/c9")
c10 = phpfetch.getval(srvip, "info/pinfo1/c10")

d1 = phpfetch.getval(srvip, "info/pinfo1/d1")
d2 = phpfetch.getval(srvip, "info/pinfo1/d2")
d3 = phpfetch.getval(srvip, "info/pinfo1/d3")
d4 = phpfetch.getval(srvip, "info/pinfo1/d4")
d5 = phpfetch.getval(srvip, "info/pinfo1/d5")
d6 = phpfetch.getval(srvip, "info/pinfo1/d6")
d7 = phpfetch.getval(srvip, "info/pinfo1/d7")
d8 = phpfetch.getval(srvip, "info/pinfo1/d8")
d9 = phpfetch.getval(srvip, "info/pinfo1/d9")
d10 = phpfetch.getval(srvip, "info/pinfo1/d10")

e1 = phpfetch.getval(srvip, "info/pinfo1/e1")
e2 = phpfetch.getval(srvip, "info/pinfo1/e2")
e3 = phpfetch.getval(srvip, "info/pinfo1/e3")
e4 = phpfetch.getval(srvip, "info/pinfo1/e4")
e5 = phpfetch.getval(srvip, "info/pinfo1/e5")
e6 = phpfetch.getval(srvip, "info/pinfo1/e6")
e7 = phpfetch.getval(srvip, "info/pinfo1/e7")
e8 = phpfetch.getval(srvip, "info/pinfo1/e8")
e9 = phpfetch.getval(srvip, "info/pinfo1/e9")
e10 = phpfetch.getval(srvip, "info/pinfo1/e10")

f1 = phpfetch.getval(srvip, "info/pinfo1/f1")
f2 = phpfetch.getval(srvip, "info/pinfo1/f2")
f3 = phpfetch.getval(srvip, "info/pinfo1/f3")
f4 = phpfetch.getval(srvip, "info/pinfo1/f4")
f5 = phpfetch.getval(srvip, "info/pinfo1/f5")
f6 = phpfetch.getval(srvip, "info/pinfo1/f6")
f7 = phpfetch.getval(srvip, "info/pinfo1/f7")
f8 = phpfetch.getval(srvip, "info/pinfo1/f8")
f9 = phpfetch.getval(srvip, "info/pinfo1/f9")
f10 = phpfetch.getval(srvip, "info/pinfo1/f10")

g1 = phpfetch.getval(srvip, "info/pinfo1/g1")
g2 = phpfetch.getval(srvip, "info/pinfo1/g2")
g3 = phpfetch.getval(srvip, "info/pinfo1/g3")
g4 = phpfetch.getval(srvip, "info/pinfo1/g4")
g5 = phpfetch.getval(srvip, "info/pinfo1/g5")
g6 = phpfetch.getval(srvip, "info/pinfo1/g6")
g7 = phpfetch.getval(srvip, "info/pinfo1/g7")
g8 = phpfetch.getval(srvip, "info/pinfo1/g8")
g9 = phpfetch.getval(srvip, "info/pinfo1/g9")
g10 = phpfetch.getval(srvip, "info/pinfo1/g10")

h1 = phpfetch.getval(srvip, "info/pinfo1/h1")
h2 = phpfetch.getval(srvip, "info/pinfo1/h2")
h3 = phpfetch.getval(srvip, "info/pinfo1/h3")
h4 = phpfetch.getval(srvip, "info/pinfo1/h4")
h5 = phpfetch.getval(srvip, "info/pinfo1/h5")
h6 = phpfetch.getval(srvip, "info/pinfo1/h6")
h7 = phpfetch.getval(srvip, "info/pinfo1/h7")
h8 = phpfetch.getval(srvip, "info/pinfo1/h8")
h9 = phpfetch.getval(srvip, "info/pinfo1/h9")
h10 = phpfetch.getval(srvip, "info/pinfo1/h10")

i1 = phpfetch.getval(srvip, "info/pinfo1/i1")
i2 = phpfetch.getval(srvip, "info/pinfo1/i2")
i3 = phpfetch.getval(srvip, "info/pinfo1/i3")
i4 = phpfetch.getval(srvip, "info/pinfo1/i4")
i5 = phpfetch.getval(srvip, "info/pinfo1/i5")
i6 = phpfetch.getval(srvip, "info/pinfo1/i6")
i7 = phpfetch.getval(srvip, "info/pinfo1/i7")
i8 = phpfetch.getval(srvip, "info/pinfo1/i8")
i9 = phpfetch.getval(srvip, "info/pinfo1/i9")
i10 = phpfetch.getval(srvip, "info/pinfo1/i10")

j1 = phpfetch.getval(srvip, "info/pinfo1/j1")
j2 = phpfetch.getval(srvip, "info/pinfo1/j2")
j3 = phpfetch.getval(srvip, "info/pinfo1/j3")
j4 = phpfetch.getval(srvip, "info/pinfo1/j4")
j5 = phpfetch.getval(srvip, "info/pinfo1/j5")
j6 = phpfetch.getval(srvip, "info/pinfo1/j6")
j7 = phpfetch.getval(srvip, "info/pinfo1/j7")
j8 = phpfetch.getval(srvip, "info/pinfo1/j8")
j9 = phpfetch.getval(srvip, "info/pinfo1/j9")
j10 = phpfetch.getval(srvip, "info/pinfo1/j10")

print("Done! Here is the current board...")
board = phpfetch.getboard(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, )
print(board)
game = 1
turn = 2
while game == 1:
    os.system("curl 'http://" + srvip + "/setinfo.php?turn=1'")
    time.sleep(2)
    print("Clients connected!")
    while turn != 1:

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
        os.system("curl http://" + srvip + "/setinfo.php?win=0")
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
            if winck == 0:
                win = 0
                iswin = 1
    if win == 1:
        print("Player 1 wins!")
    if win == 2:
        print("Player 2 wins!")
    if win == 0:
        print("Tie!")
    time.sleep(3)
    os.system("curl 'http://" + srvip + "/index.php?clean=2'")
    turn = 2