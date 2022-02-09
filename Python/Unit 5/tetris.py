import turtle as tur
import time
tur.down()
tur.forward(20)
tur.right(90)
tur.forward(20)
tur.left(90)
tur.forward(20*3)
tur.right(90)
tur.forward(20)
tur.right(90)
tur.forward(20*4)
tur.right(90)
tur.forward(20*2)

#another#

tur.up()
tur.goto(30,40)
tur.right(90)
tur.down()
count = 0
while count != 4:
    tur.down()
    tur.forward(20*2)
    tur.left(90)
    count = count+1

#another#

tur.up()
tur.goto(-40,40)
tur.right(90*3)
tur.down()
for x in range(0,2):
    tur.left(90)
    tur.forward(20*4)
    tur.left(90)
    tur.forward(20)

count = 0
while count != 5:
    time.sleep(1)
    count = count+1