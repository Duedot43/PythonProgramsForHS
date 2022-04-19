import get, roll, room, setup, set, goto, console
game = 1
var_list = setup.load_game()
player_list = setup.load_player_info()
while game == 1:
    yes = console.user_input(var_list, player_list)
    while yes != 0:
        print("Invalid input")
        yes = console.user_input(var_list, player_list)