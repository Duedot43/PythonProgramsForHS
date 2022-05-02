import get
def outpost(user_list):
    pos = get.pos(user_list)
    if pos == 3 or pos == 4 or pos == 7 or pos == 9 or pos == 22:
        return True
    else:
        return False
def barn(user_list):
    pos = get.pos(user_list)
    if pos == 2 or pos == 5 or pos == 10 or pos == 23 or pos == 24 or pos == 25 or pos == 27:
        return True
    else:
        return False
def shop(user_list):
    pos = get.pos(user_list)
    if pos == 6 or pos == 28 or pos == 20:
        return True
    else:
        return False
def cityorout(user_list):
    pos = get.pos(user_list)
    if pos == 6 or pos == 28:
        return 3
    if pos == 20:
        return 4
def fight(user_list, main_list):
    pos = get.pos(user_list)
    if outpost(user_list) == True:
        if get.outpost(0, get.pos2outpost(user_list), main_list) == 1:
            return [0,1]
    if pos == 17:
        return True
    if pos == 16 or pos == 15 or pos ==  11 or pos == 18 or pos ==29 or pos == 22 or pos == 13:
        return [0,1]
    return False
def outpost_raw(pos):
    if pos == 3 or pos == 4 or pos == 7 or pos == 9 or pos == 22:
        return True
    else:
        return False
def barn_raw(pos):
    if pos == 2 or pos == 5 or pos == 10 or pos == 23 or pos == 24 or pos == 25 or pos == 27:
        return True
    else:
        return False
def city_raw(pos):
    if pos == 8 or pos == 12 or pos == 13 or pos == 14 or pos == 18 or pos == 20:
        return True
    else:
        return False
def mil_raw(pos):
    if pos == 29:
        return True
    else:
        return False
def gate_raw(pos):
    if pos == 11 or pos ==15 or pos ==16:
        return True
    else:
        return False
def forest_raw(pos):
    if pos == 17:
        return True
    else:
        return False
def river_raw(pos):
    if pos == 21:
        return True
    else:
        return False
def mineshaft_raw(pos):
    if pos == 18:
        return True
    else:
        return False
def outlaw_raw(pos):
    if pos == 28:
        return True
    else:
        return False
def vinyard_raw(pos):
    if pos == 6:
        return True
    else:
        return False
def pier_raw(pos):
    if pos == 1:
        return True
    else:
        return False
def wepon(usr_list):
    if get.inventory(usr_list, 5) >= 1 or get.inventory(usr_list, 8) >= 1 or get.inventory(usr_list, 9) >= 1 or get.inventory(usr_list, 10) >= 1 or get.inventory(usr_list, 11) >= 1 or get.inventory(usr_list, 12) >= 1:
        return True
    else:
        return False