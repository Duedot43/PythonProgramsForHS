import turtle as tur
import time
count = 0
while count != 4:
    tur.down()
    tur.forward(20)
    tur.left(90)
    count = count+1
count = 0
tur.up()
tur.goto(30,30)
tur.down()
while count != 3:
    tur.down()
    tur.forward(20)
    tur.left(60*2)
    count = count+1
count = 0
tur.up()
tur.goto(-30,30)
tur.down()
while count != 3:
    tur.down()
    tur.forward(20)
    tur.left(60*2)
    count = count+1

count = 0
tur.up()
tur.goto(-15,-30)
tur.down()
tur.right(90/2)
while count != 20:
    tur.down()
    tur.forward(3)
    tur.left(5)
    count = count+1
###keep the window open for 5 seconds###
count = 0
while count != 5:
    time.sleep(1)
    count = count+1
