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

ta1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo" + clientnum + "/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)
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