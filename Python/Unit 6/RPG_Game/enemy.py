from random import randint
import get, at
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
    print("You have encountered a " + make_out[0] + " which has " + str(make_out[1]) + " health!\nPress 'a' to attack.")
    ##wepon system here##
    if at.wepon(plr_list):
        while True:
            usr_input = input("> ")
            if usr_input.lower() == "a":
                miss = randint(0,3)
                if miss == 0:
                    print("You missed!")
                else:
                    hit = randint(10,15)
                    print("You deal " + hit + " damage!")
                    make_out[1] = make_out[1]-hit
    else:
        print("You do not have a weapon! You cannot fight")
        return 0



