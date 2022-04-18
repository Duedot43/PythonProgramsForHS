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
def price(location, item, ck_what, main_list):
    #location should be 3 for price_outland or 4 for price_city
    location_list = main_list[location]
    #item should be 0 = bread 1 = corn 2 = wheat 3 = tnt 4 = fresh_water 5 = bow 6 = arrows 7 = banoculars
    item_list = location_list[item]
    #ck_what should be 0 for cost 1 for sellable 2 quant_per_price
    output = item_list[ck_what]
    return output