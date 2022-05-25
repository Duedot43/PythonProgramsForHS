from random import randint
from os import system
from time import sleep


def roll():
    #this is not used
    for x in range(0, 20):
        dice_ran = randint(1, 6)
        system("clear")
        dice(dice_ran)
        sleep(.1)
    return dice_ran


def dice(dicenum):
    # just display the dice!
    if dicenum == 1:
        return " ____\n|    |\n| O  |\n|    |\n ----"
    elif dicenum == 2:
        return " ____\n|O   |\n|    |\n|   O|\n ----"
    elif dicenum == 3:
        return " ____\n|  O |\n| O  |\n|O   |\n ----"
    elif dicenum == 4:
        return " ____\n|O  O|\n|    |\n|O  O|\n ----"
    elif dicenum == 5:
        return " ____\n|O  O|\n| O  |\n|O  O|\n ----"
    elif dicenum == 6:
        return " ____\n|O  O|\n|O  O|\n|O  O|\n ----"
