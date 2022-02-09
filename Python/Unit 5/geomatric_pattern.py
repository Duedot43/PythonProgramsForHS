import turtle
import time
t = turtle.Pen()
for z in range(100):
    turtle.bgcolor("black")
    time.sleep(1)
    turtle.bgcolor("blue")
    time.sleep(1)
    t.speed(0)
    colors = ["red", "light sky blue", "green", "blue", "yellow", "white", "dark blue", "light green",]
    for x in range(100):
        t.pencolor( colors [x % 8])
        t.forward(2*x)
        t.left(91)

    
