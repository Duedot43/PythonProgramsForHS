def disp(cpos):
    #we have 28 Total rooms.
    #pier
    if cpos == 1: 
        print("You are at the pier\nTo the northeast is a barn\nTo the east there is a military outpost")
        ava = [["northeast", 2], ["east", 7]]
        return ava
    #NWbarn
    if cpos == 2:
        print("You are at a barn\nTo the south there is a military outpost\nTo the east there is a military outpost\nTo the west is the pier")
        ava = [["south", 7], ["east", 3], ["west", 1]]
        return ava
    #occupiedoutpost
    if cpos == 3:
        print("You are at a military outpost\nTo the east there is the military base\nTo the west there is a barn")
        ava = [["east", 29], ["west", 2]]
        return ava
    #military base
    if cpos == 29:
        print("You are at the military base\nTo the south of you is the city\nTo the southeast of you is a military outpost\nTo the west of you is a military outpost")
        ava = [["southeast", 4], ["west", 3]]
        return ava
    #NEoutpost1
    if cpos == 4:
        print("You are at a military outpost\nTo the northeast of you is a barn\nTo the northwest of you is the military base")
        ava = [["northeast", 5], ["northwest", 29]]
        return ava
    #NEbarn
    if cpos == 5:
        print("You are at a barn\nTo the east of you is a mountan village\nTo the southeast of you is a millitary outpost\nTo the west of you is a military outpost")
        ava = [["east", 6], ["southeast", 9], ["west", 4]]
        return ava
    #vinyard
    if cpos == 6:
        print("You are at a mountan village you can buy things here\nTo the southeast of you is a military outpost\nTo the west of you is a barn")
        ava = [["southeast", 9], ["west", 5]]
        return ava
    #NWoutpost
    if cpos == 7:
        print("You are at a military outpost\nTo the north of you is a barn\nTo the west of you is the pier\nTo the south of you is the East City Gates")
        ava = [["north", 2], ["west", 1],["south", 11]]
        return ava
    #Military District
    if cpos == 8:
        print("You are in the military district of the city\nTo the south of you looms the castle\nTo the southwest of you is the commerce district\nTo the southeast of you is the housing district")
        ava = [["south", 13], ["southwest", 12], ["southeast", 14]]
        return ava
    #NEoutpost2
    if cpos == 9:
        print("You are at a military outpost\nTo the northwest there is a barn\nTo the south of you is the forest\nTo the southwest of you is the East city gates")
        ava = [["northwest", 5], ["south", 17], ["southwest", 16]]
        return ava
    #Wbarn
    if cpos == 10:
        print("You are at a barn\nTo the east there is the West City Gates\nTo the south is a mineshaft")
        ava = [["east",11], ["south", 18]]
        return ava
    #Egate
    if cpos == 11:
        print("You are at the West City Gates\nTo the west is a barn\nTo the east inside the gates is the Commerce District\nTo the north is an outpost\nTo the southwest is a mineshaft")
        ava = [["west", 10],["north", 7], ["southwest",18]]
        return ava
    #commerce district
    if cpos == 12:
        print("You are at the Commerce District\nTo the northeast is the Military District\nTo the south is the Political District\nTo the west is the West City Gates")
        ava = [["northeast", 8],["south",19],["west",11]]
        return ava
    #castle
    if cpos == 13:
        print("You are at the Castle\nTo the north is the Military District\nTo the southeast is the Political District")
        ava = [["were_doin_it_boys!",None]]
        return ava
    #housing district
    if cpos == 14:
        print("You are in the Housing District\nTo the northwest is the Military District\nTo the east is the East City Gates\nTo the southwest is the City General District")
        ava = [["northwest",8],["east",15],["southwest",20]]
        return ava
    #West Gate
    if cpos == 15:
        print("You are at the West City Gates\nTo the east is a barn\nTo the northeast is a outpost\nTo the south is a river\nTo the west is the Housing District")
        ava = [["west",14],["east",16],["northeast",9],["south",21]]
        return ava
    #Ebarn
    if cpos == 16:
        print("You are at a barn\nTo the east is a forest\nTo the northeast is a outpost\nTo the north is another outpost\nTo the southeast is a river")
        ava = [["east",17],["northeast",9],["north",4],["southeast",21]]
        return ava
    #forest
    if cpos == 17:
        print("You can barely see anything in the dense forest")
        ava = [["north",9],["west",16]]
        return ava
    #mineshaft
    if cpos == 18:
        print("You are at the enterance to a mineshaft\nTo the north is a barn\nTo the northeast is the West City Gates\nTo the south is a outpost\nTo the southeast is a barn")
        ava = [["north",10],["northeast",11],["south",22],["southeast",23]]
        return ava
    if cpos == 19:
        print("You are in the political district\nTo the north is the commerce district\nTo the northeast is the castle\nTo the southeast is the City General District")
        ava = [["northeast",13],["southeast",20],["north",12]]
        return ava
    if cpos == 20:
        print("You are in the City General District\nTo the northwest is the Political District\nTo the northeast is the Housing District")
        ava = [["northwest",19],["northeast",14]]
        return ava
    if cpos == 21:
        print("You are at the River\nTo the north is the East City Gates\nTo the northeast is a barn\nTo the southeast is a second barn\nTo the south is a third barn")
        ava = [["north",15],["northeast",16],["southest",24],["south",27]]
        return ava
    if cpos == 22:
        print("You are at a outpost\nTo the north is a mineshaft\nTo the east is a barn\nTo the south is another barn\nTo the southeast is the ditch you woke up in")
        ava = [["north",18],["east",23],["south",25],["southeast",26]]
        return ava
    if cpos == 23:
        print("You are at a barn\nTo the south is the ditch you woke up in\nTo the southwest is another barn\nTo the west is a outpost\nTo the east is a 3rd barn\nTo the southeast is a 4th barn")
        ava = [["south",26],["southwest",25],["west",22],["east",24],["southeast",27]]
        return ava
    if cpos == 24:
        print("You are at a barn\nTo the west is another barn\nTo the south is a 3rd barn\nTo the southwest is the ditch you woke up in")
        ava = [["west",23],["south",27],["southwest",26]]
        return ava
    if cpos == 25:
        print("You are at a barn\nTo the north is a outpost\nTo the east is the ditch you woke up in\nTo the northeast is another barn")
        ava = [["north",22],["east",26],["northeast",23]]
        return ava
    if cpos == 26:
        print("You are at a ditch\nTo the west there is a barn\nTo the northwest there is a outpost\nTo the north there is another barn\nTo the northeast there is a 3rd barn\nTo the east there is a 4th barn")
        ava = [["west",25],["northwest",22],["north",23],["northeast",24],["east",27]]
        return ava
    if cpos == 27:
        print("You are at a barn\nTo the west is the ditch you woke up in\nTo the north is another barn\nTo the northwest is a 3rd barn")
        ava = [["west",26],["north",24],["northwest",23]]
        return ava
    if cpos == 28:
        print("You are at a hidden outlaws camp\nTo the west there is the forest")
        ava = [["west",17]]
        return ava