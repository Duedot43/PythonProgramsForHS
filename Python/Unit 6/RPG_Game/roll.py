from random import randint
from os import system
from time import sleep
def roll():
    for x in range(0,20):
        dice_ran = randint(1,6)
        system("clear")
        dice(dice_ran)
        sleep(.1)
    return dice_ran
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
