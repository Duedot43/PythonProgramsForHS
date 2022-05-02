from random import randint
import get, at, set
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
        while make_out[1] >= 0 and get.inventory(plr_list, 14) >= 0:
            usr_input = input("E> ")
            if usr_input.lower() == "a":
                miss = randint(0,3)
                if miss == 0:
                    print("You missed!")
                else:
                    hit = randint(10,15)
                    print("You deal " + str(hit) + " damage!")
                    make_out[1] = make_out[1]-hit
                enm_hit = randint(10,20)
                plr_list = set.item(plr_list, 14, get.inventory(plr_list, 14)-enm_hit)
                print("The enemy hit you! you now have " + str(get.inventory(plr_list, 14)) + " health left.")
        if get.pos(plr_list) == 13:
            print("You have your family! You win!")
            exit()
        return plr_list
    else:
        print("You do not have a weapon! You cannot fight")
        return 0



