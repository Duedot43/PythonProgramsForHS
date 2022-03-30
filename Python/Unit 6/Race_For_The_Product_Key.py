import os
import random
def mkboard():
    global player_stats
    global enemy_distance
    print(f"Distance: {player_stats[0]} Thirst: {player_stats[1]} Drinks left: {player_stats[2]} Enegry: {player_stats[3]}\nEnemy distance: {enemy_distance}")
def ckwin():
    pass
def drink():
    global player_stats
    global enemy_distance
    if player_stats[1] == 0:
        print("You cannot drink water!")
        return 1
    elif player_stats[2] == 0:
        print("You are out of water!")
        return 1
    else:
        player_stats[1] = player_stats[1]-1
        player_stats[2] = player_stats[2]-1
        return 0
def sleep():
    global player_stats
    global enemy_stats
    if player_stats[3] == 10:
        print("You cannot sleep")
        return 1
    else:
        player_stats[3] = player_stats[3] + 1
        return 0
def walk():
    global player_stats
    global enemy_stats
    if player_stats[1] >= 9:
        print("You cannot walk! You are too thirsty.")
        return 1
    elif player_stats[3] <= 1:
        print("You cannot walk! You are too tired.")
        return 1
    else:
        player_stats[0] = player_stats[0]+10
        player_stats[1] = player_stats[1]+1
        player_stats[3] = player_stats[3]-2
def sprint():
    global player_stats
    global enemy_stats
    if player_stats[1] >= 7:
        print("You cannot walk! You are too thirsty.")
        return 1
    elif player_stats[3] <= 3:
        print("You cannot walk! You are too tired.")
        return 1
    else:
        player_stats[0] = player_stats[0]+20
        player_stats[1] = player_stats[1]+2
        player_stats[3] = player_stats[3]-3
def run():
    global player_stats
    global enemy_stats
    if player_stats[1] >= 4:
        print("You cannot walk! You are too thirsty.")
        return 1
    elif player_stats[3] <= 5:
        print("You cannot walk! You are too tired.")
        return 1
    else:
        player_stats[0] = player_stats[0]+30
        player_stats[1] = player_stats[1]+3
        player_stats[3] = player_stats[3]-4
def setup():
    global player_stats
    global enemy_distance
    player_stats = [0, 0, 5, 10]
    enemy_distance = 0
def choose():
    global player_stats
    global enemy_distance
    global choice
    #choice = int(input("(1) Drink water\n(2) Walk\n(3) Sprint\n(4) Run\n(5) Sleep for the night\n(6) Quit\n? "))
    redo = 1
    while redo == 1:
        choice = int(input("(1) Drink water\n(2) Walk\n(3) Sprint\n(4) Run\n(5) Sleep for the night\n(6) Quit\n? "))
        if choice == 1:
            redo = drink()
        elif choice == 2:
            redo = walk()
        elif choice == 3:
            redo = sprint()
        elif choice == 4:
            redo = run()
        elif choice == 5:
            redo = sleep()
        elif choice == 6:
            exit()
def enemy_move():
    global player_stats
    global enemy_distance
    choice = random.randint(2,4)
    if choice == 2:
        enemy_distance = enemy_distance+5
    elif choice == 3:
        enemy_distance = enemy_distance+15
    elif choice == 4:
        enemy_distance = enemy_distance+20
def ckwin():
    global player_stats
    global enemy_distance
    if player_stats[0] <= enemy_distance:
        print("The enemy got you!")
    elif player_stats[1] >= 10:
        print("You died of thirst!")
    elif player_stats[3] <= 0:
        print("You died of exaustion!")
    elif player_stats[0] >= 100:
        print("You made it home!")
setup()
game = 1
while game == 1:
    mkboard()
    ckwin()
    choose()
    ckwin()
    if choice == 5:
        go = random.randint(0,100)
        if go >= 20 and go <= 30:
            enemy_move()
    else:
        enemy_move()
    ckwin()
