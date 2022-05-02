import get, goto, set, at, enemy, room, random
def Convert(string):
    li = list(string.split(" "))
    return li
def raw_item(user_input):
    if user_input.lower() == "bread":
        return 0
    if user_input.lower() == "corn":
        return 1
    if user_input.lower() == "wheat":
        return 2
    if user_input.lower() == "tnt":
        return 3
    if user_input.lower() == "water":
        return 4
    if user_input.lower() == "bow":
        return 5
    if user_input.lower() == "arrows":
        return 6
    if user_input.lower() == "banoculars":
        return 7
    if user_input.lower() == "sword":
        return 8
    if user_input.lower() == "spear":
        return 9
    if user_input.lower() == "mace":
        return 10
    if user_input.lower() == "dagger":
        return 11
    if user_input.lower() == "axe":
        return 12
    return False
def raw_item_sell(user_input):
    if user_input.lower() == "bread":
        return 0
    if user_input.lower() == "corn":
        return 1
    if user_input.lower() == "wheat":
        return 2
    if user_input.lower() == "tnt":
        return False
    if user_input.lower() == "water":
        return False
    if user_input.lower() == "bow":
        return False
    if user_input.lower() == "arrows":
        return 6
    if user_input.lower() == "banoculars":
        return False
    if user_input.lower() == "sword":
        return False
    if user_input.lower() == "spear":
        return False
    if user_input.lower() == "mace":
        return False
    if user_input.lower() == "dagger":
        return False
    if user_input.lower() == "axe":
        return False
    if user_input.lower() == "wood":
        return 13
    return False
def ck_fight(var_list, player_list):
    if at.fight(player_list, var_list) != False or at.outpost(player_list):
        if at.outpost(player_list):
            if get.outpost(0, get.pos2outpost(player_list), var_list) == 1:
                make_out = enemy.make(at.fight(player_list, var_list))
                plr_list = enemy.fight(make_out, player_list, var_list)
                if plr_list != 0:
                    return plr_list
                else:
                    return 0
        make_out = enemy.make(at.fight(player_list, var_list))
        plr_list = enemy.fight(make_out, player_list, var_list)
        if plr_list != 0:
            return plr_list
        else:
            return 0
def user_input(var_list, player_list):
    cpos = get.pos(player_list)
    ava = goto.disp(cpos)
    ck_fit = ck_fight(var_list, player_list)
    if ck_fit != 0:
        ck_fit = player_list
    raw_raw_input = input("\n\n> ").lower()
    raw_input = Convert(raw_raw_input)
    if raw_input[0] == "walk" or raw_input[0] == "go" or raw_input[0] == "move" or raw_input[0] == "run":
        if int(len(raw_input)) == 1:
            print("You must provide somewhere to walk")
            return 0
        usr_input = raw_input[1]
        place_out = get.place(ava, usr_input)
        if place_out[0] == 1:
            locked = get.lock(player_list, var_list, raw_input[1], ava)
            if locked == 0:
                player_list = set.pos(player_list, place_out)
                room.desc(player_list, var_list)
                #hunger system
                hunger = get.advantages(player_list,2)
                hunger = hunger - random.randint(3,7)
                set.advantage(player_list,2,hunger)
                #death by hunger
                if hunger <= 0:
                    print()
                    print("You have died of hunger!")
                    print()
                    exit()
            if locked == 1:
                print("You cannot enter this room it is locked")
            return 0
        else:
            print("You cannot walk " + raw_input[1])
            return 0
    
    if raw_input[0] == "sell":
        if at.shop(player_list):
            cityout = at.cityorout(player_list)
            if int(len(raw_input)) == 1:
                print("You must provide something to sell or type " + raw_input[0] + " list to get a list of items to buy")
                return 0
            if raw_item_sell(raw_input[1]):
                item_num = raw_item_sell(raw_input[1])
                if item_num == False and raw_input[1] == "list":
                    print("You can sell bread,  corn,  wheat, arrows, wood")
                    return 0
                price = get.item(cityout, item_num, 0, var_list)
                usr_money = get.inventory(player_list, 14)
                choice = input("You can sell " + str(raw_input[1]) + " for " + str(price) + " you have " + str(usr_money) + " after this you will have " + str(usr_money+price) + " money. Are you sure you want to sell this?\n> ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    set.money(player_list, usr_money+price)
                    player_list = set.item(player_list, item_num, get.inventory(player_list, item_num)-get.item(cityout, item_num, 2, var_list))
                    return 0
                else:
                    return 0
    if raw_input[0] == "loot":
        if len(raw_input) == 1:
            print("You must provide something to loot.")
            return 0
        if at.outpost(player_list) == True:
            if raw_input[1] == "bread":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 0:
                    breadb4 = get.inventory(player_list,0)
                    player_list = set.item(player_list,0,breadb4+1)
                    print("You took a piece of bread.")
                    return 0
                else:
                    print("There is no bread here.")
                    return 0
            if raw_input[1] == "corn":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 1:
                    cornb4 = get.inventory(player_list,1)
                    player_list = set.item(player_list,1,cornb4+1)
                    print("You took a piece of corn.")
                    return 0
                else:
                    print("There is no corn here.")
                    return 0
            if raw_input[1] == "wheat":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 2:
                    wheatb4 = get.inventory(player_list,2)
                    player_list = set.item(player_list,2,wheatb4+1)
                    print("You took a piece of wheat.")
                    return 0
                else:
                    print("There is no wheat here.")
                    return 0
            if raw_input[1] == "tnt":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 3:
                    tntb4 = get.inventory(player_list,3)
                    player_list = set.item(player_list,3,tntb4+1)
                    print("You took a tnt.")
                    return 0
                else:
                    print("There is no tnt here.")
                    return 0
            if raw_input[1] == "water":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 4:
                    waterb4 = get.inventory(player_list,4)
                    player_list = set.item(player_list,4,waterb4+1)
                    print("You took a glass water.")
                    return 0
                else:
                    print("There is no water here.")
                    return 0
            if raw_input[1] == "bow":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 5:
                    bowb4 = get.inventory(player_list,5)
                    player_list = set.item(player_list,5,bowb4+1)
                    print("You took a bow.")
                    return 0
                else:
                    print("There is no bow here.")
                    return 0
            if raw_input[1] == "arrow" or raw_input[0] == "arrows":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 6:
                    arrowb4 = get.inventory(player_list,6)
                    player_list = set.item(player_list,6,arrowb4+1)
                    print("You took a arrow(s).")
                    return 0
                else:
                    print("There is no arrow(s) here.")
                    return 0
            if raw_input[1] == "sword":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 7:
                    swordb4 = get.inventory(player_list,7)
                    player_list = set.item(player_list,7,swordb4+1)
                    print("You took a sword.")
                    return 0
                else:
                    print("There is no sword here.")
                    return 0
            if raw_input[1] == "spear":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 8:
                    spearb4 = get.inventory(player_list,8)
                    player_list = set.item(player_list,8,spearb4+1)
                    print("You took a spear.")
                    return 0
                else:
                    print("There is no spear here.")
                    return 0
            if raw_input[1] == "mace":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 9:
                    maceb4 = get.inventory(player_list,9)
                    player_list = set.item(player_list,9,maceb4+1)
                    print("You took a mace.")
                    return 0
                else:
                    print("There is no mace here.")
                    return 0
            if raw_input[1] == "dagger":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 10:
                    daggerb4 = get.inventory(player_list,10)
                    player_list = set.item(player_list,10,daggerb4+1)
                    print("You took a dagger.")
                    return 0
                else:
                    print("There is no dagger here.")
                    return 0
            if raw_input[1] == "axe":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 11:
                    axeb4 = get.inventory(player_list,11)
                    player_list = set.item(player_list,11,axeb4+1)
                    print("You took a axe.")
                    return 0
                else:
                    print("There is no axe here.")
                    return 0
            if raw_input[1] == "wood":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 12:
                    woodb4 = get.inventory(player_list,12)
                    player_list = set.item(player_list,12,woodb4+1)
                    print("You took a wood.")
                    return 0
                else:
                    print("There is no wood here.")
                    return 0
            if raw_input[1] == "money":
                if get.outpost(1,get.pos2outpost(player_list), var_list) == 13:
                    moneyb4 = get.inventory(player_list,13)
                    player_list = set.item(player_list,13,moneyb4+1)
                    print("You took some money.")
                    return 0
                else:
                    print("There is no money here.")
                    return 0
        elif at.barn(player_list) == True:
            if raw_input[1] == "bread":
                if get.barn(1,get.pos2barn(player_list), var_list) == 0:
                    breadb4 = get.inventory(player_list,0)
                    player_list = set.item(player_list,0,breadb4+1)
                    print("You took a piece of bread.")
                    return 0
                else:
                    print("There is no bread here.")
                    return 0
            if raw_input[1] == "corn":
                if get.barn(1,get.pos2barn(player_list), var_list) == 1:
                    cornb4 = get.inventory(player_list,1)
                    player_list = set.item(player_list,1,cornb4+1)
                    print("You took a piece of corn.")
                    return 0
                else:
                    print("There is no corn here.")
                    return 0
            if raw_input[1] == "wheat":
                if get.barn(1,get.pos2barn(player_list), var_list) == 2:
                    wheatb4 = get.inventory(player_list,2)
                    player_list = set.item(player_list,2,wheatb4+1)
                    print("You took a piece of wheat.")
                    return 0
                else:
                    print("There is no wheat here.")
                    return 0
            if raw_input[1] == "tnt":
                if get.barn(1,get.pos2barn(player_list), var_list) == 3:
                    tntb4 = get.inventory(player_list,3)
                    player_list = set.item(player_list,3,tntb4+1)
                    print("You took a tnt.")
                    return 0
                else:
                    print("There is no tnt here.")
                    return 0
            if raw_input[1] == "water":
                if get.barn(1,get.pos2barn(player_list), var_list) == 4:
                    waterb4 = get.inventory(player_list,4)
                    player_list = set.item(player_list,4,waterb4+1)
                    print("You took a glass water.")
                    return 0
                else:
                    print("There is no water here.")
                    return 0
            if raw_input[1] == "bow":
                if get.barn(get.pos2barn(player_list), var_list) == 5:
                    bowb4 = get.inventory(player_list,5)
                    player_list = set.item(player_list,5,bowb4+1)
                    print("You took a bow.")
                    return 0
                else:
                    print("There is no bow here.")
                    return 0
            if raw_input[1] == "arrow" or raw_input[0] == "arrows":
                if get.barn(get.pos2barn(player_list), var_list) == 6:
                    arrowb4 = get.inventory(player_list,6)
                    player_list = set.item(player_list,6,arrowb4+1)
                    print("You took a arrow(s).")
                    return 0
                else:
                    print("There is no arrow(s) here.")
                    return 0
            if raw_input[1] == "binoculars":
                if get.barn(get.pos2barn(player_list), var_list) == 7:
                    arrowb4 = get.inventory(player_list,7)
                    player_list = set.item(player_list,7,arrowb4+1)
                    print("You took binoculars.")
                    return 0
                else:
                    print("There is no binoculars here.")
                    return 0
            if raw_input[1] == "sword":
                if get.barn(get.pos2barn(player_list), var_list) == 8:
                    swordb4 = get.inventory(player_list,8)
                    player_list = set.item(player_list,8,swordb4+1)
                    print("You took a sword.")
                    return 0
                else:
                    print("There is no sword here.")
                    return 0
            if raw_input[1] == "spear":
                if get.barn(get.pos2barn(player_list), var_list) == 9:
                    spearb4 = get.inventory(player_list,8)
                    player_list = set.item(player_list,9,spearb4+1)
                    print("You took a spear.")
                    return 0
                else:
                    print("There is no spear here.")
                    return 0
            if raw_input[1] == "mace":
                if get.barn(get.pos2barn(player_list), var_list) == 10:
                    maceb4 = get.inventory(player_list,10)
                    player_list = set.item(player_list,10,maceb4+1)
                    print("You took a mace.")
                    return 0
                else:
                    print("There is no mace here.")
                    return 0
            if raw_input[1] == "dagger":
                if get.barn(get.pos2barn(player_list), var_list) == 11:
                    daggerb4 = get.inventory(player_list,11)
                    player_list = set.item(player_list,11,daggerb4+1)
                    print("You took a dagger.")
                    return 0
                else:
                    print("There is no dagger here.")
                    return 0
            if raw_input[1] == "axe":
                if get.barn(get.pos2barn(player_list), var_list) == 12:
                    axeb4 = get.inventory(player_list,12)
                    player_list = set.item(player_list,12,axeb4+1)
                    print("You took a axe.")
                    return 0
                else:
                    print("There is no axe here.")
                    return 0
            if raw_input[1] == "wood":
                if get.barn(get.pos2barn(player_list), var_list) == 13:
                    woodb4 = get.inventory(player_list,13)
                    player_list = set.item(player_list,13,woodb4+1)
                    print("You took a wood.")
                    return 0
                else:
                    print("There is no wood here.")
                    return 0
            if raw_input[1] == "money":
                if get.barn(get.pos2barn(player_list), var_list) == 14:
                    moneyb4 = get.inventory(player_list,14)
                    player_list = set.item(player_list,14,moneyb4+1)
                    print("You took some money.")
                    return 0
                else:
                    print("There is no money here.")
                    return 0
    if raw_input[0] == "see":
        if len(raw_input) == 1:
            print("You must provide somewhere to see.")
            return 0
        if raw_input[1] != "inventory":
            output = room.see(player_list, var_list, raw_input[1], ava)
            return output
        else:
            invtry_list = []
            for x in range(0,15):
                invtry_list.append(get.inventory(player_list,x))
            print("You have " + str(invtry_list[0]) + " bread(s), " + str(invtry_list[1]) + " corn(s), " + str(invtry_list[2]) + " wheat(s), " + str(invtry_list[3]) + " TNT(s), " + str(invtry_list[4]) + " water(s), " + str(invtry_list[5]) + " bow(s), " + str(invtry_list[6]) + " arrow(s), " + str(invtry_list[7]) + " binoculars, " + str(invtry_list[8]) + " sword(s), " + str(invtry_list[9]) + " spear(s), " + str(invtry_list[9]) + " mace(s) " + str(invtry_list[10]) + " dagger(s), " + str(invtry_list[11]) + " axe(s)" + str(invtry_list[12]) + " wood, " + str(invtry_list[13]) + " money.")

    if raw_input[0] == "eat":
        if len(raw_input) == 1:
            print("You must provide something to eat.")
            return 0
        else:
            foodnumlist = []
            for x in range(0,3):
                foodnumlist.append(get.inventory(player_list,x))
            cornnumber = get.inventory(player_list,1)
            breadnumber = get.inventory(player_list,0)
            wheatnumber = get.inventory(player_list,2)
            hungernumber = get.advantages(player_list,2)
            if raw_input[1] == "corn":
                set.item(player_list,1,cornnumber-1)
                set.advantage(player_list,hungernumber+random.randint(5,10))
            elif raw_input[1] == "wheat":
                set.item(player_list,2,wheatnumber-1)
                set.advantage(player_list,hungernumber+random.randint(3,7))
            elif raw_input[1] == "bread":
                set.item(player_list,3,breadnumber-1)
                set.advantage(player_list,hungernumber+random.randint(10,15))
    if raw_input[0] == "blow":
        pos = get.pos(player_list)
        if pos == 22 or pos == 23 or pos == 10 and get.inventory(player_list, 3) >= 1:
            var_list = set.lock(var_list)
    if raw_input[0] == "buy" or raw_input[0] == "purchase":
        if at.shop(player_list) == True:
            cityorout = at.cityorout(player_list)
            if cityorout == 3 or cityorout == 4:
                #outpost
                if int(len(raw_input)) == 1:
                    print("You must provide something to buy or type " + raw_input[0] + " list to get a list of items to buy")
                    return 0
                item_num = raw_item(raw_input[1])
                if item_num == False:
                    if raw_input[1] == "list":
                        print("You can buy wheat,  corn,  wheat,  tnt,  water,  bow,  arrows,  banoculars,  sword,  spear,  mace,  dagger,  axe")
                        return 0
                    print("You cannot buy " + raw_input[1])
                    return 0
                price = get.item(cityorout, item_num, 0, var_list)
                usr_money = get.inventory(player_list, 14)
                if usr_money >= price:
                    choice = input("The price of " + str(raw_input[1]) + " is " + str(price) + " You have " + str(usr_money) + " money on you you will have " + str(usr_money-price) + " after this. You will get " + str(get.item(cityorout, item_num, 2, var_list)) + " " + str(raw_input[1]) + "\nWould you like to buy this?\n> ")
                    if choice.lower() == "y" or choice.lower() == "yes":
                        set.money(player_list, usr_money-price)
                        player_list = set.item(player_list, item_num, get.item(cityorout, item_num, 2, var_list))
                        return 0
                    else:
                        return 0
                else:
                    print("You cannot afford this!")
                    return 0
        else:
            print("You cannot buy anything here")
            return 0