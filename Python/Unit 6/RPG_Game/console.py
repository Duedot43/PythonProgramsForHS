import get, goto, set, at
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
def user_input(var_list, player_list):
    cpos = get.pos(player_list)
    ava = goto.disp(cpos)
    raw_raw_input = input("\n\n> ").lower()
    raw_input = Convert(raw_raw_input)
    if raw_input[0] == "walk" or raw_input[0] == "go" or raw_input[0] == "move" or raw_input[0] == "run":
        usr_input = raw_input[1]
        place_out = get.place(ava, usr_input)
        if place_out[0] == 1:
            player_list = set.pos(player_list, place_out)
            return 0
        else:
            return 1
    if raw_input[0] == "sell":
        pass
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
                        print("You can buy bread,  corn,  wheat,  tnt,  water,  bow,  arrows,  banoculars,  sword,  spear,  mace,  dagger,  axe")
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