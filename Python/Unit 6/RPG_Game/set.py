def money(usr_list, money_var):
    inventory_list = usr_list[1]
    inventory_list[14] = money_var
    usr_list[1] = inventory_list
    return usr_list
def item(usr_list, item, quant):
    inventory_list = usr_list[1]
    #[0 = bread,1 = corn,2 = wheat,3 = tnt,4 = fresh_water,5 = bow,6 = arrows,7 = banoculars,8 = sword,9 = spear,10 = mace,11 = dagger,12 = axe,13 = wood,14 = money]
    inventory_list[item] = quant
    usr_list[1] = inventory_list
    return usr_list
def pos(usr_list, place_out):
    pos_list = usr_list[0]
    pos_list[0] = place_out[1]
    usr_list[0] = pos_list
    return usr_list