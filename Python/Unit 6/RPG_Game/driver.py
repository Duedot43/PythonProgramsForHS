import get, roll, room, setup, set, goto, console
game = 1
var_list = setup.load_game()
player_list = setup.load_player_info()
print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
print()
print("Welcome to Aristocrat.")
print()
print("Aristocrat is a text based RPG, where you must save your family from the aristocrats of the city.")
print("Every move you lose hunger.")
print()
print("Authorized commands in game: go {direction}, sell {item}, loot {item}, see {direction/inventory}, eat {food}, blow up {place}, and buy {item}.")
print()
print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
print()
print("Enter to continue")
input()
while game == 1:
    yes = console.user_input(var_list, player_list)
    while yes != 0:
        print("That is not a verb I know...")
        yes = console.user_input(var_list, player_list)

#TODO **Fighting systemDONE!,   **selling systemDONE!,    *seeing systemDONE!,     *eating systemDONE! (including death by hunger)     *looting system - random room gen done,     **unlocking systemDONE! *** TREE SYSTEM
#**Jack
#* Eli
#buy what? you cannot buy bread!!!!