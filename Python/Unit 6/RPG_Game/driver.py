import get, roll, room, setup, set, goto
game = 1
var_list = setup.load_game()
player_list = setup.load_player_info()
while game == 1:
    cpos = get.pos(player_list)
    ava = goto.disp(cpos)
    usr_input = input("\n\n>")
    place_out = get.place(ava, usr_input)
    if place_out[0] == 1:
        player_list = set.pos(player_list, place_out)
    print(player_list)
    game = 0