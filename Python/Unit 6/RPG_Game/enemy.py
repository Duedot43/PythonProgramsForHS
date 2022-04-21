from random import randint
import get
def make(at_fight):
    if at_fight == True:
        typ = randint(0,3)
    else:
        typ = randint(at_fight[0], at_fight[1])
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
def fight(make_out, plr_list, var_list):
    print("You have encountered a " + make_out[0] + " which has " + str(make_out[1]) + " health!\n")
    ##wepon system here##

