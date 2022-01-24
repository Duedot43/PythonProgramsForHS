#once upon a time i saw a meme in r/programing_humor that said "*me spending hours on a program that does something i can do in a few seconds and only use once*" i think that describes this pretty well
rookposx = int(input("What is the current x position if your rook?\n"));
rookposy = int(input("What is the current y position of your rook?\n"));
rookumovx = int(input("Where in the x plane do you want to move your rook?\n"));
rookumovy = int(input("Where in the y plane do you want to move your rook?\n"));
#x 1 2 3 4 5 6 7 8  y
#* * * * * * * * * *1
#* - - - - - - - - *2
#* - - - - - - - - *3
#* - - - - - - - - *4
#* - - - - - - - - *5
#* - - - - - - - - *6
#* - - - - - - - - *7
#* - - - - - - - - *8
#* * * * * * * * * *
f = float(rookposy)
if (f < 0):
    print("What?")
    exit()
f = float(rookposx)
if (f < 0):
    print("What?")
    exit()
if rookposx > 8:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookposy > 8:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookumovx > 8:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookumovy > 8:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookposx == 0:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookposy == 0:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookumovx == 0:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookumovy == 0:
    print("Ay we got a smart one over here tryna go off the board. Invalid");
    exit();
if rookposx == rookumovx:
    print("Valid");
    exit();
if rookposy == rookumovy:
    print("Valid");
    exit();
print("Are you stupid? Its invalid by the way idiot.")