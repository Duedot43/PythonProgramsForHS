import turtle as tur
import time
tur.down()
tur.circle(180)
tur.up()
tur.goto(-80,180/2+90)
tur.down()
tur.circle(40)

tur.up()
tur.goto(80,180/2+90)
tur.down()
tur.circle(40)

tur.up()
tur.goto(0,180/2-30)
for x in range(0,20):
    tur.down()
    tur.forward(5)
    tur.left(3)
tur.up()
tur.goto(0,180/2-30)
tur.setheading(180)
for x in range(0,20):
    tur.down()
    tur.forward(5)
    tur.right(3)
count = 0
while count != 5:
    time.sleep(1)
    count = count+1