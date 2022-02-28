import turtle as tur
def square(color):
    tur.fillcolor(color)
    tur.begin_fill()
    for i in range(0,5):
        tur.forward(20)
        tur.right(90)
    tur.left(90)
    tur.end_fill()
square("red")