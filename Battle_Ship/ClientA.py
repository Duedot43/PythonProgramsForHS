import os
import requests
import time
import phpfetch
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=2&connect=0'")
srvip = "127.0.0.1:8080"
clientnum = str(input("What is your client number?"))
os.system("curl 'http://" + srvip + "/addclient.php?client=" + clientnum + "&connect=1'")
cl2con = "0"
while cl2con == "0":
    time.sleep(1)
    res = requests.get("http://" + srvip + "/connect/all")
    if res.status_code == 200:
        p2 = int(res.text)
        if p2 == 1:
            cl2con = "1"
phpfetch.setval(srvip, "addclient.php?clientdatafoldernumber=" + clientnum)
clients = phpfetch.getval(srvip, "connect/clients")
clients = int(clients)
waow = 200*clients
print("Hold on while I set ", waow, " variabels in the server this may take a while...")
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=a" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=b" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=c" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=d" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=e" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=f" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=g" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=h" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=i" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=top&pos=j" + countstr)

##

count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=a" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=b" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=c" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=d" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=e" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=f" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=g" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=h" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=i" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=" + clientnum + "&board=bot&pos=j" + countstr)

print("Done!")

print("Time to set your ships! Here is the current board. Give me a minute i need to get all those variables again....")

a1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a1")
a2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a2")
a3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a3")
a4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a4")
a5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a5")
a6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a6")
a7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a7")
a8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a8")
a9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a9")
a10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/a10")

b1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b1")
b2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b2")
b3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b3")
b4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b4")
b5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b5")
b6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b6")
b7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b7")
b8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b8")
b9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b9")
b10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/b10")

c1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c1")
c2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c2")
c3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c3")
c4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c4")
c5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c5")
c6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c6")
c7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c7")
c8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c8")
c9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c9")
c10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/c10")

d1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d1")
d2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d2")
d3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d3")
d4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d4")
d5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d5")
d6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d6")
d7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d7")
d8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d8")
d9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d9")
d10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/d10")

e1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e1")
e2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e2")
e3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e3")
e4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e4")
e5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e5")
e6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e6")
e7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e7")
e8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e8")
e9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e9")
e10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/e10")

f1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f1")
f2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f2")
f3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f3")
f4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f4")
f5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f5")
f6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f6")
f7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f7")
f8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f8")
f9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f9")
f10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/f10")

g1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g1")
g2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g2")
g3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g3")
g4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g4")
g5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g5")
g6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g6")
g7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g7")
g8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g8")
g9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g9")
g10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/g10")

h1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h1")
h2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h2")
h3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h3")
h4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h4")
h5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h5")
h6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h6")
h7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h7")
h8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h8")
h9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h9")
h10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/h10")

i1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i1")
i2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i2")
i3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i3")
i4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i4")
i5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i5")
i6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i6")
i7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i7")
i8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i8")
i9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i9")
i10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/i10")

j1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j1")
j2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j2")
j3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j3")
j4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j4")
j5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j5")
j6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j6")
j7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j7")
j8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j8")
j9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j9")
j10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/j10")

print("Done! Here is the current board...")
board = phpfetch.getboard(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, )
print(board)
#phpfetch.setval(srvip, "setinfo.php?val=")
game = 1
turn = 1
while game == 1:
    time.sleep(2)
    print("Clients connected!")
    while turn != clientnum:

        time.sleep(1)
        res = requests.get("http://" + srvip + "/info/turn")
        if res.status_code == 200:
            turn = int(res.text)
            if turn == clientnum:
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