import get, goto, set
def user_input(var_list, player_list):
    cpos = get.pos(player_list)
    ava = goto.disp(cpos)
    usr_input = input("\n\n> ")
    place_out = get.place(ava, usr_input)
    if place_out[0] == 1:
        player_list = set.pos(player_list, place_out)
        return 0
    else:
        return 1