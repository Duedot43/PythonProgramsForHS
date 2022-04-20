from random import randint
import get
def make(random):
    if random == 1:
        typ = randint(0,3)
    else:
        typ == random
    if typ == 0:
        enm = ["guard",  15]
        return enm
    if typ == 1:
        enm = ["royal guard", 30]
        return enm
    if typ == 2:
        enm = ["wolf", 20]
        return enm
    if typ == 3:
        enm = ["bear", 40]
        return enm
def fight(make_out, plr_list):
    print("You have encountered a " + make_out[0] + " which has " + str(make_out[1]) + "health!\n")
    ##wepon system here##

