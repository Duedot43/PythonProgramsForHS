import random

# ____
#|O  O|
#| O  |
#|O  O|
# ----
#
def dice(dicenum):
    if dicenum == 1:
        print(" ____\n|    |\n| O  |\n|    |\n ----")
    elif dicenum == 2:
        print(" ____\n|O   |\n|    |\n|   O|\n ----")
    elif dicenum == 3:
        print(" ____\n|  O |\n| O  |\n|O   |\n ----")
    elif dicenum == 4:
        print(" ____\n|O  O|\n|    |\n|O  O|\n ----")
    elif dicenum == 5:
        print(" ____\n|O  O|\n| O  |\n|O  O|\n ----")
    elif dicenum == 6:
        print(" ____\n|O  O|\n|O  O|\n|O  O|\n ----")
thing = 0
while thing == 0:
    dicenum = random.randint(1,6)
    dice(dicenum)
    play = int(input("Play again?\n(1)Yes\n(2)No\n"))
    if play == 1:
        continue
    elif play == 2:
        exit()
