def  outpost(ck_what, what_outpost, main_list):
    #Check this for occupancy
    outpost_list = main_list[0]
    #what_outpost should be 0~4
    what_outpost_list = outpost_list[what_outpost]
    #ck_what should be 0 or 1, 0 for occupancy 1 for loot
    output = what_outpost_list[ck_what]
    return output
def  barn(what_barn, main_list):
    barn_list = main_list[1]
    #what_barn should be 0~7
    what_barn_list = barn_list[what_barn]
    output = what_barn_list[0]
    return output
def tree(ck_what, what_tree, main_list):
    tree_list = main_list[2]
    #what_tree should be 0~4
    what_tree_list = tree_list[what_tree]
    #ck_what should be either 0 for dead or 1 for size
    output = what_tree_list[ck_what]
    return output
def item(location, item, ck_what, main_list):
    #location should be 3 for price_outland or 4 for price_city
    location_list = main_list[location]
    #item should be 0 = bread 1 = corn 2 = wheat 3 = tnt 4 = fresh_water 5 = bow 6 = arrows 7 = banoculars
    item_list = location_list[item]
    #ck_what should be 0 for cost 1 for sellable 2 quant_per_price
    output = item_list[ck_what]
    return output
def place(goto_out, usr_input):
    for x in goto_out:
        if usr_input.lower() == x[0]:
            return [1, x[1]]
    return [0,0]
def inventory(user_list, ck_what):
    inventory_list = user_list[1]
    #[0 = bread,1 = corn,2 = wheat,3 = tnt,4 = fresh_water,5 = bow,6 = arrows,7 = banoculars,8 = sword,9 = spear,10 = mace,11 = dagger,12 = axe,13 = wood,14 = money]
    output = inventory_list[ck_what]
    return output
def pos(user_list):
    pos_list = user_list[0]
    output = pos_list[0]
    return output
def pos2outpost(user_list):
    posi = pos(user_list)
    if posi == 3:
        output = 0
        return output
    if posi == 4:
        output = 1
        return output
    if posi == 7:
        output = 2
        return output
    if posi == 9:
        output = 3
        return output
    if posi == 22:
        output = 4
        return output
    return None
def pos2barn(user_list):
    posi = pos(user_list)
    if posi == 2:
        return 0
    if posi == 5:
        return 1
    if posi == 10:
        return 2
    if posi == 23:
        return 3
    if posi == 24:
        return 4
    if posi == 25:
        return 5
    if posi == 27:
        return 6
def lock(usr_list, main_list, usr_input, ava):
    lock_list = main_list[5]
    avas = place(ava, usr_input)
    if avas[0] == 1:
        if lock_list[avas[1]] == 1:
            output = lock_list[avas[1]]
        else:
            output = 0
    return output
def advantages(usr_list, advantage):
    advantages_list = usr_list[2]
    #advantages 0 for guard armour 1 for health 3 for hunger
    output = advantages_list[advantage]
    return output