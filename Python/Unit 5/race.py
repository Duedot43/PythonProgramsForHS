import turtle as tur
import random as ran
from tkinter import messagebox
while True:
    tur.speed(100)
    tur.setheading(0)
    tur.goto(0,0)
    print("start")
    tur.up()
    #tur.left(90)
    tur.forward(200)
    tur.right(90)
    tur.down()
    tur.forward(125)
    tur.right(90)
    tur.up()
    tur.forward(400)
    tur.down()
    tur.right(90)
    tur.forward(125)
    tur.right(90)
    tur.up()
    tur.forward(200)
    tur.right(90)
    tur.forward(125/2)
    tur.right(90)
    tur.up()
    tur.goto(900,900)

    ##line##

    t1 = tur.Turtle()
    t1.speed(100)
    t1.up()
    t1.forward(200)
    t1.right(90)
    forw = 100/6
    t1.forward(forw)
    t1.right(90)
    t1.down()

    ##t2##

    t2 = tur.Turtle()
    t2.speed(100)
    t2.up()
    t2.forward(200)
    t2.right(90)
    forw = 100/6
    t2.forward(forw+forw)
    t2.right(90)
    t2.down()

    ##t3##

    t3 = tur.Turtle()
    t3.speed(100)
    t3.up()
    t3.forward(200)
    t3.right(90)
    forw = 100/6
    t3.forward(forw+forw+forw)
    t3.right(90)
    t3.down()

    ##t4##

    t4 = tur.Turtle()
    t4.speed(100)
    t4.up()
    t4.forward(200)
    t4.right(90)
    forw = 100/6
    t4.forward(forw+forw+forw+forw)
    t4.right(90)
    t4.down()

    ##t5##

    t5 = tur.Turtle()
    t5.speed(100)
    t5.up()
    t5.forward(200)
    t5.right(90)
    forw = 100/6
    t5.forward(forw+forw+forw+forw+forw)
    t5.right(90)
    t5.down()

    ##t6##

    t6 = tur.Turtle()
    t6.speed(100)
    t6.up()
    t6.forward(200)
    t6.right(90)
    f6rw = 100/6
    t6.forward(forw+forw+forw+forw+forw+forw)
    t6.right(90)
    t6.down()

    ##racing##
    game = 1
    cpos1 = 0
    cpos2 = 0
    cpos3 = 0
    cpos4 = 0
    cpos5 = 0
    cpos6 = 0
    t1.color("pink")
    t2.color("green")
    t3.color("blue")
    t4.color("red")
    t5.color("purple")
    t6.color("orange")
    t1.speed(30)
    t2.speed(30)
    t3.speed(30)
    t4.speed(30)
    t5.speed(30)
    t6.speed(30)
    while game == 1:
        random1 = ran.randint(1,30)
        random2 = ran.randint(1,30)
        random3 = ran.randint(1,30)
        random4 = ran.randint(1,30)
        random5 = ran.randint(1,30)
        random6 = ran.randint(1,30)
        t1.forward(random1)
        t2.forward(random2)
        t3.forward(random3)
        t4.forward(random4)
        t5.forward(random5)
        t6.forward(random6)
        cpos1 = cpos1+random1
        cpos2 = cpos2+random2
        cpos3 = cpos3+random3
        cpos4 = cpos4+random4
        cpos5 = cpos5+random5
        cpos6 = cpos6+random6
        if int(cpos1) >= 400 or int(cpos2) >= 400 or int(cpos3) >= 400 or int(cpos4) >= 400 or int(cpos5) >= 400 or int(cpos6) >= 400:
            winners = ['','','','','','',]
            winners[0] = cpos1
            winners[1] = cpos2
            winners[2] = cpos3
            winners[3] = cpos4
            winners[4] = cpos5
            winners[5] = cpos6
            winners.sort()
            messagebox.showinfo('information', 'Hi!')
            tur.reset()
            t1.reset()
            t2.reset()
            t3.reset()
            t4.reset()
            t5.reset()
            t6.reset()
            t1.up()
            t2.up()
            t3.up()
            t4.up()
            t5.up()
            t6.up()
            break
