import get, goto, set, at
def Convert(string):
    li = list(string.split(" "))
    return li
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
        if at.outpost(player_list) == True:
            pass
        else:
            print("You cannot buy anything here")